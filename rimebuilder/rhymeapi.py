import fetchurl

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

	def rhyme(self, word):
		self.rhymed_words.append(word)
		return fetchurl.fetchJSON(self.url+self.rhymeswith+word)

	def means_like(self, word):
		return fetchurl.fetchJSON(self.url+self.meanslike+word)

	def sounds_like(self, word):
		return fetchurl.fetchJSON(self.url+self.soundslike+word)

	def spelled_like(self, word):
		return fetchurl.fetchJSON(self.url+self.spelledlike+word)

	def suggest(self, word):
		return fetchurl.fetchJSON(self.url+self.suggested+word)
