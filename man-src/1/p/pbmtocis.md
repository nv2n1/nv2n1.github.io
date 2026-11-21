---
title: "pbmtocis(1)"
name: "pbmtocis"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pbmtocis/"
description: "pbmtocis – convert a PBM image to a CompuServe RLE image"
---

<h2>SYNOPSIS</h2>
<p> <code>pbmtocis</code> [<code>-i</code>] [<code>-w</code>] [<i>cisfile</i>] </p>
<h2>DESCRIPTION</h2>
<p> This program is part of <code><a href="/docs/linux/man/1-netpbm/">Netpbm</a></code>(1) </p>
<p> <code>pbmtocis</code> reads a PBM image as input and produces a CompuServe RLE image as output. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-i</code></dt>
<dd> Inverse: Reverse the mapping of foreground/background to black/white. </dd>
<dt><code>-w</code></dt>
<dd> If the input image is smaller than the fixed size of the output image, pad with white pixels rather than black. </dd>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-cistopbm/">cistopbm</a></code>(1) , <code>pbm</code>(1) CompuServe RLE file format </p>
<h2>HISTORY</h2>
<p> <code>pbmtocis</code> was new in Netpbm 10.48 (September 2009). </p>
<h2>AUTHOR</h2>
<p> Copyright (C) 2009 John Elliot &lt;jce [at] seasip.demon.co.uk&gt; </p>
