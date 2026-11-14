---
title: "metapixel(1)"
name: "metapixel"
section: "1"
letter: "m"
url: "/docs/linux/man/1-metapixel/"
description: "metapixel – generator for photomosaics"
---

<h2>NAME</h2>
<p> metapixel &#8211; generator for photomosaics</p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>metapixel-prepare</code> [<i>options</i>] [<i>srcdir</i>] [<i>destdir</i>] </p>
<dd>prepares the pictures in <i>srcdir</i> by creating resized images and a table file in <i>destdir</i> </p>
<dt> <code>metapixel</code> [<i>options</i>] [&#8211;metapixel&nbsp;<wbr><i>input.jpg</i>&nbsp;<wbr><i>output.png</i>&nbsp;<wbr>&#8211;library&nbsp;<wbr><i>destdir</i>] </p>
<dd>creates a photomosaic <i>output.png</i> using <i>input.jpg</i> as the input image and <i>destdir/tables.mxt</i> as table file </p>
</dl>
<h2>DESCRIPTION</h2>
<p> This manual page documents briefly the <code>metapixel</code> and <code>metapixel-prepare</code> commands. For more information check the README file included in the distribution. </p>
<p> <code>metapixel</code> is a program for generating photomosaics. It can generate classical photomosaics, in which the source image is viewed as a matrix of equally sized rectangles for each of which a matching image is substitued, as well as collage-style photomosaics, in which rectangular parts of the source image at arbitrary positions (i.e. not aligned to a matrix) are substituted by matching images. </p>
<p> <code>metapixel-prepare</code> is a utility that needs to be run before metapixel can be used. It prepares your source images so that they can be used by <code>metapixel</code> to create the actual photomosaic. </p>
<h2>USAGE</h2>
<p> <code>metapixel-prepare </code><i>srcdir</i> <i>destdir</i> has to be run first. <i>srcdir</i> is the path to the directory containing the source images, e.g. <i>~/Pictures/Holidays</i>. <i>destdir</i>, e.g. <i>~/.metapixel</i>, is the path to the directory where you want to store the rescaled images and the <i>tables.mxt</i> index file. This directory should be created manually before running <code>metapixel-prepare</code>. </p>
<p> <code>metapixel &#8211;metapixel </code><i>input.jpg</i> <i>output.png</i> &#8211;library <i>destdir</i> is then used to transform an image (<i>input.jpg</i>) into a mosaic (<i>output.png</i>) using the source images (described by <i>destdir/tables.mxt</i>). </p>
<h2>OPTIONS</h2>
<p> The options are described in the README file or by running <code>metapixel</code> or <code>metapixel-prepare</code> with the &#8211;help option. </p>
<h2>SEE ALSO</h2>
<p> The README file is included in the Metapixel distribution. </p>
<h2>AUTHOR</h2>
<p> This manual page was written by Chris Vanden Berghe &lt;Chris [at] VandenBerghe.org&gt; for the Debian system (but may be used by others). Permission is granted to copy, distribute and/or modify this document under the terms of the GNU General Public License, Version 2 any later version published by the Free Software Foundation. </p>
<p> On Debian systems, the complete text of the GNU General Public License can be found in /usr/share/common-licenses/GPL. </p>
<h2>AUTHOR</h2>
<p> Chris Vanden Berghe. </p>
<h2>Index</h2>
