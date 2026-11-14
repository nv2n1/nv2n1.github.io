---
title: "sgitopnm(1)"
name: "sgitopnm"
section: "1"
letter: "s"
url: "/docs/linux/man/1-sgitopnm/"
description: "sgitopnm – convert a SGI image file to a portable anymap"
---

<h2 class="name">NAME</h2>
<p> sgitopnm &#8211; convert a SGI image file to a portable anymap </p>
<h2>SYNOPSIS</h2>
<p> <code>sgitopnm</code> [<code>-verbose</code>] [<code>-channel</code> <i>c</i>] [<i>SGIfile</i>]</p>
<h2>DESCRIPTION</h2>
<p> Reads an SGI image file as input. Produces a PGM image for a 2-dimensional (1 channel) input file, and a PPM image for a 3-dimensional (3 or more channels) input file. </p>
<p> Alternatively, produces a PGM image of any one of the channels in the input file. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-verbose</code></p>
<dd> Give some information about the SGI image file.</p>
<dt><code>-channel</code><i> c</i></p>
<dd> Extract channel <i>c</i> of the image as a PGM image. Without this option, <code>sgitopnm</code> extracts the first 3 channels as a PPM image or, if the input has only 1 channel, extracts that as a PGM image, and if the input has 2 channels, fails. </p>
</dl>
<h2>REFERENCES</h2>
<p> SGI Image File Format documentation (draft v0.95) by Paul Haeberli (paul [at] sgi.com). Available via ftp at sgi.com:graphics/SGIIMAGESPEC. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/5-pnm/">pnm</a></code>(5), <code><a href="/docs/linux/man/1-pnmtosgi/">pnmtosgi</a></code>(1) </p>
<h2>AUTHOR</h2>
<p> Copyright (C) 1994 by Ingo Wilken (Ingo.Wilken [at] informatik.uni-oldenburg.de) </p>
<h2>Index</h2>
