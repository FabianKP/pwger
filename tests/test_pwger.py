
import numpy as np

from pwger import pwger

from tests.hat_sonderzeichen import hat_sonderzeichen


def execute_pwger(n: int = 5, g: bool = False, s: bool = False, z: bool = False, a: bool = False):
    passwort = pwger(e=a, n=n, g=g, s=s, z=z)
    print(passwort)
    # If g is False, the returned password must not contain capitals.
    has_upper = _has_upper(passwort)
    if not g:
        assert not has_upper
    # if s is true, the output string must contain special characters (not that the test is)
    contains_numbers = any(i.isdigit() for i in passwort)
    if z:
        assert contains_numbers
    else:
        assert not contains_numbers
    # if s is true, the output string must contain special characters (not that the test is)
    contains_special_chars = hat_sonderzeichen(passwort)
    if s:
        assert contains_special_chars
    else:
        assert not contains_special_chars


def test_pwger_basic():
    execute_pwger()

def test_pwger_number():
    execute_pwger(n=42)


def test_pwger_capitals():
    execute_pwger(g=True)


def test_pwger_numbers():
    execute_pwger(z=True)


def test_pwger_special_chars():
    execute_pwger(s=True)

def test_pwger_a():
    execute_pwger(a=True)


def test_pwger_numbers_and_special_chars():
    execute_pwger(z=True, s=True)


def test_pwger_all_options_on():
    execute_pwger(g=True, z=True, s=True, a=True, n=7)


def _has_upper(string: str) -> bool:
    """
    Checks whether a given string contains uppercase letters.

    :param string:
    :return:
    """
    string_has_upper = np.any([np.char.isupper(c) for c in string])
    return string_has_upper