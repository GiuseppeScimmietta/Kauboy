import sys
sys.path.insert(0, '..\packages')

import pygments
from pygments import lexers
from pygments import styles
from pygments import formatters

codeTxt = open('test.py').read()

codeTokens = pygments.lex(codeTxt, lexers.PythonLexer())

for token in codeTokens:
  print(token)

formatter = formatters.HtmlFormatter(linenos=True, noclasses=True , style='manni')
formatedTxt = (pygments.highlight(codeTxt, lexers.PythonLexer(), formatter))

#print(formatedTxt)

with open("highlightedCode.html", "w") as htmlFile:
    htmlFile.write(formatedTxt)