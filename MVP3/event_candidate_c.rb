# == Schema Information
#
# Table name: events
#
#  id               :integer          not null, primary key
#  starts_at        :datetime
#  ends_at          :datetime
#  kind             :string
#  weekly_recurring :boolean
#  created_at       :datetime         not null
#  updated_at       :datetime         not null
#

class EventCandidateC < ApplicationRecord
  self.table_name = 'events'

  ::Time::DATE_FORMATS[:hour_minutes] = '%-H:%M'

  SLOT_LENGTH = 30.minutes
  BASE_TIME_RANGE = 6.days
  KIND_OPENING = 'opening'.freeze
  KIND_APPOINTMENT = 'appointment'.freeze

  validates :starts_at, :ends_at, :kind, :weekly_recurring, presence: true

  scope :recurring, -> { where(weekly_recurring: true) }
  scope :openings, -> { where(kind: KIND_OPENING) }
  scope :appointments, -> { where(kind: KIND_APPOINTMENT) }
  scope :on_day, ->(date) { where('date(starts_at) = ?', date.to_date) }

  # @param base_date [DateTime] Point from which the availabilities are returned
  # @return [Array<Hash>] 7 following days. Each hash corresponds to day
  #         key [Symbol] :date
  #         value [Array<String>] Times available for that :day
  def self.availabilities(base_date)
    time_span = base_date.upto(base_date + BASE_TIME_RANGE).to_a
    time_span.each_with_object([]) do |day, obj|
      obj << availabilities_for_day(date: day)
    end
  end

  # Compute openings for a given day
  # @param date [DateTime]
  # @return [Hash]
  #         key: date [Date]
  #         value [Array] Slots: ["09:30", "11:00"]
  def self.availabilities_for_day(date:)
    slots = if day_off?(date: date)
              []
            else
              openings = openings_for_day(date: date)
              appointments = appointments_for_day(date: date)
              (openings - appointments)
            end
    { date: date.to_date, slots: slots }
  end

  # Format the openings
  # @param date [DateTime]
  # @return [Array<String>] e.g.: ["09:30", "11:00"]
  def self.openings_for_day(date:)
    isolated = openings.on_day(date)
    isolated_openings_hours = isolated.map(&:time_range_to_slots).flatten

    recurring = recurring_openings[date.wday] || []
    (isolated_openings_hours + recurring).uniq
  end

  # Format the appointments
  # @param date [DateTime]
  # @return [Array<String>] e.g.: ["09:30", "11:00"]
  def self.appointments_for_day(date:)
    appointments = EventCandidateC.appointments.on_day(date)
    appointments.map(&:time_range_to_slots).flatten
  end

  # Check if the given day should be excluded? (i.e. Sunday, holiday...)
  # @param day [DateTime / Time]
  # @return [Boolean]
  def self.day_off?(date:)
    date.sunday?
  end

  # Compute recurring openings' times
  # @return [Hash]
  #         key: wday of the recurring event opening
  #         value [Array] Slots: ["09:30", "11:00"]
  #  e.g.: {1 => ["9:30", "10:30"], 4 => ["11:00"]}
  def self.recurring_openings
    recurring.openings.each_with_object({}) do |event, obj|
      wday = event.starts_at.wday
      computed_slots = event.time_range_to_slots
      slots = obj.key?(wday) ? obj[wday].push(computed_slots).flatten : computed_slots
      obj[wday] = slots
    end
  end

  # Recursively return all the wdays with openings
  # @return [Array<String>] : ["09:30", "11:00"]
  def time_range_to_slots(appointment_time = starts_at, slots_array = [])
    ends_at_formatted = ends_at.to_formatted_s(:hour_minutes)
    appointment_time_formatted = appointment_time.to_formatted_s(:hour_minutes)

    return slots_array if ends_at_formatted == appointment_time_formatted
    slots_array << appointment_time_formatted
    next_day = appointment_time + SLOT_LENGTH
    time_range_to_slots(next_day, slots_array)
  end
end
