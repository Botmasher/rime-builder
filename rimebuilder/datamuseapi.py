import fetchurl
import random

class DatamuseAPI:
	url = "https://api.datamuse.com"
	rhymeswith = "/words?rel_rhy="		# words that rhyme
	meanslike = "/words?ml="					# words with similar meaning
	soundslike = "/words?sl="					# words with similar sound
	spelledlike = "/words?sp=" 				# words with similar spelling
	suggested = "/sug?s=" 						# word completion suggestions
	matched_words = {} 								# memo
		
	def __init__(self):
		self.matches = []

	def reset_matches(self):
		self.matches = []
		return True

	def add_match(self, match):
		self.matches.append(match)
		return True

	def filter_single_syllable_rhymes(self, rhymes_dict):
		for rhyme in rhymes_dict:
			if rhyme['numSyllables'] == 1: self.add_match(rhyme['word'])
		return None

	def select_random_match(self, word):
		if len(self.matched_words[word]) > 0:
			return random.choice(self.matched_words[word])
		return None

	def store_rhymes(self, word):
		self.matched_words[word] = self.matches
		return True

	def single_syllable_rhyme(self, word):
		self.reset_matches()
		if word not in self.matched_words:
			rhymes = self.rhyme(word)
			self.filter_single_syllable_rhymes(rhymes)
			self.store_rhymes(word)
		syll_rhyme = self.select_random_match(word)
		return syll_rhyme

	def rhyme(self, word):
		return fetchurl.fetchJSON(self.url+self.rhymeswith+word)

	def means_like(self, word):
		return fetchurl.fetchJSON(self.url+self.meanslike+word)

	def sounds_like(self, word):
		return fetchurl.fetchJSON(self.url+self.soundslike+word)

	def spelled_like(self, word):
		return fetchurl.fetchJSON(self.url+self.spelledlike+word)

	def suggest(self, word):
		return fetchurl.fetchJSON(self.url+self.suggested+word)
