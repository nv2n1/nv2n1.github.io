---
title: "pamtoavs(1)"
name: "pamtoavs"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pamtoavs/"
description: "pamtoavs – convert a Netpbm image to an AVS X image"
---

<h2 class="name">NAME</h2>
<p> pamtoavs &#8211; convert a Netpbm image to an AVS X image </p>
<h2>SYNOPSIS</h2>
<p> <code>pamtoavs</code> [<i>netpbmfile</i>] </p>
<h2>DESCRIPTION</h2>
<p> This program is part of <code><a href="/docs/linux/man/1-netpbm/">Netpbm</a></code>(1) </p>
<p> <code>pamtoavs</code> reads a Netpbm image as input and produces a Stardent &lt;acronym xml:lang=&quot;en&quot; title=&quot;Application Visualization System&quot;&gt;AVS&lt;/acronym&gt; X image as output. AVS X images are one of the few image formats Gnuplot &nbsp;<wbr>v4.2 and later can use. </p>
<p> <i>netpbmfile</i> is the input file, which defaults to Standard Input. Output is always on Standard Output. </p>
<p> Try the following: </p>
<pre>
    gnuplot&gt; plot 'myimage.avs' binary filetype=avs with rgbimage
</pre>
<p> See the <code>Gnuplot</code> manual (1)<br />
&nbsp;<wbr>for more information. </p>
<h2>AUTHOR</h2>
<p> Copyright&nbsp;<wbr>&#169; 2010 Scott Pakin, <i>scott+pbm [at] pakin.org.</i> </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-avstopam/">avstopam</a></code>(1) , gnuplot , <code><a href="/docs/linux/man/1-pam/">pam</a></code>(1) </p>
<h2>Index</h2>
