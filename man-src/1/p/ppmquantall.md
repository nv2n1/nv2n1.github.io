---
title: "ppmquantall(1)"
name: "ppmquantall"
section: "1"
letter: "p"
url: "/docs/linux/man/1-ppmquantall/"
description: "ppmquantall – run ppmquant on a bunch of files all at once, so they share a common colormap"
---

<h2 class="name">NAME</h2>
<p> ppmquantall &#8211; run ppmquant on a bunch of files all at once, so they share a common colormap</p>
<h2>SYNOPSIS</h2>
<p> <code>ppmquantall</code> [<code>-ext</code> <i>extension</i>] <i>ncolors ppmfile</i> &#8230; </p>
<h2>DESCRIPTION</h2>
<p> Takes a bunch of portable pixmap as input. Chooses <i>ncolors</i> colors to best represent all of the images, maps the existing colors to the new ones, and <code>overwrites the input files</code> with the new quantized versions. </p>
<p> If you don&#8217;t want to overwrite your input files, use the <code>-ext</code> option. The output files are then named the same as the input files, plus a period and the extension text you specify. </p>
<p> Verbose explanation: Let&#8217;s say you&#8217;ve got a dozen pixmaps that you want to display on the screen all at the same time. Your screen can only display 256 different colors, but the pixmaps have a total of a thousand or so different colors. For a single pixmap you solve this problem with <i>ppmquant</i>; this script solves it for multiple pixmaps. All it does is concatenate them together into one big pixmap, run <i>ppmquant</i> on that, and then split it up into little pixmaps again. </p>
<p> (Note that another way to solve this problem is to pre-select a set of colors and then use <i>ppmquant</i>&#8216;s <code>-map</code> option to separately quantize each pixmap to that set.) </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-ppmquant/">ppmquant</a></code>(1), <code><a href="/docs/linux/man/5-ppm/">ppm</a>(5)</code> </p>
<h2>AUTHOR</h2>
<p> Copyright (C) 1991 by Jef Poskanzer. </p>
<h2>Index</h2>
