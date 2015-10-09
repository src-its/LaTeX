import argparse
import subprocess
import shlex
import os

#builds the actual LaTeX file

content=r"""\documentclass{article}

\usepackage{tikz}
\usepackage[top=2cm, bottom=2cm, outer=0cm, inner=0cm]{geometry}
\begin{document}
 Some content
\tikz[remember picture,overlay] \node[opacity=0.3,inner sep=0pt] at (current page.center){\includegraphics[width=\paperwidth,height=\paperheight]{%(image)}};
\clearpage
text

\end{document}"""
#parser data below to make the input fields

parser=argparse.ArgumentParser()
parser.add_argument('-bg', '--image', default='Capture.PNG')
parser.add_argument('-t', '--title', default='Aaron would be ashamed that you are not paying attention')
parser.add_argument('-ca', '--ca', default='Nemo')
parser.add_argument('-d', '--date', default='4/20')

args=parser.parse_args()
content%args.__dict__

with open('cover.tex','w') as f:
    f.write(content%args.__dict__)

proc=subprocess.Popen(shlex.split('pdflatex cover.tex'))
proc.communicate()
