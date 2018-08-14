#-*- coding: UTF-8 -*-
'''
Created on 14.08.2018

@author: Sehri Singh
'''

from auto_ratespiel import Ratespiel
from editable_extensions import Editable_extensions
from editable_extensions import time
import re
class Player(object):
    """
    Gibt den Spieler zurück.
    """
    def __init__(self):
        """Initialisiert variablen."""
        self.counter = 0
        self.test_name2 = re.compile("1")
        self.unit_test = False
        self.bot = Ratespiel()
        self.ed_ext = Editable_extensions()
    def player_number_question(self):
        """Die Abfrage für die Zahlen."""
        while True:
            if self.unit_test == True:
                break
            time.sleep(0.1)                
            #Versucht nur Zahlen als Werte zu nehmen
            try:                            
                self.vspiel = int(raw_input())
            except ValueError: 
                print(self.ed_ext.attentions(case=2))
            else: 
                break
        return True
    
    def player_new_game (self):
        """Abfrage für ein neues Spiel"""
        while True:
            if self.unit_test == True:
                break
            self.newgamepl = raw_input()
            if self.newgamepl in ("J", "j"):
                print("{}: Ich will ein neues Spiel anfangen!".format(self.spielername))
                
                break
            if self.newgamepl in ("N", "n"):
                self.close_game()
                print("{}: Ich will dieses Spiel beenden.".format(self.spielername))
            else:
                print(self.ed_ext.attentions(case=1))
        return True
    
    def player_get_name(self):
        """Funktion für den Spielernamen."""
        while True:
            self.spielername = raw_input()
            if self.spielername.isalnum() == True or not self.test_name2.match(self.spielername): 
                if self.spielername.isalpha() == False:
                    print(self.ed_ext.attentions(case=3))
                else:
                    print ("{}: Mein Name lautet {} und Ich werde dich besiegen!".format(self.spielername, self.spielername))
                    break
        return True
    
if __name__ == '__main__':
    player = Player()
    player.player_get_name()
    player.player_new_game()