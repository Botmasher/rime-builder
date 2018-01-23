import os
import random

# TODO account for cases with 0 initial (only main vowel)
# TODO account for searched headword not in dictionary
# TODO account for 

class InitialAPI:
	matched_words = {} 			# memo
	vowel_tag = "{$VOWELS}"
	is_vowel = False

	def __init__(self, path, file):
		self.matches = []
		self.path = os.path.join(os.getcwd(), path, file)
		# TODO fetch vowels from CMU: http://svn.code.sf.net/p/cmusphinx/code/trunk/cmudict/cmudict-0.7b.phones
		self.vowels = ["AA", "AE", "AH", "AO", "AW", "AY", "EH", "ER", "EY", "IH", "IY", "OW", "OY", "UH", "UW"]

	def check_for_pretty_word(self, word):
		punctuation = [".", ":", ";", "!", "?", "*", "(", ")", ",", "'", "/", "*", "$", "#", "@"]
		if len(word) < 2: return False
		for char in word:
			if char in punctuation: return False
		return True

	def select_random_match(self, word):
		if len(self.matched_words[word]) > 0:
			return random.choice(self.matched_words[word])
		return None

	def add_match(self, match):
		self.matches.append(match)
		return True

	def reset_matches(self):
		self.matches = []
		return True

	def store_matches(self, word):
		self.matched_words[word] = self.matches
		return True

	def trim_syllable_to_initial(self, phonemes):
		"""
		Input:	sequential list of phonemes in a single word
		Return: sequential list of only phonemes in the word's initial
		"""
		vowels = [s for s in phonemes if s[:2] in self.vowels]
		# not one syllable
		if vowels == [] or len(vowels) > 1:
			return None
		# zero consonant initial
		if phonemes.index(vowels[0]) == 0:
			return self.vowel_tag
		# cut at first vowel
		initial = phonemes[0:phonemes.index(vowels[0])]
		return initial

	def find_matches(self, phonemes):
		"""
		Input: 	sequential list of phonemes in a single word
		Return: string of single-syllable word with the same initial
		"""
		word_initial = self.trim_syllable_to_initial(phonemes)
		# check target words for single-syllable words with matching initial
		# TODO handle cases where target has no vowel
		with open(self.path, "r") as file:
			for line in file:
				line_items = line.split(" ")
				line_word = line_items[0]
				line_phonemes = line_items[2:]
				line_initial = self.trim_syllable_to_initial(line_phonemes)
				# search valid entries for a match
				if line[:3] != ";;;" and line_initial and line_initial == word_initial:
					if line_initial == self.vowel_tag: self.is_vowel = True
					is_pretty_word = self.check_for_pretty_word(line_word)
					if is_pretty_word: self.add_match(line_items[0])
		return None

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

	def find_and_store_matches(self, word):
		word_phonemes = self.transliterate_word(word)
		self.find_matches(word_phonemes)
		self.store_matches(word)
		return True

	def rhyme_initial(self, word):
		self.reset_matches()
		self.is_vowel = False
		# memoization for searched initial rhymes
		if word not in self.matched_words:
			self.find_and_store_matches(word)
		match = self.select_random_match(word)
		if match and self.is_vowel:
			return "%s%s" % (match, " (initial vowel/glottal)")
		return match
