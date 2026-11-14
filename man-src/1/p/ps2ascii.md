---
title: "ps2ascii(1)"
name: "ps2ascii"
section: "1"
letter: "p"
url: "/docs/linux/man/1-ps2ascii/"
description: "ps2ascii – Ghostscript translator from PostScript or PDF to ASCII"
---

<h2 class="name">NAME</h2>
<p> ps2ascii &#8211; Ghostscript translator from PostScript or PDF to ASCII </p>
<h2>SYNOPSIS</h2>
<p> <code>ps2ascii</code> [ <i>input.ps</i> [ <i>output.txt</i> ] ]<br />
 <code>ps2ascii</code> <i>input.pdf</i> [ <i>output.txt</i> ]</p>
<h2>DESCRIPTION</h2>
<p> <code>ps2ascii</code> uses <code><a href="/docs/linux/man/1-gs/">gs</a></code>(1) to extract ASCII text from <code>PostScript</code>(tm) or Adobe <code>Portable Document Format</code> (PDF) files. If no files are specified on the command line, <code>gs</code> reads from standard input; but PDF input must come from an explicitly-named file, not standard input. If no output file is specified, the ASCII text is written to standard output. </p>
<p> <code>ps2ascii</code> doesn&#8217;t look at font encoding, and isn&#8217;t very good at dealing with kerning, so for PostScript (but not currently PDF), you might consider <code>pstotext</code> (see below).</p>
<h2>FILES</h2>
<p> Run &quot;<code>gs -h</code>&quot; to find the location of Ghostscript documentation on your system, from which you can get more details.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-pstotext/">pstotext</a>(1), <a rel="nofollow" href="http://www.research.digital.com/SRC/virtualpaper/pstotext.html">http://www.research.digital.com/SRC/virtualpaper/pstotext.html</a></p>
<h2>VERSION</h2>
<p> This document was last revised for Ghostscript version 9.55.0.</p>
<h2>AUTHOR</h2>
<p> Artifex Software, Inc. are the primary maintainers of Ghostscript. David M. Jones &lt;dmjones [at] theory.lcs.mit.edu&gt; made substantial improvements to <code>ps2ascii</code>. </p>
<h2>Index</h2>
