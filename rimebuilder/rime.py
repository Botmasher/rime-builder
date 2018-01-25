import textui
import cmuapi
import fanqieapi

# TODO handle 404 file not found

def rime_start():
	fanqie_rhymer = fanqieapi.FanqieAPI()
	english_rhymer = cmuapi.LocalEnglishRimeAPI()
	textui.run_ui(fanqie_rhymer, english_rhymer)
	return None
