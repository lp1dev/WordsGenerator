#!/bin/python

from random import randrange

alpha = "abcdefghijklmnopqrstuvwxyz"

def     usage():
  return 0

def generate_word():
  wordlength = randrange(2, len(alpha))
  word = ""
  i = 0
  while i < wordlength:
    word += alpha[randrange(2, len(alpha))]
    i += 1
  return word

def	main():
  print(generate_word())
  return 0

if __name__ == '__main__':
  main()
