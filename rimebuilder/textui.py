import re
import wordlookupapi

# TODO check that input has one syllable
# TODO account for zero returns (incl word==""), zero-rhyme returns, zero-initial or vowel-initial returns from API
# TODO handle illegal character input
# TODO handle keyboard input interrupted
# TODO disentangle passing around rhyme api objects from the ui

kw_variants = {
	'yes': ["Yes", "yes", "YES", "Y", "y", "ok", "OK", "Ok"], 'no': ["No", "no", "NO", "N", "n"],
	'quit': ["Q", "q", "QUIT", "Quit", "quit", "EXIT", "Exit", "exit"],
	'#': r"[(]?[1-3][.),]?"
}
# TODO hold good initials or finals through when found in lookup_rhymes

word_lookup = wordlookupapi.WordLookupAPI()
def lookup_word(word):
	print("Looking for your word in my dictionary...")
	if word_lookup.is_word(word):
		print("Found it!")
		return True
	return False

def lookup_rhymes(word, english_fanqieizer, attempts=10):
	"""Find initial and final rhymes, verify that they are normal words, try again if not"""
	if attempts <= 0: return None
	rimeset = english_fanqieizer.rhyme_both(word)
	if rimeset is not None:
		if word_lookup.is_word(rimeset['initial']) and word_lookup.is_word(rimeset['final']):
			return rimeset
	print("Did not find a good match. Trying again (%s retries)..." % attempts)
	return lookup_rhymes(word, english_fanqieizer, attempts-1)

def run_trad_fanqie(fanqie_rhymer):
	"""Text interface for the Hanzi fanqie lookup"""
	print("\n--- Chinese Fanqie Finder ---")
	print("Type a Hanzi character. I will look up a traditional Fanqie for that character.")
	zi = input("One character: ")
	print("Finding an initial and a final match . . .")
	fanqie = fanqie_rhymer.rhyme(zi)
	if fanqie is not None:
		print("\nFanqie for %s: %s" % (zi, fanqie))
	else:
		print("\nCould not find a fanqie for your character.\nYou can try again though.")
	reset = input("\nFind another Chinese fanqie? ")
	if reset in kw_variants['yes']:
		return run_trad_fanqie(fanqie_rhymer)
	return None	

def run_en_fanqie(english_fanqieizer):
	"""Text interface for the English fanqie initial rhymer and final rhymer"""
	print("\n--- English Fanqie Builder ---")
	print("This tool analyzes the phonology of basic English words using a fanqie-style method.")
	print("Type a one syllable word. I will build an initial and final rhyme for you.\n")
	word = input("A single syllable word: ")
	is_word = lookup_word(word)
	if is_word:
		rimeset = lookup_rhymes(word, english_fanqieizer)
	if is_word and rimeset is not None and 'initial' in rimeset and 'final' in rimeset:
		print("Rhyming from front to back . . .")
		initial = rimeset['initial']
		final = rimeset['final']
		vowel = " (initial vowel/glottal)" if rimeset['vowel'] else ""
		print("\nYour word has the same initial as: %s%s\nYour word has the same final as: %s" % (initial, vowel, final))
		print("The fanqie for your word is: %s, %s" % (initial.upper(), final.upper()))
	else:
		print("Could not build a fanqie for your word.")
		print("It could be that I didn't recognize your word or that I think it has multiple syllables.")
		print("You can try again though.")
	reset = input("\nBuild another English fanqie? ")
	if reset in kw_variants['yes']:
		return run_en_fanqie(english_fanqieizer)
	return None

def run_en_reverser(english_fanqieizer):
	print("\n--- English Fanqie Reverser ---")
	print("This tool takes two words and returns an original word for which they are the fanqie.")
	print("Type two one syllable words. I will find the original word rhyming with the initial of the first and final of the second.\n")
	initial_word = input("An initial rhyme: ")
	final_word = input("A final rhyme: ")
	print("Rhyming both to find one . . .")
	# TODO check that inputs are words (extra calc if the else catch below is insufficient)
	rime = english_fanqieizer.reverse_rhyme_both(initial_word, final_word)
	if rime is not None:
		print("The fanqie for your word is  %s: %s, %s" % (rime, initial_word.upper(), final_word.upper()))
	else:
		print("Could not reverse a fanqie for your words.")
		print("It could be that I didn't recognize one of your words or I think it has multiple syllables.")
		print("You can try again though.")
	reset = input("\nReverse another English fanqie? ")
	if reset in kw_variants['yes']:
		return run_en_reverser(english_fanqieizer)
	return None

def select_subtool():
	"""Text interface for the tool select menu"""
	print("\n  Choose a tool:")
	print("  1 - fanqie rhyme builder for English words")
	print("  2 - fanqie finder for Chinese characters")
	print("  3 - fanqie reverser for English")
	print("  q - quit")
	selected = input("\n  1, 2 or q? ")
	if not re.match(kw_variants['#'], selected) and selected not in kw_variants['quit']:
		print("\n  I did not recognize your input.")
		return select_subtool()
	return selected

def run_ui(fanqie_rhymer, english_fanqieizer):
	"""Text interface for the overall rimebuilder"""
	print("\n-- Welcome to the FANQIE RIME BUILDER --")
	print("Explore this Chinese linguistic tradition. Use it to take a different look at English pronunciation.")
	selected_subtool = select_subtool()
	if "1" in selected_subtool:
		run_en_fanqie(english_fanqieizer)
	elif "2" in selected_subtool:
		run_trad_fanqie(fanqie_rhymer)
	elif "3" in selected_subtool:
		run_en_reverser(english_fanqieizer)
	else:
		print("\nExiting...\n")
		return None
	reset = input("\nExit the Fanqie program? ")
	if reset not in kw_variants['yes'] and reset not in kw_variants['quit']:
		return run_ui(fanqie_rhymer, english_fanqieizer)
	print("\nExiting...\n")
	return None
