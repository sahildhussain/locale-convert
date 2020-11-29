from textblob import TextBlob
from processor.fileProcess import GetFileData

def detectLanguage(text):
    l_blob = TextBlob(text)
    return de_blob.detect_language()

def translateLanguage(_src,_to):
    textArray = GetFileData()
    for index in range(len(textArray)):
        text = textArray[index]
        if(_src == ''):
            _src = detectLanguage(text)
        l_blob = TextBlob(text)
        try:
            textArray[index] = str(l_blob.translate(from_lang=_src,to=_to))
        except:
            None
    return textArray
