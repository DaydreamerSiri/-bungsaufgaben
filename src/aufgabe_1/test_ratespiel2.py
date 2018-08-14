# coding=<UTF-8>
'''
Created on 06.08.2018

@author: Sehri Singh
This program just counts the lines,letters and words in a specific File.
'''
from ratespiel2 import Ratespiel
import unittest

class Test(unittest.TestCase):
    def setUp(self):
        self.test = Ratespiel()
        
        pass

    def tearDown(self):
        pass

    def test_aufgabe1(self):
        """ tests modules."""
        self.test.unit_test = True
        # tests the the game
        res = self.test.ratespiel()
        self.assertEqual(res, True)
        
        res = self.test.start()
        self.assertEqual(res, True)
       
        res = self.test.number_question()
        self.assertEqual(res, True)
        
        res = self.test.lose_check()
        self.assertEqual(res, True)
       
        res = self.test.close_game()
        self.assertEqual(res, True)
       
        res = self.test.new_number()
        self.assertEqual(res, True)
       
        res = self.test.win_check()
        self.assertEqual(res, True)
        
        res = self.test.new_game()
        self.assertEqual(res, True)
if __name__ == "__main__":
    unittest.main() 
    