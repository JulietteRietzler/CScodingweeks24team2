from MVP3.centralisation import *


def test_centralisation():
   assert type(resultats_comparaison('EventCandidatA.rb','EventCandidatATest.rb', ['event_candidate_b.rb','event_candidate_c.rb'],['event_candidate_b_test.rb','event_candidate_c_test.rb']))==tuple
   assert type(resultats_comparaison('EventCandidatA.rb','EventCandidatATest.rb', ['event_candidate_b.rb','event_candidate_c.rb'],['event_candidate_b_test.rb','event_candidate_c_test.rb'])[0])==str
   assert type(resultats_comparaison('EventCandidatA.rb','EventCandidatATest.rb', ['event_candidate_b.rb','event_candidate_c.rb'],['event_candidate_b_test.rb','event_candidate_c_test.rb'])[1])==dict
   assert resultats_comparaison('EventCandidatA.rb','EventCandidatATest.rb', ['event_candidate_b.rb','event_candidate_c.rb'],['event_candidate_b_test.rb','event_candidate_c_test.rb'])[1]["pourcentage de similarité des méthodes avec les fichiers"]==0.13983260310488904
   assert resultats_comparaison('EventCandidatA.rb','EventCandidatATest.rb', ['event_candidate_b.rb','event_candidate_c.rb'],['event_candidate_b_test.rb','event_candidate_c_test.rb'])[1]["pourcentage de similarité des noms de variable avec les fichiers"]==0.270991832679432
   assert resultats_comparaison('EventCandidatA.rb','EventCandidatATest.rb', ['event_candidate_b.rb','event_candidate_c.rb'],['event_candidate_b_test.rb','event_candidate_c_test.rb'])[1]["pourcentage de similarité des tests avec les fichiers"]==0.22483454432013594
   assert resultats_comparaison('EventCandidatA.rb','EventCandidatATest.rb', ['event_candidate_b.rb','event_candidate_c.rb'],['event_candidate_b_test.rb','event_candidate_c_test.rb'])[1]["nombre moyenne de noms de méthodes identiques avec les fichiers"]==0.13043478260869565
   assert resultats_comparaison('EventCandidatA.rb','EventCandidatATest.rb', ['event_candidate_b.rb','event_candidate_c.rb'],['event_candidate_b_test.rb','event_candidate_c_test.rb'])[1]["fichier le plus similaire"]==[0]
   assert resultats_comparaison('EventCandidatA.rb','EventCandidatATest.rb', ['event_candidate_b.rb','event_candidate_c.rb'],['event_candidate_b_test.rb','event_candidate_c_test.rb'])[1]["fraude probable"]==True
   assert resultats_comparaison('EventCandidatA.rb','EventCandidatATest.rb', ['event_candidate_b.rb','event_candidate_c.rb'],['event_candidate_b_test.rb','event_candidate_c_test.rb'])[1]["fichier ayant les tests les plus similaires"]==[1]
