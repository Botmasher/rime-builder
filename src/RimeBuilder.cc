#include <iostream>
#include <vector>
#include "api.h"

char* splitInitialFromRhyme(char* s) {
	// send string to single-word rhyme API endpoint
	// determine the suffix of the rhyme
	// cut the suffix from the prefix
	// determine the IPA value of the suffix
	// determine the IPA value of the prefix
	// return an array containing two strings, first IPA prefix then IPA suffix
		// - pointer to first char in array
}

bool isRhymeMatch(char* s1, char* s2) {
	// check API if two strings rhyme
		// - compare string one to string two (endpoint?)
	return true;
}

bool isInitialMatch(char* s1, char* s2) {
	// compare initials (dict / wiktionary API)
	// decide which letters (phones?) peel off into rhyme
		// - find IPA value for s1
		// - peel off the rhyme phones
		// - find IPA value for s2
		// - peel off the rhyme phones	
}

char* findRhymeMatches(char* s) {
	// call API endpoint to find string rhyme info
	// return array of strings rhyming with string argument
}

char* findInitialMatch(char* s) {
	// find IPA value for initial
	// search for matches with the same initial: http://www.speech.cs.cmu.edu/cgi-bin/cmudict
	// return first match
}

std::vector<std::string> findRhymes(char* s) {
	std::vector<std::string> rhymes;
	// check API for results
	return rhymes;
}

int main(int argc, char* argv[]) {
	std::cout << "Rime Builder project - in development" << std::endl;
	//std::cout << "Testing api front connect function: " << apiFrontConnectTest(2) << std::endl;
	return 0;
}
