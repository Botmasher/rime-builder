import textui
import initialapi
import rhymeapi

def rime_start():
	initial_rhymer = initialapi.InitialAPI("rimebuilder/tools", "cmudict-0.7b.txt")
	final_rhymer = rhymeapi.RhymeAPI()
	textui.run_ui(initial_rhymer, final_rhymer)
	return None
