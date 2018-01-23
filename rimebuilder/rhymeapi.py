import fetchurl
import random

# TODO account for 0-rhymes
# TODO account for URL does not exist

class RhymeAPI:
	url = "https://api.datamuse.com"
	rhymeswith = "/words?rel_rhy="		# words that rhyme
	meanslike = "/words?ml="					# words with similar meaning
	soundslike = "/words?sl="					# words with similar sound
	spelledlike = "/words?sp=" 				# words with similar spelling
	suggested = "/sug?s=" 						# word completion suggestions
	
	def __init__(self):
		self.rhymed_words = []
		self.matches = []

	def reset_matches(self):
		self.matches = []
		return True

	def add_match(self, match):
		self.matches.append(match)
		return True

	def select_random_match(self):
		if len(self.matches) > 0:
			return random.choice(self.matches)
		return None

	def filter_single_syllable_rhymes(self, rhymes_dict):
		for rhyme in rhymes_dict:
			if rhyme['numSyllables'] == 1: self.add_match(rhyme['word'])
		return None

	def rhyme(self, word):
		self.rhymed_words.append(word)
		return fetchurl.fetchJSON(self.url+self.rhymeswith+word)

	def single_syllable_rhyme(self, word):
		self.reset_matches()
		rhymes = self.rhyme(word)
		self.filter_single_syllable_rhymes(rhymes)
		syll_rhyme = self.select_random_match()
		return syll_rhyme

	def means_like(self, word):
		return fetchurl.fetchJSON(self.url+self.meanslike+word)

	def sounds_like(self, word):
		return fetchurl.fetchJSON(self.url+self.soundslike+word)

	def spelled_like(self, word):
		return fetchurl.fetchJSON(self.url+self.spelledlike+word)

	def suggest(self, word):
		return fetchurl.fetchJSON(self.url+self.suggested+word)
