# Fanqie Rime Builder

A tool for exploring Qieyun-style fanqie rimes in Chinese and applying the same method to one-syllable words in English.

## Background

While preparing a project on the linguistic history of Chinese, I read hundreds of pages that focused on analyzing, explaining and reconstructing words with the fanqie rhyming tradition. This unique system condenses the key phonological insights of Chinese linguistics, which contended with an interesting problem: how to represent Chinese phonology using a complex, non-alphabetic writing system. Instead of an alphabet or phonetic transcription, Chinese scholars had access to sound-alike characters. For any syllable, a fanqie entry lists a "top term" with the same initial reading and a "bottom term" with the same final reading.

Take one an example from early rime dictionaries. The character 韻 means "rhyme". Many centuries ago, the pronunciation for that character was given with the following fanqie:

```
韻
王
問
切
```

This reading contains the headword 韻 and its pronunciation 王問切. In the fanqie pronunciation, 王 is the upper character for the initial rhyme, and 問 is the lower character for the final rhyme. The last character, 切, indicates that this is a fanqie reading. This reading is simplified to avoid the complexities of the actual [entry structure](https://commons.wikimedia.org/wiki/File:Qieyun_Dong_entry_fanqie.svg) and [dictionary structure](http://www.academia.edu/2261552/Introduction_to_Chinese_historical_phonology) (pages 6-7).

I wondered how English might look if analyzed using fanqie. This method uses coarser grains than the standard approach, which has been to transcribe pronunciation using a segmental system like IPA. For example, the word "thumb" is typically represented as `/θʌm/`. By contrast, using fanqie, "thumb" shares an initial with "thing" (not "this") and a final with "sum", so "thumb" can be respresented as `THING SUM`. Similarly, "write" could yield "reed" and "height". Curiosity about these different approaches led me to build this tool for exploring initial and final rhymes using fanqie.

## Getting Started

This project is set up as a single Python package called `rimebuilder`. Here's a straighforward way to run it:

1. check that you have [Python](https://www.python.org/downloads/) installed on your machine (developed with 3.6.4)
2. download, fork or clone this repository
3. navigate to the root repo directory on your local machine
4. run `pip` to install the `rimebuilder` package: `pip3 install . --upgrade`
5. run the installed package: `python3 rimebuilder`

## Using the Tools

This project has three objectives:
1. find any fanqie for a Chinese character
2. build a fanqie reading for any single-syllable English word
3. reverse a fanqie reading to find the single-syllable English word

To meet these objectives, the project is divided into three subtools.

### Chinese Fanqie Finder

This subtool accepts a Chinese character. It searches the character's entry on [Wiktionary](https://en.wiktionary.org/wiki/) for a traditional fanqie rhyme. If one is listed in the normal format, it reads and returns the two fanqie characters. Example: inputting "韻" returns "王問切".

### English Fanqie Builder

This subtool accepts an English term one syllable in length. It uses a fanqie-inspired method to propose an initial and a final that represent a two-word fanqie reading for that English word. Examples allow analysis of a Western language using a tool native to Chinese linguistics. One potential benefit, and one that drove me to develop this tool, is the ability to understand the fanqie system "natively" for those outside of that linguistic tradition. Another is to draw insights from the results, if such a perspective shift could reveal anything about non-Chinese phonology. Example: inputting "rhyme" may return "WRONG, TIME".

### English Fanqie Reverser

This subtool accepts two English words, each one syllable long. It uses a fanqie-inspired method to treat the first word as an initial match and the second word as a final match within a fanqie. It then searches for a single English word that contains the same initial as the first word and the same final as the second word. Example: inputting "wrong" and "time" returns "RHYME".

## Source code

### Development

This project is primarily developed in Python. The main `rimebuilder` Python package makes API calls to [datamuse](https://www.datamuse.com/api/) for final rhymes and reads the [CMU speech dictionary](http://www.speech.cs.cmu.edu/cgi-bin/cmudict) to find initial rhymes. The initial development was in C++ but shifted to Python for ease of making web requests.

### Feature Branches

Currently all production features are found in `master`. The now-merged `localrhymes` branch was developed to compute not just initial matches but also final matches for English fanqie from the locally stored sounds dictionary rather than fetching rhymes from an API server. 

## Contributing

If you've used the tool and have ideas, bug fixes or enhancements in mind, you're a contributor! Whether you're programming, tinkering or just searching, if you've done some local testing and find ways to improve the tool, you're welcome to open an issue or a pull request. Please do document reproducible steps for fixes. Give as much relevant context as possible for enhancements.

