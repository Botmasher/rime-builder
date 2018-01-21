def filter_rhymes(rhymes_dict):
	for rhyme in rhymes_dict:
		if rhyme['numSyllables'] == 1: return rhyme['word']
	return ""

def filter_single_syllable_rhyme(word, rhyme_api):
	rhymes = rhyme_api.rhyme(word)
	syll_rhyme = filter_rhymes(rhymes)
	return syll_rhyme
