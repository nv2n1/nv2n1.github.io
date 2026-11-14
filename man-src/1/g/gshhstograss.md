---
title: "gshhstograss(1)"
name: "gshhstograss"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gshhstograss/"
description: "gshhs2grass – Extracting GSHHS and WDBII data in GRASS-compatible ASCII format"
---

<h2>NAME</h2>
<p> gshhs2grass &#8211; Extracting GSHHS and WDBII data in GRASS-compatible ASCII format</p>
<h2>SYNOPSIS</h2>
<p> <code>gshhs2grass</code> <code>-i</code> gshhs_[f|h|i|l|c].b [ <code>-x</code><i>minx</i> ] [<code>-X</code><i>maxx</i> ] [ <code>-y</code><i>miny</i> ] [ <code>-Y</code><i>maxy</i> ]</p>
<h2>DESCRIPTION</h2>
<p> <code>gshhs2grass</code> reads the binary coastline (GSHHS) and and translates it into an ASCII format suitable for import into GRASS. It automatically handles byte-swabbing between different architectures.</p>
<dl>
<dt><i>gshhs_[f|h|i|l|c].b</i></p>
<dd> One of the GSHHS binary data file as distributed with the GSHHS data supplement. Any of the 5 standard resolutions (full, high, intermediate, low, crude) can be used. The resulting files are called dig_[ascii|att|cats].gshhs_[f|h|i|l|c].</dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>-x</code></p>
<dd> Specify a minimum (west) longitude.</p>
<dt><code>-X</code></p>
<dd> Specify a maximum (east) longitude.</p>
<dt><code>-y</code></p>
<dd> Specify a minimum (south) latitude.</p>
<dt><code>-Y</code></p>
<dd> Specify a maximum (north) latitude.</dl>
<h2>EXAMPLES</h2>
<p> To convert the full GSHHS data set , try </p>
<p> <code>gshhs2grass</code> <i>gshhs_f.b</i></p>
<h2>BUGS</h2>
<p> Not updated to handle the WDBII line data (borders or rivers).</p>
<h2>AUTHOR</h2>
<p> Original version by Simon Cox (simon [at] ned.dem.csiro.au) with some maintenance by Paul Wessel (pwessel [at] hawaii.edu).</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-gmt/">GMT</a></i>(1), <i><a href="/docs/linux/man/1-gshhs/">gshhs</a></i>(1) <i><a href="/docs/linux/man/1-gshhs_dp/">gshhs_dp</a></i>(1) </p>
<h2>Index</h2>
