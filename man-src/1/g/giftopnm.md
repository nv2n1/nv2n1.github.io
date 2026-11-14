---
title: "giftopnm(1)"
name: "giftopnm"
section: "1"
letter: "g"
url: "/docs/linux/man/1-giftopnm/"
description: "giftopnm – convert a GIF file into a portable anymap"
---

<h2 class="name">NAME</h2>
<p> giftopnm &#8211; convert a GIF file into a portable anymap </p>
<h2>SYNOPSIS</h2>
<p> <code>giftopnm</code> [<code>&#8211;alphaout=</code>{<i>alpha-filename</i>,<code>&#8211;</code>}] [<code>-verbose</code>] [<code>-comments</code>] [<code>-image</code> <i>N</i>] [<i>GIFfile</i>] </p>
<h2>DESCRIPTION</h2>
<p> This is a graphics format converter from the GIF format to the PNM (i.e. PBM, PGM, or PPM) format. </p>
<p> If the image contains only black and maximally bright white, the output is PBM. If the image contains more than those two colors, but only grays, the output is PGM. If the image contains other colors, the output is PPM. </p>
<p> If you have an animated GIF file, you can extract individual frames from it with <code>gifsicle</code> and then convert those using <code>giftopnm</code>. </p>
<p> A GIF image contains rectangular pixels. They all have the same aspect ratio, but may not be square (it&#8217;s actually quite unusual for them not to be square, but it could happen). The pixels of a Netpbm image are always square. Because of the engineering complexity to do otherwise, <code>giftopnm</code> converts a GIF image to a Netpbm image pixel-for-pixel. This means if the GIF pixels are not square, the Netpbm output image has the wrong aspect ratio. In this case, <code>giftopnm</code> issues an informational message telling you to run <code>pnmscale</code> to correct the output. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;alphaout=</code><i>alpha-filename</i></p>
<dd> <code>giftopnm </code> creates a PGM (portable graymap) file containing the alpha channel values in the input image. If the input image doesn&#8217;t contain an alpha channel, the <i>alpha-filename</i> file contains all zero (transparent) alpha values. If you don&#8217;t specify <code>&#8211;alphaout</code>, <code>giftopnm</code> does not generate an alpha file, and if the input image has an alpha channel, <code>giftopnm</code> simply discards it. </p>
<p> If you specify <code>&#8211;</code> as the filename, <code>giftopnm</code> writes the alpha output to Standard Output and discards the image. </p>
<p> See <code><a href="/docs/linux/man/1-pnmcomp/">pnmcomp</a></code>(1) for one way to use the alpha output file.</p>
<dt><code>-verbose</code></p>
<dd> Produce verbose output about the GIF file input.</p>
<dt><code>-comments</code></p>
<dd> Only output GIF89 comment fields.</p>
<dt><code>-image </code><i>N</i></p>
<dd> Output the specified gif image from the input GIF archive (where <i>N</i> is &#8216;1&#8217;, &#8216;2&#8217;, &#8217;20&#8217;&#8230;). Normally there is only one image per file, so this option is not needed.</dl>
<p> All flags can be abbreviated to their shortest unique prefix. </p>
<h2>RESTRICTIONS</h2>
<p> This does not correctly handle the Plain Text Extension of the GIF89 standard, since I did not have any example input files containing them. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-ppmtogif/">ppmtogif</a></code>(1), <code><a href="/docs/linux/man/1-ppmcolormask/">ppmcolormask</a></code>(1), <code><a href="/docs/linux/man/1-pnmcomp/">pnmcomp</a></code>(1), <code><a href="/docs/linux/man/1-gifsicle/">gifsicle</a></code>(1) &lt;<a rel="nofollow" href="http://www.lcdf.org/gifsicle">http://www.lcdf.org/gifsicle</a>&gt;, <code><a href="/docs/linux/man/5-ppm/">ppm</a></code>(5).</p>
<h2>AUTHOR</h2>
<p> Copyright (c) 1993 by David Koblas (koblas [at] netcom.com) </p>
<h2>LICENSE</h2>
<p> If you use <code>giftopnm</code>, you are using a patent on the LZW compression method which is owned by Unisys, and in all probability you do not have a license from Unisys to do so. Unisys typically asks $5000 for a license for trivial use of the patent. Unisys has never enforced the patent against trivial users, and has made statements that it is much less concerned about people using the patent for decompression (which is what <code>giftopnm</code> does than for compression. The patent expires in 2003 / 2004, depending on the country. </p>
<p> Rumor has it that IBM also owns a patent covering <code>giftopnm</code>. </p>
<p> A replacement for the GIF format that does not require any patents to use is the PNG format. </p>
<h2>Index</h2>
