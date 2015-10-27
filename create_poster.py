import argparse
import subprocess

def create_pdf(input_filename, output_filename):
    process = subprocess.Popen([
        "C:\\Program Files (x86)\\MiKTeX 2.9\\miktex\\bin\\latex.exe",
        "-output-format=pdf",
        "-job-name=" + output_filename, input_filename])
    process.wait()

p = argparse.ArgumentParser()
p.add_argument('-o', type=argparse.FileType('w'), metavar='output',
               help='File to be written to.')
flags = p.parse_args()

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

