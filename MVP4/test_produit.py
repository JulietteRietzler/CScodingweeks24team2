from MVP4.MVP4_produit import *

def test_prod():
    assert 0<= note_candidat('EventCandidatA.rb','EventCandidatATest.rb',['event_candidate_b.rb','event_candidate_c.rb'],['event_candidate_b_test.rb','event_candidate_c_test.rb']) <=20
    assert type(produit('EventCandidatA.rb','EventCandidatATest.rb', ['event_candidate_b.rb','event_candidate_c.rb'],['event_candidate_b_test.rb','event_candidate_c_test.rb'])[0][0])==str
    assert type(produit('EventCandidatA.rb','EventCandidatATest.rb', ['event_candidate_b.rb','event_candidate_c.rb'],['event_candidate_b_test.rb','event_candidate_c_test.rb'])[0][1])==str
    assert type(produit('EventCandidatA.rb','EventCandidatATest.rb', ['event_candidate_b.rb','event_candidate_c.rb'],['event_candidate_b_test.rb','event_candidate_c_test.rb'])[1])==float
    assert type(produit('EventCandidatA.rb','EventCandidatATest.rb', ['event_candidate_b.rb','event_candidate_c.rb'],['event_candidate_b_test.rb','event_candidate_c_test.rb'])[2])==str
