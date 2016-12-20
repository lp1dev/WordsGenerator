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
  return wordgen.index()

@app.route('/<length>')
def index_length(length):
  return wordgen.index(int(length))

def	main():
  app.run(host=host, port=port)

if __name__ == '__main__':
  main()
