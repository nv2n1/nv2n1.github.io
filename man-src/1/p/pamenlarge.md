---
title: "pamenlarge(1)"
name: "pamenlarge"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pamenlarge/"
description: "pamenlarge – Enlarge a Netpbm image N times"
---

<h2 class="name">NAME</h2>
<p> pamenlarge &#8211; Enlarge a Netpbm image N times</p>
<h2>SYNOPSIS</h2>
<p> <code>pamenlarge</code> <i>N</i> [<i>pnmfile</i>] </p>
<h2>DESCRIPTION</h2>
<p> This program is part of <code><a href="/docs/linux/man/1-netpbm/">Netpbm</a></code>(1) </p>
<p> <code>pamenlarge</code> reads a Netpbm image as input, replicates its pixels <i>N</i> times, and produces a Netpbm image as output. The output is the same type of image as the input. </p>
<p> If you enlarge by a factor of 3 or more, you should probably add a <code>pnmsmooth</code> step; otherwise, you can see the original pixels in the resulting image. </p>
<p> For PBM images, <code>pamenlarge</code> uses special fast algorithms for scale factors up to 10. For larger factors, it uses a simple but slow algorithm. As a result, you can often get a significantly faster scale by running <code>pamenlarge</code> multiple times. For example, enlarging by 3 and then by 5 is faster than enlarging once by 15. And because the algorithms are different for the different scale factors, some faster than others, the order matters too. For example, the following examples all produce the same output &#8212; an image 15 times bigger on edge than the input &#8212; but with at different spees, each being faster than the one before. </p>
<pre>
<tt>
     $ pamenlarge 15 test.pbm
     $ pamenlarge 5 test.pbm | pamenlarge 3
     $ pamenlarge 3 test.pbm | pamenlarge 5
</tt>
</pre>
<p> The special fast cases for factors up to 10 have existed since Release 10.50 (March 2010). The special cases for 1, 2, 3, and 5 go back to Release 10.41 (December 2007). Before 10.41, there are no special scale factors and PBM enlargement is significantly slower than today for all scale factors. </p>
<p> <code>pamenlarge</code> can enlarge only by integer factors. The slower but more general <code>pamscale</code> can enlarge or reduce by arbitrary factors. <code>pamscale</code> allows you to enlarge by resampling, which gives you smoother enlargements. But it is much slower. </p>
<p> <code>pamstretch</code> is another enlarging program that enlarges by integer factors. It does a simple kind of resampling that gives you a smoothed enlargement with less computational cost. </p>
<p> <code>pbmreduce</code> can reduce by integer factors, but only for PBM images. </p>
<h2>HISTORY</h2>
<p> <code>pamenlarge</code> was new in Netpbm 10.25 (October 2004). It is designed as a replacement for <code>pnmenlarge</code> by Jef Poskanzer, which was in Pbmplus as far back as 1989. The major difference is that <code>pamenlarge</code> can enlarge PAM format images in addition to PNM. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pbmreduce/">pbmreduce</a></code>(1) , <code><a href="/docs/linux/man/1-pamscale/">pamscale</a></code>(1) , <code><a href="/docs/linux/man/1-pamstretch/">pamstretch</a></code>(1) , <code><a href="/docs/linux/man/1-pbmpscale/">pbmpscale</a></code>(1) , <code><a href="/docs/linux/man/1-pnmsmooth/">pnmsmooth</a></code>(1) , <code><a href="/docs/linux/man/1-pnm/">pnm</a></code>(1) </p>
<h2>AUTHOR</h2>
<p> Copyright (C) 1989 by Jef Poskanzer. </p>
<h2>Index</h2>
