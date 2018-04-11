#!/usr/bin/env python
# -*- coding: utf-8 -*-
import gtranslate
import banglishTools
from googletrans import Translator 

banglishText = []
translator = Translator()
with open("input/banglish_dataset2.txt", "r") as f:
  for line in f:
    banglishText.append(line)
toBanglaTextFile = open("output/converted2.txt","w+")


def wordBywordTranslate(line):
    words = line.split(' ')
    convertedWords = []
    for word in words:
        translated = ""
        try:
            translated = translator.translate(word, src='bn')
        except:
            print("")
        if translated:
            toEnglish = translated.text.encode("utf-8")
            convertedWords.append(toEnglish)
        else: 
            toEnglish = ""
    return ' '.join(convertedWords)




print ("processing...")
for text in banglishText:
    cleanBanglish = banglishTools.makeCleanBanglish(text)
    toBangla = banglishTools.convertToBangla(cleanBanglish)
    translationDirect = ""
    translation = ""
    toEnglishDirect = ""
    toEnglish = ""
    try:
        translationDirect =  translator.translate(text, src='bn')
        if translationDirect :
            toEnglishDirect =  translationDirect.text.encode("utf-8") 
        else:    
            toEnglishDirect = ""
    except: 
        print("")

    try:
        translation =  translator.translate(toBangla, src='bn')
        if translation:
            toEnglish =  translation.text.encode("utf-8") 
        else:
            toEnglish = ""
    except:
        print("")

    wordBywordTranslation = wordBywordTranslate(toBangla)
    toBanglaTextFile.write("original   >> " + text + 
      "banglish   >> " + cleanBanglish.encode("utf-8") + 
    "\ntranslated >> " + toBangla.encode("utf-8") + 
    "\nengDirect  >> "  + toEnglishDirect + 
    "\nenglish    >> "  + toEnglish + 
    "\nwordByWord >> "  + wordBywordTranslation + "\n\n\n")
print ("complete")
toBanglaTextFile.close()

