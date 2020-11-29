import json
from pathlib import Path
import re

def getKeydata():
    file = open('keyData.json')
    data = json.load(file)
    return data

def GetFileData():
    p = Path.cwd()/Path('default.xml')
    text = p.read_text()
    regex = re.compile(r'\>[a-zA-Z0-9_ !?.]*\<')
    localeData = regex.findall(text)

    for i in range(len(localeData)):
        localeData[i] = localeData[i].strip('>')
        localeData[i] = localeData[i].strip('<')
    return localeData

def saveFile(language,changedLocale):
    p = Path.cwd()/Path('default.xml')
    text = p.read_text()
    fileName = language+'.xml'
    changedFile = open(fileName,'w')

    regex = re.compile(r'\>[a-zA-Z0-9_ !?.]*\<')
    localeData = regex.findall(text)
    updatedLocale = text

    for i in range(len(localeData)):
        updatedLocale = re.sub(localeData[i],'>'+changedLocale[i]+'<',updatedLocale)

    changedFile.write(updatedLocale)
