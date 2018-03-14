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

### File specific
- [ ] move or repeat TODOS from files here
	- [ ] browse `rimebuilder/` files for local TODOS
	- [ ] place each of those TODOS in this list
	- [ ] format each entry with `path/filename (ln)`: `todo_txt`
		- where `todo_txt` is the string after `# TODO `
		- and where `(ln)` is the optional line number (if TODO is tied to a specific line)

### UI and input
- [ ] handle illegal character input
- [ ] handle keyboard input interrupted
- [ ] better encapsulation of ui pieces to streamline calls, reloads and flow between pieces

### Data and API
- [ ] account for zero returns (incl word==""), zero-rhyme returns, zero-initial or vowel-initial returns from API
- [ ] disentangle passing around api objects within the ui
- [ ] handle url/file not found
- [ ] switch between CMU vs datamuse if have internet connection

### Rime analysis
- [ ] keep reverser from returning identical matches, e.g. "are are" will return "our" but not "are"
- [ ] more thorough word lookups
	- [ ] is the word obsolete?
	- [ ] does the word have a different pronunciation than suggested by `cmuapi`?
	- [ ] use the `datamuseapi` tool to double check rhymes
- [ ] handle initial vowels in reverser, e.g. "ace cat" returns "at"
- [X] look up a word given EN fanqie input, e.g. "write lede" returns "read"
- [X] account for 0-rhymes
- handling vowels in the rhymer/fanqieizer
	- [X] cases where vowel-only syllable matches to an initial and final, e.g. "a"
	- [ ] repair vowel-initial (e.g. "our") and vowel-only (e.g. "a") not finding good matches
	- [ ] better ways to handle zero initial (first phone is main vowel)
- [ ] cases where words only have an "initial" (langs other than EN?)
- [X] account for searched headword not in dictionary
- [X] search through multisyllabic rhymes for a one syllable variant, e.g. OUR OUR(1) OUR(2) in CMUdict

## Experiments
- [X] `localrhymes` branch
	- [X] build both initial and rhyme matches entirely from phone dict
	- [X] merge into master

## Potential Upgrades
- Some thoughts from my experiments with the tool:
	- Collections of generated fanqie (larger sets instead of single searches) would help spot trends across the results.
	- Identifying multiple matches would provide more support for a term.
	- In line with what I've read about historical Chinese phonology, English results are coherent but do not correspond to phonemes. It seems this method would require chaining and scale to build a case for English phonology, as was done for Middle Chinese.
	- Why no helpful negative examples, like the "thing" vs "this" above?
	- Fanqie entries have peculiar formatting in Chinese manuscripts, both internally and with respect to other entries. Any interesting results from parallelling these?
