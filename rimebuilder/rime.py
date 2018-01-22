import textui
import initialapi
import rhymeapi
import fanqieapi

# TODO handle 404 file not found

def rime_start():
	fanqie_rhymer = fanqieapi.FanqieAPI()
	fanqie_rhymer.rhyme(u"本")
	#initial_rhymer = initialapi.InitialAPI("rimebuilder/tools", "cmudict-0.7b.txt")
	#final_rhymer = rhymeapi.RhymeAPI()
	#textui.run_ui(initial_rhymer, final_rhymer)
	return None
