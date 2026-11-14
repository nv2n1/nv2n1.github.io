---
title: "g3data(1)"
name: "g3data"
section: "1"
letter: "g"
url: "/docs/linux/man/1-g3data/"
description: "g3data – A tool for extracting data from graphs."
---

<h2>NAME</h2>
<p> g3data &#8211; A tool for extracting data from graphs.</p>
<h2>SYNOPSIS</h2>
<p> <code>g3data</code> [ <code>-max</code><i> x y</i> ] [ <code>-scale</code><i> factor</i> ] [ <code>-coords</code><i> llx lly rux ruy</i> ] [ <code>-errors</code> ] [ <code>-lnx</code> ] [ <code>-lny</code> ] [ <i>filename(s) &#8230;</i> ]</p>
<h2>DESCRIPTION</h2>
<p> <code>g3data</code> is a tool for extracting data from scanned graphs. For graphs published in scientific articles the actual data is usually not explicitly given ; g3data makes the process of extracting this data easy.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-max </code><i>x y</i></p>
<dd> If picture is larger x-wise than x or y-wise than y, the picture is scaled down accordingly otherwise this parameter has no effect.</p>
<dt><code>-scale </code><i>factor</i></p>
<dd> Scales the picture size by factor. This parameter nullifies effect of the -max parameter.</p>
<dt><code>-coords </code><i>llx lly rux ruy</i></p>
<dd> Preset the coordinates of the left lower (ll) corner and the right upper (ru) corner.</p>
<dt><code>-errors</code></p>
<dd> Print out the error of the x value in column 3 and the error of y value in column 4 of the output.</p>
<dt><code>-lnx</code></p>
<dd> Use logarithmic scale for x coordinates.</p>
<dt><code>-lny</code></p>
<dd> Use logarithmic scale for y coordinates.</p>
<dt><i>filename(s) &#8230;</i></p>
<dd> The filename(s) of the image(s) to open. Supported image formats: PNG, XPM, JPEG, TIFF, PNM, RAS, BMP and GIF.</dl>
<h2>USAGE</h2>
<p> <code>g3data</code> -scale 2 -errors test1.png </p>
<p> <code>g3data</code> -scale 2 -lny -errors test2.png</p>
<h2>BUGS</h2>
<p> None known.</p>
<h2>AUTHOR</h2>
<p> Jonas Frantz &lt;jonas.frantz [at] welho.com&gt; </p>
<h2>Index</h2>
