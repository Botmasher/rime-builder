import os
import random

# TODO account for cases with 0 initial (only main vowel)
# TODO account for searched headword not in dictionary
# TODO search through multisyllabic rhymes for a one syllable variant, e.g. OUR OUR(1) OUR(2) in CMUdict
# TODO switching between CMU vs datamuse if have internet connection

class LocalEnglishRimeAPI:
	files = {
		'tools': "rimebuilder/tools/",
		'dict': "cmudict-0.7b.txt",
		'phones': "cmudict-0.7b.phones"
	}
	# vowel checks
	vowel_tag = "{$VOWELS}"
	vowel_initial = False
	vowels = []
	# memos
	matched_initials = {}
	matched_finals = {}
	
	def __init__(self):
		self.raw_dict = self.build_path(self.files['tools'], self.files['dict'])
		self.raw_phones = self.build_path(self.files['tools'], self.files['phones'])
		self.vowels = self.fetch_vowels(self.raw_phones)

	def build_path(self, path, file):
		"""Construct full path to a file within current working directory"""
		return os.path.join(os.getcwd(), path, file)

	def fetch_vowels(self, file):
		"""Find and store all vowels found in the CMU English phones list"""
		vowels = []
		with open(file, "r") as file:
			for line in file:
				line_items = line.split()
				line_phone = line_items[0]
				line_type = line_items[len(line_items)-1]
				if line_type.lower() == "vowel": vowels.append(line_phone)
		return vowels

	def check_pretty_word(self, word):
		"""Verify that a word is long, well formatted and contains no special characters"""
		punctuation = [".", ":", ";", "!", "?", "*", "(", ")", ",", "'", "/", "*", "$", "#", "@"]
		if len(word) < 2: return False
		for char in word:
			if char in punctuation: return False
		return True

	def select_random_match(self, items):
		"""Retrieve one random item from a list"""
		if len(items) > 0: return random.sample(items, 1)
		return None

	def select_random_initial_match(self, phones):
		"""Retrieve one stored word rhyming with this initial"""
		return self.select_random_match(self.matched_initials[phones])[0]

	def select_random_final_match(self, phones):
		"""Retrieve one stored word rhyming with this final"""
		return self.select_random_match(self.matched_finals[phones])[0]

	def add_initial_match(self, phones_list, word):
		"""Store this word among list of initial rhymes in phoneme initials map"""
		phones = " ".join(phones_list)
		if phones not in self.matched_initials:
			self.matched_initials[phones] = set()
		self.matched_initials[phones].add(word)
		return True

	def add_final_match(self, phones_list, word):
		"""Store this word among list of final rhymes in phoneme finals map"""
		phones = " ".join(phones_list)
		if phones not in self.matched_finals:
			self.matched_finals[phones] = set()
		self.matched_finals[phones].add(word)
		return True

	def split_initial_final(self, phonemes):
		"""Take a word's phonemes and split the initial from the final rhyme"""
		vowels = [s for s in phonemes if s[:2] in self.vowels]
		# not one syllable
		if vowels == [] or len(vowels) > 1:
			return None
		# zero consonant initial
		if phonemes.index(vowels[0]) == 0:
			initial = [self.vowel_tag]
		else:
			initial = phonemes[:phonemes.index(vowels[0])]
		# split at first vowel
		final = phonemes[phonemes.index(vowels[0]):]
		# remove trailing newline from last phone
		if len(final) > 0: final.append(final.pop().rstrip("\n"))
		return [initial, final]

	def find_matches(self, word_initial, word_final):
		"""Find and store all words rhyming with this initial and all words rhyming with this final"""
		with open(self.raw_dict, "r") as file:
			for line in file:
				line_word, *line_phonemes = line.split()
				line_rimeset = self.split_initial_final(line_phonemes)
				# skip if one syllable or invalid
				if line_rimeset is None or not self.check_pretty_word(line_word): continue
				# search valid entries for a match
				line_initial, line_final = line_rimeset
				line_initial == word_initial and self.add_initial_match(line_initial, line_word)
				line_final == word_final and self.add_final_match(line_final, line_word)
		return None

	def transliterate_word(self, headword):
		"""Convert a string spelling a single word into a sequential list of phonemes in that word"""
		word_phonemes = []
		capsed_word = headword.upper() 		# resource headwords are all uppercase
		with open(self.raw_dict, "r") as file:
			for line in file:
				# strip newline
				line = line[:-1] if line.endswith("\n") else line
				# find headword phones
				line_items = line.split()
				if line_items[0] == capsed_word: word_phonemes = line_items[1:]
		return word_phonemes

	def find_reverse_rhyme(self, initial_word_phonemes, final_word_phonemes):
		"""Find reverse rhyme words whose initial matches initial word's initial and final matches final word's final"""
		matches = []
		initial_phonemes = self.split_initial_final(initial_word_phonemes)[0]
		final_phonemes = self.split_initial_final(final_word_phonemes)[1]
		# store matches from memo
		if " ".join(initial_phonemes) in self.matched_initials:
			matched_initials = self.matched_initials[initial_phonemes]
			for word in matched_initials:
				matched_phonemes = self.transliterate_word(word)
				matched_final = self.split_initial_final(matched_phonemes)[1]
				if matched_final and matched_final == final_phonemes:
					matches.append(word)
		# store matches from file
		else:
			with open(self.raw_dict, "r") as file:
				for line in file:
					line_items = line.split(" ")
					line_word = line_items[0]
					line_phonemes = line_items[2:]
					line_initial_final = self.split_initial_final(line_phonemes)
					if line_initial_final is not None:
						line_initial = line_initial_final[0]
						line_final = line_initial_final[1]
						if line_initial == initial_phonemes and line_final == final_phonemes:
							matches.append(line_word)
		if len(matches) < 1: return None
		return matches

	def reverse_rhyme_both(self, initial_word, final_word):
		"""Find and select one word with the same initial as initial word and final as final word"""
		initial_word_phonemes = self.transliterate_word(initial_word)
		final_word_phonemes = self.transliterate_word(final_word)
		matches = self.find_reverse_rhyme(initial_word_phonemes, final_word_phonemes)
		if matches is not None and len(matches) > 0:
			return random.choice(matches)
		else:
			return None

	def rhyme_both(self, word):
		"""Find both initial and final rhymes for the given word

		Return map containing the original word, the initial rhyming word, the final rhyming word and flag for vowel-initial
		"""
		phonemes = self.transliterate_word(word)
		rimeset = self.split_initial_final(phonemes)
		# pass up non matches
		if rimeset is None:
			return None
		self.vowel_initial = False
		initial_phones, final_phones = rimeset
		# memoization for past searches
		if " ".join(initial_phones) not in self.matched_initials or " ".join(final_phones) not in self.matched_finals:
			self.find_matches(initial_phones, final_phones)
		initial_match = self.select_random_initial_match(" ".join(initial_phones))
		if initial_phones == [self.vowel_tag]: self.vowel_initial = True
		final_match = self.select_random_final_match(" ".join(final_phones))
		return {'word': word, 'initial': initial_match, 'final': final_match, 'vowel': self.vowel_initial}
