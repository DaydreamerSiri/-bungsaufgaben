#-*- coding: UTF-8 -*-
'''
Created on 15.08.2018

@author: Sehri Singh
Dieses Python Programm soll von Conway das Spiel des Lebens simulieren in einem x * y Feld.
'''


import time
import random
from copy import deepcopy
from editable_extensions import Editable_extensions

#■ █
class GameOfLife(object):
    """Klasse für das Game_of_Life Programm."""
    
    
    
    def __init__(self, width=None, height=None, initial_field=None):
        self.ed_ext = Editable_extensions()
        self.generation = 0
        #self.field wird berechnet
        if width is None or height is None:
            if initial_field is None:
                raise ValueError("Attribute has invalid Value")
            else:
                if initial_field is list:
                    self.field = deepcopy(initial_field)
                else:
                    self.field = initial_field
        else:
            self.field = Field(width, height)
            
        #initial field wird initialisiert
        self.initial_field = self.field
        
        return None
    
    def __eq__(self, other_field):
        return self.field.cells == other_field.cells
    
    def initial_field_copy(self):
        """Macht eine blanke Kopie vom initial_Field."""
        initial_field = deepcopy(self.initial_field)
        return initial_field
    
    def start_options(self, width, height):
        """Funktion für die Abfrage der Start-Bedinungen."""
        self.width
    
    def simulation(self):
        """Funktion für die Simulation ohne Spielerinput"""
        new_cycle = deepcopy(self.field)
        for row in range(len(new_cycle.cells)):
            for col in range(len(new_cycle.cells)):
                if new_cycle.cells[row][col] == Field.DEADCELL:
                    new_cycle.cells[row][col] = Field.FREECELL
                if self.field.get_neighbour_amount(col, row) > 3 or self.field.get_neighbour_amount(col, row) < 2:
                    if new_cycle.cells[row][col] == Field.DEADCELL:
                        new_cycle.cells[row][col] = Field.FREECELL
                        
                    if new_cycle.cells[row][col] == Field.PLANT:
                        new_cycle.cells[row][col] = Field.DEADCELL  
                        
                if self.field.get_neighbour_amount(col, row) == 3:
                    if new_cycle.cells[row][col] == Field.DEADCELL:
                        new_cycle.cells[row][col] = Field.PLANT
                    else:
                        new_cycle.cells[row][col] = Field.PLANT
                    
        return new_cycle
    
    def start_simulation(self):
        """Funktion um die Simulation zu starten"""
        self.ed_ext.clean_console()
        print ("\n" * 20)
        self.field.clear()
        self.field.create_enviroment()
        self.field.print_unicode_field()
        time.sleep(1)
        self.next_life_step()
        return True
    
    def next_life_step(self):
        """Funktion für den Zyklus wechsel"""
        while True:
            self.generation += 1 
            self.field.save_presets()
            self.ed_ext.clean_console()
            print ("\n" * 30)
            self.replace()
            self.field.print_unicode_field()
            time.sleep(1)
            if self.field.get_live_count() == 0:
                if self.field.get_dead_count() > 0 :
                    continue
                else:
                    #self.ed_ext.clean_exit()
                    return True
        raise Exception
    
    def test_next_life_step(self):
        self.generation += 1 
        self.field.save_presets()
        self.ed_ext.clean_console()
        print ("\n" * 30)
        self.replace()
        self.field.print_unicode_field()
        time.sleep(1)
        if self.field.get_live_count() == 0:
            if self.field.get_dead_count() > 0 :
                self.test_next_life_step()
            else:
                #self.ed_ext.clean_exit()
                return True
    
    def get_state(self):
        """Funktion um den State auszugeben"""
        if len(self.field.cells) == 0:
            state = self.field.cells
        else:
            state = self.field
        return state
    
    def replace(self):
        """Funktion um den neuen Zyklus zu setzen"""
        self.field = deepcopy(self.simulation())
        return self.field
    
    def get_new_field(self):
        """Funktion um ein neues Field zu erstellen"""
        field = self.cells.field
        return field
    
    def get_generation_index(self):
        """Gibt die Anzahl der Generationen vom self.field wieder"""
        generation_index = self.generation
        return generation_index
    
    def get_initial_field(self):
        """Gibt das gegebene Initial Feld zurück"""
        return self.initial_field
        
    def get_field(self):
        """Gibt Feld an."""
        field = self.field
        return field
    
    def get_live_count(self):
        """Zählt die Zellen von self.field nach lebende Pflanzen."""
        live_amount = 0
        for row in self.field.cells:
            for field in row:
                if field == Field.PLANT:
                    live_amount += 1
                    
        return live_amount
    
#===============================================================================
# Field
#===============================================================================
class Field(object): 
    """Klasse um das Feld zu initialisieren"""
    PLANT = 1 
    FREECELL = 0 
    DEADCELL = 2 
    
    def __init__(self, width=None, height=None, initial_state=None):
        self.width = width
        self.height = height
        if width == None or height == None:
            if initial_state is None:
                raise ValueError("Attribute has invalid Value")  # @@ direktes raise
            else:
                if hasattr(initial_state, "cells") :
                    self.width = self._get_width(initial_state.cells) 
                    self.height = self._get_height(initial_state.cells)
                    self.cells = initial_state.cells
                    self.preset_counter = 0
                else:
                    self.width = self._get_width(initial_state) 
                    self.height = self._get_height(initial_state)
                    self.cells = deepcopy(initial_state)
                    self._check_for_index()
                    self.preset_counter = 0
        else:
            self.cells = []
            self.preset_counter = 0
            self.clear()
            
    def __eq__(self, other):
        """Checkt die eigenen Zellen mit den Anderen"""
        return self.cells == other
    
    def clear(self):
        """Funktion für die Erstellung der Felder."""
        self.cells = []
        for y in range(self.height):
            row = [self.FREECELL] * self.width
            self.cells.append(row)
        return self.cells
    
    def print_field(self):
        """Funktion welches das Feld dekoriert ausgibt"""
        for row in self.cells:
            for cell in row:
                print "|",cell,
            print "|"
        print "Plants alive:", self.get_live_count()
        print "Plants dead:", self.get_dead_count()
        return
    
    def print_unicode_field(self):
        """Gibt das Feld dekoriert mit Unicode Zeichen aus"""
        for row in self._unicode_decoder():
            for cell in row:
                print cell,
            print 
        print "Plants alive:", self.get_live_count()
        print "Plants dead:", self.get_dead_count()
        return

    def get_cells(self):
        """Funktion um den State auszugeben"""
        state = self.cells
        return state
    
    def create_enviroment(self):
        """Funktion damit das Feld eigene Lebewesen generiert"""
        self.get_cells()
        item = random.Random()
#         plant_counter = 0 
        for row in range(len(self.cells)):
            for items in range(len(self.cells)):
#                 if plant_counter == 2:
#                     break
                itemnumber = item.randint(self.FREECELL, self.PLANT)
#                 if itemnumber == self.PLANT:
#                     plant_counter += 1
                self.cells[row][items] = itemnumber
                
        return self.cells
    
    def save_presets(self):
        """Funktion um die Vorgaben anszugeben"""
        self.preset_counter += 1
        with open("presets.txt", "a") as f:
            f.write("Preset {}: ".format(self.preset_counter))
            for row in self.cells:
                f.write(str(row) * 1)
            f.write("\n")
        return True
    
    def save(self):
        """Funktion um jedes einzelne State zu speichern"""
        save = []
        return save
        #u"\u2740"
        
    def _unicode_decoder(self):
        """Funktion um Unicode in Listen wiederzugeben"""
        unicode_field = deepcopy(self.cells)
        
        for row in range(len(unicode_field)):
            for col in range(len(unicode_field)):
                if unicode_field[row][col] == self.FREECELL:
                    unicode_field[row][col] = " "#u"\u25a0"
                elif unicode_field[row][col] == self.PLANT:
                    unicode_field[row][col] = u"\U0001F33B"     
                elif unicode_field[row][col] == self.DEADCELL:
                    unicode_field[row][col] = u"\U0001F940"
                else:
                    raise RuntimeError
        return unicode_field

        
    def get_live_count(self):
        """Funktion um die Anzahl der Lebende Zellen zu bekommen"""
        live_amount = 0
        
        for row in self.cells:
            for field in row:
                if field == Field.PLANT:
                    live_amount += 1
                    
        return live_amount
    
    def get_dead_count(self):
        """Zählt wie viele tote Pflanzen noch verfügbar sind"""
        dead_amount = 0
        for row in self.cells:
            for field in row:
                if field == Field.DEADCELL:
                    dead_amount += 1
        return dead_amount
    pass

    def is_alive(self, x, y):
        """Prüft ob die angegebene Zelle eine Pflanze ist"""
        if y >= 0 and x >= 0 and y < len(self.cells) and x < len(self.cells[0]):
            return self.cells[y][x] == Field.PLANT
        return False
    
#     def is_alive_2(self, x, y):
#         """Prüft ob die angegebene Zelle eine Pflanze ist"""
#         try: 
#             return self.cells[y][x] == Field.PLANT
#         except IndexError:
#             return False
    
    def get_neighbour_amount(self, x, y):
        """Funktion um Nachbarzellen zu zählen.
        Parameters:
            x : Field of X
            y : Field of Y
        Extras:
            AoF = Area_of_Fields
        """
        
        if y < 0 or x < 0 or  y > len(self.cells) or x > len(self.cells[0]) :
            raise IndexError("Out of Field")
        
        neighbour_amount = 0
        #Für die Überschaubarkeit, habe ich anstatt direkt 0 und 1 Sie einer Variable zugewiesen mit einem Passendem Namen 
        Range_of_X = 0
        Range_of_Y = 1
        #Die Range bei der die Felder untersucht werden (Von Oben bis nach unten ohne sich selbst zu untersuchen)
        Area_of_Fields = (
            (x-1, y-1), (x,   y-1), (x+1, y-1),
            (x-1, y),               (x+1, y),   
            (x-1, y+1), (x+1, y+1), (x,   y+1),
            )
        #Hier wird das Area_of_Fields in kleinen Items zerkleinert und das X und Y entsprechend den Parametern zugewiesen.
        for x, y in Area_of_Fields:
            if self.is_alive(x, y):
                neighbour_amount += 1
                
        #print neighbour_amount
        return neighbour_amount
    
    def initial_field_copy(self):
        """Kopiert das initial Field vom Game"""
        initial_field = deepcopy(self.cells)
        return initial_field
    
    def _get_width(self, state):
        """Zählt die Breite nach wenn Initial_State gegeben ist"""
        amount = 0
        is_diameter = 0 
        rows = 0 
        for row in state:
            amount = 0 
            for cell in row:
                amount += 1
            if rows == 1:
                if is_diameter != amount:
                    raise ValueError
            rows += 1 
            is_diameter = amount
             
        if self.width != amount:
            if self.width is None:
                return amount
            else:
                raise ValueError    
            
        return amount
    
    def _get_height(self, state):
        """Zählt die Höhe nach wenn Initial_State gegeben ist"""
        amount = 0 
        for row in state[:][:]: 
            amount += 1
        if self.height != amount:
            if self.height is None:
                return amount
            else:
                raise ValueError
        return amount
    
    def is_empty(self):
        """Überprüft ob das eigene Feld leer ist"""
        diameter = self.width * self.height
        empty_counter = 0
        for row in range(self.height):
            for col in range(self.width):
                if self.cells[row][col] == self.FREECELL:
                    empty_counter += 1
        if empty_counter is diameter:
            return True
        else:
            return False
    
    def copy_from(self, Field):
        """Kopiert ein anderes Feld"""
        self.cells = Field.cells
        return self.cells
    
    def _check_for_index(self):
        """Schaut ob die Größe des Feldes passt."""
        for row in range(self.height):
            for col in range(self.width):
                if self.cells[row][col] is not self.FREECELL:
                    if self.cells[row][col] is not self.PLANT:  
                        if self.cells[row][col] is not self.DEADCELL:
                            raise ValueError("Insert in {}.cells please proper Values".format(self))
        return True
    
if __name__ == '__main__': 
    game = GameOfLife(3, 3)
    game.start_simulation()
    pass