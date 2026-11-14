---
title: "any2djvu(1)"
name: "any2djvu"
section: "1"
letter: "a"
url: "/docs/linux/man/1-any2djvu/"
description: "any2djvu – Convert .ps/.ps.gz/.pdf to .djvu"
---

<h2>NAME</h2>
<p> any2djvu &#8211; Convert .ps/.ps.gz/.pdf to .djvu </p>
<h2>SYNOPSIS</h2>
<p> <code>any2djvu</code> <i>url {filename(s)}</i></p>
<h2>DESCRIPTION</h2>
<p> Converts files from .ps/.ps.gz/.pdf to .djvu by running them through a web server willing to perform this task. </p>
<p> Invoke with -h switch for usage information.</p>
<h2>ENVIRONMENT</h2>
<p> Non-empty value of DJVU_ONLINE_ACK acknowledges transmission of the documents to the server (so that no warning dialog is displayed).</p>
<h2>EXAMPLES</h2>
<p> any2djvu <a rel="nofollow" href="http://www.bcl.hamilton.ie/~barak/papers">http://www.bcl.hamilton.ie/~barak/papers</a> mesh-preprint.ps.gz </p>
<p> any2djvu localfile.pdf</p>
<h2>AUTHORS</h2>
<p> David Kreil, Barak A. Pearlmutter, Yaroslav O. Halchenko</p>
<h2>BUGS</h2>
<p> Using a web-based encoder server is a stop-gap measure until better encoders enjoy wide free distribution. </p>
<p> There is a security issue in operating on documents not intended for widespread distribution, which could be partially although not completely ameliorated by using a secure web connection.</p>
<h2>SEE ALSO</h2>
<p> The entire djvu suite, eg <a href="/docs/linux/man/1-djvu/">djvu</a>(1), <a href="/docs/linux/man/1-djview/">djview</a>(1), and <a href="/docs/linux/man/1-djvuserver/">djvuserver</a>(1). </p>
<h2>Index</h2>
