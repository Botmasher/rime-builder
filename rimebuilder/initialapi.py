import os

class InitialAPI:
	def __init__(self, path, file):
		self.checked_words = []
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

	def find_initial_match(self, phonemes):
		"""
		Input: 	sequential list of phonemes in a single word
		Return: string of single-syllable word with the same initial
		"""
		word_initial = self.find_one_syllable_initial(phonemes)
		# check target words for single-syllable words with matching initial
		# TODO handle cases where target has no vowel
		found_initial_match = ""
		with open(self.path, "r") as file:
			for line in file:
				line_items = line.split(" ")
				line_phonemes = line_items[2:]
				line_initial = self.find_one_syllable_initial(line_phonemes)
				# search valid entries for a match
				if line[:3] != ";;;" and line_initial and line_initial == word_initial:
					found_initial_match = line_items[0]
		return found_initial_match

	def transliterate_word(self, word):
		"""
		Input: 	string spelling a single word
		Return: sequential list of phonemes in that word
		"""
		word_phonemes = []
		capsed_word = word.upper() 						# resource headwords are all uppercase
		with open(self.path, "r") as file:
			for line in file:
				# BETTER - redo the word using CMU transliteration to avoid two lin searches
				if line.split(" ")[0] == capsed_word:
					word_phonemes = line.split(" ")[2:]
		return word_phonemes

	def rhyme_initial(self, word):
		self.checked_words.append(word)
		word_phonemes = self.transliterate_word(word)
		return self.find_initial_match(word_phonemes)