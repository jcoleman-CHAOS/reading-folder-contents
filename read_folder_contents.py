'''
Published by: James Coleman
Date: May 1 2017

Example:
>>>folder = Folder()
>>>folder._print()
'''

from os import walk, getcwd, rename, path, mkdir
from termcolor import colored

# Where you want to import files from
source_directory = '/your/path/'

# An object to contain all functions
class Folder:
    def __init__(self):
        self.dirpath = []
        self.dirnames = []
        self.filenames = []

        self.select_files = []

        self.gen_results()

    def gen_results(self):
        for (dirpath, dirnames, filenames) in walk(source_directory):
            # Load response from walk
            self.dirpath.extend(dirpath)
            self.dirpath = "".join(self.dirpath)
            self.filenames.extend(filenames)
            self.dirnames.extend(dirnames)
            break

        # remove hidden
        self.filenames = [i for i in self.filenames if i[0] != "."]
        self.dirnames = [i for i in self.dirnames if i[0] != "."]

    def update(self):
        self.dirpath = []
        self.dirnames = []
        self.filenames = []

        self.gen_results()

    def _print(self):
        print colored('Path:', 'green')
        print self.dirpath
        print colored('Folders:', 'cyan')
        for folder in self.dirnames:
            print '\t' + colored(folder, 'blue')
        print colored('Files:', 'red')
        for _file in self.filenames:
            print '\t' + _file

    def selective_suffix(self, _suffix):
        self.update()
        self.select_files = [_f for _f in self.filenames if _suffix in _f]
        return self.select_files
