# Fanqie Rime Builder

A simple program for exploring Qieyun-framework fanqie rimes in Chinese and applying the same method to English.

## Background

Over the course of preparing a project on the linguistic history of Chinese, I read hundreds of pages principally focused on analyzing, explaining and reconstructing words based on the unique Fanqie rhyming tradition. This complex system condenses the key phonological insights of Chinese linguistics, which contented with the problem of accurately representing Chinese phonology using a complex, non-alphabetic writing system.

## Use

For a Chinese term, this tool will simply fetch data from web backends to gather information on rhymes for a single character. For a one syllable English term, it will use a fanqie-inspired method to propose an initial and a final that indicate the rhyme. Examples will allow to analyze a Western language using a tool native to Chinese linguistics. One benefit is the ability to understand "natively" for those outside of that linguistic tradition. Another is to draw insights from the results.

## Source code

This project is developed in C++ and lightly trails the [Google C++ styleguide](https://google.github.io/styleguide/cppguide.html) whenever that's convenient or remembered. Any proposed cleanup should aim to move the code towards and not away from those standards.
