"""def commandlines(self):
         a function for the commandlines.
        Args:
            file_name(str)
                Name of the input File for Compiling 
        Returns:
            a is_active Boolean
                    
        #initialise new Commands for version,verbose,out,input and clear.
        new_parse = argparse.ArgumentParser(description="Game_of_Life")
        new_parse.add_argument("--version", action="version", version="latest_branch", help="prints current Version name")
        new_parse.add_argument("--verbose", action="store_true", help="prints out Developer name")
        new_parse.add_argument("--out", action="store", metavar="File_Name", help="tba", dest="file_name2")
        new_parse.add_argument("--input", action="store", type=str, metavar="File_Name", help="tba", dest="file_name") 
        new_parse.add_argument("--clear", action="store", metavar= "File_Name", help="--clear to clear Screen", dest="clear")
        new_parse.add_argument("--stop", action="store")   
        args = new_parse.parse_args()
        #prints out the available options
        new_parse.print_help()
        #if verboose executed prints out extra informations
        if args.verbose:
            print "Programm geschrieben von: Sehri Singh"
        if args.clear:
            self.ed_ext.clean_console()
        if args.stop:
            self.ed_ext.clean_exit()"""
            
if __name__ == "__main__":
    black_square = u"\u25a0"
    print black_square