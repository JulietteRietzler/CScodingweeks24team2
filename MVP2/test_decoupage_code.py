import pytest
from MVP2.decoupage_code import *

def test_decoupage_du_code():
    assert type(decoupage_du_code('EventCandidatA.rb')[0])==list
    assert type(decoupage_du_code('EventCandidatA.rb')[1])==list
    assert type(decoupage_du_code('EventCandidatA.rb')[2])==list
    assert type(decoupage_du_code('EventCandidatA.rb')[3])==list
    assert decoupage_du_code('EventCandidatA.rb')==([["    kind.eql? 'opening'\n", '  end\n'], ["    kind.eql? 'appointment'\n", '  end\n'], ['    availabilities = []\n', '\n', '    (start_date..end_date).each do |date|\n', '      availabilities << { date: date.to_date, slots: slots_available(date)}\n', '    end\n'], ['    if starts_at.present? and ends_at.present? and starts_at >= ends_at\n'], ['    if starts_at.present? and ends_at.present? and starts_at.to_date != ends_at.to_date\n'], ['    [:starts_at, :ends_at].each do |attribute|\n', '      if self[attribute.to_sym].present? and not self[attribute.to_sym].to_i.multiple_of?(30.minutes)\n'], ['    if kind.present? and starts_at.present? and ends_at.present? and\n'], ['    if starts_at.present? and ends_at.present? and\n'], ['    openings = split_into_slots(EventCandidatA.openings_on(date))\n', '    appointments = split_into_slots(EventCandidatA.appointments_on(date))\n', '\n', '    openings.reject { |slot| appointments.include? slot }\n', '  end\n'], ['    slots = []\n', '\n', '    events.each do |event|\n', '      (event.starts_at.to_i..(event.ends_at.to_i - 30.minutes)).step(30.minutes) do |timestamp|\n', "        slots << Time.at(timestamp).utc.strftime('%-H:%M')\n", '      end\n']], [['    if starts_at.present? and ends_at.present? and starts_at >= ends_at\n', "      errors.add(:starts_at, 'cannot be greater than ends_at')\n"], ['    if starts_at.present? and ends_at.present? and starts_at.to_date != ends_at.to_date\n', "      errors.add(:ends_at, 'cannot be a different day than starts_at')\n"], ['      if self[attribute.to_sym].present? and not self[attribute.to_sym].to_i.multiple_of?(30.minutes)\n', "        errors.add(attribute.to_sym, 'must be a multiple of thirty minutes')\n"], ['    if kind.present? and starts_at.present? and ends_at.present? and\n', '        EventCandidatA.where(kind: kind).overlapping(starts_at, ends_at).any?\n'], ['    if starts_at.present? and ends_at.present? and\n', '        EventCandidatA.openings_on(starts_at).cover(starts_at, ends_at).empty?\n']], [], [], [])


def test_indentation():
    assert indentation('    bonjour')==4
