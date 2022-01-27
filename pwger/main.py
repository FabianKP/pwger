from optparse import OptionParser
from .pwger import pwger


def cli():
    usage = "usage: pwger_private [ OPTIONS ]"
    # Read command line options:
    parser = OptionParser(usage=usage)
    parser.add_option("-e", action="store_true", dest="e", default=False, help="benutzt den erweiterten Wortschatz")
    parser.add_option("-g", action="store_true", dest="g", default=False, help="Output erhält Groß- und Kleinschreibung.")
    parser.add_option("-n", type="int", dest="n", default=5,
                      help="Bestimme die Anzahl der generierten Wörter (Grundeinstellung: 5).")
    parser.add_option("-s", action="store_true", dest="s", default=False,
                      help="Output enthält zufällig generierte Sonderzeichen.")
    parser.add_option("-z", action="store_true", dest="z", default=False,
                       help="Output enthält zufällig platzierte Zahlen.")
    (options, args) = parser.parse_args()

    # n-Option muss eine Zahl größer als 0 sein.
    if not options.n > 1:
        raise Exception("n muss größer als 0 sein.")

    # Call the Python implementation to generate password.
    password_string = pwger(e=options.e, g=options.g, n=options.n, s=options.s, z=options.z)

    # Print the password to the console.
    print(password_string)