class EventCandidateB < ApplicationRecord

  self.table_name = 'events'

  # Validations of model
  validates :kind, presence: true, inclusion: ["opening", "appointment"]
  validates :starts_at, presence: true
  validates :ends_at, presence: true
  validate :date_order_validation # verify that ends_at is after starts_at
  validate :event_same_date # verify that the event concerns a single  day


  # Sould return the availabilities of the 7 next days of a day given
  def self.availabilities(start_date)
    # Create an array of the 7 days from start date
    array_of_days_to_display = (start_date..(start_date + 6)).to_a

    # initiating result array
    results_to_display = []

    array_of_days_to_display.each do |day|
      day_result_schedule = {}

      # Create opening schedule of the day
      day_result_schedule = self.event_specific_query(day, 'opening', day_result_schedule)
      day_result_schedule = self.event_recurring_query(day, 'opening', day_result_schedule)

      # Change Availabilities acording to appointments
      day_result_schedule = self.event_specific_query(day, 'appointment', day_result_schedule)
      day_result_schedule = self.event_recurring_query(day, 'appointment', day_result_schedule)

      # Store results of the day
      results_to_display << {date: day, slots: self.schedule_availibilities(day_result_schedule) }
    end

    return results_to_display
  end


  # VALIDATION METHODS -----------------------------------------------------------------------

  # Method that query specifics events related to day given and kind and return the schedule
  def self.event_specific_query(day, kind, day_result_schedule)
    EventCandidateB.where(kind: kind, starts_at: day.midnight..day.end_of_day).each do |event|
        day_result_schedule = event.day_schedule_creator(kind, day_result_schedule)
    end
    return day_result_schedule
  end

  # Method that query recurring events related to day given and kind and return the schedule
  def self.event_recurring_query(day, kind, day_result_schedule)
    EventCandidateB.where(kind: kind, weekly_recurring: true).each do |event|
      if event.starts_at.wday == day.wday
        day_result_schedule = event.day_schedule_creator(kind, day_result_schedule)
      end
    end
    day_result_schedule
    return day_result_schedule
  end

  # Method that create/update the schedule of the day with this format:
  # { :09:30 => {availability:true}, :10:00 => {availibility:false} .... }
  # regarding the event type
  def day_schedule_creator(kind, schedule_hash)
    counter = self.starts_at
    while counter < self.ends_at
      if kind == "opening"
        # Didn't go past TEST01: schedule_hash[counter.strftime("%H:%M").to_sym] = {availibility: true}
        schedule_hash[counter.strftime("%-H:%M").to_sym] = {availibility: true}
      elsif kind == "appointment"
        # Didn't go past TEST01: schedule_hash[counter.strftime("%H:%M").to_sym] = {availibility: false}
        schedule_hash[counter.strftime("%-H:%M").to_sym] = {availibility: false}
      end
      counter += 30.minutes
    end
    return schedule_hash
  end

  # Method that transform the schedule creator into result output format ["09:30", "10:00"]
  def self.schedule_availibilities(day_schedule_hash)
    slots = []
    day_schedule_hash.each do |key,value|
      slots << key.to_s if value[:availibility]
    end
    return slots
  end

  private

  # VALIDATION METHODS -------------------------------------------------------

  # Date order validation
  def date_order_validation
    if self[:ends_at] && self[:starts_at]
      if self[:ends_at] < self[:starts_at]
        errors[:ends_at] << "should be after start date"
        return false
      end
    end
  end

  # Date same day validation
  def event_same_date
    if self[:ends_at] && self[:starts_at]
      if self[:ends_at].to_date != self[:starts_at].to_date
        errors[:ends_at] << "should be the same day of start date"
        return false
      end
    end
  end
end
