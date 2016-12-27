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
  length = wordgen.generate_length()
  return wordgen.index(length)

@app.route('/generate/<length>')
def index_length(length):
  try:
    return wordgen.index(int(length))
  except Exception as e:
    return "The parameter must be a valid number"

@app.route('/colorize/<word>')
def colorize_word(word):
  return wordgen.colorize(word)

@app.route('/colors_only/<word>')
def colors_only(word):
  return wordgen.colors_only(word)

def	main():
  app.run(host=host, port=port)

if __name__ == '__main__':
  main()
