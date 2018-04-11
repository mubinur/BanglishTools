#!/usr/bin/env python
# -*- coding: utf-8 -*-

import enchant as englishDictionary
import gtranslate
from pyavrophonetic import avro
import json


def makeCleanBanglish(banglishText):
	banglishWords = banglishText.split(' ')
	cleanBanglishWords = []
	for word in banglishWords:
		word = word.replace('\n', '')
		fixedBanglishWord = fixBadBanglishSpelling(word)
		cleanBanglishWords.append(fixedBanglishWord.decode('utf-8'))
	return ' '.join(cleanBanglishWords)

def convertToBangla(line):
    banglishWords = line.split(' ')
    banglaWords = []
    for word in banglishWords:
        if englishDictionary.check(word) and not isFrequentlyUsedBanglaWord(word):
            banglaWords.append(word)
        elif word == "???":
            continue
        else:
            banglaWord = translateBanglishToBangla(word)
            banglaWords.append(banglaWord)
    return ' '.join(banglaWords)


def fixBadBanglishSpelling(potentialBadBanglishWord):
	fixedBanglishWord = isFrequentlyUsedBanglaWord(potentialBadBanglishWord)
	if not fixedBanglishWord:
		return potentialBadBanglishWord

	return fixedBanglishWord


def isFrequentlyUsedBanglaWord(word):
	return frequentBanglaPhoneticsDictionary.get(word.lower(), False)


def translateBanglishToBangla(banglishWord):
	return avro.parse(banglishWord)


def addWordsToEnglishDictionary(filePath):
	englishWordsToAdd = []
	with open(filePath, "r") as words:
		for word in words:
			englishWordsToAdd.append(word.replace('\n',''))
	for word in englishWordsToAdd:
		englishDictionary.add_to_session(word)



englishDictionary = englishDictionary.Dict("en_US")
jsonDataFrequentBanglaPhoneticsDictionary = open("dictionaries/frequentPhonetics.json")
frequentBanglaPhoneticsDictionary = json.load(jsonDataFrequentBanglaPhoneticsDictionary)
addWordsToEnglishDictionary("dictionaries/englishLingos.txt")