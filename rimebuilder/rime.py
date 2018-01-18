import urllib.request, json

def fetch(path):
	with urllib.request.urlopen(path) as url:
		data = json.loads(url.read().decode())
		url.close()
		return data

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
		return fetch(self.url+self.rhymeswith+word)

	def means_like(self, word):
		return fetch(self.url+self.meanslike+word)

	def sounds_like(self, word):
		return fetch(self.url+self.soundslike+word)

	def spelled_like(self, word):
		return fetch(self.url+self.spelledlike+word)

	def suggest(self, word):
		return fetch(self.url+self.suggested+word)

def filter_rhymes(rhymes_dict):
	for rhyme in rhymes_dict:
		if rhyme['numSyllables'] == 1: return rhyme['word']
	return ""

def single_syllable_rhyme(word, rhyme_api):
	rhymes = rhyme_api.rhyme(word)
	syll_rhyme = filter_rhymes(rhymes)
	return syll_rhyme
	
def test_method():
	return "rimebuilder package in development"

def rime_start():
	rhymer = RhymeAPI()
	word = input("Type a one syllable word for me to rhyme: ")
	rhyme = single_syllable_rhyme(word, rhymer)
	print (rhyme)
	return None
