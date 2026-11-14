---
title: "pamsummcol(1)"
name: "pamsummcol"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pamsummcol/"
description: "pamsummcol – summarize (sum, average, etc) a Netpbm image by column"
---

<h2 class="name">NAME</h2>
<p> pamsummcol &#8211; summarize (sum, average, etc) a Netpbm image by column</p>
<h2>SYNOPSIS</h2>
<p> <code>pamsummcol</code> { <code>-sum</code> | <code>-mean</code> | <code>-min</code> | <code>-max</code> } [<i>imagefile</i>] </p>
<p> All options can be abbreviated to their shortest unique prefix. You may use two hyphens instead of one. You may separate an option name and its value with white space instead of an equals sign. </p>
<h2>DESCRIPTION</h2>
<p> This program is part of <code><a href="/docs/linux/man/1-netpbm/">Netpbm</a></code>(1) </p>
<p> <code>pamsummcol</code> reads a Netpbm image (PNM or PAM) and performs a summary function over all the rows in each column (sum, mean, etc.). It produces an image of the same kind that the same width and depth as the input, and one row high. Its sample values are the result of the summary. </p>
<p> <code>pamsummcol</code> performs the summary operation on each plane independently. </p>
<p> <code>pamsummcol</code> performs the operation on the actual sample values, not on the light intensities represented by them in the case that the image is a PGM or PPM image. </p>
<p> If you want to summarize by row instead of by column, run the input through <code>pamflip</code> first (and if you want the output to be a single column instead of a single row, use <code>pamflip</code> again). </p>
<p> If you want to summarize over the entire image (getting a one-tuple output image), use <code>pamsumm</code> to get a summary row, <code>pamflip</code> to turn that into a column, the <code>pamsumm</code> again to summarize the column. </p>
<p> If you want to summarize the individual samples in an entire image, instead of by tuple, use <code>pamsumm</code>. </p>
<p> <code>pamsummcol</code> performs the operation on the actual sample values, not on the light intensities represented by them in the case that the image is a PGM or PPM image or PAM equivalent. You can use <code>pnmgamma</code> to convert such an image to one with samples proportional to light intensity, and then use <code>pamsummcol</code> on the result. </p>
<p> You can achieve the same thing as <code>pamsummcol -mean</code> with <code>pamscale</code>. Just scale vertically to a single row, without scaling horizontally at all. Use the pixel mixing method. </p>
<h2>OPTIONS</h2>
<p> You must specify exactly one of <code>-sum</code>, <code>-mean</code>, <code>-min</code>, or <code>-max</code>. </p>
<dl>
<dt><code>-sum</code></p>
<dd>
<p> This option makes the summary function addition.<br />
&nbsp;<wbr>&nbsp;<wbr>In each column and plane of the output row, the sample value is the<br />
&nbsp;<wbr>&nbsp;<wbr>sum of all the samples values in the same column and plane of the input.<br />
&nbsp;<wbr>&nbsp;<wbr>If a result is greater than the image maxval, it is clipped to<br />
&nbsp;<wbr>&nbsp;<wbr>the maxval. </p>
<dt><code>-mean</code></p>
<dd>
<p> This option makes the summary function arithmetic mean.<br />
&nbsp;<wbr>&nbsp;<wbr>In each column and plane of the output row, the sample value is the<br />
&nbsp;<wbr>&nbsp;<wbr>mean of all the samples values in the same column and plane of the input. </p>
<dt><code>-min</code></p>
<dd>
<p> This option makes the summary function arithmetic minimum.<br />
&nbsp;<wbr>&nbsp;<wbr>In each column and plane of the output row, the sample value is the<br />
&nbsp;<wbr>&nbsp;<wbr>minimum of all the samples values in the same column and plane of<br />
&nbsp;<wbr>&nbsp;<wbr>the input. </p>
<dt><code>-max</code></p>
<dd>
<p> This option makes the summary function arithmetic maximum.<br />
&nbsp;<wbr>&nbsp;<wbr>In each column and plane of the output row, the sample value is<br />
&nbsp;<wbr>&nbsp;<wbr>the maximum of all the samples values in the same column and<br />
&nbsp;<wbr>&nbsp;<wbr>plane of the input. </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pamsumm/">pamsumm</a></code>(1) , <code><a href="/docs/linux/man/1-pamscale/">pamscale</a></code>(1) , <code><a href="/docs/linux/man/1-pamfunc/">pamfunc</a></code>(1) , <code><a href="/docs/linux/man/1-pamarith/">pamarith</a></code>(1) , <code><a href="/docs/linux/man/1-pamscale/">pamscale</a></code>(1) , <code><a href="/docs/linux/man/1-pam/">pam</a></code>(1) , </p>
<h2>HISTORY</h2>
<p> <code>pamsummcol</code> was added to Netpbm in Release 10.21 (March 2004). </p>
<h2>Index</h2>
