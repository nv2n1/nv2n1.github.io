---
title: "texlogfilter(1)"
name: "texlogfilter"
section: "1"
letter: "t"
url: "/docs/linux/man/1-texlogfilter/"
---

<h2>texlogfilter</h2>
<h3><font SIZE="-1">NAME</font></h3>
<p> texlogfilter &#8211; filter latex engines output or log file</p>
<h3><font SIZE="-1">SYNOPSIS</font></h3>
<pre>
    texlogfilter [options] file.log
</pre>
<h3><font SIZE="-1">DESCRIPTION</font></h3>
<p> Filter latex engines output or log file. For latex, pdflatex, lualatex or xelatex output or log file. </p>
<p> Without input file, standard input is used. Use on latex engine output with: </p>
<pre>
    latex file.tex &lt; /dev/null | texlogfilter
</pre>
<h3><font SIZE="-1">OPTIONS</font></h3>
<pre><code>
    --help                 : print this help and exit
    --version              : print version and exit
    --box                  : show box warnings
    --no-box               : mask box warnings
    --ref                  : show reference/citation warnings
    --no-ref               : mask reference/citation warnings
    --filename             : print current file name
    --no-filename          : do not print current file name
    --files-ext=string     : regex pattern used to match files extension (default: tex|sty|cls|bib)
    --skips                : indicate skipped lines
    --no-skips             : mask skipped lines
    --skip-marker=string   : marker used to indicate skipped lines (defaut: ...)
    --add-filter=string    : add user filter pattern (as perl regular expression)
    --full-log             : show full log (don't filter - only colorize latex engine output)
    --errors-color=string
    --warnings-color=string
    --infos-color=string
    --skips-color=string
    --user-color=string    : colors used for errors, warnings, informations and skipped lines
</code></pre>
<h3><font SIZE="-1">ALTERNATIVES</font></h3>
<dl>
<dt>&bull;</p>
<dd> <code>texlog-extract</code> : &lt;<a rel="nofollow" href="https://www.ctan.org/pkg/texlog-extract">https://www.ctan.org/pkg/texlog-extract</a>&gt;</p>
<dt>&bull;</p>
<dd> <code>texloganalyser</code> : &lt;<a rel="nofollow" href="https://www.ctan.org/pkg/texloganalyser">https://www.ctan.org/pkg/texloganalyser</a>&gt;</dl>
<h3><font SIZE="-1">AUTHOR</font></h3>
<p> Written by Julien Labbe. </p>
<p> Inspired from a script given by Martin Scharrer on Stack Exchange network (see &lt;<a rel="nofollow" href="https://tex.stackexchange.com/a/10564">https://tex.stackexchange.com/a/10564</a>&gt;).</p>
<h3><font SIZE="-1">LICENCE</font></h3>
<p> This work may be distributed and/or modified under the conditions of the LaTeX Project Public License, either version 1.3 of this license or (at your option) any later version. The latest version of this license is in &lt;<a rel="nofollow" href="http://www.latex-project.org/lppl.txt">http://www.latex-project.org/lppl.txt</a>&gt; and version 1.3 or later is part of all distributions of LaTeX version 2005/12/01 or later.</p>
<h3><font SIZE="-1">VERSION</font></h3>
<p> 1.0</p>
<h3><font SIZE="-1">HISTORY</font></h3>
<dl>
<dt>&bull;</p>
<dd> 2021, november : version 1.0 (initial version).</dl>
<h3><font SIZE="-1">DOCUMENTATION</font></h3>
<p> The documentation is integrated, writtent in Plain Old Documentation (<font SIZE="-1">POD</font>) format. Exported versions are available, in the following files:</p>
<dl>
<dt>&bull;</p>
<dd> <i></i><font SIZE="-1"><i>README</i></font><i></i>: created with perldoc.</p>
<dt>&bull;</p>
<dd> <i>texlogfilter.html</i>: created with pod2html. </p>
</dl>
<h2>Index</h2>
</dl>
