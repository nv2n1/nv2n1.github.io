---
title: "pnmquant(1)"
name: "pnmquant"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pnmquant/"
description: "pnmquant – quantize the colors in a Netpbm image to a smaller set"
---

<h2 class="name">NAME</h2>
<p> pnmquant &#8211; quantize the colors in a Netpbm image to a smaller set</p>
<h2>SYNOPSIS</h2>
<p> <code>pnmquant</code> [<code>-center</code>|<code>-meancolor</code>|<code>-meanpixel</code>] [<code>-floyd</code>|<code>-fs</code>] [<code>-nofloyd</code>|<code>-nofs</code>] [<code>-spreadbrightness</code>|<code>-spreadluminosity</code>] <i>ncolors</i> [<i>pnmfile</i>] </p>
<p> All options can be abbreviated to their shortest unique prefix. You may use two hyphens instead of one to designate an option. You may use either white space or equals signs between an option name and its value. </p>
<h2>DESCRIPTION</h2>
<p> Reads a PNM image as input. Chooses <i>ncolors</i> colors to best represent the image, maps the existing colors to the new ones, and writes a PNM image as output. </p>
<p> This program is simply a combination of <code>pnmcolormap</code> and <code>pnmremap</code>, where the colors of the input are remapped using a color map which is generated from the colors in that same input. The options have the same meaning as in those programs. See their documentation to understand <code>pnmquant</code>. </p>
<p> It is much faster to call <code>pnmcolormap</code> and <code>pnmremap</code> directly than to run <code>pnmquant</code>. <code>pnmquant</code> is just a convenience. </p>
<p> <code>ppmquant</code> is an older program which does the same thing as <code>pnmquant</code>, but on only PPM images. It is, however, faster than either <code>pnmquant</code> or <code>ppmcolormap</code>/<code>pnmremap</code>. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pnmcolormap/">pnmcolormap</a></code>(1), <code><a href="/docs/linux/man/1-pnmremap/">pnmremap</a></code>(1), <code><a href="/docs/linux/man/1-ppmquantall/">ppmquantall</a></code>(1), <code><a href="/docs/linux/man/1-pnmdepth/">pnmdepth</a></code>(1), <code><a href="/docs/linux/man/1-ppmdither/">ppmdither</a></code>(1), <code><a href="/docs/linux/man/1-ppmquant/">ppmquant</a></code>(1), <code><a href="/docs/linux/man/5-pnm/">pnm</a></code>(5) </p>
<h2>AUTHOR</h2>
<p> Written by Bryan Henderson </p>
<h2>Index</h2>
