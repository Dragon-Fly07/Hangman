import random

class select_word:
    def __init__(self):
        return
    
    def open_file(self):
        l = []
        with open("src/Words/words.txt", "r") as file:
            l = file.readlines()
        return l[random.randint(0, len(l))]