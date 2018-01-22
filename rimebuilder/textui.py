import filterrhymes

# TODO account for zero returns (incl word==""), zero-rhyme returns, zero-initial or vowel-initial returns from API
# TODO handle illegal character input
# TODO handle keyboard input interrupted

kw_variants = {'yes': ["Yes", "yes", "YES", "Y", "y", "ok", "OK", "Ok"], 'no': ["No", "no", "NO", "N", "n"]}

def run_trad_fanqie(fanqie_rhymer):
	print("\n--- Traditional Fanqie Finder ---")
	print("Type a Hanzi character. I will look up a traditional Fanqie for that character.")
	zi = input("Type one character for me to rhyme: ")
	print("Finding an initial and a final match . . .")
	#fanqie_rhymer.rhyme(u"本")
	fanqie = fanqie_rhymer.rhyme(zi)
	# TODO handle if result is None
	print("\nFanqie for %s: %s" % (zi, fanqie))
	reset = input("Find another Chinese fanqie?")
	if reset in kw_variants['yes']:
		return run_trad_fanqie(fanqie_rhymer)
	return None	

def run_en_fanqie(initial_rhymer, final_rhymer):
	print("\n--- English Fanqie Builder ---")
	print("Type a one syllable word. I will build an initial and final rhyme for you.\n")
	word = input("Type a single syllable word for me to rhyme: ")
	print("Rhyming from front to back . . .")
	rhyme = filterrhymes.filter_single_syllable_rhyme(word, final_rhymer)
	initial = initial_rhymer.rhyme_initial(word).lower()
	print("\nYour word has the same initial as: " + initial)
	print("Your word has the same end rhyme as: " + rhyme)
	print("The fanqie for your word is: %s, %s" % (initial.upper(), rhyme.upper()))
	reset = input("Build another English fanqie?")
	if reset in kw_variants['yes']:
		return run_en_fanqie(initial_rhymer, final_rhymer)
	return None	

def select_subtool():
	print("\nChoose a tool:")
	print("1   traditional fanqie finder for Chinese characters")
	print("2   fanqie rhyme builder English words")
	print("q   quit")
	selected = input("1, 2 or q? ")
	if selected not in ["1", "2", "q"]:
		return select_subtool()
	return selected

def run_ui(fanqie_rhymer, initial_rhymer, final_rhymer):
	print("\n-- Welcome to the ENGLISH FANQIE RIME BUILDER --")
	print("\nUse the Chinese linguistic tradition to take a different look at English pronunciation.")
	print("This tool analyzes the phonology of basic English words using a method akin to Fanqie.")
	selected = select_subtool()
	if (selected == "1"):
		run_trad_fanqie(fanqie_rhymer)
	elif selected == "2":
		run_en_fanqie(initial_rhymer, final_rhymer)
	else:
		print("Exiting...\n\n")
		return None
	reset = input("\nExit the Fanqie program? ")
	if reset not in kw_variants['yes']:
		return run_ui(fanqie_rhymer, initial_rhymer, final_rhymer)
	print("Exiting...\n\n")
	return None
