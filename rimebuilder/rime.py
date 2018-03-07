import textui
import initialapi
import rhymeapi
import fanqieapi
import wordlookup

# TODO handle 404 file not found

def rime_start():
	fanqie_rhymer = fanqieapi.FanqieAPI()
	initial_rhymer = initialapi.InitialAPI("rimebuilder/tools", "cmudict-0.7b.txt")
	final_rhymer = rhymeapi.RhymeAPI()
	word_lookup = wordlookup.WordLookupAPI()
	textui.run_ui(fanqie_rhymer, initial_rhymer, final_rhymer, word_lookup)
	return None
