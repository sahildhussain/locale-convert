from processor.requestProcess import *
from processor.fileProcess import *
from processor.translateProcess import translateLanguage

def Translate():
    filePath = input('Enter file Path: ') 
    original_language = input('Select the original Language:')

    print('Select the languages you want to convert this document to:')
    convert_to = [x for x in input().split(' ')]

    for lang in convert_to:
        # response = getResponse(original_language,lang) : used via API request
        response = translateLanguage(original_language,lang,filePath)
        saveFile(lang,response,filePath)


