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

  def self.appointments_for_day(date:)
    appointments = EventCandidateC.appointments.on_day(date)
    appointments.map(&:time_range_to_slots).flatten
  end

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

