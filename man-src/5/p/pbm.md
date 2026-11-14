---
title: "pbm(5)"
name: "pbm"
section: "5"
letter: "p"
url: "/docs/linux/man/5-pbm/"
description: "pbm – portable bitmap file format"
---

<p>pbm &#8211; portable bitmap file format</p>
<h2>Description</h2>
<p>The portable bitmap format is a lowest common denominator monochrome file format. It serves as the common language of a large family of bitmap conversion filters. Because the format pays no heed to efficiency, it is simple and general enough that one can easily develop programs to convert to and from just about any other graphics format, or to manipulate the image. This is not a format that one would normally use to store a file or to transmit it to someone &#8212; it&#8217;s too expensive and not expressive enough for that. It&#8217;s just an intermediary format. In it&#8217;s purest use, it lives only in a pipe between two other programs. The format definition is as follows. A PBM file consists of a sequence of one or more PBM images. There are no data, delimiters, or padding before, after, or between images. Each PBM image consists of the following:</p>
<dl>
<dt>&#8211;</p>
<dd>A &quot;magic number&quot; for identifying the file type. A pbm image&#8217;s magic number is the two characters &quot;P4&quot;.</p>
<dt>&#8211;</p>
<dd>Whitespace (blanks, TABs, CRs, LFs).</p>
<dt>&#8211;</p>
<dd>The width in pixels of the image, formatted as ASCII characters in decimal.</p>
<dt>&#8211;</p>
<dd>Whitespace.</p>
<dt>&#8211;</p>
<dd>The height in pixels of the image, again in ASCII decimal.</p>
<dt>&#8211;</p>
<dd>Newline or other single whitespace character.</p>
<dt>&#8211;</p>
<dd>A raster of Height rows, in order from top to bottom. Each row is Width bits, packed 8 to a byte, with don&#8217;t care bits to fill out the last byte in the row. Each bit represents a pixel: 1 is black, 0 is white. The order of the pixels is left to right. The order of their storage within each file byte is most significant bit to least significant bit. The order of the file bytes is from the beginning of the file toward the end of the file.</p>
<dt>&#8211;</p>
<dd>Characters from a &quot;#&quot; to the next end-of-line, before the width/height line, are comments and are ignored.</dl>
<p> There is actually another version of the PBM format, even more more simplistic, more lavishly wasteful of space than PBM, called Plain PBM. Plain PBM actually came first, but even its inventor couldn&#8217;t stand its recklessly squanderous use of resources after a while and switched to what we now know as the regular PBM format. But Plain PBM is so redundant &#8212; so overstated &#8212; that it&#8217;s virtually impossible to break. You can send it through the most liberal mail system (which was the original purpose of the PBM format) and it will arrive still readable. You can flip a dozen random bits and easily piece back together the original image. And we hardly need to define the format here, because you can decode it by inspection. The difference is:</p>
<dl>
<dt>&#8211;</p>
<dd>There is exactly one image in a file.</p>
<dt>&#8211;</p>
<dd>The &quot;magic number&quot; is &quot;P1&quot; instead of &quot;P4&quot;.</p>
<dt>&#8211;</p>
<dd>Each pixel in the raster is represented by a byte containing ASCII &#8216;1&#8217; or &#8216;0&#8217;, representing black and white respectively. There are no fill bits at the end of a row.</p>
<dt>&#8211;</p>
<dd>White space in the raster section is ignored.</p>
<dt>&#8211;</p>
<dd>You can put any junk you want after the raster, if it starts with a white space character.</p>
<dt>&#8211;</p>
<dd>No line should be longer than 70 characters.</dl>
<p> Here is an example of a small bitmap in the plain PBM format: </p>
<pre>P1
# feep.pbm
24 7
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 1 1 1 1 0 0 1 1 1 1 0 0 1 1 1 1 0 0 1 1 1 1 0
0 1 0 0 0 0 0 1 0 0 0 0 0 1 0 0 0 0 0 1 0 0 1 0
0 1 1 1 0 0 0 1 1 1 0 0 0 1 1 1 0 0 0 1 1 1 1 0
0 1 0 0 0 0 0 1 0 0 0 0 0 1 0 0 0 0 0 1 0 0 0 0
0 1 0 0 0 0 0 1 1 1 1 0 0 1 1 1 1 0 0 1 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0</pre>
<p>You can generate the Plain PBM format from the regular PBM format (first image in the file only) with the <code>pnmtoplainpnm</code> program. Programs that read this format should be as lenient as possible, accepting anything that looks remotely like a bitmap. </p>
<h2>Compatibility</h2>
<p>Before July 2000, there could be at most one image in a PBM file. As a result, most tools to process PBM files ignore (and don&#8217;t read) any data after the first image.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-libpbm/">libpbm</a></code>(3),<code><a href="/docs/linux/man/5-pnm/">pnm</a></code>(5),<code><a href="/docs/linux/man/5-pgm/">pgm</a></code>(5),<code><a href="/docs/linux/man/5-ppm/">ppm</a></code>(5)</p>
<h2>Author</h2>
<p>Copyright (C) 1989, 1991 by Jef Poskanzer.</p>
