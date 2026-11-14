---
title: "tiffcmp(1)"
name: "tiffcmp"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tiffcmp/"
description: "tiffcmp – compare two TIFF files"
---

<h2>NAME</h2>
<p> tiffcmp &#8211; compare two <font SIZE="-1">TIFF</font> files</p>
<h2>SYNOPSIS</h2>
<p> <code>tiffcmp</code> [ <i>options</i> ] <i>file1.tif file2.tif</i></p>
<h2>DESCRIPTION</h2>
<p> <i>Tiffcmp</i> compares the tags and data in two files created according to the Tagged Image File Format, Revision 6.0. The schemes used for compressing data in each file are immaterial when data are compared-data are compared on a scanline-by-scanline basis after decompression. Most directory tags are checked; notable exceptions are: <i>GrayResponseCurve</i>, <i>ColorResponseCurve</i>, and <i>ColorMap</i> tags. Data will not be compared if any of the <i>BitsPerSample</i>, <i>SamplesPerPixel</i>, or <i>ImageWidth</i> values are not equal. By default, <i>tiffcmp</i> will terminate if it encounters any difference.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-l</code></p>
<dd> List each byte of image data that differs between the files.</p>
<dt><code>-z</code><i> number</i></p>
<dd> List specified number of image data bytes that differs between the files.</p>
<dt><code>-t</code></p>
<dd> Ignore any differences in directory tags.</dl>
<h2>BUGS</h2>
<p> Tags that are not recognized by the library are not compared; they may also generate spurious diagnostics. </p>
<p> The image data of tiled files is not compared, since the <i>TIFFReadScanline()</i> function is used. An error will be reported for tiled files. </p>
<p> The pixel and/or sample number reported in differences may be off in some exotic cases.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pal2rgb/">pal2rgb</a></code>(1), <code><a href="/docs/linux/man/1-tiffinfo/">tiffinfo</a></code>(1), <code><a href="/docs/linux/man/1-tiffcp/">tiffcp</a></code>(1), <code><a href="/docs/linux/man/1-tiffmedian/">tiffmedian</a></code>(1), <code><a href="//www.systutorials.com/docs/linux/man/3TIFF-libtiff/">libtiff</a></code>(3TIFF) </p>
<p> Libtiff library home page: <code><a rel="nofollow" href="http://www.remotesensing.org/libtiff/">http://www.remotesensing.org/libtiff/</a></code> </p>
<h2>Index</h2>
