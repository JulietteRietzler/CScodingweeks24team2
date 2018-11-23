require 'test_helper'

class EventCandidateBTest < ActiveSupport::TestCase
  # Test validations on presence
  test 'presences validations' do
    # Set up
    kind_test_presence = EventCandidateB.create starts_at: DateTime.parse("2014-08-04 09:30"), ends_at: DateTime.parse("2014-08-04 12:30")
    start_test_presence = EventCandidateB.create kind: 'opening', ends_at: DateTime.parse("2014-08-04 12:30")
    end_test_presence = EventCandidateB.create kind: 'appointment', starts_at: DateTime.parse("2014-08-04 09:30")
    weekly_recurring_non_presence = EventCandidateB.create! kind: 'opening', starts_at: DateTime.parse("2014-08-04 09:30"), ends_at: DateTime.parse("2014-08-04 12:30")
    # Exercice
    assert_not kind_test_presence.valid?
    assert_not start_test_presence.valid?
    assert_not end_test_presence.valid?
    assert weekly_recurring_non_presence.valid?
    # Cleaning
    kind_test_presence.destroy
    start_test_presence.destroy
    end_test_presence.destroy
    weekly_recurring_non_presence.destroy
  end

  test "format validations" do
    # Set up
    kind_format = EventCandidateB.create kind: "foo", starts_at: DateTime.parse("2014-08-04 09:30"), ends_at: DateTime.parse("2014-08-04 12:30")
    ends_before_start = EventCandidateB.create kind: "opening", starts_at: DateTime.parse("2014-08-04 09:30"), ends_at: DateTime.parse("2014-08-04 08:00")
    same_day = EventCandidateB.create kind: "opening", starts_at: DateTime.parse("2014-08-04 09:30"), ends_at: DateTime.parse("2014-08-05 08:00")

    assert_not kind_format.valid?
    assert_not ends_before_start.valid?
    assert_not same_day.valid?

    # Cleaning
    kind_format.destroy
    ends_before_start.destroy
    same_day.destroy
  end

  test "event with a recurring opening" do
    puts "Recurrence Opening"
    # 1 - Set Up
      EventCandidateB.create kind: 'opening', starts_at: DateTime.parse("2014-08-04 09:30"), ends_at: DateTime.parse("2014-08-04 12:30"), weekly_recurring: true
      EventCandidateB.create kind: 'appointment', starts_at: DateTime.parse("2014-08-11 10:30"), ends_at: DateTime.parse("2014-08-11 11:30")
      availabilities = EventCandidateB.availabilities DateTime.parse("2014-08-10")

    # 2 - Exercice
      assert_equal Date.new(2014, 8, 10), availabilities[0][:date]
      assert_equal [], availabilities[0][:slots]
      assert_equal Date.new(2014, 8, 11), availabilities[1][:date]
      # Wrong format: assert_equal ["09:30", "10:00", "11:30", "12:00"], availabilities[1][:slots]
      assert_equal ["9:30", "10:00", "11:30", "12:00"], availabilities[1][:slots]
      assert_equal Date.new(2014, 8, 16), availabilities[6][:date]
      assert_equal 7, availabilities.length
  end

  test "when an event with a specific date exist without recurrence" do
    puts "Specific date without recurrence"
    # 1 - Set Up
      EventCandidateB.create kind: 'opening', starts_at: DateTime.parse("2014-08-11 09:30"), ends_at: DateTime.parse("2014-08-11 14:30")
      EventCandidateB.create kind: 'appointment', starts_at: DateTime.parse("2014-08-11 10:30"), ends_at: DateTime.parse("2014-08-11 13:30")
      availabilities = EventCandidateB.availabilities DateTime.parse("2014-08-10")
    # 2 - Exercice
      assert_equal Date.new(2014, 8, 10), availabilities[0][:date]
      assert_equal [], availabilities[0][:slots]
      assert_equal Date.new(2014, 8, 11), availabilities[1][:date]
      # Wrong format: assert_equal ["09:30", "10:00", "13:30", "14:00"], availabilities[1][:slots]
      assert_equal ["9:30", "10:00", "13:30", "14:00"], availabilities[1][:slots]
      assert_equal Date.new(2014, 8, 16), availabilities[6][:date]
      assert_equal 7, availabilities.length
  end

  test "when an event with a recurring and specific appointments and spe" do
    puts "Conflics between recurring and specific"
    # 1 - Set Up
      EventCandidateB.create kind: 'opening', starts_at: DateTime.parse("2014-08-11 09:00"), ends_at: DateTime.parse("2014-08-11 12:00")
      EventCandidateB.create kind: 'appointment', starts_at: DateTime.parse("2014-08-11 10:00"), ends_at: DateTime.parse("2014-08-11 11:00")
      EventCandidateB.create kind: 'appointment', starts_at: DateTime.parse("2014-08-04 09:00"), ends_at: DateTime.parse("2014-08-04 10:00"), weekly_recurring: true

      availabilities = EventCandidateB.availabilities DateTime.parse("2014-08-10")
    # 2 - Exercice
      assert_equal Date.new(2014, 8, 10), availabilities[0][:date]
      assert_equal [], availabilities[0][:slots]
      assert_equal Date.new(2014, 8, 11), availabilities[1][:date]
      assert_equal ["11:00", "11:30"], availabilities[1][:slots]
      assert_equal Date.new(2014, 8, 16), availabilities[6][:date]
      assert_equal 7, availabilities.length
  end

end
