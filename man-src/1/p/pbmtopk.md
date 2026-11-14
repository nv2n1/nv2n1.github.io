---
title: "pbmtopk(1)"
name: "pbmtopk"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pbmtopk/"
description: "pbmtopk – convert a PBM image into a packed (PK) format font"
---

<h2 class="name">NAME</h2>
<p> pbmtopk &#8211; convert a PBM image into a packed (PK) format font </p>
<h2>SYNOPSIS</h2>
<p> <code>pbmtopk</code> <i>pkfile</i>[<code>.pk</code>] <i>tfmfile</i>[<code>.tfm</code>] <i>resolution</i> [<code>-s</code> <i>designsize</i>] [<code>-p</code> <i>num</i> <i>param</i>&#8230;] [<code>-C</code> <i>codingscheme</i>] [<code>-F</code> <i>family</i>] [<code>-f</code> <i>optfile</i>] [<code>-c</code> <i>num</i>] [<code>-W</code> <i>width</i>] [<code>-H</code> <i>height</i>] [<code>-D</code> <i>depth</i>] [<code>-I</code> <i>ital</i>] [<code>-h</code> <i>horiz</i>] [<code>-v</code> <i>vert</i>] [<code>-x</code> <i>xoff</i>] [<code>-y</code> <i>yoff</i>] [<i>pbmfile</i> &#8230;] </p>
<h2>DESCRIPTION</h2>
<p> This program is part of <code><a href="/docs/linux/man/1-netpbm/">Netpbm</a></code>(1) </p>
<p> <code>pbmtopk</code> reads PBM images as input and produces a packed (PK) font file and a TFM (TeX font metric) file as output. The resolution parameter indicates the resolution of the font, in dots per inch. If the filename &#8216;-&#8216; is used for any of the filenames, <code>pbmtopk</code> uses Standard Input or Standard Output. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-s</code> <i>designsize</i></p>
<dd> Sets the design size of the font, in TeX&#8217;s points (72.27pt to the inch). The default design size is 1. The TFM parameters are given as multiples of the design size. </p>
<dt><code>-p</code> <i>num</i> <i>param</i>&#8230;</p>
<dd> Sets the first num font parameters for the font. The first seven parameters are the slant, interword spacing, interword space stretchability, interword space shrinkability, x-height, quad width, and post-sentence extra space of the font. Math and symbol fonts may have more parameters; see The TeXbook for a list of these. Reasonable default values are chosen for parameters which are not specified. </p>
<dt><code>-C</code> <i>codingscheme</i></p>
<dd> Sets the coding scheme comment in the TFM file. </p>
<dt><code>-F</code> <i>family</i></p>
<dd> Sets the font family comment in the TFM file. </p>
<dt><code>-f</code> <i>optfile</i></p>
<dd> Reads the file optfile, which should contain a lines of the form: </p>
<pre>
   filename xoff yoff horiz vert width height depth ital
</pre>
<p> The PBM files specified by the filename parameters are inserted consecutively in the font with the specified attributes. If any of the attributes are omitted, or replaced with &#8216;*&#8217;, a default value will be calculated from the size of the bitmap. The settings of the -W, -H, -D, -I, -h, -v, -x, and -y options do not affected characters created in this way. The character number can be changed by including a line starting with &#8216;=&#8217;, followed by the new number. Lines beginning with &#8216;%&#8217; or &#8216;#&#8217; are ignored. </p>
<dt><code>-c</code> <i>num</i></p>
<dd> Sets the character number of the next bitmap encountered to num. </p>
<dt><code>-W</code> <i>width</i></p>
<dd> Sets the TFM width of the next character to width (in design size multiples). </p>
<dt><code>-H</code> <i>height</i></p>
<dd> Sets the TFM height of the next character to height (in design size multiples). </p>
<dt><code>-D</code> <i>depth</i></p>
<dd> Sets the TFM depth of the next character to depth (in design size multiples). </p>
<dt><code>-I</code> <i>ital</i></p>
<dd> Sets the italic correction of the next character to ital (in design size multiples). </p>
<dt><code>-h</code> <i>horiz</i></p>
<dd> Sets the horizontal escapement of the next character to horiz (in pixels). </p>
<dt><code>-v</code> <i>vert</i></p>
<dd> Sets the vertical escapement of the next character to vert (in pixels). </p>
<dt><code>-x</code> <i>xoff</i></p>
<dd> Sets the horizontal offset of the next character to xoff (in pixels). </p>
<dt><code>-y</code> <i>yoff</i></p>
<dd> Sets the vertical offset of the next character to yoff (in pixels, from the top row). </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pktopbm/">pktopbm</a></code>(1) , <code><a href="/docs/linux/man/1-pbm/">pbm</a></code>(1) </p>
<h2>AUTHOR</h2>
<p> Adapted from Tom Rokicki&#8217;s pxtopk by Angus Duggan &lt;<i>ajcd [at] dcs.ed.ac.uk</i>&gt;. </p>
<h2>Index</h2>
