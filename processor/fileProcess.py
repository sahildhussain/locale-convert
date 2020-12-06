import json
from pathlib import Path
import re

regex = re.compile(r'\>[a-zA-Z0-9_ !?.,]*\<')

def getKeydata():
    file = open('keyData.json')
    data = json.load(file)
    return data

def GetFileData(filePath):
    p = Path(filePath)
    text = p.read_text()
    localeData = regex.findall(text)

    for i in range(len(localeData)):
        localeData[i] = localeData[i].strip('>')
        localeData[i] = localeData[i].strip('<')
    return localeData

def saveFile(language,changedLocale,filePath,directoryPath):
    p = Path(filePath)
    text = p.read_text()

    fileName = directoryPath+ '/'+language+'.xml'

    print(fileName)
    changedFile = open(fileName,'w')

    localeData = regex.findall(text)
    updatedLocale = text

    for i in range(len(localeData)):
        updatedLocale = re.sub(localeData[i],'>'+changedLocale[i]+'<',updatedLocale)

    changedFile.write(updatedLocale)
