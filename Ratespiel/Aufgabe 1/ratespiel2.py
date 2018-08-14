#ratespiel.py
#-*- coding: utf-8 -*-

import random
import time
import threading 
"""
Ein Spiel bei dem man eine Zahl zwischen 1 und 20 erraten muss.

"""

"""
@@ Martin, 10.8.2018
  - Docstrings: bitte ganze Sätze (Große geschrieben, Punkt am Ende. Wenn mehrzeilig, dann eine Leerzeile nach dem Titel)
  - Ich habe auch im Code Rewview-Kommentare eingefügt: @@
    Bitte beheben (nach dem erneute Review können die später raus)

"""
class Ratespiel(object):
    """gesamte Klasse für das Spiel"""
    
    def __init__(self):
        """initialisiert variablen"""
        self.rzahl = random  # @@ hier weist du ein Modul 'random' der Variablen zu. Besser direkt mit dem Modul arbeiten?
        self.b = 0
        self.check = True  # @@ PEP8: eine Leerzeile zwischen Methoden
    def ratespiel(self):
        """startet das Spiel/führt Sie weiter aus"""
        
        time.sleep(0.2)
        if self.b > 5:
            print("Sie haben verloren")
            time.sleep(0.2)
            print("Die richtige Zahl waere {}".format(self.zzahl))
            print(self.spielername,"Moechtest du ein weiteres Spiel (J/N)?")
            self.newgamepl = raw_input()
            # @@ Sollte auch mit Kleinbuchstaben funktionieren
            if self.newgamepl == "J":       #startet das Spiel neu oder beendet es 
                self.nzahl()    
                # @@ hier wird eine Rekursion ausgeführt, d.h. jedesmal wieder ein Unteraufruf
                # Das sollten wir vermeiden (weiter unten auch)
                self.ratespiel()
            elif self.newgamepl == "N":
                quit()
        self.check = True
        self.vspiel = 0
        if self.check:
            time.sleep(0.1)
            self.b += 1
            print("Hallo {}, {}-ter Versuch welche Zahl habe ich mir gedacht?".format(self.spielername, self.b))
        try:                            #Versucht nur Zahlen als Werte zu nehmen
            self.vspiel = input()       
        except NameError: 
            print("Bitte eine Zahl eingeben!")
            self.check = False
            self.ratespiel()
                
        # Abfragen für die Zufallszahlen
        if self.vspiel == self.zzahl:
            print("Glueckwunsch,{}, das ist richtig! Moechtest du ein weiteres Spiel (J/N)?".format(self.spielername))
            self.newgamepl = raw_input()
            
            if self.newgamepl == "J" or "j":  # @@ hat das wirklich funktioniert als du es getestet hast?
                self.nzahl()           
                self.ratespiel()
            elif self.newgamepl == "N" or "n":  # @@ auch hier: ein kleiner Fehler in der Logik
                # @@ Siehe Anmerkungen zur Rekursion.
                # Versuche einmal ohne quit auszukommen.
                # Die Hauptfunktion 'ratespiel' sollte einfach unten ankommen wenn Programm zu ende ist
                quit()
        
        if self.vspiel != self.zzahl:
            
            if self.vspiel < self.zzahl:
                print("Leider falsch, meine Zahl ist größer")
                self.ratespiel()
            elif self.vspiel > self.zzahl:
                print("Leider falsch, meine Zahl ist kleiner")
                self.ratespiel()
                
    def start(self):
        """fragt nach Namen und startet dannach das Spiel"""
        
        time.sleep(0.2)  # @@ warum?
        self.spielername = ""  # @@ wird ja gleich wieder überschrieben. Außerdem sollten self Initioalisierungen in __init__ passieren
        self.spielername = raw_input("wie heißen Sie?")
        
        if not self.spielername.isalpha():  # @@ ERROR Guter Test, aber funktioniert be mir nicht, weil ein '\r' an den Name gehängt wurde
            print("Bitte nur buchstaben!")  # Rechtschreibung
            self.start()  # @@ Bitte schau dir mal beim Debuggen den Stacktrace an. Es sollte keine Rekursion sein (-> besser while)
        self.zzahl = self.rzahl.randint(1,20)
        self.ratespiel()
        
    def nzahl(self):
        """generiert neue Zahlen für ein neues Spiel"""
        # @@ Der Methodenname könnte sprechender sein
        self.b = 0  # @@ was ist b? Überdenke bitte den Namen noch einmal
        self.zzahl = self.rzahl.randint(1,20)
        
if __name__ == "__main__":
    ratenstart = Ratespiel()  # @@ warum ein neuer Name? ratespiel oder spiel wäre evtl. klarer
    ratenstart.start()