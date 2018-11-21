import pytest
from MVP3.similarité_méthode import *

def test_identique():
   assert type(identique('il fait beau','il fait chaud'))==bool

def test_similatite_methode():
   assert type(similatite_methode('il fait beau','il fait chaud'))==float
   assert 0<=similatite_methode('il fait beau','il fait chaud')<=1
