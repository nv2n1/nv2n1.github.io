---
title: "jbigtopnm(1)"
name: "jbigtopnm"
section: "1"
letter: "j"
url: "/docs/linux/man/1-jbigtopnm/"
description: "jbigtopnm – JBIG to PNM image file converter"
---

<h2 class="name">NAME</h2>
<p> jbigtopnm &#8211; JBIG to PNM image file converter</p>
<h2>SYNOPSIS</h2>
<p> <code>jbigtopnm</code> [<i>options</i>] [<i>input-file</i> [<i>output-file</i>]] </p>
<h2>DESCRIPTION</h2>
<p> This program is part of <code><a href="/docs/linux/man/1-netpbm/">Netpbm</a></code>(1) </p>
<p> <code>jbigtopnm</code> reads a JBIG bi-level image entity (BIE) from a file or standard input, decompresses it, and outputs a PBM or PGM file. If the input has one plane, or you choose just one plane of it, the output is PBM. Otherwise, the output is PGM. </p>
<p> JBIG is a highly effective lossless compression algorithm for bi-level images (one bit per pixel), which is particularly suitable for scanned document pages. </p>
<p> A JBIG encoded image can be stored in several resolutions in one or several BIEs. All resolution layers except the lowest one are stored efficiently as differences to the next lower resolution layer. You can use options <code>-x</code> and <code>-y</code> to stop the decompression at a specified maximal output image size. The input file can consist of several concatenated BIEs which contain different increasing resolution layers of the same image. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-x</code> <i>number</i></p>
<dd> Decode only up to the largest resolution layer which is still not more than <i>number</i> pixels wide. If no such resolution layer exists, then use the smallest one available. </p>
<dt><code>-y</code><i> number</i></p>
<dd> Decode only up to the largest resolution layer which is still not more than <i>number</i> pixels high. If no such resolution layer exists, then use the smallest one available. You can also use options <code>-x</code> and <code>-y</code> together which selects the largest layer that satisfies both limits. </p>
<dt><code>-b</code></p>
<dd> Use binary values instead of Gray code words in order to decode pixel values from multiple bitplanes. This option has effect only if the input has more than one bitplane and you don&#8217;t select just one of those bitplanes. Note that the decoder has to be used in the same mode as the encoder and cannot determine from the BIE, whether Gray or binary code words were used by the encoder. </p>
<dt><code>-d</code></p>
<dd> Diagnose a BIE. With this option, <code>jbigtopnm</code> only prints a summary of the header information found in the input file and then exits. </p>
<dt><code>-p</code><i> number</i></p>
<dd> If the input contains multiple bitplanes, then extract only the specified single plane as a PBM file. The first plane has number 0. </p>
</dl>
<h2>STANDARDS</h2>
<p> This program implements the JBIG image coding algorithm as specified in ISO/IEC 11544:1993 and ITU-T T.82(1993). </p>
<h2>AUTHOR</h2>
<p> <code>jbigtopnm</code> is based on the JBIG library by Markus Kuhn, part of his <code>JBIG-KIT</code> package . The <code>jbgtopbm</code> program is part of the <code>JBIG-KIT</code> package. </p>
<p> <code>jbigtopnm</code> is part of the Netpbm package of graphics tools. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pnm/">pnm</a></code>(1) , <code><a href="/docs/linux/man/1-pnmtojbig/">pnmtojbig</a></code>(1) </p>
<h2>LICENSE</h2>
<p> If you use <code>jbigtopnm</code>, you are using various patents, particularly on its arithmetic encoding method, and in all probability you do not have a license from the patent owners to do so. </p>
<h2>Index</h2>
