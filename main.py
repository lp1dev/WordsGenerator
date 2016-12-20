#!/bin/python

import cherrypy
from random import randrange
from wordgen import WordGen

def	main():
  wordlength = randrange(2, 26)
  cherrypy.server.socket_host = "0.0.0.0"
  cherrypy.quickstart(WordGen())

if __name__ == '__main__':
  main()
