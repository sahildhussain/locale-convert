from processor.fileProcess import *
from processor.translateProcess import translateLanguage
from pathlib import Path

def Translate():
    filePath = input('Enter file Path(Enter for default.xml): ')
    original_language = input('Select the original Language(Enter for AutoDetect):')

    print('Select the languages you want to convert this document to:')
    convert_to = [x for x in input().split(' ')]

    if filePath == '':
        filePath = Path.cwd()/Path('default.xml')

    directoryPath = str(filePath).split('/')
    directoryPath.pop()
    directoryPath = ('/').join(directoryPath)
    
    for lang in convert_to:
        response = translateLanguage(original_language,lang,filePath)
        saveFile(lang,response,filePath,directoryPath)
