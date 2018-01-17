#ifndef __RHYME_H_INCLUDED__
#define __RHYME_H_INCLUDED__

char* splitInitialFromRhyme(char* s);

bool isRhymeMatch(char* s1, char* s2);

bool isInitialMatch(char* s1, char* s2);

char* findRhymeMatches(char* s);

char* findInitialMatch(char* s);

#endif	// __RHYME_H_INCLUDED
