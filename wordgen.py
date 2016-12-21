#!/bin/python

from flask import Flask
from random import randrange
from modules.wordgen import WordGen

host='0.0.0.0'
port='8083'
wordgen = WordGen()
app = Flask(__name__)

@app.route('/')
def index():
  return wordgen.index(randrange(2, 26))

@app.route('/generate/<length>')
def index_length(length):
  try:
    return wordgen.index(int(length))
  except Exception as e:
    return "The parameter must be a valid number"

@app.route('/colorize/<word>')
def colorize_word(word):
  return wordgen.colorize(word)

def	main():
  app.run(host=host, port=port)

if __name__ == '__main__':
  main()
