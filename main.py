#!/bin/python

from sys import exit
from random import randrange
from rules import wordRules

vowels = "aeiouy"
consonants = "bcdfghjklmnpqrstvwxyz"
letters = vowels + consonants

def     usage():
  return 0

def num_vowels(word):
  total = 0
  for letter in word:
    if letter in vowels:
      total += 1
  return total

def num_consonants(word):
  total = 0
  for letter in word:
    if letter in consonants:
      total += 1
  return total

def is_rules_compliant(length, word, new_letter):
  for rule in wordRules:
    try:
      if not eval(rule):
        return False
    except SyntaxError as e:
      exit(e)
  return True

def generate_word(length, word=""):
  if len(word) == length:
    return word
  new_letter = letters[randrange(2, len(letters))]
  if is_rules_compliant(length, word, new_letter):
    word += new_letter
  return generate_word(length, word)

def	main():
  wordlength = randrange(2, len(letters))
  print(generate_word(wordlength))
  return 0

if __name__ == '__main__':
  main()
