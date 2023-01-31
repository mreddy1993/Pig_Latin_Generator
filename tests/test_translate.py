import pytest
from pig_latin_generator.pig_latin import translate
#This test suite tests the translate function
def test_one():
    test_case = "happy"
    assert translate(test_case) == "appyhay"

def test_two():
    test_case = "child"
    assert translate(test_case) == "ildchay"

def test_three():
    test_case = "awesome"
    assert translate(test_case) == "awesomeway"

