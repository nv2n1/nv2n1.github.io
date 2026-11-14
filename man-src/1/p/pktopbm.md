---
title: "pktopbm(1)"
name: "pktopbm"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pktopbm/"
description: "pktopbm – convert packed (PK) format font into PBM"
---

<h2 class="name">NAME</h2>
<p> pktopbm &#8211; convert packed (PK) format font into PBM</p>
<h2>SYNOPSIS</h2>
<p> pktopbm pkfile[.pk] [ -x width ] [ -y height ] [-c num] pbmfile &#8230; </p>
<h2>DESCRIPTION</h2>
<p> This program is part of <code><a href="/docs/linux/man/1-netpbm/">Netpbm</a></code>(1) </p>
<p> <code>pktopbm</code> reads a packed (PK) font file as input, and produces PBM images as output. If the filename &#8216;-&#8216; is used for any of the filenames, the standard input stream (or standard output where appropriate) will be used. If either the width or height is specified, this value will be used for all bitmaps produced. Also if one or both values are specified, the bitmap will be relocated with the hoffset and voffset given in the pkfile. The basepoint will be placed in the lower left corner of the bitmap if the bitmap is bigger than the specified size it will be truncated at the top or right. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-c</code> <i>num</i></p>
<dd> Sets the character number of the next bitmap written to <i>num</i>. </p>
<dt><code>-x</code> <i>width</i></p>
<dd> Sets the width of the image in columns. </p>
<dt><code>-y</code> <i>width</i></p>
<dd> Sets the height of the image in rows. </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pbmtopk/">pbmtopk</a></code>(1) , <code><a href="/docs/linux/man/1-pbm/">pbm</a></code>(1) </p>
<h2>AUTHOR</h2>
<p> Adapted from Tom Rokicki&#8217;s pxtopk by Angus Duggan &lt;<i>ajcd [at] dcs.ed.ac.uk</i>&gt;. &lt;<i>bartel [at] informatik.tu-muenchen.de</i>&gt; in March 1995. </p>
<h2>Index</h2>
