---
title: "asciitopgm(1)"
name: "asciitopgm"
section: "1"
letter: "a"
url: "/docs/linux/man/1-asciitopgm/"
description: "asciitopgm – convert ASCII graphics into a portable graymap"
---

<h2 class="name">NAME</h2>
<p> asciitopgm &#8211; convert ASCII graphics into a portable graymap </p>
<h2>SYNOPSIS</h2>
<p> <code>asciitopgm</code> <i>[</i>-d divisor<i>]</i> <i>height width</i> [<i>asciifile</i>]</p>
<h2>DESCRIPTION</h2>
<p> Reads ASCII data as input. Produces a portable graymap with pixel values which are an approximation of the &quot;brightness&quot; of the ASCII characters, assuming black-on-white printing. In other words, a capital M is very dark, a period is ver light, and a space is white. Input lines which are fewer than <i>width</i> characters are automatically padded with spaces. </p>
<p> The <i>divisor</i> argument is a floating-point number by which the output pixels are divided; the default value is 1.0. This can be used to adjust the brightness of the graymap: for example, if the image is too dim, reduce the divisor. </p>
<p> In keeping with (I believe) Fortran line-printer conventions, input lines beginning with a + (plus) character are assumed to &quot;overstrike&quot; the previous line, allowing a larger range of gray values. </p>
<p> This tool contradicts the message in the <i>pbmtoascii</i> manual: &quot;Note that there is no asciitopbm tool &#8211; this transformation is one-way.&quot;</p>
<h2>BUGS</h2>
<p> The table of ASCII-to-grey values is subject to interpretation, and, of course, depends on the typeface intended for the input.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-pbmtoascii/">pbmtoascii</a>(1), <a href="/docs/linux/man/5-pgm/">pgm</a>(5)</p>
<h2>AUTHOR</h2>
<p> Wilson H. Bent. Jr. (whb [at] usc.edu) </p>
<h2>Index</h2>
