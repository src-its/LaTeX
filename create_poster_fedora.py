import argparse
import subprocess
import shlex
import os

#builds the actual LaTeX file

content=r"""\documentclass{beamer}

\usetheme{simple}


\usepackage{lmodern}
\usepackage[scale=2]{ccicons}
"""
#watermark = "\setwatermark{\includegraphics[height=8cm]{""" + image + "}}"

maketitle = r"""\title{""" + title + r"""}
"""
name = r"""\subtitle{with """ + ca + r"""}
"""

date = r"""\date{""" + eventdate + r"""}
\author{@theCADesk}

\begin{document}

\maketitle



\end{document}"""
#parser data below to make the input fields

parser=argparse.ArgumentParser()
#parser.add_argument('-bg', '--image')
parser.add_argument('-t', '--title', default='Aaron would be ashamed that you are not paying attention')
parser.add_argument('-ca', '--ca', default='Nemo')
parser.add_argument('-d', '--date', default='4/20')

args=parser.parse_args()
content%args.__dict__

with open('cover.tex','w') as f:
    f.write(content%args.__dict__)

proc=subprocess.Popen(shlex.split('pdflatex cover.tex'))
proc.communicate()
