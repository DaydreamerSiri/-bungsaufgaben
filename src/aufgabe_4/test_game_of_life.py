#-*- coding: UTF-8 -*-
'''
Created on 15.08.2018

@author: Sehri Singh
'''
import unittest
from aufgabe_4.game_of_life import GameOfLife , Field
from copy import deepcopy
class Test(unittest.TestCase):


    def setUp(self):
        self.empty_cells = [
            [0, 0, 0],
            [0, 0, 0], 
            [0, 0, 0],
            ]
        self.test_cells = [
            [1, 0, 0],
            [1, 1, 0], 
            [2, 1, 0],
            ]
        self.bad_cells_1 = [
            [1, 0, 0],
            [1, 1], 
            [0, 1, 0],
            ]
        self.bad_cells_2 = [
            [1, 0, 0],
            [1, 1, 3], 
            [0, 1, 0],
            ]
        self.next_cells = [  #neues Feld für next_life_step
            [1, 1, 0],
            [1, 1, 0],
            [1, 1, 0],
            ]
    def tearDown(self):
#         self.game = None
        pass

    def test_field(self):
        """Test Field class core functionality."""
        empty_cells = self.empty_cells
        test_cells = self.test_cells
        bad_cells_1 = self.bad_cells_1
        bad_cells_2 = self.bad_cells_2
 
        field = Field(3, 3)
        self.assertEqual(field.get_cells(), empty_cells, "Fields are initialized with empty cells")
        self.assertEqual(field.get_cells(), field.cells)
        self.assertTrue(field.is_empty())

        self.assertEqual(field.width, 3)
        self.assertEqual(field.height, 3)

        field_2 = Field(initial_state=test_cells)
        field_3 = Field(initial_state=test_cells)

        assert field_2 is not field_3
        assert field_2 == field_3
        assert field_2 is not field
        assert field_2 != field

        self.assertEqual(field_2.width, 3)
        self.assertEqual(field_2.height, 3)
        self.assertEqual(field_2.get_live_count(), 4)

        field_2.clear()
        self.assertTrue(field_2.is_empty())
        self.assertTrue(field_2 is not field)
        self.assertEqual(field_2, field)
        self.assertEqual(field_2, empty_cells)

        field_2.copy_from(field_3)
        self.assertFalse(field_3.is_empty()) 
        self.assertFalse(field_2.is_empty()) 
        assert field_2 is not field_3
        assert field_2 == field_3

        # Copy constructor
        field_4 = Field(initial_state=field_3)
        assert field_4 is not field_3
        assert field_4 == field_3

        # Validations
        with self.assertRaises(Exception):
            field = Field()
 
        with self.assertRaises(Exception):
            field = Field(initial_state=test_cells, width=4)
 
        with self.assertRaises(Exception):
            field = Field(initial_state=test_cells, height=4)

        with self.assertRaises(ValueError):
            field = Field(initial_state=bad_cells_1)

        with self.assertRaises(ValueError):
            field = Field(initial_state=bad_cells_2)

        # is_alive
        self.assertEqual(field_3.is_alive(0, 0), True)
        self.assertEqual(field_3.is_alive(2, 0), False)
        self.assertEqual(field_3.is_alive(1, 1), True)
        self.assertEqual(field_3.is_alive(-1, -1), False)
        self.assertEqual(field_3.is_alive(8, 0), False)

        # get_neighbour_amount
        count = field_3.get_neighbour_amount(1, 1)
        self.assertEqual(count, 3)
        
        count = field_3.get_neighbour_amount(0, 0)
        self.assertEqual(count, 2)
        
        with self.assertRaises(Exception):
            field_3.get_neighbour_amount(-1, -2)
        with self.assertRaises(Exception):
            field_3.get_neighbour_amount(-1, -3)


    def test_game(self):
        """Test GameOfLife class core functionality."""
        empty_cells = self.empty_cells
        test_cells = self.test_cells
        bad_cells_1 = self.bad_cells_1
        bad_cells_2 = self.bad_cells_2
        next_cells = self.next_cells
        
        # Random init
        game = GameOfLife(3, 3)

        self.assertTrue(isinstance(game.field, Field))
        self.assertTrue(isinstance(game.get_state(), Field))

        # Pre-init
        field = Field(initial_state=test_cells)
        game = GameOfLife(initial_field=field)

        self.assertEqual(game.get_generation_index(), 0)
        self.assertEqual(game.get_initial_field(), field)
        self.assertEqual(game.get_field(), field)
        self.assertEqual(game.get_live_count(), 4)

        # Generate
        game.test_next_life_step()

        self.assertEqual(game.get_generation_index(), 1)
        self.assertEqual(game.get_initial_field(), field)
        self.assertNotEqual(game.get_field(), field)
        self.assertEqual(game.get_live_count(), 6)

        self.assertEqual(game.get_field(), next_cells) #überprüfung für next_life_step


    # def test_basic(self):
        
    #     initial_state = [
    #         [1, 0, 0],
    #         [1, 1, 0],
    #         [0, 0, 1],
    #         ]

    #     self.assertEqual(initial_state[0][0], Field.PLANT)

    #     field = Field(3, 3)
        
    #     game = GameOfLife(initial_field=field)
        
    #     state = game.get_cells()
        
    #     state[0][0] = Field.PLANT
    #     state[1][1] = Field.PLANT
    #     state[1][0] = Field.PLANT
    #     state[2][2] = Field.PLANT
        
    #     self.assertEqual(state, initial_state)
    #     self.assertEqual(field.width, 3)
    #     self.assertEqual(field.height, 3)

    #     initial_state[1][1] = 0
    #     self.assertNotEqual(state, initial_state)
                
    #     self.assertEqual(state[1][0], Field.PLANT)
    #     self.assertEqual(state[2][0], Field.FREECELL)

    #     field.field[0][0] = Field.PLANT
    #     field.field[1][1] = Field.PLANT
    #     field.field[1][0] = Field.PLANT
    #     field.field[2][2] = Field.PLANT
        
    #     self.assertEqual(field.is_alive(0, 0), True)
    #     self.assertEqual(field.is_alive(2, 0), False)
    #     self.assertEqual(field.is_alive(1, 1), True)
    #     self.assertEqual(field.is_alive(-1, -1), False)
    #     self.assertEqual(field.is_alive(8, 0), False)
        
        
    #     count = field.get_live_count()
    #     self.assertEqual(count, 4)
        
    #     count = field.get_neighbour_amount(1, 1)
    #     self.assertEqual(count, 3)
        
    #     count = field.get_neighbour_amount(0, 0)
    #     self.assertEqual(count, 2)
        
    #     with self.assertRaises(Exception):
    #         field.get_neighbour_amount(-1, -2)
    #     with self.assertRaises(Exception):
    #         field.get_neighbour_amount(-1, -3)
    #     return


    # def test_cells_internal(self):
    #     initial_state = [
    #             [0, 0, 0],
    #             [0, 1, 0],
    #             [1, 1, 1],
    #         ]
         
    #     self.assertEqual(initial_state[0][0], Field.FREECELL)
         
    #     new_Field = Field(width=3, height=3)


    #     new_Field.create_empty()
        
    #     state = new_Field.get_state()
         
    #     self.assertEqual(state, new_Field.field)
         
    #     self.assertEqual(new_Field.width, 3)
    #     self.assertEqual(new_Field.height, 3)
         
    #     self.assertEqual(state[1][0], Field.FREECELL)
    #     self.assertEqual(state[2][0], Field.FREECELL)
        
    #     new_Field.field[1][1] = Field.PLANT
    #     new_Field.field[2][1] = Field.PLANT
    #     new_Field.field[2][0] = Field.PLANT
    #     new_Field.field[2][2] = Field.PLANT
        
    #     self.assertEqual(state, initial_state)
        
           
           
    # def test_cells_environment(self):
    #     """ """
    #     empty_cells = [
    #         [0, 0, 0],
    #         [0, 0, 0], 
    #         [0, 0, 0],
    #         ]
 
    #     field = Field(width=3, height=3)
    #     field.create_empty() 
         
    #     self.assertEqual(field.width, 3)
    #     self.assertEqual(field.height, 3)
         
    #     self.assertEqual(field.get_state(), empty_cells)
 
    #     self.assertEqual(field.get_live_count(), 0)
         
         
    # def test_cells_unicode(self):
        
    #     field = Field(3, 3)
    #     field.create_empty()
        
    #     game = GameOfLife(initial_field=field)
    #     state = game.get_state()
        
    #     initial_start = [
    #             [0, 0, 0],
    #             [0, 0, 0],
    #             [0, 0, 0],
    #             ] 
        
    #     initial_unicode = [
    #                 [" ",  u"\U0001F33B", u"\U0001F33B"],
    #                 [" ",  u"\U0001F33B", u"\U0001F33B"],
    #                 [" ",  u"\U0001F33B", u"\U0001F33B"],
    #             ]
        
    #     self.assertEqual(state, initial_start) 
         
        
    #     field.field[0][1] = Field.PLANT
    #     field.field[0][2] = Field.PLANT
    #     field.field[1][1] = Field.PLANT
    #     field.field[1][2] = Field.PLANT
    #     field.field[2][1] = Field.PLANT
    #     field.field[2][2] = Field.PLANT
        
    #     self.assertEqual(field._unicode_decoder(), initial_unicode)
        
    # def test_save_presets(self):
        
    #     new_Field = Field()
    #     empty_cells = new_Field.create_empty(3, 3)
    #     self.assertEqual(empty_cells, [[0, 0, 0],
    #                                    [0, 0, 0], 
    #                                    [0, 0, 0]
    #                                    ])
        
    #     save = new_Field.save()
    #     self.assertNotEqual(save, 0)
        
    #     #next_state = game.get_state()
    #     # self.assertEqual(next_state, [
    #     #    [1, 1, 0],
    #     #    [1, 1, 0],
    #     #    [0, 1, 1],
    #     #    ])
        

if __name__ == "__main__":
    unittest.main()