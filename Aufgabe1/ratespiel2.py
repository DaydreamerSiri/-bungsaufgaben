#ratespiel.py
#-*- coding: utf-8 -*-

import random
import time
import threading 
"""
Ein Spiel bei dem man eine Zahl zwischen 1 und 20 erraten muss.

"""
class Ratespiel(object):
    """gesamte Klasse für das Spiel"""
    
    def __init__(self):
        """initialisiert variablen"""
        self.rzahl = random
        self.b = 0
        self.check = True
    def ratespiel(self):
        """startet das Spiel/führt Sie weiter aus"""
        
        time.sleep(0.2)
        if self.b > 5:
            print("Sie haben verloren")
            time.sleep(0.2)
            print("Die richtige Zahl waere {}".format(self.zzahl))
            print(self.spielername,"Moechtest du ein weiteres Spiel (J/N)?")
            self.newgamepl = raw_input()
            
            if self.newgamepl == "J":       #startet das Spiel neu oder beendet es 
                self.nzahl()           
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
            
            if self.newgamepl == "J" or "j":         
                self.nzahl()           
                self.ratespiel()
            elif self.newgamepl == "N" or "n":
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
        
        time.sleep(0.2)
        self.spielername = ""
        self.spielername = raw_input("wie heißen Sie?")
        
        if not self.spielername.isalpha(): 
            print("Bitte nur buchstaben!")
            self.start()
        self.zzahl = self.rzahl.randint(1,20)
        self.ratespiel()
        
    def nzahl(self):
        """generiert neue Zahlen für ein neues Spiel"""
        
        self.b = 0
        self.zzahl = self.rzahl.randint(1,20)
        
if __name__ == "__main__":
    ratenstart = Ratespiel()
    ratenstart.start()