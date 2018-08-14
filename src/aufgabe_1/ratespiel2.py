#ratespiel.py
#-*- coding: UTF-8 -*-

import random
import time
import re
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
    """Gesamte Klasse für das Spiel."""
    
    def __init__(self):
        """Initialisiert variablen."""
        self.counter = 0
        self.test_name2 = re.compile("1")
        self.unit_test = False
        self.zzahl = 0
    def ratespiel(self):
        """Startet das Spiel/führt Sie weiter aus."""
        while True:
            if self.unit_test == True:
                break
            print self.zzahl
            self.lose_check()
            self.number_question()
            self.win_check()
        return True
                
    def start(self):
        """Fragt nach Namen und startet dannach das Spiel."""
          
        while True:
            if self.unit_test == True:
                break
            self.spielername = raw_input("wie heißen Sie?")
            if self.spielername.isalnum() == True or not self.test_name2.match(self.spielername): 
                if self.spielername.isalpha() == False:
                    print("Bitte nur Buchstaben!") 
                else:
                    break 
            else:
                break
        self.new_number()
        self.ratespiel()
        return True
    
    def new_number(self):
        """Generiert neue Zahlen für ein neues Spiel."""
        self.counter = 0  
        self.zzahl = random.randint(1,20)
        return True
    
    def lose_check(self):
        """checkt ob der counter höher ist als es soll"""
        self.counter += 1
        if self.counter > 5:
            print("Sie haben verloren.")
            time.sleep(0.2)
            print("Die richtige Zahl waere {}.".format(self.zzahl))
            print("{}, Möchtest du ein weiteres Spiel (J/N)?".format(self.spielername))
            self.new_game()
        return True
   
    def win_check(self):
        """Die Abfrage ob Spieler gewonnen hat oder verfehlt hat."""
        while True:
            if self.unit_test == True:
                break
            if self.vspiel == self.zzahl:
                print("Glückwunsch,{}, das ist richtig! Möchtest du ein weiteres Spiel (J/N)?".format(self.spielername))   
                self.new_game()
                                  
            elif self.vspiel != self.zzahl:
                if self.vspiel < self.zzahl:
                    print("Leider falsch, meine Zahl ist größer.")
                    break
                elif self.vspiel > self.zzahl:
                    print("Leider falsch, meine Zahl ist kleiner.")
                    break
        return True
   
    def number_question(self):
        """Die Abfrage für die Zahlen."""
        while True:
            if self.unit_test == True:
                break
            time.sleep(0.1)                
            print("Hallo {}, {}-ter Versuch welche Zahl habe ich mir gedacht?".format(self.spielername, self.counter))
            
            #Versucht nur Zahlen als Werte zu nehmen
            try:                            
                self.vspiel = int(raw_input())
            except ValueError: 
                print("Bitte eine Zahl eingeben!")
            else: 
                break
        return True
   
    def close_game(self):
        """Ruft SystemExit auf um das Programm ordentlich zu schließen."""
        if self.unit_test == True:
            return True
        raise SystemExit
    
    def new_game (self):
        """Abfrage für ein neues Spiel"""
        while True:
            if self.unit_test == True:
                break
            self.newgamepl = raw_input()
            if self.newgamepl in ("J", "j"):
                self.counter = 0
                self.new_number()
                self.ratespiel()
                break
            if self.newgamepl in ("N", "n"):
                self.close_game()
            else:
                print("Bitte nur J oder N schreiben!")
        return True  
    
if __name__ == "__main__":
    game = Ratespiel() 
    game.start()
    