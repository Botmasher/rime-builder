import filterrhymes

def make_ui_kw_variants():
	ui_kw_variants = {'yes': ["Yes", "yes", "YES", "Y", "y", "ok", "OK", "Ok"], 'no': ["No", "no", "NO", "N", "n"]}
	return ui_kw_variants

def run_ui(initial_rhymer, final_rhymer):
	kw_variants = make_ui_kw_variants()
	print("\n-- Welcome to the ENGLISH FANQIE RIME BUILDER --")
	print("\nThis uses a Chinese linguistic tradition to take another look at English words.")
	print("This tool aims to analyze the phonology of basic English words from another perspective.")
	print("Give me a one syllable word. I will build an initial and final rhyme for you.\n")
	# TODO handle illegal character input
	word = input("Type a single syllable word for me to rhyme: ")
	print("Rhyming from front to back . . .")
	rhyme = filterrhymes.filter_single_syllable_rhyme(word, final_rhymer)
	initial = initial_rhymer.rhyme_initial(word).lower()
	print("\nYour word has the same initial as: " + initial)
	print("Your word has the same end rhyme as: " + rhyme)
	print("The fanqie for your word is: %s, %s" % (initial.upper(), rhyme.upper()))
	reset = input("\nFind another English fanqie? ")
	if reset in kw_variants['yes']:
		return run_ui(initial_rhymer, final_rhymer)
	print("Exiting...\n\n")
	return None
