wordRules = {
    "len(word) == 0 or new_letter != word[len(word) - 1]",
    "len(word) < 2 or new_letter in vowels or self.num_vowels(word) >= len(word) / 3",
    "len(word) < 2 or not last_letter or (new_letter in vowels) != (last_letter in vowels)"
}
