---
title: "pstex2eps(1)"
name: "pstex2eps"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pstex2eps/"
description: "pstex2eps – Generate EPS file from PLplot pstex driver generated file"
---

<h2 class="name">NAME</h2>
<p> pstex2eps &#8211; Generate EPS file from PLplot pstex driver generated file </p>
<h2>SYNOPSIS</h2>
<p> <code>pstex2eps</code> &lt;filename&gt;</p>
<h2>DESCRIPTION</h2>
<p> <code>pstex2eps</code> is a program that generates an Encapsulated Postscript file (eps) from the PLplot pstex driver generated files. </p>
<p> &lt;filename&gt; is the name of the output file you specified with the -o option in PLplot. There must exist two files, the postscript file without text, &lt;filename&gt;, and the latex file with the text, &lt;filename&gt;_t. </p>
<p> The output file will be named &lt;filename&gt;.eps. </p>
<p> The Computer Modern Type 1 fonts will be included in the output eps file. If you intent to use the plot figure in LaTeX, just use a plain \include{&lt;filename&gt;_t} in your latex file.</p>
<h2>SEE ALSO</h2>
<p> The PLplot package at <a rel="nofollow" href="http://plplot.sf.net">http://plplot.sf.net</a></p>
<h2>AUTHOR</h2>
<p> This manual page was written by Rafael Laboissiere &lt;rafael [at] debian.org&gt;. </p>
<h2>Index</h2>
