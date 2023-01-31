import pytest
from pig_latin_generator.pig_latin import detranslate
#This test suite is to test the detranslate function"
def test_one():
    test_case = "appyhay"
    assert detranslate(test_case) == "happy"

def test_two():
    test_case = "ildchay"
    assert detranslate(test_case) == "child"

def test_three():
    test_case = "awesomeway"
    assert detranslate(test_case) == "awesome"
#I added an extra test case as this use case was more problematic than the other two.
def test_four():
    test_case = "alloyway"
    assert detranslate(test_case) == "alloy"