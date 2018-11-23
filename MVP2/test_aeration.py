from MVP2.aeration import *
import pytest

fichier = open("ExamCandidatC.txt", "a")
fichier.write('''# == Schema Information
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
 end ''')
fichier.close()

def test_pourcentages_d_espaces():
   assert 0<=pourcentage_d_espaces("ExamCandidatC.txt")<=1

