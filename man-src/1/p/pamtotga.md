---
title: "pamtotga(1)"
name: "pamtotga"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pamtotga/"
description: "pamtotga – convert a Netpbm image to a TrueVision Targa file"
---

<h2 class="name">NAME</h2>
<p> pamtotga &#8211; convert a Netpbm image to a TrueVision Targa file</p>
<h2>SYNOPSIS</h2>
<p> <code>pamtotga</code> [<code>-mono|-cmap|-rgb</code>] [<code>-norle</code>] [<code>-name=</code><i>name</i> [<i>pamfile</i>] </p>
<p> All options can be abbreviated to their shortest unique prefix. You may use two hyphens instead of one to designate an option. You may use either white space or equals signs between an option name and its value. </p>
<h2>DESCRIPTION</h2>
<p> This program is part of <code><a href="/docs/linux/man/1-netpbm/">Netpbm</a></code>(1) </p>
<p> <code>pamtotga</code> reads a PBM, PGM, PPM, or PAM image as input and produces a TrueVision Targa file as output. The PAM image may be either a BLACKANDWHITE, GRAYSCALE, RGB, or RGB_ALPHA image. </p>
<p> To create a TGA image with transparency (i.e. with an alpha mask), use RGB_ALPHA PAM input. Some Netpbm programs that generate images with alpha masks generate them in that format. For another way to create the proper input stream, see <code><a href="/docs/linux/man/1-pamstack/">pamstack</a></code>(1) </p>
<p> It is unclear that anything except <code>pamtotga</code> knows about TGAs with transparency. The history behind this feature of <code>pamtotga</code> is not clear. The format <code>pamtotga</code> produces is simply the same as an ordinary RGB TGA image except with a 4th plane added for transparency. The PixelSize field of the TGA header specifies 32 bits instead of 24 and the raster has an extra byte added to each pixel, at the tail end. The value of that byte has the same meaning as in a PAM image with maxval 255. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-cmap</code></p>
<dd> Make output Targa file of type 24 bit colormapped. Input must contain no more than 256 distinct colors. </p>
<dt><code>-mono</code></p>
<dd> Make output Targa file of type 8 bit monochrome. Input must be PBM or PGM or a PAM with BLACKANDWHITE or GRAYSCALE tuple type. See <code>-cmap</code>. </p>
<p> You may specify at most one of <code>-mono</code>, <code>-cmap</code>, and <code>-rgb</code>. If you specify neither, the default image type is the most highly constrained compatible type is used, where monochrome is more constrained than colormapped which is in turn more constrained than unmapped. </p>
<dt><code>-rgb</code></p>
<dd> Make output Targa file of type 24 bit unmapped color. See <code>-cmap</code>. </p>
<dt><code>-norle</code></p>
<dd> Do not use run-length encoding in the output Targa file. Run-length encoded files are smaller, but Some Targa readers can&#8217;t read run-length encoded files. </p>
<dt><code>-name=</code><i>name</i></p>
<dd> This is the value for the image ID stated in the header of the TGA output file. <code>pamtotga</code> truncates it as necessary to meet TGA standards. </p>
<p> By default, <code>pamtotga</code> uses the input file name argument, up to the first period (or the whole thing if there is no period). It truncates it as necessary to meet TGA standards. If you specify (or default to) Standard Input, <code>pamtotga</code> omits the image ID from the TGA header. </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-tgatoppm/">tgatoppm</a></code>(1) , <code><a href="/docs/linux/man/1-pnmquant/">pnmquant</a></code>(1) , <code><a href="/docs/linux/man/1-pamstack/">pamstack</a></code>(1) , <code><a href="/docs/linux/man/1-pam/">pam</a></code>(1) </p>
<p> <code><a href="/docs/linux/man/1-pnm/">pnm</a></code>(1) </p>
<h2>HISTORY</h2>
<p> This program was called <code>ppmtotga</code> until Netpbm 10.6 (July 2002). That was always a misnomer, though, because a PPM class program would not be able to tell the difference between PGM and PPM input (it would all look like PPM), and thus could not choose the output Targa image type based on the type of the input. Netpbm 10.6 also added the ability to handle an alpha channel, so it became a PAM class program. </p>
<p> In Netpbm 10.15 (April 2003), the program became the first in the Netpbm package to recognize an alpha channel in a PAM. It recognized tuple type &#8216;RGBA&#8217;. But when this kind of PAM image was later added to the PAM specification, it was specified with tuple type &#8216;RGB_ALPHA&#8217;. So in Netpbm 10-26 (January 2005), <code>pamtotga</code> changed to recognize &#8216;RGB_ALPHA&#8217; instead of &#8216;RGBA&#8217;. </p>
<h2>AUTHOR</h2>
<p> Copyright (C) 1989, 1991 by Mark Shand and Jef Poskanzer. </p>
<h2>Index</h2>
