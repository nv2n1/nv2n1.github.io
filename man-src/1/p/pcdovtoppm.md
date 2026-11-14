---
title: "pcdovtoppm(1)"
name: "pcdovtoppm"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pcdovtoppm/"
description: "pcdovtoppm – create index image for a photo CD"
---

<h2 class="name">NAME</h2>
<p> pcdovtoppm &#8211; create index image for a photo CD</p>
<h2>SYNOPSIS</h2>
<p> <code>pcdovtoppm</code> [<code>-m </code><i>width</i>] [<code>-s </code><i>size</i>] [<code>-a </code><i>across</i>] [<code>-c </code><i>colors</i>] [<code>-f </code><i>font</i>] [<code>-b</code>|<code>-w</code>] [<i>pcdfile</i>] </p>
<h2>DESCRIPTION</h2>
<p> This program is part of <code><a href="/docs/linux/man/1-netpbm/">Netpbm</a></code>(1) </p>
<p> This program generates an index image in PPM format for a photo CD, based on the photo CD overview file. </p>
<p> You can achieve a similar result with <code>hpcdtoppm -Overview</code> followed by <code>pnmindex -black</code> on the generated PPM images. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-w</code><i>width</i></p>
<dd> Maximum width of the result image (default: 1152).</p>
<dt><code>-s</code><i>size</i></p>
<dd> Maximum size of each of the images (default: 192).</p>
<dt><code>-a</code><i>across</i></p>
<dd> Maximum number of images across (default: 6).</p>
<dt><code>-c</code><i>colors</i></p>
<dd> Maximum number of colors, or <code>n</code> </p>
<p> to mean no quantization</p>
<dt><code>-f</code><i>font</i></p>
<dd> Font to be used for annotation (default: internal font).</p>
<dt><code>-b</code></p>
<dd> Black background color (default).</p>
<dt><code>-w</code></p>
<dd> White background color. </p>
</dl>
<h2>EXAMPLES</h2>
<pre>
<code>pcdovtoppm -m 768 -s 96 -f smallfont.pbm overview.pcd &gt; overview.ppm</code>
</pre>
<pre>
<code>pcdovtoppm /cdrom/photo_cd/overview.pcd | ppmtojpeg &gt; overview.jpg</code>
</pre>
<h2>HISTORY</h2>
<p> This program was formerly called <code>pcdindex</code>, which did not fit Netpbm naming conventions. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-hpcdtoppm/">hpcdtoppm</a></code>(1) , <code><a href="/docs/linux/man/1-pnmindex/">pnmindex</a></code>(1) , <code><a href="/docs/linux/man/1-ppmtojpeg/">ppmtojpeg</a></code>(1) , <code><a href="/docs/linux/man/1-ppm/">ppm</a></code>(1) </p>
<h2>Index</h2>
