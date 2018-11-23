class EventCandidatA < ApplicationRecord
  self.table_name = 'events'
  KIND = %w(opening appointment).freeze

  validates :kind, inclusion: { in: KIND, message: 'is not a valid kind of event' }
  validates :starts_at, presence: true
  validates :ends_at, presence: true
  validate :starts_at_cannot_be_greater_than_ends_at,
           :ends_at_cannot_be_a_different_day_than_starts_at,
           :hours_must_be_a_multiple_of_thirty_minutes,
           :same_kind_of_event_cannot_be_in_a_same_time_slot

  with_options if: :appointment? do |appointment|
    appointment.validates :weekly_recurring, absence: true
    appointment.validate :appointment_cannot_be_outside_of_opening_hours
  end

  scope :openings, -> { where(kind: :opening) }
  scope :appointments, -> { where(kind: :appointment) }
  scope :recurring, -> { where(weekly_recurring: true) }
  scope :recurring_on, -> (day) { recurring.where(EventCandidatA.arel_table[:starts_at].lt(day.beginning_of_day)).
      where("STRFTIME('%w', starts_at) = :week_day", week_day: day.to_date.wday.to_s) }
  scope :overlapping, -> (starts_at, ends_at) { where(starts_at: (starts_at..ends_at)).
      or(EventCandidatA.where(ends_at: (starts_at..ends_at))) }
  scope :cover, -> (starts_at, ends_at) { where("TIME(starts_at) <= TIME(:starts_at) AND
      TIME(ends_at) >= TIME(:ends_at)", starts_at: starts_at, ends_at: ends_at) }
  scope :on, -> (day) { where(EventCandidatA.arel_table[:starts_at].gteq(day.beginning_of_day).and(
      EventCandidatA.arel_table[:ends_at].lteq(day.end_of_day))) }
  scope :openings_on, -> (day) { openings.on(day).or(recurring_on(day)) }
  scope :appointments_on, -> (day) { appointments.on(day) }

  def opening?
    kind.eql? 'opening'
  end

  def appointment?
    kind.eql? 'appointment'
  end

  def self.availabilities(start_date, end_date = start_date + 6.day)
    availabilities = []

    (start_date..end_date).each do |date|
      availabilities << { date: date.to_date, slots: slots_available(date)}
    end

    return availabilities
  end

  private

  def starts_at_cannot_be_greater_than_ends_at
    if starts_at.present? and ends_at.present? and starts_at >= ends_at
      errors.add(:starts_at, 'cannot be greater than ends_at')
    end
  end

  def ends_at_cannot_be_a_different_day_than_starts_at
    if starts_at.present? and ends_at.present? and starts_at.to_date != ends_at.to_date
      errors.add(:ends_at, 'cannot be a different day than starts_at')
    end
  end

  def hours_must_be_a_multiple_of_thirty_minutes
    [:starts_at, :ends_at].each do |attribute|
      if self[attribute.to_sym].present? and not self[attribute.to_sym].to_i.multiple_of?(30.minutes)
        errors.add(attribute.to_sym, 'must be a multiple of thirty minutes')
      end
    end
  end

  def same_kind_of_event_cannot_be_in_a_same_time_slot
    if kind.present? and starts_at.present? and ends_at.present? and
        EventCandidatA.where(kind: kind).overlapping(starts_at, ends_at).any?
      errors.add(:base, 'cannot be in a same time slot than an other')
    end
  end

  def appointment_cannot_be_outside_of_opening_hours
    if starts_at.present? and ends_at.present? and
        EventCandidatA.openings_on(starts_at).cover(starts_at, ends_at).empty?
      errors.add(:base, 'cannot be outside of opening hours')
    end
  end

  def self.slots_available(date)
    openings = split_into_slots(EventCandidatA.openings_on(date))
    appointments = split_into_slots(EventCandidatA.appointments_on(date))

    openings.reject { |slot| appointments.include? slot }
  end

  def self.split_into_slots(events)
    slots = []

    events.each do |event|
      (event.starts_at.to_i..(event.ends_at.to_i - 30.minutes)).step(30.minutes) do |timestamp|
        slots << Time.at(timestamp).utc.strftime('%-H:%M')
      end
    end

    return slots
  end
end
