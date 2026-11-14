---
title: "pamtosrf(1)"
name: "pamtosrf"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pamtosrf/"
description: "pamtosrf – convert a sequence of Netpbm images to a SRF image file"
---

<p>&lt;html xmlns=&quot;<a rel="nofollow" href="http://www.w3.org/1999/xhtml">http://www.w3.org/1999/xhtml</a>&quot; xml:lang=&quot;en&quot;&gt; </p>
<h2 class="name">NAME</h2>
<p> pamtosrf &#8211; convert a sequence of Netpbm images to a SRF image file </p>
<h2>SYNOPSIS</h2>
<p> <code>pamtosrf</code> [<code>-verbose</code>] [<i>netpbmfile</i>] </p>
<h2>DESCRIPTION</h2>
<p> This program is part of <code><a href="/docs/linux/man/1-netpbm/">Netpbm</a></code>(1) </p>
<p> <code>pamtosrf</code> reads a Netpbm image stream as input and produces a an SRF image file as output. I don&#8217;t know exactly what SRF is, but on popular use of it is in Garmin vehicle information files, which tell a GPS receiver how to depict a vehicle on its display. </p>
<p> An SRF file can contain multiple images; each image in a multi-image Netpbm input stream becomes one image in the SRF. </p>
<p> <code>pamtosrf</code> does not care how many images there are or what their dimensions or content are. However, a Garmin vehicle information file has specific requirements, so if you don&#8217;t make your Netpbm input conform, neither will your SRF output. For such a file, you should have two image: the first for 3D oblique views of the vehicle and the second for overhead views. Each image is a horizontal concatenation of 36 square images, each rotated 10 degrees from the previous, thereby covering the full 360 degree circle. You could create this concatenation with <code>pnmcat -lr</code> and you could create the invidual views with <code>pnmrotate</code>. </p>
<p> One way to use <code>pamtosrf</code> is to get an SRF file, convert it to PAM with <code>srftopam</code>, manipulate it, then convert it back with <code>pamtosrf</code>. </p>
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
<p> <code><a href="/docs/linux/man/1-srftopam/">srftopam</a></code>(1) </p>
<dt>&bull;</p>
<dd>
<p> <code><a href="/docs/linux/man/1-pnmcat/">pnmcat</a></code>(1) </p>
<dt>&bull;</p>
<dd>
<p> <code><a href="/docs/linux/man/1-pam/">pam</a></code>(1) </p>
<p>&nbsp;<wbr>&nbsp;<wbr> </p>
</dl>
<h2>HISTORY</h2>
<p> <code>srftopam</code> was new in Netpbm 10.55 (June 2011). </p>
<p> It was contributed by Mike Frysinger. </p>
<h2>Index</h2>
