---
title: "ppmtospu(1)"
name: "ppmtospu"
section: "1"
letter: "p"
url: "/docs/linux/man/1-ppmtospu/"
description: "ppmtospu – convert a PPM image to an Atari Spectrum 512 image"
---

<h2 class="name">NAME</h2>
<p> ppmtospu &#8211; convert a PPM image to an Atari Spectrum 512 image</p>
<h2>SYNOPSIS</h2>
<p> <code>ppmtospu</code> </p>
<p> [<code>-d0</code>|<code>-d2</code>|<code>-d4</code>] [<i>ppmfile</i>] </p>
<p> All options can be abbreviated to their shortest unique prefix. You may use two hyphens instead of one. You may separate an option name and its value with white space instead of an equals sign. </p>
<h2>DESCRIPTION</h2>
<p> This program is part of <code><a href="/docs/linux/man/1-netpbm/">Netpbm</a></code>(1) </p>
<p> This program converts from the PPM format to the uncompressed Spectrum 512 image format used on Atari ST computers. </p>
<p> Input comes from the file you name with the <i>ppmfile</i> argument, or Standard Input by default. Output goes to Standard Output. </p>
<p> The input must be 320 pixels wide by 200 pixels high. If you have an image of a different size, you can use <code>pamcut</code> or <code>pamscale</code> to force it to these dimensions. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-d0</code></p>
<dd> The program does no dithering. </p>
<dt><code>-d2</code></p>
<dd> The program uses a 2&#215;2 ordered dither. </p>
<p> This is the default. </p>
<dt><code>-d4</code></p>
<dd> The program uses a 4&#215;4 ordered dither.<br />
&nbsp;<wbr> </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-sputoppm/">sputoppm</a></code>(1) , <code><a href="/docs/linux/man/1-sputoppm/">sputoppm</a></code>(1) , <code><a href="/docs/linux/man/1-pamscale/">pamscale</a></code>(1) , <code><a href="/docs/linux/man/1-pamcut/">pamcut</a></code>(1) , <code><a href="/docs/linux/man/1-ppm/">ppm</a></code>(1) </p>
<h2>AUTHOR</h2>
<p> Copyright (C) 1990 by Steve Belczyk </p>
<h2>HISTORY</h2>
<p> This program was new in Netpbm 10.58 (March 2012). </p>
<p> But it was written in 1990. Steve Belczyk posted it along with <code>sputoppm</code>, <code>spctoppm</code>, <code>pi1toppm</code>, and <code>pi1toppm</code> &#8211; all programs for dealing with Atari image formats &#8211; to comp.sources.misc on July 15, 1990. For reasons that have been lost to history, all of these entered the Netpbm (then Pbmplus) distribution <i>except</i> <code>ppmtospu</code>. </p>
<p> Georges Kesseler wondered In March 2012 why there was no counterpart to <code>sputoppm</code> in Netpbm and searched the web, finding only one reference to <code>ppmtopsu</code>: the 1990 comp.sources.misc posting, including the source code. He emailed the Netpbm maintainer suggesting it be added. </p>
<p> Bryan Henderson found the source code to be extremely primitive, not even using common library code. So Bryan completely recoded it, but retained nearly all of the original logic. </p>
<h2>Index</h2>
