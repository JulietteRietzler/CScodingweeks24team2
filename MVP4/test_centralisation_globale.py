import pytest
from MVP4.centralisation_global import *

def test_centralisation_globale():
   assert type(resultat_final('EventCandidatA.rb','EventCandidatATest.rb',['event_candidate_b.rb','event_candidate_c.rb'],['event_candidate_b_test.rb','event_candidate_c_test.rb'])==tuple
   assert type(resultat_final('EventCandidatA.rb','EventCandidatATest.rb',['event_candidate_b.rb','event_candidate_c.rb'],['event_candidate_b_test.rb','event_candidate_c_test.rb'])[0])==str
   assert type(resultat_final('EventCandidatA.rb','EventCandidatATest.rb',['event_candidate_b.rb','event_candidate_c.rb'],['event_candidate_b_test.rb','event_candidate_c_test.rb'])[1])==dict
