#Conditions for a word to be invalid
wordRules = {
    "len(word) and new_letter == last_letter",
    "len(word) > 2 and self.num_vowels(word) < len(word) / 3 and new_letter not in vowels",
    "len(word) > 1 and self.num_consonants(word) == len(word) and new_letter in consonants"
}
