---
title: "pambackground(1)"
name: "pambackground"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pambackground/"
description: "pambackground – create a mask of the background area of an image"
---

<h2 class="name">NAME</h2>
<p> pambackground &#8211; create a mask of the background area of an image</p>
<h2>SYNOPSIS</h2>
<p> <code>pambackground</code> </p>
<p> [<i>netpbmfile</i>] </p>
<p> [<code>-verbose=</code>] </p>
<p> Minimum unique abbreviations of options are acceptable. You may use double hyphens instead of single hyphen to denote options. You may use white space in place of the equals sign to separate an option name from its value. </p>
<h2>DESCRIPTION</h2>
<p> This program is part of <code><a href="/docs/linux/man/1-netpbm/">Netpbm</a></code>(1) </p>
<p> <code>pambackground</code> reads a PNM or PAM image as input. It generates as output a PAM image that identifies the background area of the image (a mask). </p>
<p> To identify the background, <code>pambackground</code> assumes the image is a foreground image, smaller than the total image size, placed over a single-color background. It assumes that foreground image is solid &#8212; it does not have holes through which the background can be seen. So in specific, <code>pambackground</code> first identifies the background color, then finds all contiguous pixels of that color in regions touching any edge of the image. Think of it as starting at each of the four edges and moving inward as far as possible until it hits pixels of another color (the foreground image). </p>
<p> <code>pambackground</code> identifies the background color as follows: If any 3 corners of the image are the same color, that&#8217;s the background color. If not, but 2 corners are the same color, the background color is the color of a pair of identically colored corners in this priority order: top, right, left, bottom. If no two corners have the same color, the background color is the color of the upper left corner. </p>
<p> In a typical photograph, the area that you would consider the background is many shades of a color, so to <code>pambackground</code> it is multiple colors and <code>pambackground</code> will not meaningfully identify the background of your image. To use <code>pambackground</code> in this case, you might use <code>ppmchange</code> to change all similar colors to a single one first. For example, if the photograph is a building against a blue sky, where nothing remotely sky-blue appears in the building, you could use <code>ppmchange</code> to change all pixels within 20% of &#8216;SkyBlue&#8217; to SkyBlue, then run <code>pambackground</code> on it. </p>
<p> In Release 10.37, <code>pambackground</code> does not really do what is promised above. It can&#8217;t see places where the background appears in the middle of a row (think of the sky between two buildings). From Release 10.38 forward, it snakes through whatever passages it has to to find all the background. </p>
<p> The PAM that <code>pambackground</code> creates has a single plane, with a maxval of 1. The sample value 1 means background; 0 means foreground. There is no tuple type. Some older programs (but none that are part of Netpbm) don&#8217;t know what a PAM is and expect a mask to be in the form of a PGM or PBM image. To convert <code>pambackground</code>&#8216;s output to PBM, use <code>pamtopnm -assume</code>. To convert to PGM, use <code>pgmtopgm</code>. </p>
<p> <i>netpbmfile</i> is the file specification of the input file, or <code>&#8211;</code> to indicate Standard Input. The default is Standard Input. </p>
<p> A common use for a background mask is with <code>pamcomp</code>. You could replace the entire background (or foreground) of your image with something else. </p>
<p> Another common use is to make an image with the background transparent (in some image format that has a concept of transparency; not Netpbm formats) so that image can be overlaid onto another image later. Netpbm&#8217;s converters to image formats that have transparency (e.g. PNG) let you use the mask that <code>pambackground</code> generates to identify the transparent areas for the output. </p>
<p> To simply make a mask of all the areas of a specified color, use <code>ppmcolormask</code>. If you have a unique background color (one that doesn&#8217;t occur in the foreground) and know what it is, this can create a background mask in cases that <code>pambackground</code> cannot: where there are see-through holes in the foreground image. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-verbose</code></p>
<dd> Tell interesting facts about the process. </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-ppmcolormask/">ppmcolormask</a></code>(1) , <code><a href="/docs/linux/man/1-pamcomp/">pamcomp</a></code>(1) , <code><a href="/docs/linux/man/1-pamtopnm/">pamtopnm</a></code>(1) , <code><a href="/docs/linux/man/1-pgmtopgm/">pgmtopgm</a></code>(1) , <code><a href="/docs/linux/man/1-pnm/">pnm</a></code>(1) , <code><a href="/docs/linux/man/1-pam/">pam</a></code>(1) , </p>
<h2>HISTORY</h2>
<p> <code>pambackground</code> was new in Netpbm 10.37 (December 2006). </p>
<h2>Index</h2>
