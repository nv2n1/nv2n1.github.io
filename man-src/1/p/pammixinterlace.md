---
title: "pammixinterlace(1)"
name: "pammixinterlace"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pammixinterlace/"
description: "pammixinterlace – mix adjacent lines to merge interlaced images"
---

<h2 class="name">NAME</h2>
<p> pammixinterlace &#8211; mix adjacent lines to merge interlaced images</p>
<h2>SYNOPSIS</h2>
<p> <code>pammixinterlace</code> </p>
<p> [<code>-filter=</code>{<code>linear</code>, <code>fir</code>, <code>ffmpeg</code>}] </p>
<p> [<code>-adaptive</code>] </p>
<p> [<i>infile</i>] </p>
<h2>DESCRIPTION</h2>
<p> This program is part of <code><a href="/docs/linux/man/1-netpbm/">Netpbm</a></code>(1) </p>
<p> <code>pammixinterlace</code> is meant to operate on an image which is the interlacing of two images, where raster rows 0, 2, 4, etc. are from one image and rows 1, 3, 5, etc. are from another. (See below for why you might expect to encounter such an image). </p>
<p> <code>pammixinterlace</code> makes each row of the output a mixture of the corresponding row of the input and its two neighbors. It uses half of the main row and a quarter each of the two neighbor rows. </p>
<p> This can be useful if the image is a video capture from an interlaced video source. In that case, each row shows the subject 1/60 second before or after the two rows that surround it. If the subject is moving, this can detract from the quality of the image. </p>
<p> In video data streams, you often find each frame contains only half the rows of the image &#8212; the odd half or the even half. The displayer of the stream displays the rows in their proper positions on a CRT as they come in. When you display the rows in this order, the CRT has less flicker because a particular area of the screen gets refreshed twice as often. In the process of capturing such a stream, computers often generate the interlaced image of the type that <code>pammixinterlace</code> works with. But this interlaced image, when displayed on a CRT, does not look the same as if a displayer were rendering the stream directly on a CRT as it arrived, because of the timing of when the various pixels get drawn and subsequently fade. That&#8217;s why you need something like <code>pammixinterlace</code>. </p>
<p> You may prefer the effect of simply extracting one of two images. You can do that with <code>pamdeinterlace</code>. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-filter=</code>{<code>linear</code>,<code>fir</code>,<code>ffmpeg</code>}</p>
<dd> This option chooses between one of the three filtering mechanisms. <code>linear</code> is a linear-blend formula. <code>fir</code> is a size-5 FIR low-pass filter, and <code>ffmpeg</code> is a formula pulled from the documentation of the program <code>ffmpeg</code> . </p>
<p> The default is <code>fir</code>. </p>
<dt><code>-adaptive</code></p>
<dd> This option turns on &quot;adaptive&quot; filtering mode. In this mode <code>pammixinterlace</code> modifies only pixels that are obviously part of a &quot;comb&quot; pattern. </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pamdeinterlace/">pamdeinterlace</a></code>(1) , <code><a href="/docs/linux/man/1-pam/">pam</a></code>(1) </p>
<p> <code><a href="/docs/linux/man/1-pnm/">pnm</a></code>(1) </p>
<h2>Index</h2>
