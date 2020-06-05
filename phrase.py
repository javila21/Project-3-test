import re
import copy
from character import Character

"""A list of the phrase where each character is a string"""
character_list = []
"""The phrase that the player sees"""
consol_output = []

# keep your chin up', 'wild at heart', 'hello world', 'embrace the journey',
# 'be the change','focus and win', 'do it now', 'never give up'

phrase_1 = 'keep your chin up'
phrase_2 = 'wild at heart'
phrase_3 = 'hello world'

class Phrase():
    def __init__(self, phrase, player_guess, new_game=False, run_extend=True, *args, **kwargs):
        phrase_1 = 'keep your chin up'
        phrase_2 = 'wild at heart'
        phrase_3 = 'hello world'
        self.phrase = phrase
        self.phrase = []
        for char in phrase:
            self.phrase.append(Character(char, phrase))
        self.new_game = new_game
        self.run_extend = run_extend
        self.player_guess = player_guess
        self.consol_output(phrase)
        if new_game is True:
            print(self.phrase)
            print(phrase)

        #
        # if new_game is True:
        #     character_list.clear()
        #     consol_output.clear()

    """Generates the initial output to be displayed to player"""
    def consol_output(self, character_list):
        if self.run_extend is True:
            consol_output.extend(copy.deepcopy(character_list))
            for n, char in enumerate(consol_output):
                if char != " ":
                    consol_output[n] = "_"
#                    print("{}".format("".join(consol_output)))

# Try def def __str__(self):
#        return "{}: {}".format(__class__.__name__, self.name)
