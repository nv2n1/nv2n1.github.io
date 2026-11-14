---
title: "pnmquantall(1)"
name: "pnmquantall"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pnmquantall/"
description: "pnmquantall – run Pnmquant on a bunch of files all at once, so they share a common colormap"
---

<h2 class="name">NAME</h2>
<p> pnmquantall &#8211; run Pnmquant on a bunch of files all at once, so they share a common colormap</p>
<h2>SYNOPSIS</h2>
<p> <code>pnmquantall</code> </p>
<p> [<code>-ext</code> <i>extension</i>] <i>ncolors</i> <i>netpbm_file</i>&#8230; </p>
<p> Note that the usual syntax rules for Netpbm programs <i>don&#8217;t apply</i> to this program. For example, you can&#8217;t abbreviation -ext and you can&#8217;t put it anywhere on the line you want. </p>
<h2>DESCRIPTION</h2>
<p> This program is part of <code><a href="/docs/linux/man/1-netpbm/">Netpbm</a></code>(1) </p>
<p> <code>pnmquantall</code> takes a bunch of Netpbm image files as input, chooses <i>ncolors</i> colors to best represent all of the images, maps the existing colors to the new ones, and <code>overwrites the input files</code> with the new quantized versions. </p>
<p> If you don&#8217;t want to overwrite your input files, use the <code>-ext</code> option. The output files are then named the same as the input files, plus a period and the extension text you specify. </p>
<p> The purpose is this: Let&#8217;s say you&#8217;ve got a dozen PPMs that you want to display on the screen all at the same time. Your screen can only display 256 different colors, but the PPMs have a total of a thousand or so different colors. For a single image you solve this problem with <code>pnmquant</code>; <code>pnmquantall</code> solves it for multiple images. </p>
<p> Note that another approach to this problem is to pre-select a set of colors and then use <code>pnmremap</code> to separately quantize each PPM to that set.) </p>
<p> This is a rather simple program that runs <code>pnmcolormap</code> and <code>pnmremap</code>. If you are considering using it in a program of any sophistication, you should probably just run those programs directly. Even if you are typing it, you may want to do the steps manually because it gives you access to the various options of <code>pnmcolormap</code> and <code>pnmremap</code> for doing the quantization differently. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pnmquant/">pnmquant</a></code>(1) , <code><a href="/docs/linux/man/1-pnmremap/">pnmremap</a></code>(1) , <code><a href="/docs/linux/man/1-pnmcolormap/">pnmcolormap</a></code>(1) , <code><a href="/docs/linux/man/1-pnm/">pnm</a></code>(1) </p>
<h2>Index</h2>
