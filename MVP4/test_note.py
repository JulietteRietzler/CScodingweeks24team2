from MVP4.note import *

def test_note():
   assert type(note_candidat('EventCandidatA.rb','EventCandidatATest.rb',['event_candidate_b.rb','event_candidate_c.rb'],['event_candidate_b_test.rb','event_candidate_c_test.rb']))==float
   assert 0<=note_candidat('EventCandidatA.rb','EventCandidatATest.rb',['event_candidate_b.rb','event_candidate_c.rb'],['event_candidate_b_test.rb','event_candidate_c_test.rb'])<=20
