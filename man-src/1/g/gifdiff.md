---
title: "gifdiff(1)"
name: "gifdiff"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gifdiff/"
description: "gifdiff – compares GIF images"
---

<h2>NAME</h2>
<p> gifdiff &#8211; compares GIF images</p>
<h2>SYNOPSIS</h2>
<p> <code>gifdiff</code> [options] GIF-file-1 GIF-file-2</p>
<h2>DESCRIPTION</h2>
<p> <code>gifdiff</code> compares two GIF files and determines if they appear identical. Differences that don&#8217;t affect appearance (like colormap ordering or how much an animation is optimized) are not reported. </p>
<p> <code>gifdiff</code> prints details of any differences it finds. If the GIFs are the same, it prints nothing. It exits with status 0 if there were no differences, 1 if there were some differences, and 2 if there was trouble.</p>
<h2>OPTIONS</h2>
<dl>
<dt> <code>&#8211;brief</code>, <code>-q</code></p>
<dd> Report only whether the GIFs differ, not the details of the differences. </p>
<dt> <code>&#8211;ignore-redundancy</code>, <code>-w</code></p>
<dd> Do not report differences in the numbers of redundant frames (frames which do not change the displayed image). </p>
<dt> <code>&#8211;ignore-background</code>, <code>-B</code></p>
<dd> Do not report differences in background colors. </p>
<dt> <code>&#8211;help</code></p>
<dd> Print usage information and exit. </p>
<dt> <code>&#8211;version</code></p>
<dd> Print the version number and some quickie warranty information and exit.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-gifsicle/">gifsicle</a></code>(1)</p>
<h2>BUGS</h2>
<p> Please email suggestions, additions, patches and bugs to ekohler [at] gmail.com.</p>
<h2>AUTHORS</h2>
<p> Eddie Kohler, ekohler [at] gmail.com<br />
 <a rel="nofollow" href="http://www.read.seas.harvard.edu/~kohler/">http://www.read.seas.harvard.edu/~kohler/</a> </p>
<p> <a rel="nofollow" href="http://www.lcdf.org/gifsicle/">http://www.lcdf.org/gifsicle/</a><br />
 The <code>gifsicle</code> home page. </p>
<h2>Index</h2>
