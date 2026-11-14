---
title: "pamsumm(1)"
name: "pamsumm"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pamsumm/"
description: "pamsumm – Summarize the samples in a Netpbm image arithmetically"
---

<h2 class="name">NAME</h2>
<p> pamsumm &#8211; Summarize the samples in a Netpbm image arithmetically</p>
<h2>SYNOPSIS</h2>
<p> <code>pamsumm</code> { <code>-sum</code> | <code>-mean</code> | <code>-min</code> | <code>-max</code> } [<code>-normalize</code>] [<code>-brief</code>] [<i>imagefile</i>] </p>
<p> All options can be abbreviated to their shortest unique prefix. You may use two hyphens instead of one. You may separate an option name and its value with white space instead of an equals sign. </p>
<h2>DESCRIPTION</h2>
<p> This program is part of <code><a href="/docs/linux/man/1-netpbm/">Netpbm</a></code>(1) </p>
<p> <code>pamsumm</code> reads a Netpbm image (PNM or PAM) and performs a summary function over all the samples in all the rows, columns, and planes and prints the result to Standard Output. </p>
<p> <code>pamsumm</code> performs the operation on the actual sample values. In the case of a PGM or PPM or PAM equivalent (i.e. a visual image), this is not the same as the light intensities represented by those samples. See the format specifications of <code><a href="/docs/linux/man/1-pgm/">PGM</a></code>(1) , <code><a href="/docs/linux/man/1-ppm/">PPM</a></code>(1) , and <code><a href="/docs/linux/man/1-pam/">PAM</a></code>(1) , for the precise meanings of samples in these formats. If you want to do arithmetic on light intensities of such a visual image, you can use <code>pnmgamma</code> to convert it to one with samples proportional to light intensity, and then use <code>pamsumm</code> on the result. </p>
<p> If you want to summarize by column (e.g. add up the columns separately), use <code>pamsummcol</code>. If you want to summarize by row, use a combination of <code>pamsummcol</code> and <code>pamflip</code>. If you want to summarize a particular plane, use <code>pamchannel</code> to extract it and then <code>pamsumm</code>. </p>
<h2>OPTIONS</h2>
<p> You must specify exactly one of <code>-sum</code>, <code>-mean</code>, <code>-min</code>, or <code>-max</code>. </p>
<dl>
<dt><code>-sum</code></p>
<dd>
<p> This option makes the summary function addition. </p>
<dt><code>-mean</code></p>
<dd>
<p> This option makes the summary function arithmetic mean. </p>
<dt><code>-min</code></p>
<dd>
<p> This option makes the summary function arithmetic minimum. </p>
<dt><code>-max</code></p>
<dd>
<p> This option makes the summary function arithmetic maximum. </p>
<dt><code>-normalize</code></p>
<dd>
<p> This option causes each sample to be normalized to a fraction<br />
&nbsp;<wbr>&nbsp;<wbr>(in the range 0..1)&nbsp;<wbr>so the result is independent of the image&#8217;s<br />
&nbsp;<wbr>&nbsp;<wbr>maxval.&nbsp;<wbr>&nbsp;<wbr>E.g. if you request the mean of an image which has maxval<br />
&nbsp;<wbr>&nbsp;<wbr>200 and all the samples have value 50,&nbsp;<wbr><code>pamsumm</code>&nbsp;<wbr>will give you<br />
&nbsp;<wbr>&nbsp;<wbr>50 as an answer.&nbsp;<wbr>&nbsp;<wbr>But&nbsp;<wbr><code>pamsumm -normalize</code>&nbsp;<wbr>will give you .25. </p>
<p> If instead you want a result that is independent of maxval but still<br />
&nbsp;<wbr>&nbsp;<wbr>in integers, you can use&nbsp;<wbr><code>pamdepth</code>&nbsp;<wbr>to convert the input to some<br />
&nbsp;<wbr>&nbsp;<wbr>standard maxval and not use&nbsp;<wbr><code>-normalize</code>.&nbsp;<wbr>&nbsp;<wbr>For example, if you want<br />
&nbsp;<wbr>&nbsp;<wbr>the mean brightness of a PPM image, on a scale of 0 to 99, do </p>
<pre>
<tt>
    pamdepth 99 myimage.ppm | pamsumm -mean
</tt>
</pre>
<p> This option was new in Netpbm 10.22 (April 2004)<br />
&nbsp;<wbr>&nbsp;<wbr></p>
<dt><code>-brief</code></p>
<dd>
<p> This option causes <code>pamsumm</code> to display the answer as a bare<br />
&nbsp;<wbr>&nbsp;<wbr>number, rather than in a complete sentence. </p>
<p> This option was new in Netpbm 10.22 (April 2004) </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pamsumm/">pamsumm</a></code>(1) , <code><a href="/docs/linux/man/1-pam/">pam</a></code>(1) , </p>
<h2>HISTORY</h2>
<p> <code>pamsumm</code> was added to Netpbm in Release 10.21 (March 2004). </p>
<h2>Index</h2>
