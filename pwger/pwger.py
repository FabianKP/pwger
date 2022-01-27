
import os
import numpy as np

from pwger.sonderzeichen import SONDERZEICHEN
SCRIPT_DIR = os.path.dirname(__file__)

# Initialisiere numpy-Zufallsgenerator von Systementropie.
rng = np.random.default_rng(None)


def pwger(e: bool,  g: bool, n: int, s: bool, z: bool) -> str:
    """
    Dies ist ein Programm um ein Passwort bestehend aus zufälligen deutschen Wörtern zu generieren.

    :param e: Wenn True, dann wird das Passwort mithilfe des erweiterten Wortschatzes in data/wortschatz_gross.dat
        generiert.
    :param n: Die gewünschte Anzahl an Worten.
    :param z: Wenn True, dann enthält das Passwort zwischen den Wörtern verstreute Zahlen.
    :param s: Wenn True, dann enthält das Passwort zwischen den Wörter verstreute Sonderzeichen. Diese werden nach
        demselben Prinzip generiert, wie die Zahlen.
    :param g: Wenn True, dann berücksichtigt das Passwort Groß- und Kleinschreibung
    :return: Das Passwort als String.
    """
    # Anzahl der Passwörter muss größer als 0 sein.
    if n < 1:
        raise Exception("'n' muss größer als 0 sein.")

    # Wähle den entsprechenden Wortschatz.
    if e:
        wortschatz = np.loadtxt(os.path.join(SCRIPT_DIR, "data", "wortschatz_gross.dat"), delimiter="\n", dtype=str)
    else:
        wortschatz = np.loadtxt(os.path.join(SCRIPT_DIR, "data", "wortschatz.dat"), delimiter="\n", dtype=str)
    anzahl_woerter = wortschatz.size

    # Generiere n Zufallszahlen zwischen 0 und anzahl_woerter - 1.
    indizes = rng.integers(size=n, low=0, high=anzahl_woerter)
    woerter = wortschatz[indizes]

    # Entscheide, ob Groß- und Kleinschreibung beibehalten wird.
    if not g:
        # woerter sollen nur kleingeschrieben sein.
        for i in range(woerter.size):
            woerter[i] = woerter[i].lower()

    # Kreiere die Füllung (die Zeichen, mit denen generierte Wörter getrennt werden).
    fuellung = np.full((n + 1,), "", dtype=object)

    # Falls die z-Option aktiv ist, generiere zufällige Ziffern die in die Lücken eingefügt werden.
    if z:
        def generiere_zufallszahlen(n_z: int):
            return rng.integers(0, 10, size=n_z)
        fuellung = _zufalls_fuellung(fuellung, n, generiere_zufallszahlen)

    # Falls die s-Option aktiv ist, generiere zufällige Sonderzeichen die in die Lücken eingefügt werden.
    if s:
        fuellung = _zufalls_fuellung(fuellung, n, _zufaellige_sonderzeichen)

    # Alle Füllungen, die noch kein Zeichen enthalten, bekommen ein Leerzeichen, außer sie sind am Anfang oder Ende der
    # Passphrase.
    for i in range(len(fuellung) - 2):
        if fuellung[i + 1] == "":
            fuellung[i + 1] = " "

    # Generiere den Passphrasen-String.
    passphrase = fuellung[0]
    for (wort, fill) in zip(woerter, fuellung[1:]):
        passphrase += wort + fill
    return passphrase


def _zufaellige_sonderzeichen(n: int) -> np.array:
    """
    Generiert zufällige Sonderzeichen.

    :param n: Gewünschte Anzahl der Sonderzeichen.
    :return: Ein Array mit Länge 'n', wobei jeder Eintrag ein zufälliges Sonderzeichen ist.
    """
    # lade Sonderzeichen in ein Array
    sonderzeichen_arr = np.array(list(SONDERZEICHEN))
    # ziehe 'n' Sonderzeichen (mit Zurücklegen)
    random_sample = rng.choice(sonderzeichen_arr, size=n)
    return random_sample


def _zufalls_fuellung(fuellung: np.ndarray, n: int, generator: callable) -> np.ndarray:
    # Die Anzahl der generierten Zahlen ist eine Zufallszahl zwischen 1 und n + 1.
    n_z = rng.integers(1, n + 1)
    # Generiere die n_z Zufallsziffern.
    zahlen = generator(n_z)
    # Für jede generierte Ziffer, bestimme zufällig ihre Position.
    possible_positions = n + 1  # n + 1 mägliche Positionen, nämlich Anfang, Ende, und Zwischenräume.
    positions = rng.integers(0, possible_positions, size=n_z)
    # Fülle die entsprechenden Ziffern an die zugeordneten Positionen.
    for i in range(n_z):
        fuellung[positions[i]] += str(zahlen[i])

    return fuellung
