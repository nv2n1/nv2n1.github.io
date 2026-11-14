---
title: "pbmtopsg3(1)"
name: "pbmtopsg3"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pbmtopsg3/"
description: "pbmtopsg3 – convert PBM images to Postscript with G3 fax compression"
---

<h2 class="name">NAME</h2>
<p> pbmtopsg3 &#8211; convert PBM images to Postscript with G3 fax compression</p>
<h2>SYNOPSIS</h2>
<p> <code>pbmtopsg3</code> [<code>&#8211;title=</code><i>title</i>] [<code>&#8211;dpi=</code><i>dpi</i>] [<i>filespec</i>] </p>
<h2>DESCRIPTION</h2>
<p> Converts the PBM images in the input PBM file to pages in a Postscript file encoded with G3 fax compression. </p>
<p> If you don&#8217;t specify <i>filespec</i>, the input is from Standard Input. </p>
<p> Remember that you can create a multi-image PBM file simply by concatenating single-image PBM files, so if each page is in a different file, you might do: </p>
<p> <code>cat faxpage* | pbmtopsg3 &gt;fax.ps</code> </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-title</code></p>
<dd> The Postscript title value. Default is no title.</p>
<dt><code>-dpi</code></p>
<dd> The resolution of the Postscript output. Default is 72 dpi. </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pnmtops/">pnmtops</a></code>(1), <code><a href="/docs/linux/man/1-pstopnm/">pstopnm</a></code>(1), <code><a href="/docs/linux/man/1-gs/">gs</a></code>(1), <code><a href="/docs/linux/man/1-pstopnm/">pstopnm</a></code>(1), <code><a href="/docs/linux/man/1-pbmtolps/">pbmtolps</a></code>(1), <code><a href="/docs/linux/man/1-pbmtoepsi/">pbmtoepsi</a></code>(1), <code><a href="/docs/linux/man/1-pbmtog3/">pbmtog3</a></code>(1), <code><a href="/docs/linux/man/1-g3topbm/">g3topbm</a></code>(1), <code><a href="/docs/linux/man/5-pbm/">pbm</a></code>(5) </p>
<h2>Index</h2>
