"""Word Finder: finds random words from a dictionary."""
import random

class WordFinder:
    def __init__(self, file):
        dictFile = open(file)
        self.words = self.parse(dictFile)
        print (f"{len(self.words)} words were read.")

    def parse(self, dictFile):
        return [w.strip() for w in dictFile]

    def random(self):
        return random.choice(self.words)

class SpecialWordFinder(WordFinder):
    def parse(self, dict_file):
        return [w.strip() for w in dict_file
            if w.strip() and not w.startswith("#")]