from processor.fileProcess import getKeydata, GetFileData
import requests

def frameURL(urlParams):
    keyData = getKeydata()
    urlParams['key'] = keyData['apiKey']
    url = keyData['base_url']
    for key in urlParams:
        url = url +'&'+key+'='+urlParams[key]
    return url

def getUrl(_from, _to):
    urlParams = {'sl':_from,'tl':_to}
    url = frameURL(urlParams)
    return url


def getData():
    fileData = GetFileData()
    data = ''
    for index in range(len(fileData)):
        data = data + 'q=' + fileData[index]
        if index is not len(fileData)-1:
            data = data+'&'
    return data


def getHeader():
    keyData = getKeydata()
    header = keyData['headerData']
    return header

def getResponse(_from,_to):
    url = getUrl(_from,_to)
    data = getData()
    header = getHeader()
    response = requests.post(url,data,header)
    return response.text
