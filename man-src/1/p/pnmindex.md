---
title: "pnmindex(1)"
name: "pnmindex"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pnmindex/"
description: "pnmindex – build a visual index of a bunch of anymaps"
---

<h2 class="name">NAME</h2>
<p> pnmindex &#8211; build a visual index of a bunch of anymaps </p>
<h2>SYNOPSIS</h2>
<p> <code>pnmindex</code> [<code>-size</code> <i>N</i>] [<code>-across</code> <i>N</i>] [<code>-colors</code> <i>N</i>] [<code>-black</code>] [<code>-title</code> <i>T</i>] [<code>-quant</code>|<code>-noquant</code>] <i>pnmfile</i> &#8230; </p>
<h2>DESCRIPTION</h2>
<p> <code>pnmindex</code> creates an index image containing thumbnail (small) versions of a bunch of PNM files you supply. </p>
<p> <code>pnmindex</code> labels each thumbnail and, optionally, contains a title. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-size </code><i>N</i></p>
<dd> The size of each thumbnail. The image is scaled to fit maximally inside a <i>N</i> x <i>N</i> pixel box without changing its aspect ratio. Default is 100.</p>
<dt><code>-across </code><i>N</i></p>
<dd> The number of thumbnails in each row. Default is 6.</p>
<dt><code>-colors </code><i>N</i></p>
<dd> The maximum number of colors allowed in the overall image. If it would otherwise have more colors than these, <code>pnmindex</code> quantizes the result. The default is 256. </p>
<p> However, this value is meaningless if you specify the <code>-noquant</code> option.</p>
<dt><code>-black</code></p>
<dd> This controls the color of the padding between the images; normally it&#8217;s white and the labels are black lettering on white background, but the <code>-black</code> flag reverses this.</p>
<dt><code>-title </code><i>title</i></p>
<dd> Specifies a title top place at the top of the image. Default is no title.</p>
<dt><code>-quant</code></p>
<dd> Enables quanization (to the number of colors specified by <code>-colors</code> ). Quantization is on by default but you can disable it with <code>-noquant.</code></p>
<dt><code>-noquant</code></p>
<dd> See <code>-quant</code>. </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pnmscale/">pnmscale</a></code>(1), <code><a href="/docs/linux/man/1-pnmcat/">pnmcat</a></code>(1), <code><a href="/docs/linux/man/1-pbmtext/">pbmtext</a></code>(1), <code><a href="/docs/linux/man/1-ppmquant/">ppmquant</a></code>(1), <code><a href="/docs/linux/man/5-pnm/">pnm</a></code>(5) </p>
<h2>AUTHOR</h2>
<p> Copyright (C) 1991 by Jef Poskanzer. <code>-title</code> and <code>-noquant</code> added 2000 by John Heidemann. </p>
<h2>Index</h2>
