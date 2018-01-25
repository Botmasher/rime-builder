# Fanqie Rime Builder

A tool for exploring Qieyun-style fanqie rimes in Chinese and applying the same method to one-syllable words in English.

## Background

While preparing a project on the linguistic history of Chinese, I read hundreds of pages that focused on analyzing, explaining and reconstructing words with the Fanqie rhyming tradition. This unique, complex system condenses the key phonological insights of Chinese linguistics, which contended with an interesting problem: how to represent Chinese phonology using a complex, non-alphabetic writing system. Instead of an alphabet or a transcription system, Chinese scholars had access to sound-alike characters. For any syllable, a fanqie entry lists a "top term" with the same initial reading and a "bottom term" with the same final reading.

I wondered how English might look if analyzed using this method. For example, "thumb" shares an initial with "thing" (not "this") and a final with "sum", so one fanqie for "thumb" is "thing sum". Similarly, "write" could yield "reed" and "height". That curiosity led me to build this tool, exploring initial and final rhymes using Fanqie.

## Getting Started

This project is set up as a single Python package called `rimebuilder`. Here's a straighforward way to run it:

1. check that you have [Python](https://www.python.org/downloads/) installed on your machine (developed with 3.6.4)
2. download, fork or clone this repository
3. navigate to the root repo directory on your local machine
4. run `pip` to install the `rimebuilder` package: `pip3 install . --upgrade`
5. run the installed package: `python3 rimebuilder`

## Using the Tools

This project has two objectives:
1. find any fanqie for a Chinese character
2. build a fanqie reading for any single-syllable English word

To meet these two objectives, the project is divided into two subtools.

### Chinese Fanqie Finder

This subtool accepts a Chinese character. It searches the character's entry on [Wiktionary](https://en.wiktionary.org/wiki/) for a traditional fanqie rhyme. If one is listed in the normal format, it reads and returns the two fanqie characters.

### English Fanqie Builder

This subtool accepts an English term one syllable in length. It uses a fanqie-inspired method to propose an initial and a final that indicate a two-word fanqie reading for that English word. Examples allow for analysis a Western language using a tool native to Chinese linguistics. One potential benefit, and one that drove me to develop this tool, is the ability to understand the fanqie system "natively" for those outside of that linguistic tradition. Another is to draw insights from the results, if such a perspective shift could anything for non-Chinese phonology.

## Contributing

If you've used the tool and have ideas, bug fixes or enhancements in mind, you're a contributor! Whether you're programming, tinkering or just searching, if you've done some local testing and find ways to improve the tool, you're welcome to open an issue or a pull request. Please do document reproducible steps for fixes. Give as much relevant context as possible for enhancements.

## Source code

This project is primarily developed in Python. The main `rimebuilder` Python package makes API calls to [datamuse](https://www.datamuse.com/api/) for final rhymes and reads the [CMU speech dictionary](http://www.speech.cs.cmu.edu/cgi-bin/cmudict) to find initial rhymes. The initial development was in C++ but shifted to Python for ease of making web requests.
