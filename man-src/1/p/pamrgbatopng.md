---
title: "pamrgbatopng(1)"
name: "pamrgbatopng"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pamrgbatopng/"
description: "pamrgbatopng – convert PAM color/transparency image to PNG"
---

<h2 class="name">NAME</h2>
<p> pamrgbatopng &#8211; convert PAM color/transparency image to PNG</p>
<h2>SYNOPSIS</h2>
<p> <code>pamrgbatopng</code> [<i>pamfile</i>] </p>
<p> Minimum unique abbreviation of option is acceptable. You may use double hyphens instead of single hyphen to denote options. You may use white space in place of the equals sign to separate an option name from its value. </p>
<h2>DESCRIPTION</h2>
<p> This program is part of <code><a href="/docs/linux/man/1-netpbm/">Netpbm</a></code>(1) </p>
<p> <code>pamrgbatopng</code> reads a PAM image with the RGB_ALPHA tuple type (a color visual image with transparency) and produces an equivalent PNG image as output. </p>
<p> The input image if from the file named by the <i>pamfile</i> argument, or Standard Input if you don&#8217;t specify <i>pamfile</i>. The output goes to Standard Output. </p>
<p> The maxval of the input image must be 255. You can use <code>pamdepth</code> to change the maxval of an image to 255 if necessary. </p>
<p> <code><a href="/docs/linux/man/1-pnmtopng/">pnmtopng</a></code>(1)<br />
&nbsp;<wbr>is a much more powerful program for generating PNG images from Netpbm images, but it cannot take PAM images with transparency as input. To supply transparency information, you must supply it in a separate PGM image. That makes it considerably less convenient to use. </p>
<p> (But note that <code>pnmtopng</code> takes PAM images, even with RGB_ALPHA tuple type just fine &#8212; it just ignores the alpha plane). </p>
<p> Netpbm&#8217;s strategic direction is to add to <code>pnmtopng</code> all the capabilities of <code>pamrgbatopng</code> and retire <code>pamrgbatopng</code>. But there&#8217;s no telling when that will happen. </p>
<h2>OPTIONS</h2>
<p> None. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pam/">pam</a></code>(1) </p>
<p> <code><a href="/docs/linux/man/1-pnmtopng/">pnmtopng</a></code>(1) </p>
<p> <code><a href="/docs/linux/man/1-pngtopam/">pngtopam</a></code>(1) </p>
<h2>HISTORY</h2>
<p> <code>pamrgbatopng</code> was new in Netpbm 10.30 (October 2005). </p>
<h2>Index</h2>
