# weechat_jisearch
Simple weechat plugin to search Jisho's API and get kanji, reading and meaning corresponding to researched term

## Installation

From weechat, just type
```
/python load <path_to_jisearch.py>
```

## Usage

It can be used from any buffer, the result will display only to you, in the current buffer.
There's only one command so far

```
/jisearch <kana|kanji|english_term|>
```

## Examples

```
/jisearch test
[JiSearch] reading: テスト | meaning: test
```
==
```
/jisearch 私
[JiSearch] kanji: 私 | reading: わたし | meaning: I
```
==
```
/jisearch フランス
[JiSearch] kanji: 仏蘭西 | reading: フランス | meaning: France
```
