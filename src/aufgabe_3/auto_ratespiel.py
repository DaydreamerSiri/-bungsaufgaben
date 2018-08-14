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
            break
        time.sleep(0.2)
        self.new_number()
        time.sleep(0.2)
        self.ratespiel()
        return True
    
    def new_number(self):
        """Generiert neue Zahlen für ein neues Spiel."""
        self.counter = 0  
        self.zzahl = random.randint(1, 20)
        time.sleep(0.3)
        print("Bot: Die Würfel sind gefallen...")
        return True
    
    def lose_check(self):
        """checkt ob der counter höher ist als es soll"""
        self.counter += 1
        if self.counter > 5:
            print("Bot: Sie haben verloren.")
            time.sleep(0.2)
            print("Bot: Die richtige Zahl waere {}.".format(self.zzahl))
            print("Bot: {}, Möchtest du ein weiteres Spiel (J/N)?".format(self.spielername))
            self.new_game()
        return True
   
    def win_check(self):
        """Die Abfrage ob Spieler gewonnen hat oder verfehlt hat."""
        while True:
            time.sleep(0.3)
            if self.unit_test == True:
                break
            if self.vspiel == self.zzahl:
                print("Bot: Glückwunsch,{}, das ist richtig! Möchtest du ein weiteres Spiel (J/N)?".format(self.spielername))   
                self.new_game()
                                  
            elif self.vspiel != self.zzahl:
                if self.vspiel < self.zzahl:
                    print("Bot: Leider falsch, meine Zahl ist größer.")
                    break
                elif self.vspiel > self.zzahl:
                    print("Bot: Leider falsch, meine Zahl ist kleiner.")
                    break
        return True
   
    def number_questionbot(self):
        """Die Abfrage für die Zahlen."""
        while True:
            if self.unit_test == True:
                break
            time.sleep(0.2)                
            print("Bot: Hallo {}, {}-ter Versuch welche Zahl habe ich mir gedacht?".format(self.spielername, self.counter))
            
            #Versucht nur Zahlen als Werte zu nehmen
        return True
   
    def close_game(self):
        """Ruft SystemExit auf um das Programm ordentlich zu schließen."""
        if self.unit_test == True:
            return True
        raise SystemExit
    
if __name__ == "__main__":
    game = Ratespiel() 
    game.start()
    