---
title: "winicontopam(1)"
name: "winicontopam"
section: "1"
letter: "w"
url: "/docs/linux/man/1-winicontopam/"
description: "winicontopam – convert a Microsoft Windows icon file into a Netpbm PAM file"
---

<h2 class="name">NAME</h2>
<p> winicontopam &#8211; convert a Microsoft Windows icon file into a Netpbm PAM file </p>
<h2>SYNOPSIS</h2>
<p> <code>winicontopam</code> [<code>-image=</code><i>index</i> | <code>-allimages</code>] [<code>-andmasks</code>] [<code>-verbose</code>] [<i>icon_file</i>] </p>
<p> All options can be abbreviated to their shortest unique prefix. You may use two hyphens instead of one to designate an option. You may use either white space or equals signs between an option name and its value. </p>
<h2>DESCRIPTION</h2>
<p> This program is part of <code><a href="/docs/linux/man/1-netpbm/">Netpbm</a></code>(1) </p>
<p> <code>winicontopam</code> reads a Microsoft Windows icon file and converts it to one or more RGB_ALPHA Netpbm PAM files. </p>
<p> The alpha channel is copied from the 8-bit transparency data from the icon, if present. If no 8-bit transparency data is available, the alpha channel is constructed from the so-called &amp;lsquo;AND mask&amp;rsquo;. </p>
<p> The output goes to Standard Output. </p>
<p> The output is a multi-image PAM file. If you want a separate file for each image, use <code><a href="/docs/linux/man/1-pamsplit/">pamsplit</a></code>(1) </p>
<h2>OPTIONS</h2>
<p> In addition to the options common to all programs based on libnetpbm (most notably <code>-quiet</code>, see Common Options ), <code>winicontopam</code> recognizes the following command line options: </p>
<dl>
<dt><code>-allimages</code></p>
<dd> Convert all images in the input. </p>
<p> You may not specify this together with <code>-image</code>. </p>
<p> By default, <code>winicontopam</code> converts only the one &amp;lsquo;best quality&amp;rsquo; image (largest, then most bits per pixel). </p>
<dt><code>-image=</code><i>index</i></p>
<dd> Convert image number <i>index</i> (starting with zero). </p>
<p> You may not specify this together with <code>-allimages</code>. </p>
<p> By default, <code>winicontopam</code> converts the &amp;lsquo;best quality&amp;rsquo; image (largest, then most bits per pixel). </p>
<dt><code>-andmasks</code></p>
<dd> If the image to be extracted contains both 8-bit transparency data and AND mask, write a five-channel Netpbm PAM file with the AND mask stored to the fifth plane. </p>
<dt><code>-verbose</code></p>
<dd> Print more messages </p>
</dl>
<h2>SEE ALSO</h2>
<dl>
<dt>&bull;</p>
<dd>
<p> <code><a href="/docs/linux/man/1-pamtowinicon/">pamtowinicon</a></code>(1) </p>
<dt>&bull;</p>
<dd>
<p> <code><a href="/docs/linux/man/1-winicontoppm/">winicontoppm</a></code>(1) </p>
<dt>&bull;</p>
<dd>
<p> <code><a href="/docs/linux/man/1-pamsplit/">pamsplit</a></code>(1) </p>
<dt>&bull;</p>
<dd>
<p> <code><a href="/docs/linux/man/1-pam/">pam</a></code>(1)<br />
&nbsp;<wbr></p>
<dt>&bull;</p>
<dd>
<p> <code><a href="/docs/linux/man/1-winicon/">winicon</a></code>(1) </p>
</dl>
<p> For information on the PNG format, see <a rel="nofollow" href="http://schaik.com/png">http://schaik.com/png</a> . </p>
<h2>HISTORY</h2>
<p> <code>winicontopam</code> was new in Netpbm 10.63 (June 2013). It obsoleted <code>winicontoppm</code> by providing more function and conforming better to Netpbm conventions. </p>
<h2>AUTHOR</h2>
<p> Copyright (C) 2013 by Ludolf Holzheid. </p>
<p> Translated to Netpbm coding style by Bryan Henderson. </p>
<h2>Index</h2>
