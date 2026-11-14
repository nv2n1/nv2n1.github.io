---
title: "bdftopcf(1)"
name: "bdftopcf"
section: "1"
letter: "b"
url: "/docs/linux/man/1-bdftopcf/"
description: "bdftopcf – convert X font from Bitmap Distribution Format to Portable Compiled Format"
---

<h2 class="name">NAME</h2>
<p> bdftopcf &#8211; convert X font from Bitmap Distribution Format to Portable Compiled Format </p>
<h2>SYNOPSIS</h2>
<p> <code>bdftopcf</code> [ <code>-p</code><i>n</i> ] [ <code>-u</code><i>n</i> ] [ <code>-m</code> ] [ <code>-l</code> ] [ <code>-M</code> ] [ <code>-L</code> ] [ <code>-t</code> ] [ <code>-i</code> ] [ <code>-o</code> <i>outputfile</i> ] fontfile.bdf</p>
<h2>DESCRIPTION</h2>
<p> <i>Bdftopcf</i> is a font compiler for the X server and font server. Fonts in Portable Compiled Format can be read by any architecture, although the file is structured to allow one particular architecture to read them directly without reformatting. This allows fast reading on the appropriate machine, but the files are still portable (but read more slowly) on other machines.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-p</code><i>n</i></p>
<dd> Sets the font glyph padding. Each glyph in the font will have each scanline padded in to a multiple of <i>n</i> bytes, where <i>n</i> is 1, 2, 4 or 8.</p>
<dt><code>-u</code><i>n</i></p>
<dd> Sets the font scanline unit. When the font bit order is different from the font byte order, the scanline unit <i>n</i> describes what unit of data (in bytes) are to be swapped; the unit <i>i</i> can be 1, 2 or 4 bytes.</p>
<dt><code>-m</code></p>
<dd> Sets the font bit order to MSB (most significant bit) first. Bits for each glyph will be placed in this order; i.e., the left most bit on the screen will be in the highest valued bit in each unit.</p>
<dt><code>-l</code></p>
<dd> Sets the font bit order to LSB (least significant bit) first. The left most bit on the screen will be in the lowest valued bit in each unit.</p>
<dt><code>-M</code></p>
<dd> Sets the font byte order to MSB first. All multi-byte data in the file (metrics, bitmaps and everything else) will be written most significant byte first.</p>
<dt><code>-L</code></p>
<dd> Sets the font byte order to LSB first. All multi-byte data in the file (metrics, bitmaps and everything else) will be written least significant byte first.</p>
<dt><code>-t</code></p>
<dd> When this option is specified, <i>bdftopcf</i> will convert fonts into &quot;terminal&quot; fonts when possible. A terminal font has each glyph image padded to the same size; the X server can usually render these types of fonts more quickly.</p>
<dt><code>-i</code></p>
<dd> This option inhibits the normal computation of ink metrics. When a font has glyph images which do not fill the bitmap image (i.e., the &quot;on&quot; pixels don&#8217;t extend to the edges of the metrics) <i>bdftopcf</i> computes the actual ink metrics and places them in the .pcf file; the -t option inhibits this behaviour.</p>
<dt><code>-o </code><i>output-file-name</i></p>
<dd> By default <i>bdftopcf</i> writes the pcf file to standard output; this option gives the name of a file to be used instead.</p>
<dt><code>-v</code></p>
<dd> Print version information and exit.</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/7-x/">X</a>(7)</p>
<h2>AUTHOR</h2>
<p> Keith Packard, MIT X Consortium </p>
<h2>Index</h2>
