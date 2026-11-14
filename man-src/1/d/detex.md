---
title: "detex(1)"
name: "detex"
section: "1"
letter: "d"
url: "/docs/linux/man/1-detex/"
description: "detex – a filter to strip TeX commands from a .tex file."
---

<h2 class="name">NAME</h2>
<p> detex &#8211; a filter to strip <i>TeX</i> commands from a .tex file. </p>
<h2>SYNOPSIS</h2>
<p> <code>detex</code> [ <code>-clnstw</code> ] [ <code>-e</code><i> environment-list</i> ] [ <i>filename</i>[.tex] &#8230; ]</p>
<h2>DESCRIPTION</h2>
<p> <i>Detex</i> reads each file in sequence, removes all comments and <i>TeX</i> control sequences and writes the remainder on the standard output. All text in math mode and display mode is removed. By default, <i>detex</i> follows \input commands. If a file cannot be opened, a warning message is printed and the command is ignored. If the <code>-n</code> option is used, no \input or \include commands will be processed. This allows single file processing. If no input file is given on the command line, <i>detex</i> reads from standard input. </p>
<p> If the magic sequence &#8220;egin{document}&#8221; appears in the text, <i>detex</i> assumes it is dealing with <i>LaTeX</i> source and <i>detex</i> recognizes additional constructs used in <i>LaTeX</i>. These include the \include and \includeonly commands. The <code>-l</code> option can be used to force <i>LaTeX</i> mode and the <code>-t</code> option can be used to force <i>TeX</i> mode regardless of input content. </p>
<p> Text in various environment modes of <i>LaTeX</i> is ignored. The default modes are array, eqnarray, equation, longtable, picture, tabular and verbatim. The <code>-e</code> option can be used to specify a comma separated <i>environment-list</i> of environments to ignore. The list replaces the defaults so specifying an empty list effectively causes no environments to be ignored. </p>
<p> The <code>-c</code> option can be used in <i>LaTeX</i> mode to have detex echo the arguments to 
