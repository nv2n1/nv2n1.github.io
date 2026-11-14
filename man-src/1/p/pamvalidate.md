---
title: "pamvalidate(1)"
name: "pamvalidate"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pamvalidate/"
description: "pamvalidate – validate Netpbm image format"
---

<h2 class="name">NAME</h2>
<p> pamvalidate &#8211; validate Netpbm image format</p>
<h2>SYNOPSIS</h2>
<p> <code>pamvalidate</code> </p>
<h2>DESCRIPTION</h2>
<p> This program is part of <code><a href="/docs/linux/man/1-netpbm/">Netpbm</a></code>(1) </p>
<p> <code>pamvalidate</code> copies a Netpbm image from Standard Input to Standard Output, except that if there are certain violations of the image format in the input, <code>pamvalidate</code> fails <i>without producing any output</i>. </p>
<p> This is most useful in a pipeline, before a stage you don&#8217;t want to start working on Netpbm input until it knows it can get all the way through it. For example, assume you are converting PPM images to PNG and you don&#8217;t want to produce a partial PNG file under any circumstance. If you just use <code>pnmtopng</code>, and the PPM input is truncated halfway through the raster, <code>pnmtopng</code> fails, but also produces about half of a PNG file. To prevent that, pass your PPM input through <code>pamvalidate</code> on its way to <code>pnmtopng</code>. Then, <code>pamvalidate</code> will fail, and consequently the pipeline will fail, before <code>pnmtopng</code> has seen any input and therefore before <code>pnmtopng</code> has produced any output. </p>
<p> These are the kinds of format violations <code>pamvalidate</code> detects: </p>
<dl>
<dt>&bull;</p>
<dd> A purported sample value exceeds the declared maxval.</p>
<dt>&bull;</p>
<dd> The stream ends prematurely. </p>
</dl>
<p> This program works on multi-image streams, producing a corresponding output stream. </p>
<p> See <code>pamfix</code> for a way to salvage an invalid Netpbm image stream. </p>
<h2>OPTIONS</h2>
<p> None. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pam/">pam</a></code>(1) </p>
<p> <code><a href="/docs/linux/man/1-pnm/">pnm</a></code>(1) </p>
<p> <code><a href="/docs/linux/man/1-pamfix/">pamfix</a></code>(1) </p>
<h2>HISTORY</h2>
<p> <code>pamvalidate</code> was new in Netpbm 10.66 (March 2014). </p>
<h2>Index</h2>
