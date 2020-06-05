import random
import sys
from phrase import Phrase
from phrase import consol_output
from character import Character

class Game():

    def __init__(self,total_lives = 5, *args, **kwargs):
        phrase_1 = 'phrase_1'
        phrase_2 = 'phrase_2'
        phrase_3 = 'phrase_3'
        self.total_lives = total_lives
        self.player_guess = None
        self.phrase_list = [
             phrase_1, phrase_2, phrase_3,
            ]
        self.list_of_phrases = [Phrase(item, self.player_guess, False) for item in self.phrase_list]
        self.selected_phrase = random.choice(self.list_of_phrases)

#        phrase = Phrase(self.player_guess)
        # Phrase(self.selected_phrase, self.player_guess, True)
        print(self.selected_phrase)
        print("{}".format(self.selected_phrase))
        self.__str__()
        self.printing()


    def __str__(self):
        print("{} {}".format(__class__.__name__,self.selected_phrase))

    def printing(self):
#        phrase = Phrase(self.selected_phrase, self.player_guess)
#        print(phrase)
        pass
