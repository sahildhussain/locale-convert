# localeConvert
This locale converter/Translator translates a locale(.xml) file to other language locale(.xml) files.

Steps to follow:

1. Install textBlob and requests using PIP

```pip3 install requests textblob```

2. Run the app(python app.py)

you can enter multiple languages at a time to convert(separated by space).

location of new files will be similar to path of original file.

NOTE: use python3 and pip3
for using Microsoft translation api. you need azure key of translation project(needs to be replaced in keysData.json)

run command: 

`python app.py`

Inline command: 

`python app.py $filepath $originalLanguage $language1,language2`

defualt filePath = default.xml which is available along with the library (provide 'na' for default)
