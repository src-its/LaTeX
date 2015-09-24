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



Facundo Muñoz. "[A simple beamer theme](https://www.overleaf.com/latex/templates/a-simple-beamer-theme/qwmwbyhczrvx#.VgP_Ud9zjCI)" 

![](https://f15489c7a4793c2bed92-7907b7c5115fd43dfbc4abaca555987b.ssl.cf5.rackcdn.com/gallery-images/04ac50de86e37cf29faa3417770545937471399a.jpeg)

```
\documentclass{beamer}

\usetheme{simple}

\usepackage{lmodern}
\usepackage[scale=2]{ccicons}

% TODO: 
%   position adjustement
%   change colours
%       

% Watermark background (simple theme)

\setwatermark{\includegraphics[height=8cm]{img/Heckert_GNU_white.png}}


\title{A simple beamer theme}
\subtitle{}
\date{\today}
\author{Facundo Mu\~noz}
\institute{\url{http://github.com/famuvie}}

\begin{document}

\maketitle

\begin{frame}{simple}
  \framesubtitle{A beamer theme}

  \texttt{simple} is a minimalist Beamer theme that features

  \begin{columns}
    \column{.5\textwidth}
      \begin{itemize}
        \item a \alert{watermark} logo in the background
        \item slide \alert{numbers}
        \item \emph{emph}asized and \alert{alert}ed text
      \end{itemize}

    \column{.5\textwidth}
      \begin{block}{And of course...}
         blocks, columns, and all Beamer power
      \end{block}
  \end{columns}
  
\end{frame}



\setwatermark{\fontsize{125pt}{125pt}\selectfont{Simple}}

\begin{frame}[fragile]{watermark}
  \framesubtitle{not only for images}

  \begin{itemize}
    \item You can place \emph{any} \LaTeX{} \alert{contents} as a watermark
  \end{itemize}

  \begin{block}{In preamble}
    \begin{verbatim}
     \setwatermark{\includegraphics[height=8cm]{%
                   img/Heckert_GNU_white.png}}
    \end{verbatim}
  \end{block}

  \begin{block}{Just before this frame}
    \begin{verbatim}
     \setwatermark{\fontsize{125pt}{125pt}%
                   \selectfont{Simple}}
    \end{verbatim}
  \end{block}


\end{frame}



\setwatermark[hoffset=-3cm,voffset=-2cm]{\fontsize{125pt}{125pt}\selectfont{Simple}}


\begin{frame}{Options}
  \framesubtitle{Fine adjustement of the watermark position}

  
  \begin{itemize}
    \item \texttt{hoffset}
    \item \texttt{voffset}
  \end{itemize}
  
  They admit any \emph{positive} or \emph{negative} spacing \alert{unit}
  
  Note that some \alert{warnings} about \emph{badboxes} might be generated at compilation

\end{frame}




\begin{frame}{License}

  \begin{block}{Get the source of this theme and the demo presentation from}

  \begin{center}\url{http://github.com/famuvie/beamerthemesimple}\end{center}

  \end{block}
  
  The theme \emph{itself} is licensed under a
  \href{http://creativecommons.org/licenses/by-sa/4.0/}{Creative Commons
  Attribution-ShareAlike 4.0 International License}.

  \begin{center}\ccbysa\end{center}

\end{frame}

\end{document}

```



Sebastian Nordhoff. "[Optik Fysik1a](https://www.overleaf.com/articles/optik-fysik1a/hcdjzntrgpfk#.VgP_X99zjCI)" 

![](https://04cc30041f2b17b7c446-05c8531d4cdc1e161faed6a6f0a1f692.ssl.cf5.rackcdn.com/gallery-images/1ac33712294673a98676bd04d44d4101bc05a5a5.jpeg)

```
\documentclass{beamer}

\usetheme{simple}

\usepackage{lmodern}
\usepackage[scale=2]{ccicons}

% TODO: 
%   position adjustement
%   change colours
%       

% Watermark background (simple theme)

\setwatermark{\includegraphics[height=8cm]{logga.png}}

\title{Optik}
\subtitle{}
\date{\today}
\author{Magnus Wass}
\institute{\url{magnus.wass@nykopingsgymnasium.com}}

\begin{document}

\maketitle

\begin{frame}{Reflektion}
  \framesubtitle{ergo 264-68}

  

  
    
      \begin{itemize}
        \item \alert{Reflektionslagen} s\"ajer att reflektionsvinkeln 
        och infallsvinkeln \"ar lika stora
        \item Kom ih\aa g att vinklarna m\"ats fr\aa n \alert{normalen}
        \item \alert{Konkava speglar} ger en f\"orminskad, \emph{reell}, uppochnerv\"and 
        bild om f\"orem\aa let \"ar n\"ara spegeln och en f\"orstorad, \emph{virtuell} och
        r\"attv\"and bild annars
        \item \alert{Konvexa speglar} ger alltid en f\"orminskad,\emph{virtuell} och
        r\"attv\"and bild
      \end{itemize}

    
\end{frame}





\begin{frame}{Brytning}
\framesubtitle{ergo 269-74}
\begin{itemize}
\item \alert{Fermats princip} inneb\"ar att ljuset f\"oljer den snabbaste v\"agen mellan tv\aa punkter och leder till
 \item \alert{brytningslagen} $n_1\cdot \sin v_1=n_2\cdot \sin v_2$
 \item h\"ar \"ar det \"annu viktigare att komma ih\aa g att vinklarna m\"ats fr\aa n normalen!
 \item Ett mediums \alert{brytningsindex(n)} definieras som ljushastigheten i vakuum(c) delat med ljushastigheten i mediet(v), dvs. $n=\frac{c}{v}$.Eftersom $c \geq v$ g\"aller \"aven $n \geq 1$ 
\end{itemize}
\end{frame}

 




\begin{frame}{Prisma och linser}
\framesubtitle{ergo 275-83}
   
  \begin{itemize}
    \item Synligt ljus har v\aa gl\"angder i intervallet $400 nm$(violett)-$700 nm$(r\"ott)
    \item Brytningsindex minskar med \"okande v\aa gl\"angd
    \item F\"orem\aa ls f\"arg beror p\aa vilka v\aa gl\"angder som reflekteras
    \item vita f\"orem\aa l reflekterar alla (synliga) v\aa gl\"angder, svarta absorberar allt synligt ljus
    \item solen \"ar en svart kropp
    \item En \alert{konvex lins} bryter parallella(med optiska axeln) str\aa lar mot fokus och
    \item str\aa lar fr\aa n fokus bryts parallellt med optiska axeln
    \item En \alert{konkav lins} bryter parallella str\aa lar s\aa att de ser ut att komma fr\aa n fokus och 
    \item str\aa lar som ser ut att vara p\aa v\"ag mot fokus bryts parallella
    
  \end{itemize}
  

\end{frame}




\begin{frame}{Gauss linsformel och optiska instrument}
\framesubtitle{ergo 283-93}

  \begin{itemize}
    \item \alert{Gauss linsformel} lyder $\frac{1}{f}=\frac{1}{a}+\frac{1}{b}$
    d\"ar 
\begin{itemize}
\item f \"ar avst\aa ndet mellan lins och br\"annpunkt(kallas \"aven linsens br\"annvidd)
\item f \"ar avst\aa ndet mellan lins och f\"orem\aa l
\item f \"ar avst\aa ndet mellan lins och bild
\end{itemize}
    \item \alert{Linj\"ara f\"orstoringen } ges av $G=\frac{b}{a}$
    \item Br\"annvidden \"ar positiv f\"or de konvexa samlingslinserna och negativ f\"or de konkava spridningslinserna
    \item Bildavst\aa ndet(b) \"ar positivt f\"or reella(verkliha) bilder och negativt f\"or virtuella
    \item \alert{Dioptritalet} ges av $D=\frac{1}{f}$, d\"ar f uttrycks i meter
    \item 
  \end{itemize}
  
  

\end{frame}

\end{document}

```
