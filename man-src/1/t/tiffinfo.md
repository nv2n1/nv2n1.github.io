---
title: "tiffinfo(1)"
name: "tiffinfo"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tiffinfo/"
description: "tiffinfo – print information about TIFF files"
---

<h2>NAME</h2>
<p> tiffinfo &#8211; print information about <font SIZE="-1">TIFF</font> files</p>
<h2>SYNOPSIS</h2>
<p> <code>tiffinfo</code> [ <i>options</i> ] <i>input.tif &#8230;</i></p>
<h2>DESCRIPTION</h2>
<p> <i>Tiffinfo</i> displays information about files created according to the Tag Image File Format, Revision 6.0. By default, the contents of each <font SIZE="-1">TIFF</font> directory in each file is displayed, with the value of each tag shown symbolically (where sensible).</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-c</code></p>
<dd> Display the colormap and color/gray response curves, if present.</p>
<dt><code>-D</code></p>
<dd> In addition to displaying the directory tags, read and decompress all the data in each image (but not display it).</p>
<dt><code>-d</code></p>
<dd> In addition to displaying the directory tags, print each byte of decompressed data in hexadecimal.</p>
<dt><code>-j</code></p>
<dd> Display any <font SIZE="-2">JPEG</font>-related tags that are present.</p>
<dt><code>-o</code></p>
<dd> Set the initial <font SIZE="-1">TIFF</font> directory according to the specified file offset. The file offset may be specified using the usual C-style syntax; i.e. a leading &#8220;0x&#8221; for hexadecimal and a leading &#8220;0&#8221; for octal.</p>
<dt><code>-s</code></p>
<dd> Display the offsets and byte counts for each data strip in a directory.</p>
<dt><code>-z</code></p>
<dd> Enable strip chopping when reading image data.</p>
<dt><code>-#</code></p>
<dd> Set the initial <font SIZE="-1">TIFF</font> directory to <i>#</i>.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pal2rgb/">pal2rgb</a></code>(1), <code><a href="/docs/linux/man/1-tiffcp/">tiffcp</a></code>(1), <code><a href="/docs/linux/man/1-tiffcmp/">tiffcmp</a></code>(1), <code><a href="/docs/linux/man/1-tiffmedian/">tiffmedian</a></code>(1), <code><a href="//www.systutorials.com/docs/linux/man/3TIFF-libtiff/">libtiff</a></code>(3TIFF) </p>
<p> Libtiff library home page: <code><a rel="nofollow" href="http://www.remotesensing.org/libtiff/">http://www.remotesensing.org/libtiff/</a></code> </p>
<h2>Index</h2>
