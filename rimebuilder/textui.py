# TODO account for zero returns (incl word==""), zero-rhyme returns, zero-initial or vowel-initial returns from API
# TODO handle illegal character input
# TODO handle keyboard input interrupted
# TODO hold good initials or finals through when found in lookup_rhymes

kw_variants = {
	'yes': ["Yes", "yes", "YES", "Y", "y", "ok", "OK", "Ok"], 'no': ["No", "no", "NO", "N", "n"],
	'quit': ["Q", "q", "QUIT", "Quit", "quit", "EXIT", "Exit", "exit"],
	'1': ["1", "1.", "1)", "(1)", "1,"],
	'2': ["2", "2.", "2)", "(2)", "2,"],
	'3': ["3", "3.", "3)", "(3)", "3,"]
}

def lookup_rhymes(word, initial_rhymer, final_rhymer, word_lookup, counter=10):
	"""Helper method for repeated search of initial and final rhymes"""
	if counter <= 0:
		return {'initial': None, 'final': None}
	final = final_rhymer.single_syllable_rhyme(word)
	initial = initial_rhymer.rhyme_initial(word)
	is_word_initial = "Yes" if word_lookup.is_word(initial) else "No"
	is_word_final = "Yes" if word_lookup.is_word(final) else "No"
	if word_lookup.is_word(final) and word_lookup.is_word(initial):
		return {'initial': initial, 'final': final}
	else:
		print("Did not find a good match. Trying again (%s retries)..." % counter)
		return lookup_rhymes(word, initial_rhymer, final_rhymer, word_lookup, counter-1)

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

def run_en_fanqie(initial_rhymer, final_rhymer, word_lookup):
	"""Text interface for the English fanqie initial rhymer and final rhymer"""
	print("\n--- English Fanqie Builder ---")
	print("This tool analyzes the phonology of basic English words using a fanqie-style method.")
	print("Type a one syllable word. I will build an initial and final rhyme for you.\n")
	word = input("A single syllable word: ")
	print("Rhyming from front to back . . .")
	is_word = word_lookup.is_word(word)
	rhymes = None
	if is_word:
		rhymes = lookup_rhymes(word, initial_rhymer, final_rhymer, word_lookup)
	if is_word and rhymes is not None and rhymes.get('initial') is not None and rhymes.get('final') is not None:
		initial = rhymes['initial'].lower()
		final = rhymes['final']
		print("\nYour word has the same initial as: %s\nYour word has the same final as: %s" % (initial, final))
		print("The fanqie for your word is: %s, %s" % (initial.upper().split(" ")[0], final.upper()))
	else:
		print("Could not build a fanqie for your word.")
		print("It could be that I didn't recognize your word or that I think it has multiple syllables.")
		print("You can try again though.")
	reset = input("\nBuild another English fanqie? ")
	if reset in kw_variants['yes']:
		return run_en_fanqie(initial_rhymer, final_rhymer, word_lookup)
	return None

def run_en_reverse_fanqie(initial_rhymer, word_lookup):
	"""Text interface for the English fanqie initial rhymer and final rhymer"""
	print("\n--- English Fanqie Reverser ---")
	print("This tool takes a fanqie-style rime and looks up a matching word.")
	print("Type two one-syllable words. I will find a word matching the first word's initial and the second word's final.\n")
	upper_word = input("Upper word (initial match): ")
	lower_word = input("Lower word (final match): ")
	print("Rhyming from top to bottom . . .")
	is_upper_word = word_lookup.is_word(upper_word)
	is_lower_word = word_lookup.is_word(lower_word)
	rhyme = None
	if is_upper_word and is_lower_word:
		rhyme = initial_rhymer.reverse_fanqie(upper_word, lower_word)
	if rhyme is not None:
		print("\nThe fanqie for your word: %s. %s, %s" % (rhyme, upper_word.upper(), lower_word.upper()))
	else:
		print("Could not find a word for your a fanqie.")
		print("It could be that I didn't recognize one of your words or that I think they have multiple syllables.")
		print("You can try again though.")
	reset = input("\nFind another reverse English fanqie? ")
	if reset in kw_variants['yes']:
		return run_en_reverse_fanqie(initial_rhymer, word_lookup)
	return None

def select_subtool():
	"""Text interface for the tool select menu"""
	print("\n  Choose a tool:")
	print("  1 - fanqie rhyme builder for English words")
	print("  2 - fanqie finder for Chinese characters")
	print("  3 - fanqie reverser for English")
	print("  q - quit")
	selected = input("\n  1, 2, 3 or q? ")
	if selected not in kw_variants['1'] and selected not in kw_variants['2'] and selected not in kw_variants['3'] and selected not in kw_variants['quit']:
		return select_subtool()
	return selected

def run_ui(fanqie_rhymer, initial_rhymer, final_rhymer, word_lookup):
	"""Text interface for the overall rimebuilder"""
	print("\n-- Welcome to the FANQIE RIME BUILDER --")
	print("Explore this Chinese linguistic tradition. Use it to take a different look at English pronunciation.")
	selected_subtool = select_subtool()
	if "1" in selected_subtool:
		run_en_fanqie(initial_rhymer, final_rhymer, word_lookup)
	elif "2" in selected_subtool:
		run_trad_fanqie(fanqie_rhymer)
	elif "3" in selected_subtool:
		run_en_reverse_fanqie(initial_rhymer, word_lookup)
	else:
		print("Exiting...\n")
		return None
	reset = input("\nExit the Fanqie program? ")
	if reset not in kw_variants['yes'] and reset not in kw_variants['quit']:
		return run_ui(fanqie_rhymer, initial_rhymer, final_rhymer, word_lookup)
	print("Exiting...\n")
	return None
