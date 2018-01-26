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
	is_vowel = False
	vowels = []
	# memos
	matched_initials = {}
	matched_finals = {}
	
	def __init__(self):
		self.raw_dict = self.build_path(self.files['tools'], self.files['dict'])
		self.raw_phones = self.build_path(self.files['tools'], self.files['phones'])
		self.vowels = self.fetch_vowels(self.raw_phones)

	def build_path(self, path, file):
		return os.path.join(os.getcwd(), path, file)

	def fetch_vowels(self, file):
		vowels = []
		with open(file, "r") as file:
			for line in file:
				line_items = line.split()
				line_phone = line_items[0]
				line_type = line_items[len(line_items)-1]
				if line_type.lower() == "vowel": vowels.append(line_phone)
		return vowels

	def check_pretty_word(self, word):
		punctuation = [".", ":", ";", "!", "?", "*", "(", ")", ",", "'", "/", "*", "$", "#", "@"]
		if len(word) < 2: return False
		for char in word:
			if char in punctuation: return False
		return True

	def select_random_match(self, items):
		if len(items) > 0: return random.sample(items, 1)
		return None

	def select_random_initial_match(self, phones):
		return self.select_random_match(self.matched_initials[phones])[0]

	def select_random_final_match(self, phones):
		return self.select_random_match(self.matched_finals[phones])[0]

	def add_initial_match(self, phones_list, word):
		phones = " ".join(phones_list)
		if phones not in self.matched_initials:
			self.matched_initials[phones] = set()
		self.matched_initials[phones].add(word)
		return True

	def add_final_match(self, phones_list, word):
		phones = " ".join(phones_list)
		if phones not in self.matched_finals:
			self.matched_finals[phones] = set()
		self.matched_finals[phones].add(word)
		return True

	def split_initial_final(self, phonemes):
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
		return [initial, final]

	def find_matches(self, word_initial, word_final):
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
		"""
		Input: 	string spelling a single word
		Return: sequential list of phonemes in that word
		"""
		word_phonemes = []
		capsed_word = headword.upper() 						# resource headwords are all uppercase
		with open(self.raw_dict, "r") as file:
			for line in file:
				# strip newline
				line = line[:-1] if line.endswith("\n") else line
				# find headword phones
				line_items = line.split()
				if line_items[0] == capsed_word: word_phonemes = line_items[1:]
		return word_phonemes

	def rhyme_both(self, word):
		phonemes = self.transliterate_word(word)
		rimeset = self.split_initial_final(phonemes)
		# pass up non matches
		if rimeset is None:
			return None
		initial_phones, final_phones = rimeset
		# memoization for past searches
		if " ".join(initial_phones) not in self.matched_initials or " ".join(final_phones) not in self.matched_finals:
			self.find_matches(initial_phones, final_phones)
		initial_match = self.select_random_initial_match(" ".join(initial_phones))
		if initial_phones == [self.vowel_tag]: self.is_vowel = True
		final_match = self.select_random_final_match(" ".join(final_phones))
		return {'word': word, 'initial': initial_match, 'final': final_match, 'vowel': self.is_vowel}
