# TODO List

## Basic tool
- [X] create a prototype that achieves README goals
	- [X] fetch rhymes through datamuse API
	- [X] store and search CMU dict for initials
	- [X] fetch traditional fanqie
	- [X] calculate and display initial and final matches for an English word
	- [X] parse and display initial and final Chinese character
- [X] update README.md to reflect prototype development

## Fixes and adjustments

### User input
- [ ] handle illegal character input
- [ ] handle keyboard input interrupted

### Data and API
- [ ] account for zero returns (incl word==""), zero-rhyme returns, zero-initial or vowel-initial returns from API
- [ ] disentangle passing around api objects within the ui
- [ ] handle url/file not found
- [ ] switching between CMU vs datamuse if have internet connection

### Rime analysis
- [ ] account for 0-rhymes
- [ ] currently return None
- [ ] cases where words only have an "initial" (langs other than EN?)
- [ ] account for cases with 0 initial (only main vowel)
- [ ] account for searched headword not in dictionary
- [ ] search through multisyllabic rhymes for a one syllable variant, e.g. OUR OUR(1) OUR(2) in CMUdict

## Experiments
- [X] branch out `localrhymes`
	- build both initial and rhyme matches entirely from phone dict

## Potential Upgrades
- Some thoughts from my experiments with the tool:
	- Collections of generated fanqie (larger sets instead of single searches) would help spot trends across the results.
	- Identifying multiple matches would provide more support for a term.
	- In line with what I've read about historical Chinese phonology, English results are coherent but do not correspond to phonemes. It seems this method would require chaining and scale to build a case for English phonology, as was done for Middle Chinese.
	- Why no helpful negative examples, like the "thing" vs "this" above?
	- Fanqie entries have peculiar formatting in Chinese manuscripts, both internally and with respect to other entries. Any interesting results from parallelling these?
