---
title: "allneeded(1)"
name: "allneeded"
section: "1"
letter: "a"
url: "/docs/linux/man/1-allneeded/"
description: "allneeded – force the calculation of all fonts now needed"
---

<h2 class="name">NAME</h2>
<p> allneeded &#8211; force the calculation of all fonts now needed </p>
<h2>SYNOPSIS</h2>
<p> <code>allneeded [-r] files &#8230;</code></p>
<h2>DESCRIPTION</h2>
<p> <i>allneeded</i> forces the calculation of all fonts that are needed to preview a set of dvi files. Just specify where the program should search for files on the commandline. The fonts generation is triggered by running <i><a href="/docs/linux/man/1-dvips/">dvips</a></i>(1) over all accessible dvi-files. Therefore, the fonts are created in the resolution needed by dvips. </p>
<p> If the -r flag is specified, the command <i><a href="/docs/linux/man/1-dvired/">dvired</a></i>(1) will be used instead of dvips. </p>
<p> <i>allneeded</i> does not recalculate existing fonts (as long as the Metafont mode does not change). </p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-allec/">allec</a>(1), <a href="/docs/linux/man/1-allcm/">allcm</a>(1), <a href="/docs/linux/man/1-dvips/">dvips</a>(1), <a href="/docs/linux/man/1-dvired/">dvired</a>(1). </p>
<h2>AUTHOR</h2>
<p> Thomas Esser &lt;te [at] dbs.uni-hannover.de&gt; </p>
<h2>Index</h2>
