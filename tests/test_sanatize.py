import pytest
from pig_latin_generator.pig_latin import sanatize


def test_one():
    test_case = "4ferion34r"
    with pytest.raises(ValueError, match="Phrase contains nonalphabetic characters"):
        sanatize(test_case)


def test_two():
    test_case = "jigeaccaec"
    with pytest.raises(ValueError, match="Not an English Word"):
        sanatize(test_case)
        