---
title: "mrftopbm(1)"
name: "mrftopbm"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mrftopbm/"
description: "mrftopbm – convert an MRF image to PBM format"
---

<h2 class="name">NAME</h2>
<p> mrftopbm &#8211; convert an MRF image to PBM format</p>
<h2>SYNOPSIS</h2>
<p> <code>mrftopbm</code> [ <code>-a</code> ] [ <i>input.mrf</i> ] </p>
<h2>DESCRIPTION</h2>
<p> This program is part of <code><a href="/docs/linux/man/1-netpbm/">Netpbm</a></code>(1) </p>
<p> <code>mrftopbm</code> converts an MRF image to PBM format. </p>
<p> <code>mrftopbm</code> takes the MRF image from the file named by the <i>input.mrf</i> argument, or Standard Input if you don&#8217;t specify <i>input.mrf</i>. The output goes to Standard Output. </p>
<p> For more information about mrf, see <code>the</code>MRF specification (1) </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-a</code></p>
<dd> causes <code>mrftopbm</code> to include the edges, if any, in the output PBM. This may help when debugging a compressor&#8217;s edge optimization. </p>
</dl>
<h2>AUTHOR</h2>
<p> Russell Marks. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pbmtomrf/">pbmtomrf</a></code>(1) , <code><a href="/docs/linux/man/1-pbm/">pbm</a></code>(1) , <code><a href="/docs/linux/man/1-mrf/">mrf</a></code>(1) </p>
<h2>Index</h2>
