import fetchjson

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
		return fetchjson.fetch(self.url+self.rhymeswith+word)

	def means_like(self, word):
		return fetchjson.fetch(self.url+self.meanslike+word)

	def sounds_like(self, word):
		return fetchjson.fetch(self.url+self.soundslike+word)

	def spelled_like(self, word):
		return fetchjson.fetch(self.url+self.spelledlike+word)

	def suggest(self, word):
		return fetchjson.fetch(self.url+self.suggested+word)
