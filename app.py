from pathlib import Path
import webbrowser
import os
import re

p = Path.cwd()/Path('default.xml')
text = p.read_text()

htmlFile = open('default.html','w')

regex = re.compile(r'\</[a-zA-Z0-9_]*\>')
modifiedText = regex.sub(lambda x:x.group()+'<br/>',text)
print(modifiedText)
htmlFile.write(modifiedText)

webbrowser.open('file://' + os.path.realpath('default.html'))