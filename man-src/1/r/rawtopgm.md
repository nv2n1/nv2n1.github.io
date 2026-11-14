---
title: "rawtopgm(1)"
name: "rawtopgm"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rawtopgm/"
description: "rawtopgm – convert raw grayscale bytes into a portable graymap"
---

<h2 class="name">NAME</h2>
<p> rawtopgm &#8211; convert raw grayscale bytes into a portable graymap </p>
<h2>SYNOPSIS</h2>
<p> <code>rawtopgm</code> [<code>-bpp </code>[<code>1</code>|<code>2</code>]] [<code>-littleendian</code>] [<code>-maxval</code> <i>N</i>] [<code>-headerskip</code> <i>N</i>] [<code>-rowskip</code> <i>N</i>] [<code>-tb</code>|<code>-topbottom</code>] [<i>width</i> <i>height</i>] [<i>imagefile</i>] </p>
<h2>DESCRIPTION</h2>
<p> Reads raw grayscale values as input. Produces a PGM file as output. The input file is just a sequence of pure binary numbers, either one or two bytes each, either bigendian or littleendian, representing gray values. They may be arranged either top to bottom, left to right or bottom to top, left to right. There may be arbitrary header information at the start of the file (to which <code>rawtopgm</code> pays no attention at all other than the header&#8217;s size). </p>
<p> Arguments to <code>rawtopgm</code> tell how to interpret the pixels (a function that is served by a header in a regular graphics format). </p>
<p> The <i>width</i> and <i>height</i> parameters tell the dimensions of the image. If you omit these parameters, <code>rawtopgm</code> assumes it is a quadratic image and bases the dimensions on the size of the input stream. If this size is not a perfect square, <code>rawtopgm</code> fails. </p>
<p> When you don&#8217;t specify <i>width</i> and <i>height</i>, <code>rawtopgm</code> reads the entire input stream into storage at once, which may take a lot of storage. Otherwise, <code>rawtopgm</code> ordinarily stores only one row at a time. </p>
<p> If you don&#8217;t specify <i>imagefile</i>, or specify <code>&#8211;</code>, the input is from Standard Input. </p>
<p> The PGM output is to Standard Output. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-maxval </code><i>N</i></p>
<dd> <i>N</i> is the maxval for the gray values in the input, and is also the maxval of the PGM output image. The default is the maximum value that can be represented in the number of bytes used for each sample (i.e. 255 or 65535).</p>
<dt><code>-bpp </code>[<code>1</code>|<code>2</code>]</p>
<dd> tells the number of bytes that represent each sample in the input. If the value is <code>2</code>, The most significant byte is first in the stream. </p>
<p> The default is 1 byte per sample. </p>
<dt><code>-littleendian</code></p>
<dd> says that the bytes of each input sample are ordered with the least significant byte first. Without this option, <code>rawtopgm</code> assumes MSB first. This obviously has no effect when there is only one byte per sample. </p>
<dt><code>-headerskip </code><i>N</i></p>
<dd> <code>rawtopgm</code> skips over <i>N</i> bytes at the beginning of the stream and reads the image immediately after. The default is 0. </p>
<p> This is useful when the input is actually some graphics format that has a descriptive header followed by an ordinary raster, and you don&#8217;t have a program that understands the header or you want to ignore the header. </p>
<dt><code>-rowskip </code><i>N</i></p>
<dd> If there is padding at the ends of the rows, you can skip it with this option. Note that rowskip need not be an integer. Amazingly, I once had an image with 0.376 bytes of padding per row. This turned out to be due to a file-transfer problem, but I was still able to read the image. </p>
<p> Skipping a fractional byte per row means skipping one byte per multiple rows.</p>
<dt><code>-bt -bottomfirst</code></p>
<dd> By default, <code>rawtopgm</code> assumes the pixels in the input go top to bottom, left to right. If you specify <code>-bt</code> or <code>-bottomfirst</code>, <code>rawtopgm</code> assumes the pixels go bottom to top, left to right. The Molecular Dynamics and Leica confocal format, for example, use the latter arrangement. </p>
<p> If you don&#8217;t specify <code>-bt</code> when you should or vice versa, the resulting image is upside down, which you can correct with <code>pnmflip .</code> </p>
<p> This option causes <code>rawtopgm</code> to read the entire input stream into storage at once, which may take a lot of storage. Ordinarly, <code>rawtopgm</code> stores only one row at a time. </p>
<p> For backwards compatibility, <code>rawtopgm</code> also accepts <code>-tb </code> and <code>-topbottom</code> to mean exactly the same thing. The reasons these are named backwards is that the original author thought of it as specifying that the wrong results of assuming the data is top to bottom should be corrected by flipping the result top for bottom. Today, we think of it as simply specifying the format of the input data so that there are no wrong results. </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/5-pgm/">pgm</a></code>(5), <code><a href="/docs/linux/man/1-rawtoppm/">rawtoppm</a></code>(1), <code><a href="/docs/linux/man/1-pnmflip/">pnmflip</a></code>(1) </p>
<h2>AUTHORS</h2>
<p> Copyright (C) 1989 by Jef Poskanzer.<br />
 Modified June 1993 by Oliver Trepte, oliver [at] fysik4.kth.se </p>
<h2>Index</h2>
