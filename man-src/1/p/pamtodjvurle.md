---
title: "pamtodjvurle(1)"
name: "pamtodjvurle"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pamtodjvurle/"
description: "pamtodjvurle – convert a Netpbm image to DjVu Color RLE format"
---

<h2 class="name">NAME</h2>
<p> pamtodjvurle &#8211; convert a Netpbm image to DjVu Color RLE format</p>
<h2>SYNOPSIS</h2>
<p> <code>pamtodjvurle</code> </p>
<p> [<code>-transparent</code> <i>color</i>] [<i>netpbmfile</i> [<i>rlefile</i>]] </p>
<p> Minimum unique abbreviation of options in acceptable. </p>
<h2>DESCRIPTION</h2>
<p> This program is part of <code><a href="/docs/linux/man/1-netpbm/">Netpbm</a></code>(1) </p>
<p> <code>pamtodjvurle</code> reads a Netpbm image (PNM or PAM equivalent of PNM) as input and produces DjVu Color RLE format as output. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-transparent</code> <i>colorname</i></p>
<dd> This option indicates which color in the image should be considered transparent. </p>
<p> Specify the color (<i>color</i>) as described for the argument of the <code>ppm_parsecolor()</code> library routine . </p>
<p> Default is &#8216;white&#8217;. </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pbmtodjvurle/">pbmtodjvurle</a></code>(1) </p>
<p> <code><a href="/docs/linux/man/1-pam/">pam</a></code>(1) </p>
<h2>HISTORY</h2>
<p> <code>pamtodjvurle</code> was new in Netpbm 10.22 (April 2004) but a program that did almost the same thing, called <code>ppmtodjvurle</code>, was in Netpbm 10.21 (March 2004). The latter was written and contributed to Netpbm by Scott Pakin &lt;scott+pbm [at] pakin.org&gt;. <code>pamtodjvurle</code> uses techniques taken from <code>ppmtodjvurle</code>, but no code is copied between them. </p>
<h2>Index</h2>
