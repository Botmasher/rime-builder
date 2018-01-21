import filterrhymes

def make_ui_kw_variants():
	ui_kw_variants = {'yes': ["Yes", "yes", "YES", "Y", "y", "ok", "OK", "Ok"], 'no': ["No", "no", "NO", "N", "n"]}
	return ui_kw_variants

def run_ui(initial_rhymer, final_rhymer):
	kw_variants = make_ui_kw_variants()
	print("-- Welcome to the ENGLISH FANQIE RIME BUILDER --")
	print("This uses a Chinese linguistic tradition to take another look at English words.")
	print("This tool aims to analyze the phonology of basic English words from another perspective.")
	print("Please input a one syllable word. I will build an initial and final rhyme for you.\n")
	# TODO handle illegal character input
	word = input("Type a one syllable word for me to rhyme: ")
	rhyme = filterrhymes.filter_single_syllable_rhyme(word, final_rhymer)
	initial = initial_rhymer.rhyme_initial(word).lower()
	print("Your word has the same initial as: " + initial)
	print("Your word has the same end rhyme as: " + rhyme)
	print("The fanqie for your word is: %s, %s" % (initial_rhymer.upper(), rhyme.upper()))
	reset = input("\nFind another English fanqie? ")
	if reset in :
		return run_ui()
	print("Exiting...")
	return None
