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

require 'test_helper'

class EventCandidateCTest < ActiveSupport::TestCase
  def setup
    @opening = events(:opening_morning)
    @appointment = events(:appointment)
    @availabilities = EventCandidateC.availabilities(base_date: DateTime.parse('2014-08-10'))
  end

  test 'returns_hash_with_date_key_and_the_argument_as_its_value' do
    assert_equal Date.new(2014, 8, 10), @availabilities[0][:date]
  end

  test 'sundays_have_no_availabilities' do
    assert_equal [], @availabilities[0][:slots]
  end

  test 'the_second_key_is_arg_+=1_day' do
    assert_equal Date.new(2014, 8, 11), @availabilities[1][:date]
  end

  test 'the_second_day_has_the_expected_openings' do
    assert_equal ['9:30', '10:00', '11:30', '12:00'], @availabilities[1][:slots]
  end

  test 'the_last_date_returned_is_arg_+=6_days' do
    assert_equal Date.new(2014, 8, 16), @availabilities[6][:date]
  end

  test 'it_returns_availabilities_for_7_days' do
    assert_equal 7, @availabilities.length
  end

  test 'datetimes_can_be_formatted_correctly' do
    assert_equal '10:30', @appointment.starts_at.to_formatted_s(:hour_minutes)
  end

  test 'retrieves_recurring_wdays_with_openings' do
    assert_includes EventCandidateC.recurring_openings, @opening.starts_at.wday
  end

  test 'works_when_there_are_multiple_openings_on_the_same_day' do
    opening_afternoon = Event.create(
      starts_at: DateTime.parse('2014-08-04 14:30:00'),
      ends_at: DateTime.parse('2014-08-04 19:00:00'),
      kind: 'opening',
      weekly_recurring: true
    )

    openings_hash = EventCandidateC.recurring_openings
    assert_includes openings_hash[1], '9:30'
    assert_includes openings_hash[1], '18:30'
    opening_afternoon.destroy
  end

  test 'builds_slots_array' do
    assert_equal ['9:30', '10:00', '10:30', '11:00', '11:30', '12:00'], @opening.time_range_to_slots(@opening.starts_at)
  end

  test 'gets_all_openings_for_given_date' do
    opening_afternoon = EventCandidateC.create(
      starts_at: DateTime.parse('2014-08-04 14:30:00'),
      ends_at: DateTime.parse('2014-08-04 19:00:00'),
      kind: 'opening',
      weekly_recurring: true
    )
    openings = EventCandidateC.openings_for_day(date: DateTime.parse('2014-08-11 14:30:00'))
    assert_includes openings, '9:30'
    assert_includes openings, '18:30'
    opening_afternoon.destroy
  end
end
