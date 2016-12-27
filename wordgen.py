#!/bin/python

from flask import Flask
from random import randrange
from modules.wordgen import WordGen
from os import path

host='0.0.0.0'
port='8083'
wordgen = WordGen()
app = Flask(__name__)
app._static_folder = path.abspath("/tmp/wordgen/")

@app.route('/audio/<file>')
def audio(file):
  return app.send_static_file('%s' %file)

@app.route('/')
def index():
  length = wordgen.generate_length()
  word = wordgen.generate_word(length)
  audio = wordgen.audio_output(word)
  audio_html = '<br/><audio controls="controls"><source src="%s" type="audio/wav"/></audio>' %audio
  return wordgen.colorize(word) + audio_html

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
