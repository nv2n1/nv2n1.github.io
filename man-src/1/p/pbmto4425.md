---
title: "pbmto4425(1)"
name: "pbmto4425"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pbmto4425/"
description: "pbmto4425 – Display PBM images on an AT&T 4425 terminal"
---

<h2 class="name">NAME</h2>
<p> pbmto4425 &#8211; Display PBM images on an AT&amp;T 4425 terminal</p>
<h2>SYNOPSIS</h2>
<p> <code>pbmto4425</code> [<i>pbmfile</i>] </p>
<h2>DESCRIPTION</h2>
<p> This program is part of <code><a href="/docs/linux/man/1-netpbm/">Netpbm</a></code>(1) </p>
<p> <code>pbmto4425</code> displays PBM format images on an AT&amp;T 4425 ASCII terminal using that terminal&#8217;s mosaic graphics character set. The program should also work with other VT100-like terminals with mosaic graphics character sets such as the C. Itoh CIT-101, but it has not yet been tested on terminals other than the 4425. </p>
<p>&nbsp;<wbr><code>Pbmto4425</code>&nbsp;<wbr>puts the terminal into 132 column mode to achieve the maximum resolution of the terminal. In this mode the terminal has a resolution of 264 columns by 69 rows. The pixels have an aspect ratio of 1:2.6, therefore an image should be processed before being displayed in a manner such as this: </p>
<pre>
<code>% pamscale -xscale 2.6 </code><i>pamfile</i> <code>\
    | pamscale -xysize 264 69 \
    | ppmtopgm \
    | pamditherbw \
    | pbmto4425</code>
</pre>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pbmtoascii/">pbmtoascii</a></code>(1) , <code><a href="/docs/linux/man/1-ppmtoterm/">ppmtoterm</a></code>(1) , <code><a href="/docs/linux/man/1-pbm/">pbm</a></code>(1) </p>
<h2>AUTHOR</h2>
<p> Copyright (C) 1993 by Robert Perlberg </p>
<h2>Index</h2>
