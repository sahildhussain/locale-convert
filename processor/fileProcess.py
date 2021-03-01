import json
from pathlib import Path
import re

regex = re.compile(r'\>[a-zA-Z0-9_ !?:.,^\\n\\]*\<')

def getKeydata():
    file = open('keyData.json')
    data = json.load(file)
    return data

def newLineReader(text):
    occcurences = re.findall(' [_ ]+ ',text)
    for occurence in occcurences:
        count = occurence.count('_')
        text = text.replace(occurence,'\\n'*count)
    return text

def newLineWriter(text):
    return text.replace('\\n',' _ ')

def GetFileData(filePath):
    p = Path(filePath)
    text = p.read_text()
    text = newLineWriter(text)

    localeData = regex.findall(text)

    for i in range(len(localeData)):
        localeData[i] = localeData[i].strip('>')
        localeData[i] = localeData[i].strip('<')
    return localeData

def saveFile(language,changedLocale,filePath,directoryPath):
    p = Path(filePath)
    text = p.read_text()

    fileName = directoryPath+ '/'+language+'.xml'

    changedFile = open(fileName,'w')

    text = newLineWriter(text)
    localeData = regex.findall(text)
    updatedLocale = text

    for i in range(len(localeData)):
        changedLocale[i] = newLineReader(changedLocale[i])
        updatedLocale = updatedLocale.replace(localeData[i],'>'+changedLocale[i]+'<')

    changedFile.write(updatedLocale)
