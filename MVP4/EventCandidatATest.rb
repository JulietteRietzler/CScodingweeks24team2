require 'test_helper'

class EventCandidatATest < ActiveSupport::TestCase
  test "should not save event without kind" do
    event = EventCandidatA.new starts_at: DateTime.parse("2014-08-04 09:30"), ends_at: DateTime.parse("2014-08-04 12:30")
    assert_not event.save, "Saved the event without a kind"
  end

  test "should not save event with an invalid kind" do
    event = EventCandidatA.new kind: 'other', starts_at: DateTime.parse("2014-08-04 09:30"), ends_at: DateTime.parse("2014-08-04 12:30")
    assert_not event.save, "Saved the event with an invalid kind"
  end

  test "should not save event without starts_at" do
    event = EventCandidatA.new kind: 'opening', ends_at: DateTime.parse("2014-08-04 12:30")
    assert_not event.save, "Saved the event without a starts_at"
  end

  test "should not save event without ends_at" do
    event = EventCandidatA.new kind: 'opening', starts_at: DateTime.parse("2014-08-04 09:30")
    assert_not event.save, "Saved the event without a ends_at"
  end

  test "should not save event with a starts_at greater than an ends_at" do
    event = EventCandidatA.new kind: 'opening', starts_at: DateTime.parse("2014-08-04 13:30"), ends_at: DateTime.parse("2014-08-05 12:30")
    assert_not event.save, "Saved the event with a starts_at greater than an ends_at"
  end

  test "should not save event with an ends_at in a different day than an starts_at" do
    event = EventCandidatA.new kind: 'opening', starts_at: DateTime.parse("2014-08-04 13:30"), ends_at: DateTime.parse("2014-08-04 12:30")
    assert_not event.save, "Saved the event with an ends_at in a different day than a starts_at"
  end

  test "should not save event with a starts_at or ends_at which is not a multiple of 30 minutes" do
    event = EventCandidatA.new kind: 'opening', starts_at: DateTime.parse("2014-08-04 09:05"), ends_at: DateTime.parse("2014-08-04 12:20")
    assert_not event.save, "Saved the event with a starts_at or ends_at which is not a multiple of 30 minutes"
  end

  test "should not save appointment with a weekly_recurring: true" do
    opening = EventCandidatA.new kind: 'opening', starts_at: DateTime.parse("2014-08-04 09:30"), ends_at: DateTime.parse("2014-08-04 12:30"), weekly_recurring: true
    appointment = EventCandidatA.new kind: 'appointment', starts_at: DateTime.parse("2014-08-04 09:30"), ends_at: DateTime.parse("2014-08-04 12:30"), weekly_recurring: true
    assert opening.save, "Not saved opening with a weekly_recurring: true"
    assert_not appointment.save, "Saved appointment with a weekly_recurring: true"
  end

  test "should not save opening if an other already exist in the same time slot" do
    EventCandidatA.create kind: 'opening', starts_at: DateTime.parse("2014-08-04 09:00"), ends_at: DateTime.parse("2014-08-04 12:30")
    opening = EventCandidatA.new kind: 'opening', starts_at: DateTime.parse("2014-08-04 08:00"), ends_at: DateTime.parse("2014-08-04 10:30")
    assert_not opening.save, "Saved an opening while an other already exist in the same time slot"
  end

  test "should not save an appointment if an other already exist in the same time slot" do
    EventCandidatA.create kind: 'opening', starts_at: DateTime.parse("2014-08-04 09:00"), ends_at: DateTime.parse("2014-08-04 12:30")
    EventCandidatA.create kind: 'appointment', starts_at: DateTime.parse("2014-08-04 09:00"), ends_at: DateTime.parse("2014-08-04 12:00")
    appointment = EventCandidatA.new kind: 'appointment', starts_at: DateTime.parse("2014-08-04 11:30"), ends_at: DateTime.parse("2014-08-04 12:30")
    assert_not appointment.save, "Saved an appointment while an other already exist in the same time slot"
  end

  test "should not save an appointment if it outside of opening hours" do
    appointment = EventCandidatA.new kind: 'appointment', starts_at: DateTime.parse("2014-08-04 09:00"), ends_at: DateTime.parse("2014-08-04 12:30")
    assert_not appointment.save, "Saved an appointment wich is outside of opening hours"
  end

  test "one simple test example" do
    EventCandidatA.create kind: 'opening', starts_at: DateTime.parse("2014-08-04 09:30"), ends_at: DateTime.parse("2014-08-04 12:30"), weekly_recurring: true
    EventCandidatA.create kind: 'appointment', starts_at: DateTime.parse("2014-08-11 10:30"), ends_at: DateTime.parse("2014-08-11 11:30")

    availabilities = EventCandidatA.availabilities DateTime.parse("2014-08-10")
    assert_equal Date.new(2014, 8, 10), availabilities[0][:date]
    assert_equal [], availabilities[0][:slots]
    assert_equal Date.new(2014, 8, 11), availabilities[1][:date]
    assert_equal ["9:30", "10:00", "11:30", "12:00"], availabilities[1][:slots]
    assert_equal Date.new(2014, 8, 16), availabilities[6][:date]
    assert_equal 7, availabilities.length
  end

  test "a more complexe test" do
    EventCandidatA.create kind: 'opening', starts_at: DateTime.parse("2014-08-04 09:30"), ends_at: DateTime.parse("2014-08-04 12:30"), weekly_recurring: true
    EventCandidatA.create kind: 'opening', starts_at: DateTime.parse("2014-08-18 14:00"), ends_at: DateTime.parse("2014-08-18 18:00"), weekly_recurring: true
    EventCandidatA.create kind: 'appointment', starts_at: DateTime.parse("2014-08-11 10:30"), ends_at: DateTime.parse("2014-08-11 11:30")
    EventCandidatA.create kind: 'appointment', starts_at: DateTime.parse("2014-08-25 10:30"), ends_at: DateTime.parse("2014-08-25 11:30")
    EventCandidatA.create kind: 'appointment', starts_at: DateTime.parse("2014-08-25 14:30"), ends_at: DateTime.parse("2014-08-25 17:30")

    availabilities = EventCandidatA.availabilities(DateTime.parse("2014-08-10"), DateTime.parse("2014-08-25"))
    assert_equal Date.new(2014, 8, 10), availabilities[0][:date]
    assert_equal ["9:30", "10:00", "11:30", "12:00"], availabilities[1][:slots]
    assert_equal Date.new(2014, 8, 25), availabilities[15][:date]
    assert_equal ["9:30", "10:00", "11:30", "12:00", "14:00", "17:30"], availabilities[15][:slots]
    assert_equal 16, availabilities.length
  end
end
