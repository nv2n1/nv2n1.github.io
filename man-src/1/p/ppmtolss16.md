---
title: "ppmtolss16(1)"
name: "ppmtolss16"
section: "1"
letter: "p"
url: "/docs/linux/man/1-ppmtolss16/"
description: "ppmtolss16 — Convert a PPM to an LSS16 image"
---

<h2>NAME</h2>
<p> ppmtolss16 &#8212; Convert a PPM to an LSS16 image</p>
<h2>SYNOPSIS</h2>
<p> <code>ppmtolss16</code> [ <code><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt> </code><i>#rrggbb</i>=<i>i</i> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt> &#8230;] [&lt; input.ppm] [&gt; output.rle]</p>
<h2>DESCRIPTION</h2>
<p> This manual page documents briefly the <code>ppmtolss16</code> command. </p>
<p> The <code>ppmtolss16</code> program converts a &quot;raw&quot; PPM file with max 16 colors to a simple RLE-based format: </p>
<p> <code>simple RLE-based format</code> </p>
<table>
<tr VALIGN=top>
<td>unint32 0x1413f3d</td>
<td>magic (littleendian)
</td>
</tr>
<tr VALIGN=top>
<td>unint16 xsize</td>
<td>littleendian
</td>
</tr>
<tr VALIGN=top>
<td>unint15 ysize</td>
<td>littleendian
</td>
</tr>
<tr VALIGN=top>
<td>16 x unint8 r,g,b</td>
<td>color map
</td>
</tr>
</table>
<p> Color map is in 6-bit format (each byte is 0..63) </p>
<p> Then, a sequence of nybbles: </p>
<p> N &#8230; if N is != previous pixel, one pixel of color N, otherwise run sequence follows &#8230; </p>
<p> M &#8230; if M &gt; 0 then run length is M+1, otherwise run sequence is encoded in two nybbles, littleendian, +17 </p>
<p> The nybble sequences are on a per-row basis, runs may not extend across rows and odd-nybble rows are zero-padded. </p>
<p> At the start of a row, the &quot;previous pixel&quot; is assumed to be zero. </p>
<h2>OPTIONS</h2>
<p> A summary of options is included below.</p>
<dl>
<dt><i>#rrggbb</i>=<i>i</i></p>
<dd> Specify that the color #rrggbb (hex) should be assigned index i (decimal). </p>
</dl>
<h2>BUG</h2>
<p> This program cannot handle comments in the header, nor &quot;plain&quot; ppm format. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-ppmtolss16/">ppmtolss16</a></code>(1) </p>
<h2>AUTHOR</h2>
<p> This manual page was compiled by dann frazier &lt;dannf [at] debian.org&gt; for the <code>Debian GNU/Linux</code> system (but may be used by others). Most of the content was written by H. Peter Anvin. </p>
<h2>Index</h2>
