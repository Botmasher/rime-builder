import os
import random

# TODO account for cases with 0 initial (only main vowel)
# TODO account for searched headword not in dictionary

class InitialAPI:
	
	checked_words = []

	def __init__(self, path, file):
		self.matches = []
		self.path = os.path.join(os.getcwd(), path, file)
		# TODO fetch vowels from CMU: http://svn.code.sf.net/p/cmusphinx/code/trunk/cmudict/cmudict-0.7b.phones
		self.vowels = ["AA", "AE", "AH", "AO", "AW", "AY", "EH", "ER", "EY", "IH", "IY", "OW", "OY", "UH", "UW"]

	def find_one_syllable_initial(self, phonemes):
		"""
		Input:	sequential list of phonemes in a single word
		Return: sequential list of only phonemes in the word's initial
		"""
		vowels = [s for s in phonemes if s[:2] in self.vowels]
		if vowels == [] or len(vowels) > 1:
			return None
		first_vowel_index = phonemes.index(vowels[0])
		initial = phonemes[0:first_vowel_index]
		return initial

	def check_for_pretty_word(self, word):
		punctuation = [".", ":", ";", "!", "?", "*", "(", ")", ",", "'", "/", "*", "$", "#", "@"]
		if len(word) < 2: return False
		for char in word:
			if char in punctuation: return False
		return True

	def select_random_match(self):
		if len(self.matches) > 0:
			return random.choice(self.matches)
		return None

	def add_match(self, match):
		self.matches.append(match)
		return True

	def reset_matches(self):
		self.matches = []
		return True

	def find_initial_match(self, phonemes):
		"""
		Input: 	sequential list of phonemes in a single word
		Return: string of single-syllable word with the same initial
		"""
		word_initial = self.find_one_syllable_initial(phonemes)
		# check target words for single-syllable words with matching initial
		# TODO handle cases where target has no vowel
		with open(self.path, "r") as file:
			for line in file:
				line_items = line.split(" ")
				line_word = line_items[0]
				line_phonemes = line_items[2:]
				line_initial = self.find_one_syllable_initial(line_phonemes)
				# search valid entries for a match
				if line[:3] != ";;;" and line_initial and line_initial == word_initial:
					is_pretty_word = self.check_for_pretty_word(line_word)
					if is_pretty_word: self.add_match(line_items[0])
		return self.select_random_match()

	def transliterate_word(self, word):
		"""
		Input: 	string spelling a single word
		Return: sequential list of phonemes in that word
		"""
		word_phonemes = []
		capsed_word = word.upper() 						# resource headwords are all uppercase
		with open(self.path, "r") as file:
			for line in file:
				if line.split(" ")[0] == capsed_word:
					word_phonemes = line.split(" ")[2:]
		return word_phonemes

	def rhyme_initial(self, word):
		self.reset_matches()
		self.checked_words.append(word)
		word_phonemes = self.transliterate_word(word)
		return self.find_initial_match(word_phonemes)