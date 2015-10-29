import argparse
import subprocess

def create_pdf(input_filename, output_filename):
    subprocess.call("pdflatex " + input_filename, shell=True)

p = argparse.ArgumentParser()
p.add_argument('-o', type=argparse.FileType('w'), metavar='output',
               help='File to be written to.')
p.add_argument('-p', type=str, metavar='path', default="C:\\Program Files (x86)\\MiKTeX 2.9\\miktex\\bin\\latex.exe", help='location of latex compiler')
flags = p.parse_args()

compiler = flags.p
print(compiler)

ca = input("Who's hosting this event? ")
eventdate = input("When's it happening? ")
title = input("What's the event's title? ")
blurb = input("What additional information do you want on the slide (what's your blurb?)")
image = input("Where is the background image you want to use? ")

image = image.replace("\\", "/")

top = r"""\documentclass{beamer}

\usetheme{simple}


\usepackage{lmodern}
\usepackage[scale=2]{ccicons}
"""
watermark = "\setwatermark{\includegraphics[height=8cm]{""" + image + "}}"

maketitle = r"""\title{""" + title + r"""}
"""
name = r"""\subtitle{with """ + ca + r"""}
"""

date = r"""\date{""" + eventdate + r"""\\[2em]
{\footnotesize """ + blurb + r""" }}
\author{@theCADesk}

\begin{document}

\maketitle

\end{document}
"""


flags.o.write(top + watermark + maketitle + name + date)
pdf = "example.pdf"

create_pdf(flags.o.name, pdf)

