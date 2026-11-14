---
title: "escp2topbm(1)"
name: "escp2topbm"
section: "1"
letter: "e"
url: "/docs/linux/man/1-escp2topbm/"
description: "escp2topbm – convert an ESC/P2 printer file to a PBM image"
---

<h2 class="name">NAME</h2>
<p> escp2topbm &#8211; convert an ESC/P2 printer file to a PBM image</p>
<h2>SYNOPSIS</h2>
<p> <code>escp2topbm</code> [<i>printfile</i>] </p>
<h2>DESCRIPTION</h2>
<p> This program is part of <code><a href="/docs/linux/man/1-netpbm/">Netpbm</a></code>(1) </p>
<p> <code>escp2topbm</code> reads an ESC/P2 printer control stream as input. It produces a PBM image as output. </p>
<p> <code>escp2topbm</code> filters the raster graphic content from an Epson ESC/P2 printer control stream and writes the image it would print as a standard (raw) PBM image. </p>
<p> The input is from the file named by the <i>printfile</i> argument, or from Standard Input if you don&#8217;t specify <i>printfile</i>. The output is to Standard Output. </p>
<p> <code>escp2topbm</code> understands compression modes 0 (uncompressed) and 1 (RLE compressed) in the Epson input stream. </p>
<h2>OPTIONS</h2>
<p> none </p>
<h2>HINTS</h2>
<p> As <code>escp2topbm</code> is a simple program, created mainly to test <code>pbmtoescp2</code>, there are some restrictions: </p>
<dl>
<dt>&bull;</p>
<dd> <code>escp2topbm</code> looks only at &quot;ESC.&quot; sequences and ignores all data outside these Escape sequences. </p>
<dt>&bull;</p>
<dd> <code>escp2topbm</code> assumes that only one raster graphic is in the printer stream. If this isn&#8217;t true, the result is garbage. </p>
<dt>&bull;</p>
<dd> <code>escp2topbm</code> assumes that all &quot;ESC.&quot; sequences use the same width value. If this isn&#8217;t true, the result is garbage. </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pbmtoescp2/">pbmtoescp2</a></code>(1) , <code><a href="/docs/linux/man/1-pbm/">pbm</a></code>(1) </p>
<h2>AUTHOR</h2>
<p> Copyright (C) 2003 by Ulrich Walcher (<i>u.walcher [at] gmx.de</i>). </p>
<h2>HISTORY</h2>
<p> <code>escp2topbm</code> was added to Netpbm in Release 10.18 (August 2003); it was created around the same time. </p>
<h2>Index</h2>
