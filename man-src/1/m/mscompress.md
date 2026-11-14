---
title: "mscompress(1)"
name: "mscompress"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mscompress/"
description: "mscompress – compress data using LZ77 algorithm"
---

<h2 class="name">NAME</h2>
<p> mscompress &#8211; compress data using LZ77 algorithm </p>
<h2>SYNOPSIS</h2>
<p> <code>mscompress</code> [ <code>-h</code> ]<br />
 <code>mscompress</code> [ <code>-V</code> ]<br />
 <code>mscompress</code> [ <i>name &#8230;</i> ]</p>
<h2>DESCRIPTION</h2>
<p> <i>Mscompress</i> reduces the size of the named files using Lempel-Ziv coding (LZ77). Each input file is compressed to file eding with underscore and original file remains untouched. Output files then can be decompressed using Microsoft <code>EXPAND.EXE</code> utility or <a href="/docs/linux/man/1-msexpand/">msexpand</a>(1). In other words, <a href="/docs/linux/man/1-mscompress/">mscompress</a>(1) is binary compatible with Microsoft&#8217;s <code>COMPRESS.EXE</code> </p>
<h2>BUGS</h2>
<p> <code>Mscompress</code> cannot compress standard input as <a href="/docs/linux/man/1-gzip/">gzip</a>(1) or <a href="/docs/linux/man/1-compress/">compress</a>(1) do. </p>
<h2>AUTHORS</h2>
<p> This program is written by Martin Hinner, &lt;mhi [at] penguin.cz&gt;<br />
 Algorithm &amp; data structures by M. Winterhoff &lt;100326.2776 [at] compuserve.com&gt; </p>
<h2>DOWNLOAD</h2>
<p> mscompress package is available at <a href="ftp://ftp.penguin.cz">ftp.penguin.cz</a>/pub/users/mhi/. </p>
<h2>Index</h2>
