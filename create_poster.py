import argparse

p = argparse.ArgumentParser()
p.add_argument('-o', type=argparse.FileType('w'), metavar='destfile',
               help='File to be written to.')
p.add_argument('--image', '-i', type=str, help='Background image for your poster.')
flags = p.parse_args()

image = r"" + input("Where is the image you want to use?")

top = r"""\documentclass{beamer}

\usetheme{simple}


\usepackage{lmodern}
\usepackage[scale=2]{ccicons}
"""
image = "\setwatermark{\includegraphics[height=8cm]{""" + flags.image + "}}"

end = r"""\title{Exciting Title!}
\subtitle{with some CA}
\date{\today}
\author{@theCADesk}

\begin{document}

\maketitle



\end{document}"""

flags.o.write(top + image + end)
