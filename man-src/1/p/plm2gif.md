---
title: "plm2gif(1)"
name: "plm2gif"
section: "1"
letter: "p"
url: "/docs/linux/man/1-plm2gif/"
description: "plm2gif – converts PLplot metafiles to GIF files"
---

<h2>NAME</h2>
<p> plm2gif &#8211; converts PLplot metafiles to GIF files</p>
<h2>SYNOPSIS</h2>
<p> <code>plm2gif</code> <i>[files]</i></p>
<h2>DESCRIPTION</h2>
<p> This manual page documents briefly the <code>plm2gif</code> command. </p>
<p> <code>plm2gif</code> is a program that Converts specified PLplot metafiles to GIF format files. This is a two-step process: 1. process into postscript (with custom flags); and 2. convert to GIF using ghostscript (more custom flags). </p>
<p> Each input file must end with <i>.plm </i> , and a corresponding family of GIF files ending with <i>&lt;number&gt;.gif</i> (one for each page) is created. </p>
<h2>SEE ALSO</h2>
<p> See /usr/share/doc/plplot/plplot.ps.gz for more details.</p>
<h2>AUTHOR</h2>
<p> This manual page was written by Rafael Laboissiere &lt;rafael [at] debian.org&gt;. </p>
<h2>Index</h2>
