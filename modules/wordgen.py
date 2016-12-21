from sys import exit
from random import randrange
from modules.colors import lettersColors
from rules import wordRules

vowels = "aeiouy"
consonants = "bcdfghjklmnpqrstvwxyz"
letters = vowels + consonants

class WordGen(object):
  def     usage(self):
    return 0
  
  def num_vowels(self, word):
    total = 0
    for letter in word:
      if letter in vowels:
        total += 1
    return total
  
  def num_consonants(self, word):
    total = 0
    for letter in word:
      if letter in consonants:
        total += 1
    return total

  def is_rules_compliant(self, length, word, new_letter):
    if len(word):
      last_letter = word[len(word) - 1]
    for rule in wordRules:
      try:
        if not eval(rule):
          return False
      except SyntaxError as e:
        exit(e)
    return True

  def colorize(self, word):
    output = ""
    for letter in word:
      if letter in lettersColors.keys():
        output += '<i style="color:%s">%s</i>' %(lettersColors[letter], letter)
      else:
        output += letter
    return output

  def colors_only(self, word):
    output = ""
    for letter in word:
      if letter in lettersColors.keys():
        output += '<i style="color:%s">%s</i>' %(lettersColors[letter], '#')
      else:
        output += letter
    return output    
  
  def index(self, length=randrange(1, 26), word=""):
    word = self.generate_word(int(length), word)
    return self.colorize(word)

  def generate_word(self, length=randrange(1, 26), word=""):
    length=int(length)
    if len(word) == length:
      return word
    new_letter = letters[randrange(2, len(letters))]
    if self.is_rules_compliant(length, word, new_letter):
      word += new_letter
    return self.generate_word(length, word)
