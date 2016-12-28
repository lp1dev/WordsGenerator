## Words Generator

### Version 0.0.6

Wordgen - Words generator using pseudo random generation.

It is a HTTP API to generate random letters associations according to a list of rules, the goal is to be able to build an entire dictionnary of meaningful words of a randomly built language.

### Working

- HTTP API with the following routes :
  - GET / : Generates a word of a random length with an audio output
  - GET /generate/{length} : Generates a word of a given length

### TODO

- Store the created words and the associated outputs
- Generate a definition for each word

### Prequisites

- Python 3.4+
- Flask
- festival

### Install

With Python-Pip installed

pip install -r requirements.txt

### Usage

python wordgen.py or chmod +x wordgen.py && ./wordgen.py to run the API.

### Rules syntax

The rules for the words generation are stored in the rules.py file.

They are written in a Python syntax and evaluated using eval* in the code.

Every rule must concern 'new_letter', since it is the variable component.

You can access the following objects and methods :

- word (the whole word minus the new letter)
- new_letter (the letter to be added)
- last_letter (the last letter of the word) (usable only if len(word) > 0)
- vowels (an array of all the vowels)
- consonants (an array of all the consonants)
- self.num_vowels(word)
- self.num_consonants(word)

*Since the rules are evaluated using eval(), YOU MUST NOT use the generator on an environment containing sensitive data and only give access to the rules to restricted authorized users !*