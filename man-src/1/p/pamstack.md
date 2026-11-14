---
title: "pamstack(1)"
name: "pamstack"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pamstack/"
description: "pamstack – stack planes of multiple PAM images into one PAM image"
---

<h2 class="name">NAME</h2>
<p> pamstack &#8211; stack planes of multiple PAM images into one PAM image </p>
<h2>SYNOPSIS</h2>
<p> <code>pamstack</code> [<code>-tupletype </code><i>tupletype</i>] [<i>inputfilespec</i>] </p>
<p> All options may be abbreviated to the shortest unique prefix. </p>
<h2>DESCRIPTION</h2>
<p> Reads multiple PAM or PNM images as input. Produces a PAM image as output, consisting of all the planes (channels) of the inputs, stacked in the order specified. </p>
<p> The output is the same dimensions as the inputs, except that the depth is the sum of the depths of the inputs. It has the same maxval. <code>pamstack</code> fails if the inputs are not all the same width, height, and maxval. The tuple type is a null string unless you specify the <code>-tupletype</code> option. </p>
<p> <code>pamchannel</code> does the opposite of <code>pamstack:</code> It extracts individual planes from a single PAM. </p>
<p> Use <code>pamtopnm</code> to convert a suitable PAM image to a more traditional PNM (PBM, PGM, or PPM) image. </p>
<p> One example of using <code>pamstack</code> is that some Netpbm programs accept as input a PAM that represents graphic image with transparency information &#8212; tuple type &quot;RGBA&quot;. In Netpbm, such images were traditionally represented as two images &#8211; a PPM for the color and a PGM for the transparency. To convert a PPM/PGM pair into PAM(RGBA) input that newer programs require, do something like this: </p>
<p> pamstack -tupletype=RGBA myimage.ppm myalpha.pgm | pamtouil &gt;myimage.uil </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-tupletype </code><i>tupletype</i></p>
<dd> This specified the tuple type name to be recorded in the output. You may use any string up to 255 characters. Some programs recognize some names. If you omit this option, the default tuple type name is null. </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/5-pam/">pam</a></code>(5) </p>
<h2>AUTHOR</h2>
<p> Copyright (C) by Bryan Henderson, San Jose CA 2000.08.05 </p>
<h2>Index</h2>
