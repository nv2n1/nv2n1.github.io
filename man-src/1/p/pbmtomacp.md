---
title: "pbmtomacp(1)"
name: "pbmtomacp"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pbmtomacp/"
description: "pbmtomacp – convert a portable bitmap into a MacPaint file"
---

<h2 class="name">NAME</h2>
<p> pbmtomacp &#8211; convert a portable bitmap into a MacPaint file </p>
<h2>SYNOPSIS</h2>
<p> <code>pbmtomacp</code> [<code>-l</code> <i>left</i>] [<code>-r</code> <i>right</i>] [<code>-b</code> <i>bottom</i>] [<code>-t</code> <i>top</i>] [<i>pbmfile</i>]</p>
<h2>DESCRIPTION</h2>
<p> Reads a portable bitmap as input. If no input-file is given, standard input is assumed. Produces a MacPaint file as output. </p>
<p> The generated file is only the data fork of a picture. You will need a program such as <i>mcvert</i> to generate a Macbinary or a BinHex file that contains the necessary information to identify the file as a PNTG file to MacOS.</p>
<h2>OPTIONS</h2>
<p> Left, right, bottom &amp; top let you define a square into the pbm file, that must be converted. Default is the whole file. If the file is too large for a MacPaint-file, the bitmap is cut to fit from ( left, top ).</p>
<h2>BUGS</h2>
<p> The source code contains comments in a language other than English.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-ppmtopict/">ppmtopict</a>(1), <a href="/docs/linux/man/1-macptopbm/">macptopbm</a>(1), <a href="/docs/linux/man/5-pbm/">pbm</a>(5), <a href="/docs/linux/man/1-mcvert/">mcvert</a>(1)</p>
<h2>AUTHOR</h2>
<p> Copyright (C) 1988 by Douwe van der Schaaf (&#8230;!mcvax!uvapsy!vdschaaf). </p>
<h2>Index</h2>
