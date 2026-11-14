---
title: "allec(1)"
name: "allec"
section: "1"
letter: "a"
url: "/docs/linux/man/1-allec/"
description: "allec – force the most important ec-fonts to be calculated"
---

<h2 class="name">NAME</h2>
<p> allec &#8211; force the most important ec-fonts to be calculated </p>
<h2>SYNOPSIS</h2>
<p> <code>allec [-r]</code></p>
<h2>DESCRIPTION</h2>
<p> <i>allec</i> forces a large number of ec-style Fonts to be calculated as pixel files. This is done through running <i><a href="/docs/linux/man/1-dvips/">dvips</a></i>(1) over a certain test-file. Therefore, the fonts are created in the resolution needed by dvips. </p>
<p> If the -r flag is specified, the command <i><a href="/docs/linux/man/1-dvired/">dvired</a></i>(1) will be used instead of dvips. </p>
<p> <i>alldc</i> does not recalculate existing fonts (as long as the Metafont mode does not change). </p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-allcm/">allcm</a>(1), <a href="/docs/linux/man/1-allneeded/">allneeded</a>(1), <a href="/docs/linux/man/1-dvips/">dvips</a>(1), <a href="/docs/linux/man/1-dvired/">dvired</a>(1). </p>
<h2>AUTHOR</h2>
<p> Thomas Esser &lt;te [at] dbs.uni-hannover.de&gt; </p>
<h2>Index</h2>
