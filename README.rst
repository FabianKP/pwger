pwger
=====

Bei ``pwger`` handelt es sich um ein kleines Programm, um Passwörter aus
zufälligen deutschen Worten zu generieren. Die Idee dahinter bekam größere öffentliche Aufmerksamkeit
durch einen `xkcd-Comic <https://xkcd.com/936/>`_, findet sich aber auch in wesentlich früheren Quellen,
zum Beispiel `Diceware <https://theworld.com/~reinhold/diceware.html>`_.

``pwger`` ist ein Programm, um entsprechende Passwörter zu generieren. Im Englischen
gibt es schon entsprechende Programme, zum Beispiel
`xkcdpass <https://pypi.org/project/xkcdpass/>`_. ``pwger`` richtet sich aber
spezifisch an deutschsprachige Benutzer, welchen es möglicherweise leichter fällt,
sich Passwörter aus deutschen anstatt aus englischen Wörtern zu merken.

Ein Beispiel: Das Passwort "LLQDxz76" ist schwierig zu merken und kann mit modernen
Computern innerhalb von 1 Stunde geknackt werden.

Im Gegensatz dazu ist das Passwort "Magen weiter Hund versichern Abwrackprämie" viel
leichter zu merken (insbesondere mit Hilfe der
`Kettenmethode <https://de.wikipedia.org/wiki/Mnemotechnik#Kettenmethode,_Assoziationsketten>`_). Selbst ein
`Supercomputer <https://arstechnica.com/information-technology/2012/12/25-gpu-cluster-cracks-every-standard-windows-password-in-6-hours/>`_
würde allerdings mehr als **9 Jahre**
benötigen, um es zu knacken.

Beachten Sie hierbei, dass diese Rechnung unter der Annahme gemacht wurde, dass ihr
Gegner `weiß`, dass das Passwort aus zufälligen deutschen Wörtern besteht (siehe auch
`Kerckhoffs Prinzip
<https://de.wikipedia.org/wiki/Kerckhoffs%E2%80%99_Prinzip>`_).
Das heißt, in vielen Fällen werden die generierten Passwörter noch um einiges sicherer
sein, da eventuelle Hacker nicht wissen werden, dass ihr spezifisches Passwort
mittels ``pwger`` generiert wurde.

Installation (Linux)
============

Voraussetzungen für die Installation:

- Python (Version 3.6 oder neuer)
- pip

Installation:

1. Laden Sie die Datei `pwger-1.0.0-py2.py3-none-any.whl <dist/pwger-1.0.0-py3-none-any.whl>`_ herunter und öffnen Sie den enthaltenen Ordner
in der Kommandozeile.

2. Führen sie folgendes Kommando aus:
::
    >> pip install pwger-1.0.0-py2.py3-none-any.whl

Zum Deinstallieren genügt der Befehl.
::
    >> pip uninstall pwger

Tutorial
========

Ein einfaches Passwort generieren Sie mit dem Kommando ``pwger``:
::
    >> pwger
    lockt lebed sozialer welcher kino

Benutzen sie die Option :code:`-n`, um die Anzahl der generierten Wörter zu steuern
(Grundeinstellung sind 5 Wörter)
::

    >> pwger -n 8  # generiert 8 zufällige deutsche Wörter
    gelesen bahnen dagegen vergeben jakob erläuterte teilten belegte

Beachten Sie, dass die mit ``pwger`` generierten Wörter stets klein geschrieben sind.
Wenn Sie wollen, dass ``pwger`` die natürliche Groß- und Kleinschreibung beachtet,
so benutzen Sie die Option :code:`-g`.
::
    >> pwger -g
    Die Juni Haftbefehl Studie geplanten

Standardmäßig generiert ``pwger`` alle Passwörter aus der Liste der 10000 häufigst benutzen
deutschen Wörter. Wenn Sie wollen, dass ``pwger`` aus einem erweiterten Wortschatz von
über **130 000 Wörtern** schöpft und
damit einhergehend die Sicherheit der generierten Passwörter um ein Vielfaches erhöhen,
so können Sie dies mit der Option :code:`-a` einstellen.
::
    >> pwger -a
    verstopfungsproblem gelartig resistenzsituation beweidungsdruck fortschritt

Die hohe Länge der generierten Passwörter behebt die Notwendigkeit, dass ein Passwort
Ziffern und Sonderzeichen enthalten muss. Nichtsdestotrotz verlangen mittlerweile
ein großer Teil aller Webseiten, dass Passwörter diese Kriterien erfüllen.
``pwger`` bietet Ihnen deswegen über die Optionen :code:`-z` bzw. :code:`-s` die Möglichkeit,
eine zufällige Anzahl an Ziffern
und Sonderzeichen in das Passwort aus zufällig generierten Wörtern einzufügen.
Damit die leichte Merkbarkeit erhalten bleibt, werden Ziffern und Sonderzeichen
ausschließlich zwischen den einzelne Wörtern, nie jedoch innerhalb eines Wortes, eingefügt.
Beispiel:
::
    >> pwger -z    # fügt ein paar Zufallsziffern ins Passwort ein
    zweiten verweist2überwunden3dramatischen strategischen
    >> pwger -s     # fügt ein paar Sonderzeichen ins Passwort ein
    verliebt aufgaben verhalten befürworter_festivals
Selbstverständlich können alle Optionen auch miteinander kombiniert werden:
::
    >> pwger -g -n 3
    Wirtschaftsminister Holland Kohl
    >> pwger -s -z
    9nürnberg stecken1staub}buche medaille3



