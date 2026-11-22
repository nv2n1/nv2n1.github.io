---

title: "ilbmtoppm(1)"
name: "ilbmtoppm"
section: "1"
letter: "i"
url: "/docs/linux/man/1-ilbmtoppm/"
description: "ilbmtoppm – convert an ILBM file into a portable pixmap"
---

<p> ilbmtoppm &#8211; convert an ILBM file into a portable pixmap </p>
<h2>SYNOPSIS</h2>
<p> <code>ilbmtoppm</code> [<code>-verbose</code>] [<code>-ignore</code>&lt;chunkID&gt;<code>]</code> [<code>-isham</code>|<code>-isehb</code>] [<code>-adjustcolors</code>] [<i>ILBMfile</i>]</p>
<h2>DESCRIPTION</h2>
<p> Reads an IFF ILBM file as input. Produces a portable pixmap as output. Supported ILBM types are:</p>
<dl>
<dt>Normal ILBMs with 1-16 planes.</dt>
<dd>
</dd><dt>Amiga Extra_Halfbrite (EHB)</dt>
<dd>
</dd><dt>Amiga HAM with 3-16 planes.</dt>
<dd>
</dd><dt>24 bit.</dt>
<dd>
</dd><dt>Multiplatte (normal or HAM) pictures.</dt>
<dd>
</dd><dt>Color map (BMHD + CMAP chunk only, nPlanes = 0).</dt>
<dd>
</dd><dt>Unofficial direct color.</dt>
<dd> 1-16 planes for each color component.</dd>
<dt>Chunks used:</dt>
<dd> BMHD, CMAP, CAMG (only HAM &amp; EHB flags used), PCHG, BODY unofficial DCOL chunk to identify direct color ILBM</dd>
<dt>Chunks ignored:</dt>
<dd> GRAB, DEST, SPRT, CRNG, CCRT, CLUT, DPPV, DRNG, EPSF</dd>
<dt>Other chunks (ignored but displayed in verbose mode):</dt>
<dd> NAME, AUTH, (c), ANNO, DPI</dd>
<dt>Unknown chunks are skipped.</dt>
<dd></dd></dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>-verbose</code></dt>
<dd> Give some information about the ILBM file.</dd>
<dt><code>-ignore &lt;chunkID&gt;</code></dt>
<dd> Skip a chunk. &lt;chunkID&gt; is the 4-letter IFF chunk identifier of the chunk to be skipped.</dd>
<dt><code>-isham | -isehb</code></dt>
<dd> Treat the input file as a HAM or Extra_Halfbrite picture, even if these flags or not set in the CAMG chunk (or if there is no CAMG chunk).</dd>
<dt><code>-adjustcolors</code></dt>
<dd> If all colors in the CMAP have a value of less then 16, ilbmtoppm assumes a 4-bit colormap and gives a warning. With this option the colormap is scaled to 8 bits.</dd></dl>
<h2>BUGS</h2>
<p> The multipalette PCHG BigLineChanges and Huffman decompression code is untested.</p>
<h2>REFERENCES</h2>
<p> Amiga ROM Kernel Reference Manual &#8211; Devices (3rd Ed.)<br/>
 Addison Wesley, ISBN 0-201-56775-X</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/5-ppm/">ppm</a>(5), <a href="/docs/linux/man/1-ppmtoilbm/">ppmtoilbm</a>(1)</p>
<h2>AUTHORS</h2>
<p> Copyright (C) 1989 by Jef Poskanzer.<br/>
 Modified October 1993 by Ingo Wilken (Ingo.Wilken [at] informatik.uni-oldenburg.de) </p>
