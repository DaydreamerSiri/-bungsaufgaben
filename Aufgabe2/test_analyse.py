# coding=<UTF-8>
'''
Created on 06.08.2018

@author: Sehri Singh
This program just counts the lines,letters and words in a specific File.
'''
from analyse import Analyzer
import unittest

class Test(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_aufgabe1(self):
        """ tests modules."""
        tests = Analyzer()
        
        # tests the lines of the file
        res = tests.lines("testing.txt")
        self.assertEqual(res, 3)

        # test the amount of words of the file
        res = tests.words("testing.txt")
        self.assertEqual(res, 24)

        #test the amount of letters of the file
        res = tests.letters("testing.txt")
        self.assertEqual(res, 134)
        
        #test the amount of most words occurences
        res = tests.most_words("testing.txt")
        self.assertEqual(res, 3)
         
        #test the counter with the word with the most letters
        res = tests.count_digits("testing.txt")
        testing_list = [('a', '+++'),
                        ('c', '++'),
                        ('d', '+++'),
                        ('e', '++++++++++'),
                        ('h', '+++'),
                        ('i', '+++++'),
                        ('l', '+'),
                        ('m', '+++++++'),
                        ('n', '+++++'),
                        ('o', '++'),
                        ('p', '++'),
                        ('r', '+++'),
                        ('s', '+++++++'),
                        ('t', '+++++'),
                        ('u', '+++++++')
                        ]
        self.assertEqual(res, testing_list)
        
        #test if the programm has started
        res = tests.start("testing.txt")
        self.assertEqual(res, True)

       
if __name__ == "__main__":
    analyse = Analyzer()
    unittest.main() 
    