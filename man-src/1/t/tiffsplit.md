---
title: "tiffsplit(1)"
name: "tiffsplit"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tiffsplit/"
description: "tiffsplit – split a multi-image TIFF into single-image TIFF files"
---

<h2>NAME</h2>
<p> tiffsplit &#8211; split a multi-image <font SIZE="-1">TIFF</font> into single-image <font SIZE="-1">TIFF</font> files</p>
<h2>SYNOPSIS</h2>
<p> <code>tiffsplit</code> <i>src.tif</i> [ <i>prefix</i> ]</p>
<h2>DESCRIPTION</h2>
<p> <i>tiffsplit</i> takes a multi-directory (page) <font SIZE="-1">TIFF</font> file and creates one or more single-directory (page) <font SIZE="-1">TIFF</font> files from it. The output files are given names created by concatenating a prefix, a lexically ordered suffix in the range [<i>aaa</i>&#8211;<i>zzz</i>], the suffix <i>.tif </i> (e.g. <i>xaaa.tif</i>, <i>xaab.tif</i>, <i>&#8230;</i>, <i>xzzz.tif</i>). If a prefix is not specified on the command line, the default prefix of <i>x</i> is used.</p>
<h2>OPTIONS</h2>
<p> None.</p>
<h2>BUGS</h2>
<p> Only a select set of &#8220;known tags&#8221; is copied when splitting.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-tiffcp/">tiffcp</a></code>(1), <code><a href="/docs/linux/man/1-tiffinfo/">tiffinfo</a></code>(1), <code><a href="//www.systutorials.com/docs/linux/man/3TIFF-libtiff/">libtiff</a></code>(3TIFF) </p>
<p> Libtiff library home page: <code><a rel="nofollow" href="http://www.remotesensing.org/libtiff/">http://www.remotesensing.org/libtiff/</a></code> </p>
<h2>Index</h2>
