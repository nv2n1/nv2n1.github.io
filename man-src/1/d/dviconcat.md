---
title: "dviconcat(1)"
name: "dviconcat"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dviconcat/"
description: "dviconcat – concatenate DVI files"
---

<h2 class="name">NAME</h2>
<p> dviconcat &#8211; concatenate DVI files </p>
<h2>SYNOPSIS</h2>
<p> <code>dviconcat</code> [ <code>-m</code> <i>magnification</i> ] [ <code>-o</code> <i>outfile</i> ] <i>list of files</i></p>
<h2>DESCRIPTION</h2>
<p> <i>Dviconcat</i> concatenates the named <i>file</i>s (or standard input, if no file names are given) onto the standard output or the given <i>outfile</i>, creating a new DVI file usable by any of the TeX conversion programs, or even by <i>dviconcat</i> itself. </p>
<p> The magnification of the output file is the same as that of the first input file unless the <code>-m</code> option is given. When <i>dviconcat</i> changes the magnification of any input file, it prints a warning to this effect.</p>
<h2>AUTHOR</h2>
<p> Chris Torek, University of Maryland</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-dviselect/">dviselect</a>(1), <a href="/docs/linux/man/1-latex/">latex</a>(1), <a href="/docs/linux/man/1-tex/">tex</a>(1)<br />
 <i>MC-TeX User&#8217;s Guide</i></p>
<h2>BUGS</h2>
<p> The program should be called <i>dvicat</i>, but that name was taken (for the driver for the C/A/T typesetter). </p>
<h2>Index</h2>
