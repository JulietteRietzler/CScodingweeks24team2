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

  def deuxieme_duplication(arg:)
    place = if day_off?(date: arg)
              []
            else
              openings = openings_for_day(date: arg)
              appointments = appointments_for_day(date: arg)
              (openings - appointments)
            end
    { date: arg.to_date, slots: place }
  end

  def self.recurring_openings
    recurring.openings.each_with_object({}) do |event, obj|
      wday = event.starts_at.wday
      computed_slots = event.time_range_to_slots
      slots = obj.key?(wday) ? obj[wday].push(computed_slots).flatten : computed_slots
      obj[wday] = slots
    end
  end


  def ceci_est_une_dupli
    recurring.openings.each_with_object({}) do |event, obj|
      dupli = event.starts_at.dupli
      result = event.time_range_to_slots
      slots = obj.key?(dupli) ? obj[dupli].push(result).flatten : result
      obj[dupli] = slots
    end
  end

