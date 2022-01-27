

from string import ascii_letters, digits, whitespace


def hat_sonderzeichen(string: str) -> bool:
    """
    Bestimmt, ob der gegebene String Sonderzeichen hat. Sonderzeichen sind alle Zeichen außer Buchstaben, Ziffern
    und Leerzeichen.

    :param string:
    :return:
    """
    if set(string).difference(ascii_letters + digits + whitespace + "äöü"):
        return True
    else:
        return False