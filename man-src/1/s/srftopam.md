---
title: "srftopam(1)"
name: "srftopam"
section: "1"
letter: "s"
url: "/docs/linux/man/1-srftopam/"
description: "srftopam – convert a SRF image file to Netpbm images"
---

<p>&lt;html xmlns=&quot;<a rel="nofollow" href="http://www.w3.org/1999/xhtml">http://www.w3.org/1999/xhtml</a>&quot; xml:lang=&quot;en&quot;&gt; </p>
<h2 class="name">NAME</h2>
<p> srftopam &#8211; convert a SRF image file to Netpbm images </p>
<h2>SYNOPSIS</h2>
<p> <code>srftopam</code> [<code>-verbose</code>] [<i>netpbmfile</i>] </p>
<h2>DESCRIPTION</h2>
<p> This program is part of <code><a href="/docs/linux/man/1-netpbm/">Netpbm</a></code>(1) </p>
<p> <code>srftopam</code> reads a SRF image file as input and produces a multi-image stream of PAM images as output. </p>
<p> This program performs the inverse of the conversion that <code>pamtosrf</code> does. See that program&#8217;s manual for more information about SRF and the relationship between the SRF and Netpbm representation of the images. </p>
<p> <i>netpbmfile</i> is the input stream, which defaults to Standard Input. Output is always on Standard Output. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-verbose</code></p>
<dd> Issue informational messages about the input and the conversion process. </p>
</dl>
<h2>SEE ALSO</h2>
<dl>
<dt>&bull;</p>
<dd>
<p> <code><a href="/docs/linux/man/1-pamtosrf/">pamtosrf</a></code>(1) </p>
<dt>&bull;</p>
<dd>
<p> <code><a href="/docs/linux/man/1-pamdice/">pamdice</a></code>(1) </p>
<dt>&bull;</p>
<dd>
<p> <code><a href="/docs/linux/man/1-pamsplit/">pamsplit</a></code>(1) </p>
<dt>&bull;</p>
<dd>
<p> <code><a href="/docs/linux/man/1-pam/">pam</a></code>(1) </p>
<p>&nbsp;<wbr>&nbsp;<wbr> </p>
</dl>
<h2>HISTORY</h2>
<p> <code>srftopam</code> was new in Netpbm 10.55 (June 2011). </p>
<p> It was contributed by Mike Frysinger. </p>
<h2>Index</h2>
