---
title: "svgtopam(1)"
name: "svgtopam"
section: "1"
letter: "s"
url: "/docs/linux/man/1-svgtopam/"
description: "svgtopam – convert an SVG (Scalable Vector Graphics) image to Netpbm format"
---

<h2 class="name">NAME</h2>
<p> svgtopam &#8211; convert an SVG (Scalable Vector Graphics) image to Netpbm format</p>
<h2>SYNOPSIS</h2>
<p> <code>svgtopam</code> [<code>-trace</code>] [<i>pnmfile</i>] </p>
<p> Minimum unique abbreviation of option is acceptable. You may use double hyphens instead of single hyphen to denote options. You may use white space in place of the equals sign to separate an option name from its value. </p>
<h2>DESCRIPTION</h2>
<p> This program is part of <code><a href="/docs/linux/man/1-netpbm/">Netpbm</a></code>(1) </p>
<p> <code>svgtopam</code> reads an SVG (Scalable Vector Graphics) image as input and produces a PAM image as output. </p>
<p> <code>svgtopam</code> is so weak that it is probably not useful in general for converting SVG images. It understands only &lt;path&gt; SVG elements which use only the &#8216;M&#8217;, &#8216;L&#8217;, and &#8216;z&#8217; commands. This is sufficient for converting anything that comes out of <code>pamtosvg</code> (not by coincidence &#8211; the program was developed for the specific task of testing <code>pamtosvg</code>), but the main reason it is part of Netpbm is to provide a base for someone to create a full SVG to Netpbm converter. </p>
<p> SVG is a vector image format, which means it describes curves that compose an image. By contrast, PNM is a raster format, which means it describes dots that compose an image. The main practical difference between the two types is that you can scale vector images better. A vector image also takes a lot less data to describe an image if the image is composed of simple curves. </p>
<p> That means it is really an understatement to say that <code>svgtopam</code> is an image format converter. It&#8217;s really an image drawer, not unlike <code>ppmdraw</code>. </p>
<p> For more information on SVG, see the Worldwide Web Consortium&#8217;s SVG web page . </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-trace</code></p>
<dd> This option makes <code>svgtopam</code> issue messages describing the drawing. </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pamtosvg/">pamtosvg</a></code>(1) , <code><a href="/docs/linux/man/1-pam/">pam</a></code>(1) , </p>
<h2>HISTORY</h2>
<p> <code>svgtopam</code> was added to Netpbm in Version 10.34 (May 2006). </p>
<p> Bryan Henderson created <code>svgtopam</code> to test <code>pamtosvg</code>. </p>
<h2>Index</h2>
