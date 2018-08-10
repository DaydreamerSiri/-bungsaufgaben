# coding=<UTF-8>
'''
Created on 06.08.2018

@author: Sehri Singh
This program just counts the lines,letters and words in a specific File.
'''
from collections import OrderedDict
from _collections import defaultdict
from string import ascii_lowercase
import argparse
class Analyzer(object):
    """Class for the File analysing."""
    def __init__(self):
        self.a = ""
     
    def lines(self, file_name):
        """counts the lines.
        
        Args:
            file_name(str)
                Name of the input File
            
         
        """
        self.filereader = open(file_name, "r")
        #get the length of the lines
        amount_lines = len(self.filereader.readlines())
        print('{} Zeilen insg.'.format(amount_lines))
        
        return amount_lines
    
    def letters(self, file_name):
        """counts the letters.
        
        Args:
            file_name(str)
                Name of the input File
        """
        self.filereader = open(file_name, "r")
        #get the length of the letters
        amount_letters = len(self.filereader.read())
        
        print('{} Buchstaben insg.'.format(amount_letters))
        
        return amount_letters
    
    def words(self, file_name):
        """counts the words.
        
        Args:
            file_name(str)
                Name of the input File
        Returns:
            var words contains the amount of words
        """
        self.filereader = open(file_name,"r")
        letters = self.filereader.read()
        
        #splits now all the Words
        words = len(letters.split())
        
        print('{} Woerter insg.'.format(words))
        
        return words
    def most_words(self, file_name):
        """counts the words and list the highest most counted words.
        Args:
            file_name(str)
                Name of the input File
                
        Returns:
            max([int]) of [v] list
            
        """
        #open the File in self.filereader()
        self.filereader = open(file_name, "r")
        a = self.filereader.read()
        wordcount = {}
        
        #split the words into the {WORD : COUNT}
        for word in a.split():
            if word not in wordcount:
                wordcount[word] = 1
            else:
                wordcount[word] += 1
        #sorts the Words, changes the Key/Value into {COUNT : WORD} and gets the highest Count
        od = OrderedDict(sorted(wordcount.iteritems(), key=lambda(k,v):(v,k), reverse= True))
        list_test = []
        for k, v in od.items()[:10]:
            list_test.append(v)
            print k, v
        #print list_test
        return max(list_test)
    def count_words(self, file_name, top=10):
        """Count the words and list the highest most counted words.

        Args:
            file_name (str): 
                Name of the input file
            top [int]: 
                Name of the input file
        Returns:
            {list} Top-ten list of (COUNT, WORD) tuples
        """
        self.filereader = open(file_name, "r")
        
        # Read input file and split to words
        text = self.filereader.read()
        word_list = text.split()
        
        # Count word occurrences 
        word_dict = defaultdict(int)
        for word in word_list:
            word_dict[word] += 1
        
        # Convert into a list of (COUNT, WORD) tuples
        count_list = [ (e[1], e[0]) for e in word_dict.iteritems() ]
        
        topmost = sorted(count_list, reverse=True)[:top]
        print topmost
        return topmost    
    
    def count_digits(self,file_name):
        """ Counts all the letters and returns the most used letters.
        Args:
            file_name(str):
                Name of the input file
        Returns:
            [list] of with (keys,values), items
        """
        pl_string = "++++++++++"
        
        #creates an defaultdict named counter
        counter = defaultdict(int)
        #opens file_name(str) and counts all the lowercase letters in it
        with open(file_name, "r") as f: 
            for line in f:
                for letter in line.lower():
                    if letter in ascii_lowercase:
                        counter[letter] += 1
        #get the values of counter sorted
        values = sorted(counter.values())
        #determines the highest value of values
        max_value = max(values)
        #determines the range of class_range
        class_range = round(float(len(values)) / 10)
        #determines the range of the list
        class_list = values[0::int(class_range)]
        #copy of the defaultdict Counter(int)
        plus_dict = counter.copy()
        #sorts the items and exchanges the Keys and Values
        for key, value in sorted(counter.iteritems(), key=lambda (k,v): (v,k), reverse=True):
            if value == max_value:
                plus_dict[key] = pl_string
            else:
                cl_nums = 0
                for cl in class_list:
                    cl_nums += 1
                    if value <= cl:
                        plus_dict[key] = pl_string[:cl_nums]
                        break
            #print key, value
        #prints the highest letter
        list_test = []
        for keys,values in sorted(plus_dict.items()):
            list_test.append((keys,values))
            print "{} {} {} +-Zeichen".format(keys,values,len(values))
        return list_test
        
    def start(self,file_name):
        """ a function to starts all other functions.
        Args:
            file_name(str)
                Name of the input file
        Returns:
            bool started as True
        """
        started = True
        self.letters(file_name)
        self.lines(file_name)
        self.words(file_name)
        self.most_words(file_name)
        self.count_digits(file_name)
        if started:
            return started
    def commandlines(self,file_name):
        """ a function for the commandlines.
        Args:
            file_name(str)
                Name of the input File for Compiling 
        Returns:
            a is_active Boolean
                    """
        #initialise new Commands for version,verbose,out,input and clear.
        new_parse = argparse.ArgumentParser(description="File Analyzer")
        new_parse.add_argument("--version", action="version", version="unstable_branch", help="prints current Version name")
        new_parse.add_argument("--verbose", action="store_true", help="prints out Developer name")
        new_parse.add_argument("--out", action="store", type=argparse.FileType("w"), metavar="File_Name", help="[File_Name] needed", dest="file_name2")
        new_parse.add_argument("--input", action="store", type=str, metavar="File_Name", help="[File_Name] needed", dest="file_name") 
        new_parse.add_argument("--clear", action="store", type=argparse.FileType("w"), metavar= "File_Name", help="[File_Name].txt to clear text", dest="clear")   
        args = new_parse.parse_args()
        #prints out the available options
        new_parse.print_help()
        #if verboose executed prints out extra informations
        if args.verbose:
            print self.start(file_name)
            print "Programm geschrieben von: Unbekannt"
        #if --out "[File_Name].txt" executed the informations get stored in a new created / existing [File_Name].txt.
        if args.file_name2:
                context = self.letters(file_name)
                context2 = self.lines(file_name)
                context3 = self.words(file_name)
                context4 = self.most_words(file_name)
                context5 = self.count_digits(file_name)
                args.file_name2.write("erster Test: {}-Buchstaben".format(context))
                args.file_name2.write("\nzweiter Test: {}-Zeilen".format(context2))
                args.file_name2.write("\ndritter Test: {}-Woerter".format(context3))
                args.file_name2.write("\nvierter Test: {}-Das meist gezaehlte Wort".format(context4))
                args.file_name2.write("\nfuenfter Test: {}-Die meist gezaehlte Buchstaben".format(context5))
                args.file_name2.write("\nBei weiteren Fragen wenden Sie sich zum ihren Arzt oder Apotheker!")
                args.file_name2.write("\nProgramm geschrieben von: Unbekannt")
        #if --in "[File_Name].txt" executed the informations get stored for a new input File in a new created / existing [File_Name].txt.
        if args.file_name:
            #calls function with [File_Name]
            self.letters(args.file_name)
            self.lines(args.file_name)
            self.words(args.file_name)
            self.most_words(args.file_name)
            self.count_digits(args.file_name)
            #creates new With Method with a new method f.
            with open(args.file_name,"a") as f:
                f.write("\nerster Test: {}-Buchstaben".format(self.letters(args.file_name)))
                f.write("\nzweiter Test: {}-Zeilen".format(self.lines(args.file_name)))
                f.write("\ndritter Test: {}-Woerter".format(self.words(args.file_name)))
                f.write("\nvierter Test: {}-Das meist gezaehlte Wort".format(self.most_words(args.file_name)))
                f.write("\nfuenfter Test: {}-Die meist gezaehlte Buchstaben".format(self.count_digits(args.file_name)))
                f.write("\nBei weiteren Fragen wenden Sie sich zum ihren Arzt oder Apotheker!")
                f.write("\nProgramm geschrieben von: Unbekannt")
        # if --clear [File_name] executed the [File_Name] texts gets blank.
        if args.clear:
            args.clear.write("")
if __name__ == '__main__':
#     d = {"a": 1, "b": 2, "c": 3}
# 
#     x = [ (e[1], e[0]) for e in d.iteritems() ]
#     print x
    
    analyze = Analyzer()
    analyze.commandlines("testing.txt")
