---
title: "ppmtoapplevol(1)"
name: "ppmtoapplevol"
section: "1"
letter: "p"
url: "/docs/linux/man/1-ppmtoapplevol/"
description: "ppmtoapplevol – convert a PPM into an Apple volume label image"
---

<h2 class="name">NAME</h2>
<p> ppmtoapplevol &#8211; convert a PPM into an Apple volume label image</p>
<h2>SYNOPSIS</h2>
<p> <code>ppmtoapplevol</code> </p>
<p> [<i>ppmfile</i>] </p>
<h2>DESCRIPTION</h2>
<p> This program is part of <code><a href="/docs/linux/man/1-netpbm/">Netpbm</a></code>(1) </p>
<p> <code>ppmtoapplevol</code> reads a PPM image as input and produces an Apple volume label image as output. </p>
<p> EFI-based Apple systems use a simple image format to provide textual labels for devices. This program generates that format. </p>
<p> The input image must be exactly 12 rows tall. Use <code>pamfile</code> to see how tall your image is and <code>pamscale</code> or <code>pamcut</code> to make it 12 rows if it isn&#8217;t. </p>
<p> Netpbm does not have a converter for the other direction. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pamfile/">pamfile</a></code>(1) </p>
<p> <code><a href="/docs/linux/man/1-pamcut/">pamcut</a></code>(1) </p>
<p> <code><a href="/docs/linux/man/1-ppm/">ppm</a></code>(1) </p>
<h2>HISTORY</h2>
<p> <code>ppmtoapplevol</code> was new in Neptbm 10.54 (March 2011). </p>
<h2>Index</h2>
