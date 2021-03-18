from textblob import TextBlob
from processor.fileProcess import GetFileData, GetKeydata
import time
import requests, uuid, json

def detectLanguage(text):
    l_blob = TextBlob(text)
    return l_blob.detect_language()

def translateLanguages(_src, _multo, filePath):
    textArray = GetFileData(filePath)
    keyData = GetKeydata()
    # print(keyData)
    subscription_key = keyData["subscription_key"]
    endpoint = "https://api.cognitive.microsofttranslator.com/"

    # Add your location, also known as region. The default is global.
    # This is required if using a Cognitive Services resource.
    location = ""

    path = '/translate'
    constructed_url = endpoint + path

    params = {
        'api-version': '3.0',
        'from': 'en',
        'to': _multo
    }
    constructed_url = endpoint + path

    headers = {
        'Ocp-Apim-Subscription-Key': subscription_key,
        'Ocp-Apim-Subscription-Region': location,
        'Content-type': 'application/json',
        'X-ClientTraceId': str(uuid.uuid4())
    }

    translatedText = {}
    for lang in _multo:
        translatedText[lang] = []

    for text in textArray:
        # You can pass more than one object in body.
        body = [{
            'text': text
        }]
        request = requests.post(constructed_url, params=params, headers=headers, json=body)
        response = request.json()
        response = response[0]['translations']
        for res in response:
            translatedText[res['to']].append(res['text'])
        
    # print(translatedText)
    return translatedText

def translateLanguage(_src,_to,filePath):
    textArray = GetFileData(filePath)
    
    for index in range(len(textArray)):
        text = textArray[index]
        
        if(_src == ''):
            _src = detectLanguage(text)
        l_blob = TextBlob(text)
        try:
            textArray[index] = str(l_blob.translate(from_lang=_src,to=_to))
        except:
            print(None)
    time.sleep(5)
            
    return textArray
