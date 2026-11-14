---
title: "pbmpage(1)"
name: "pbmpage"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pbmpage/"
description: "pbmpage – create a one page test pattern for printing"
---

<h2 class="name">NAME</h2>
<p> pbmpage &#8211; create a one page test pattern for printing </p>
<h2>SYNOPSIS</h2>
<p> <code>pbmpage</code> [<code>-a4</code>] <i>test_pattern</i> </p>
<h2>DESCRIPTION</h2>
<p> <code>pbmpage</code> generates a one page test pattern to print on a sheet of paper, for use in calibrating a printer. The test pattern in is PBM format. </p>
<p> <code>pbmpage</code> produces an image intended for 600 dots per inch printer resolution. </p>
<p> If you are printing on an HP PPA printer, you can convert the output of this program to a stream that you can feed to the printer with <code>pbmtoppa</code>. </p>
<p> Bear in mind that when you print the test pattern, you are testing not only the printer, but any converter or driver software along the printing path. Any one of these components may adjust margins, crop the image, erase edges, and such. </p>
<p> If, due to addition of margins, the printer refuses to print the image because it is too big, use <code>pnmcut</code> to cut the right and bottom edges off the test pattern until it is small enough to print. </p>
<p> <i>test_pattern </i> is the number of the test pattern to generate, as follows. The default is <code>1</code>.</p>
<dl>
<dt><code>1</code></p>
<dd> A grid ruled in numbers of pixels. The outermost rules are exactly at the edges of the paper.</p>
<dt><code>2</code></p>
<dd> A vertical line segment, one pixel wide, extending 1/2&quot; up from the exact center of the page.</p>
<dt><code>3</code></p>
<dd> Two diagonal line segments, one starting at the upper left corner of the page, the other starting from the lower left corner of the page. Both extend 1/2&quot; toward the center of the page at 45 degrees. </p>
</dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>-a4</code></p>
<dd> Generate an image for A4 (European) paper. Without this option, <code>pbmpage</code> generates an image for US standard paper (8 1/2&quot; wide x 11&quot; high). </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pbmtoppa/">pbmtoppa</a></code>(1), <code><a href="/docs/linux/man/1-pnmcut/">pnmcut</a></code>(1), <code><a href="/docs/linux/man/5-pbm/">pbm</a></code>(5) </p>
<h2>AUTHOR</h2>
<p> Tim Norman. Copyright (C) 1998. Licensed under GNU Public License </p>
<p> Manual page by Bryan Henderson, May 2000. </p>
<h2>Index</h2>
