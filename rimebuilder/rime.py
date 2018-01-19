import urllib.request, json
import os

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
	
class PhonemeLocalAPI:
	def __init__(self, path, file):
		self.checked_words = []
		self.path = os.path.join(os.getcwd(), path, file)
		# TODO fetch vowels from CMU: http://svn.code.sf.net/p/cmusphinx/code/trunk/cmudict/cmudict-0.7b.phones
		self.vowels = ["AA", "AE", "AH", "AO", "AW", "AY", "EH", "ER", "EY", "IH", "IY", "OW", "OY", "UH", "UW"]

	def find_initial_match(self, word_phonemes):
		# Search for a single-syllable word with the same initials
		
		#	1. cut off source word's rhyme, leaving just the transliterated initial (or everything before main V)
		first_vowel = next(s for s in word_phonemes if s[:2] in self.vowels)
		word_initial = word_phonemes[0:word_phonemes.index(first_vowel)]
		
		# 2. check target lines for words that have the same initial (everything before main V)
		# TODO handle cases where target has no vowel
		found_initial_match = ""
		with open(self.path, "r") as file:
			for line in file:
				line_items = line.split(" ")
				line_phonemes = line_items[2:]
				line_vowels = [s for s in line_phonemes if s[:2] in self.vowels]
				if line_vowels:
					line_initial = line_phonemes[0:line_phonemes.index(line_vowels[0])]
					if line_initial == word_initial and len(line_vowels) == 1:
						found_initial_match = line_items[0]
		return found_initial_match

		# 3. count that the target is a one-syllable word

		# 	3a. store representation of all main Vs and all Cs in this class
		# 	3b. count how many Vs occur in the target's phoneme list
		# 	3c. return whether or not the target matches the single-syllable expectation

	def find_word(self, word):
		self.checked_words.append(word)
		word_phonemes = []
		capsed_word = word.upper() 						# resource headwords are all uppercase
		with open(self.path, "r") as file:
			for line in file:
				# BETTER - redo the word using CMU transliteration to avoid two lin searches
				if line[0:len(capsed_word)] == capsed_word:
					word_phonemes = line.split(" ")[2:]
		return self.find_initial_match(word_phonemes)

def rime_start():
	final_rhymer = RhymeAPI()
	initial_rhymer = PhonemeLocalAPI("rimebuilder/transliterations", "cmudict-0.7b.txt")
	word = input("Type a one syllable word for me to rhyme: ")
	rhyme = single_syllable_rhyme(word, final_rhymer)
	initial = initial_rhymer.find_word(word)
	print ("Your word has the same end rhyme as: " + rhyme)
	print ("Your word has the same initial as: " + initial.lower())
	return None
