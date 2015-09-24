# Templating with LaTeX


### Beamer: A LaTex Tool for Slides and Presentations


Examples: 

Sebastian Nordhoff. "[Language Science Press Presentation](https://www.overleaf.com/latex/templates/language-science-press-presentation/rhdhbdbfvtqk#.VgP_RN9zjCI)" 

![](https://88df6ea0630aed8027ff-0caf779119a6537399728d4d80523795.ssl.cf5.rackcdn.com/rhdhbdbfvtqk/page/d523bc2ca26e6325ba9731fe4c48f374d7222130.jpeg)

```

              
\documentclass[handout]{beamer}

\usepackage[utf8x]{inputenc}
\usepackage{textcomp} 
\useoutertheme{lsp}

\usepackage{lsptitle}

\def\two@digits#1{\ifnum#1<10 0\fi\number#1}
\def\mytoday{\two@digits{\number\day}.\two@digits{\number\month}.\number\year}


\usepackage{xspace,multicol}
\newcommand{\latex}{\LaTeX\xspace}


\newcounter{lastpagemainpart}
\footnotesep0pt
\renewcommand{\footnoterule}{}
\usefootnotetemplate{
  \noindent
  \insertfootnotemark\insertfootnotetext}

\let\beamerfn=\footnote
\renewcommand{\footnote}[1]{%
\let\oldfnsize=\footnotesize%
\let\footnotesize=\tiny%
\beamerfn<\thebeamerpauses->{#1}%
\let\footnotesize=\oldfnsize}


\date{05.03.2014}

\usepackage{eurosym} 
\usepackage{ogonek}  % Dabrowska
%\usepackage{libertine}
 
\renewcommand{\centerline}[1]{\hfill#1\hfill\hfill\mbox{}}


\title{Language Science Press}
\institute{FU Berlin}
\author{Firstname Lastname}



\begin{document}
\lspbeamertitle
\section{Hintergrund}
 
\frame{
\frametitle{Hintergrund}
\begin{itemize}[<+->]
\item first
\item sth
\item lala
\item c
\end{itemize}
} 


\section{Organisation}
\subsection{Level 2}
\subsubsection{Ebene 3}


\frame{
\frametitle{Gemeinschaftsprojekt}
\begin{itemize}[<+->]
\item 
\end{itemize}
}




\setcounter{framenumber}{\thelastpagemainpart}
\end{document}

```


