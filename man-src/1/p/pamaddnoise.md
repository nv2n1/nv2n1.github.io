---
title: "pamaddnoise(1)"
name: "pamaddnoise"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pamaddnoise/"
description: "pamaddnoise – add noise to a Netpbm image"
---

<h2 class="name">NAME</h2>
<p> pamaddnoise &#8211; add noise to a Netpbm image </p>
<h2>SYNOPSIS</h2>
<p> <code>pamaddnoise</code> </p>
<p> [<code>-type</code> <i>noise_type</i>] </p>
<p> [<code>-seed</code> <i>int</i>] <code>pamaddnoise</code> <code>-type</code> <code>gaussian</code> </p>
<p> [<code>-sigma1</code> <i>value</i>] </p>
<p> [<code>-sigma2</code> <i>value</i>] [<code>-seed</code> <i>int</i>] </p>
<p> [<i>netpbmfile</i>] <code>pamaddnoise</code> <code>-type </code> <code>multiplicative_gaussian</code> </p>
<p> [<code>-mgsigma</code> <i>value</i>] [<code>-seed</code> <i>int</i>] </p>
<p> [<i>netpbmfile</i>] <code>pamaddnoise</code> <code>-type</code> <code>impulse</code> </p>
<p> [<code>-tolerance</code> <i>ratio</i>] </p>
<p> [<code>-seed</code> <i>int</i>] [<i>netpbmfile</i>] <code>pamaddnoise</code> <code>-type </code> <code>laplacian</code> </p>
<p> [<code>-lsigma</code> <i>value</i>] </p>
<p> [<code>-seed</code> <i>int</i>] [<i>netpbmfile</i>] <code>pamaddnoise</code> <code>-type </code> <code>poisson</code> </p>
<p> [<code>-lambda</code> <i>value</i>] </p>
<p> [<code>-seed</code> <i>int</i>] [<i>netpbmfile</i>] </p>
<h2>DESCRIPTION</h2>
<p> This program is part of <code><a href="/docs/linux/man/1-netpbm/">Netpbm</a></code>(1) </p>
<p> <code>pamaddnoise</code> adds the specified noise type to a Netpbm image. <code>pamaddnoise</code> treats a PPM image as 3 independent planes, not as a plane of colors in a color space. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-lambda</code> <i>value</i></p>
<dd> Used for poisson noise only. The default value is 0.05. </p>
<dt><code>-lsigma</code> <i>value</i></p>
<dd> Used for laplacian noise only. The default value is 10.0. </p>
<dt><code>-mgsigma</code> <i>value</i></p>
<dd> Used for multiplicative gaussian noise only. The default value is 0.5. </p>
<dt><code>-seed</code> <i>int</i></p>
<dd> Used for all noise types. Set the initial random number generator seed value. </p>
<dt><code>-sigma1</code> <i>value</i></p>
<dd> Used for gaussian noise only. The default value is 4.0. </p>
<dt><code>-sigma2</code> <i>value</i></p>
<dd> Used for gaussian noise only. The default value is 20.0. </p>
<dt><code>-tolerance</code> <i>ratio</i></p>
<dd> Used for impulse noise only. The default value is 0.10. This means that 5% of all pixel values will be set to 0 and 5% will be set to the maxval </p>
<dt><code>-type</code> <i>noise_type</i></p>
<dd> Select type of noise by name. The following noise types are available: gaussian, multiplicative_gaussian, impulse, laplacian, poisson. Only enough letters to be unique are required for the noise type option. The default noise type is <code>gaussian</code>. </p>
<dt>&bull;</p>
<dd> <code>gaussian</code></p>
<dt>&bull;</p>
<dd> <code>multiplicative_gaussian</code></p>
<dt>&bull;</p>
<dd> <code>impulse</code></p>
<dt>&bull;</p>
<dd> <code>laplacian</code></p>
<dt>&bull;</p>
<dd> <code>poisson</code> </p>
</dl>
<h2>REFERENCES</h2>
<dl>
<dt>&bull;</p>
<dd> &#8216;Adaptive Image Restoration in Signal-Dependent Noise&#8217; by R. Kasturi Institute for Electronic Science, Texas Tech University, 1982 </p>
<dt>&bull;</p>
<dd> &#8216;Digital Image Processing Algorithms&#8217; by Ioannis Pitas, Prentice Hall, 1993 ISBN 0-13-145814-0 </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pgmnoise/">pgmnoise</a></code>(1) , <code><a href="/docs/linux/man/1-pgmmedian/">pgmmedian</a></code>(1) , <code><a href="/docs/linux/man/1-pnm/">pnm</a></code>(1) , <code><a href="/docs/linux/man/1-pam/">pam</a></code>(1) , </p>
<h2>HISTORY</h2>
<p> <code>pamaddnoise</code> was added to Netpbm in Version 10.29 (August 2005). It had been distributed by Mike Burns via his own web site before that (and continued to be so). </p>
<p> Burns&#8217; version, and the one in Netpbm 10.29, was called <code>pnmaddnoise</code> and worked only on PNM images. In Netpbm 10.30, it was converted to handle PAM images and renamed to <code>pamaddnoise</code>. </p>
<h2>AUTHOR</h2>
<p> Copyright (C) 1995 by Mike Burns &lt;<i>burns [at] cac.psu.edu</i>&gt; </p>
<h2>Index</h2>
