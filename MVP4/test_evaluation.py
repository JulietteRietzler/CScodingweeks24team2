from MVP4.evaluation import *

def test_evaluation():
   assert type(niveau_candidat('EventCandidatA.rb','EventCandidatATest.rb',['event_candidate_b.rb','event_candidate_c.rb'],['event_candidate_b_test.rb','event_candidate_c_test.rb']))==str
   assert niveau_candidat('EventCandidatA.rb','EventCandidatATest.rb',['event_candidate_b.rb','event_candidate_c.rb'],['event_candidate_b_test.rb','event_candidate_c_test.rb'])=='assez bon\n Attention, il y a probablement une fraude!'
