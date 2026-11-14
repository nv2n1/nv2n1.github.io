---
title: "pnmcrop(1)"
name: "pnmcrop"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pnmcrop/"
description: "pnmcrop – crop a portable anymap"
---

<h2 class="name">NAME</h2>
<p> pnmcrop &#8211; crop a portable anymap </p>
<h2>SYNOPSIS</h2>
<p> <code>pnmcrop</code> [<code>-white</code>|<code>-black</code>|<code>-sides</code>] [<code>-left</code>] [<code>-right</code>] [<code>-top</code>] [<code>-bottom</code>] [<i>pnmfile</i>] </p>
<p> All options may be abbreviated to their shortest unique prefix or specified with double hyphens. </p>
<h2>DESCRIPTION</h2>
<p> Reads a PBM, PGM, or PPM image as input. Removes borders that are the background color, and produces the same type of image as output. </p>
<p> If you don&#8217;t specify otherwise, <code>pnmcrop</code> assumes the background color is whatever color the top left and right corners of the image are and if they are different colors, something midway between them. You can specify that the background is white or black with the <code>-white</code> and <code>-black</code> options or make <code>pnmcrop</code> base its guess on all four corners instead of just two with <code>-sides</code>. </p>
<p> By default, <code>pnmcrop</code> chops off any stripe of background color it finds, on all four sides. You can tell <code>pnmcrop</code> to remove only specific borders with the <code>-left</code>, <code>-right</code>, <code>-top</code>, and <code>-bottom</code> options. </p>
<p> If you want to chop a specific amount off the side of an image, use <code>pnmcut</code>. </p>
<p> If you want to add different borders after removing the existing ones, use <code>pnmcat</code> or <code>pnmcomp</code>. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-white</code></p>
<dd> Take white to be the background color. <code>pnmcrop </code> removes borders which are white.</p>
<dt><code>-black</code></p>
<dd> Take black to be the background color. <code>pnmcrop </code> removes borders which are black.</p>
<dt><code>-sides</code></p>
<dd> Determine the background color from the colors of the four corners of the input image. <code>pnmcrop</code> removes borders which are of the background color. </p>
<p> If at least three of the four corners are the same color, <code>pnmcrop </code> takes that as the background color. If not, <code>pnmcrop</code> looks for two corners of the same color in the following order, taking the first found as the background color: top, left, right, bottom. If all four corners are different colors, <code>pnmcrop</code> assumes an average of the four colors as the background color. </p>
<p> The <code>-sides</code> option slows <code>pnmcrop</code> down, as it reads the entire image to determine the background color in addition to the up to three times that it would read it without <code>-sides</code>. </p>
<dt><code>-left</code></p>
<dd> Remove any left border.</p>
<dt><code>-right</code></p>
<dd> Remove any right border.</p>
<dt><code>-top</code></p>
<dd> Remove any top border.</p>
<dt><code>-bottom</code></p>
<dd> Remove any bottom border.</p>
<dt><code>-verbose</code></p>
<dd> Print on Standard Error information about the processing, including exactly how much is being cropped off of which sides. </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pnmcut/">pnmcut</a></code>(1), <code><a href="/docs/linux/man/1-pnmfile/">pnmfile</a></code>(1), <code><a href="/docs/linux/man/5-pnm/">pnm</a></code>(5) </p>
<h2>AUTHOR</h2>
<p> Copyright (C) 1989 by Jef Poskanzer. </p>
<h2>Index</h2>
