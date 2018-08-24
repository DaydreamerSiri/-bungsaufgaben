#-*- coding: UTF-8 -*-
'''
Created on 14.08.2018

@author: Sehri Singh
'''
import time
from os import system, name
import emot 
class Editable_extensions(object):
    '''
    Eine Klasse für den späteren Gebrauch.
    '''
    def __init__(self):
        self.a = 0
        
    def raise_new_attentions(self, case):
        """Erzeugt Fehlermeldungen."""
        self.case = case
        case1 = 1
        case2 = 2
        case3 = 3
        attention = "none"
        #Abfrage für die einzelne Fälle /// Die erste If-Abfrage nicht entfernen!
        if self.case >3 or self.case == None or self.case < 1:
            return "ParameterValueError: Range was out of index (case=1<->3)" 
        if self.case == case1:
            attention = ("Bitte nur J oder N schreiben!")
        if self.case == case2:
            attention = ("Bitte eine Zahl eingeben!")
        if self.case == case3:
            attention = ("Bitte nur Buchstaben!")
        
        return attention
    
    def raise_new_exception(self, case):
        """Erzeugt Fehlermeldungen in System"""
        
        if case == 1:
            return IndexError("Error: Out of Area: DEADPOINT reached")
        if case == 2:
            return AttributeError, ValueError("Value or given Attributes are mistaken")
            
    def clean_exit(self):
        """Ruft SystemExit auf um das Programm ordentlich zu schließen."""
        raise SystemExit
    
    def clean_console(self):
        """Damit wird die Konsole gecleaned"""
        if name == 'nt':
            system("cls")
        else:
            system('clear')

    def place_emoji(self, insert_emoji):
        emoji = emot.emoji(insert_emoji)
        return emoji
    
class Editable_extensions_timer(object):    
    def decoration(self):
        """Verschoenert die Ausgabe"""
        
        def wrap():
            print("Jetzt betraegt die Zeit")
            print("========================")
            
            self.texton = self.timenow()
            
            print("========================")
            print("Und alle sind froh darueber")
        return wrap()
    
    def timenow(self):
        """Gibt die Uhrzeit an."""
        print(time.asctime())
        return True
    
    def timer(self):
        """Die Funktion fuer die Uhr"""
        
        while True:
            self.a += 1
            self.dec()
            
            if self.a == 1:
                self.a = 0
                self.time_interval()
                break
            
        return True
    
    def time_interval(self):
        """Der Zeit intervall fuer die Ausgabe"""
        
        while True:
            time.sleep(1)
            self.a += 1
            
            if self.a == 60:
                self.a = 0
                self.timer()
                break
            
        return True
    