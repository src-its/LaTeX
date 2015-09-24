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





Sebastian Nordhoff. "[한글발표 (A Presentation using Hangul)](https://www.overleaf.com/articles/hangeulbalpyo-a-presentation-using-hangul/cvctjmvfhbvw#.VgP_at9zjCI)" 

![](https://48ed35b78c1314685eae-5c768d3cc8f4223c2d92068bc1d68611.ssl.cf5.rackcdn.com/gallery-images/7f75b71d9bd013c1ad78962f00e1e4d44bcf6cab.jpeg)

```
\documentclass{beamer}
%
% Choose how your presentation looks.
%
% For more themes, color themes and font themes, see:
% http://deic.uab.es/~iblanes/beamer_gallery/index_by_theme.html
%
\mode<presentation>
{
  \usetheme{default}      % or try Darmstadt, Madrid, Warsaw, ...
  \usecolortheme{default} % or try albatross, beaver, crane, ...
  \usefonttheme{default}  % or try serif, structurebold, ...
  \setbeamertemplate{navigation symbols}{}
  \setbeamertemplate{caption}[numbered]
} 

\usepackage{kotex} 

\usepackage[english]{babel}
%\usepackage[utf8x]{inputenc}

\title[Your Short Title]{웹브라우저로 LaTex 문서 작성하기}
\author{이영석}
\institute{충남대학교}
\date{2015.7.16}

\begin{document}

\begin{frame}
  \titlepage
\end{frame}

% Uncomment these lines for an automatically generated outline.
%\begin{frame}{Outline}
%  \tableofcontents
%\end{frame}


\section{왜 Latex ?}

\begin{frame}{왜 Latex ?}

\begin{itemize}
\item 장점
\begin{itemize}
\item 오픈소스 문서편집/조판 SW
\item 많은 양 편집, 공동 편집
\item 대학원, 논문
\item 문서파일 pdf 통일
\end{itemize}

\item 단점
\begin{itemize}
\item 초기진입장벽
\item WISIG이 아니다.
\end{itemize}

\end{itemize}
\end{frame}

\section{ShareLaTeX}

%\subsection{First Subsection}

\begin{frame}{ShareLaTeX}{http://www.sharelatex.com}
  \begin{itemize}
  \item {
    웹 브라우저에서 ShareLaTeX 접속.
  }
  \item {
    가입 후 이용: 가입할 때 추천하면 용량 증가.
  }
  \item {Template 활용: 이력서, 보고서, 논문, 발표자료.}
  \item {한글 패키지 사용 주의.}
  
  \end{itemize}
  
\end{frame}

\begin{frame}{ShareLaTeX 화면}{http://www.sharelatex.com}

\begin{figure}[h!]
\centering
\includegraphics[scale=.35]{fig-sharelatex.png}
\caption{ShareLaTeX}
\label{fig:sharelatex}
\end{figure}

\end{frame}

\section{Overleaf}

% You can reveal the parts of a slide one at a time
% with the \pause command:
\begin{frame}{Overleaf}{http://www.overleaf.com}
  \begin{itemize}
  \item {
    웹 브라우저에서 Overleaf 접속.
    %\pause % The slide will pause after showing the first item
  }
  \item {   
    가입 후 이용.
  }
  % You can also specify when the content should appear
  % by using <n->:
  \item {
    Template 활용.
  }
  \item {
    \alert{영어 스펠 자동 체크 기능이 좋음.}
  }
  \item {
    \alert{실시간 컴파일 기능이 좋음.}
  }
  % or you can use the \uncover command to reveal general
  % content (not just \items):
  %\item<5-> {
   % Fifth item. \uncover<6->{Extra text in the fifth item.}
  %}
  \end{itemize}
\end{frame}

\begin{frame}{Overleaf 화면}{http://www.overleaf.com}

\begin{figure}[h!]
\centering
\includegraphics[scale=.3]{fig-overleaf.png}
\caption{Overleaf}
\label{fig:overleaf}
\end{figure}

\end{frame}


\section{SageMath}
\begin{frame}{SageMath}{https://cloud.sagemath.com}
  \begin{itemize}
  \item {
    웹 브라우저에서 SageMath 접속.
    %\pause % The slide will pause after showing the first item
  }
  \item {   
    가입 후 이용.
  }
  % You can also specify when the content should appear
  % by using <n->:
  \item {
    Template 활용.
  }
  \item {
    R, Python, Terminal, SageMath 기능이 있음.
  }
  \item {
    SageMath는 오픈소스.
  }
  % or you can use the \uncover command to reveal general
  % content (not just \items):
  %\item<5-> {
   % Fifth item. \uncover<6->{Extra text in the fifth item.}
  %}
  \end{itemize}
\end{frame}

\begin{frame}{SageMath 화면}{https://cloud.sagemath.com}

\begin{figure}[h!]
\centering
\includegraphics[scale=.2]{fig-sagemath.png}
\caption{Sagemath}
\label{fig:sagemath}
\end{figure}

\end{frame}



% Placing a * after \section means it will not show in the
% outline or table of contents.
\section*{Summary}

\begin{frame}{Summary}
  \begin{itemize}
  \item
    \alert{LaTeX} 문서를 웹 브라우저로 작성해보기.
  \item
    \alert{ShareLaTex, Overleaf}는 Dropbox, GitHub와도 연동.
  
  \end{itemize}
  
  \begin{itemize}
  \item
    활용
    \begin{itemize}
    \item
      종합설계.
    \item
      이력서.
    \end{itemize}
  \end{itemize}
\end{frame}



% All of the following is optional and typically not needed. 
\appendix
\section<presentation>*{\appendixname}
\subsection<presentation>*{For Further Reading}

\begin{frame}[allowframebreaks]
  \frametitle<presentation>{For Further Reading}
    
  \begin{thebibliography}{10}
    
  \beamertemplatebookbibitems
  % Start with overview books.

  \bibitem{Author1990}
    KTUG.
    \newblock {\em http://www.ktug.org}.
    
    
  \beamertemplatearticlebibitems
  % Followed by interesting articles. Keep the list short. 

  \bibitem{Someone2000}
    S.~Someone.
    \newblock On this and that.
    \newblock {\em Journal of This and That}, 2(1):50--100,
    2000.
  \end{thebibliography}
\end{frame}



\end{document}


```
