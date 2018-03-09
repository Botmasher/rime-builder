import os
import random
import re

class InitialAPI:
	vowel_tag = "{$VOWEL}" 	# match without linear vowel search 
	vowels = []
	# memoize
	initials_per_word = {}	# associate each word with its initial
	words_per_initial = {} 	# associate each initial with a list of words
	
	def __init__(self, dict_dir, dict_file):
		self.matches = []
		self.dict_path = self.join_path(dict_dir, dict_file)
		self.vowels_path = self.join_path(dict_dir, "cmudict-0.7b.phones")
		self.load_vowels(self.vowels_path)

	def join_path(self, path, file_name):
		return os.path.join(os.getcwd(), path, file_name)

	def load_vowels(self, path):
		with open(path, "r") as file:
			for line in file:
				phone, feature = line.split()
				feature == "vowel" and self.vowels.append(phone)
		return True

	def check_for_pretty_word(self, word):
		punctuation = [".", ":", ";", "!", "?", "*", "(", ")", ",", "'", "/", "*", "$", "#", "@"]
		if len(word) < 2: return False
		for char in word:
			if char in punctuation: return False
		return True

	def select_random_match(self, initial, word, timeout=999):
		if timeout < 1 or len(self.words_per_initial[initial]) < 1:
			return None
		match = random.choice(self.words_per_initial[initial])
		if match != word: return match
		return self.select_random_match(initial, word, timeout-1)

	def add_match(self, match):
		self.matches.append(match)
		return True

	def reset_matches(self):
		self.matches = []
		return True

	def store_matches(self, word, initial):
		self.initials_per_word[word] = initial
		self.words_per_initial[initial] = self.matches
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
			return [self.vowel_tag]
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
		with open(self.dict_path, "r") as file:
			for line in file:
				line_items = line.split(" ")
				line_word = line_items[0]
				line_phonemes = line_items[2:]
				line_initial = self.trim_syllable_to_initial(line_phonemes)
				# search valid entries for a match
				if line_initial and line_initial == word_initial:
					self.check_for_pretty_word(line_word) and self.add_match(line_items[0])
		return word_initial

	def transliterate_word(self, word):
		"""
		Input: 	string spelling a single word
		Return: sequential list of phonemes in that word
		"""
		word_phonemes = []
		capsed_word = word.upper() 						# resource headwords are all uppercase
		with open(self.dict_path, "r") as file:
			for line in file:
				headword = line.split(" ")[0]
				# CMU headwords ending in homonym count
				if re.match(r".*\([0-9]+\)", headword): headword = headword.split("(")[0]
				# match given word to headword
				if capsed_word == headword:
					candidate_phonemes = line.split(" ")[2:]
					vowels = [s for s in candidate_phonemes if s[:2] in self.vowels]
					# one syllable
					if vowels != [] and len(vowels) == 1: return candidate_phonemes
		return word_phonemes

	def find_and_store_matches(self, word):
		word_phonemes = self.transliterate_word(word)
		if word not in self.initials_per_word:
			word_initial = self.find_matches(word_phonemes)
			word_initial is not None and self.store_matches(word, " ".join(word_initial))
		return True

	def rhyme_initial(self, word):
		self.reset_matches()
		# memoization for searched initial rhymes
		word not in self.initials_per_word and self.find_and_store_matches(word)
		if word not in self.initials_per_word: return None
		initial = self.initials_per_word[word]
		match = self.select_random_match(initial, word)
		if match is not None and initial == self.vowel_tag:
			return "%s%s" % (match, " (initial vowel/glottal)")
		return match
