---
title: "psfstriptable(1)"
name: "psfstriptable"
section: "1"
letter: "p"
url: "/docs/linux/man/1-psfstriptable/"
description: "psfstriptable – remove the embedded Unicode character table from a console font"
---

<h2 class="name">NAME</h2>
<p> psfstriptable &#8211; remove the embedded Unicode character table from a console font </p>
<h2>SYNOPSIS</h2>
<p> <code>psfstriptable</code> <i>fontfile outfile</i></p>
<h2>DESCRIPTION</h2>
<p> <code>psfstriptable</code> reads a .psf format console font from <i>fontfile</i>, removes the embedded Unicode font table if there is one, and writes the result to <i>outfile</i>. An input file name of &quot;-&quot; denotes standard input, and an output file name of &quot;-&quot; denotes standard output.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/8-setfont/">setfont</a></code>(8), <code><a href="/docs/linux/man/1-psfaddtable/">psfaddtable</a></code>(1), <code><a href="/docs/linux/man/1-psfgettable/">psfgettable</a></code>(1), <code><a href="/docs/linux/man/1-psfxtable/">psfxtable</a></code>(1) </p>
<h2>Index</h2>
