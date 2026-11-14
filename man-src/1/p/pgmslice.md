---
title: "pgmslice(1)"
name: "pgmslice"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pgmslice/"
description: "pgmslice – extract one line of pixel values out of a portable graymap"
---

<h2 class="name">NAME</h2>
<p> pgmslice &#8211; extract one line of pixel values out of a portable graymap </p>
<h2>SYNOPSIS</h2>
<p> <code>pgmslice</code> <code>-row</code>|<code>-col</code> <i>line</i> [<i>pgmfile</i>]</p>
<h2>DESCRIPTION</h2>
<p> Extracts one line of pixel values out of a portable graymap and outputs it in a two column ascii format, with the first value being the pixel&#8217;s position in the line and the second value the pixel&#8217;s greyscale value. This is useful for making cross sections through, for example, greyscale CCD images.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-row</code></p>
<dd> Extract a row of pixels</p>
<dt><code>-col</code></p>
<dd> Extract a column of pixels</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/5-pgm/">pgm</a>(5)</p>
<h2>AUTHOR</h2>
<p> pgmslice was written by Jos Dingjan &lt;jos [at] tuatha.org&gt; after being unable to find the source code to Marco Beijersbergen&#8217;s program with the same name. </p>
<h2>Index</h2>
