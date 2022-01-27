
from pwger.pwger import _zufaellige_sonderzeichen

def test_random_special_chars():
    n = 10
    sample = _zufaellige_sonderzeichen(n)
    assert sample.size == n
    for s in sample:
        print(s)