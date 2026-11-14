---
title: "pnmmontage(1)"
name: "pnmmontage"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pnmmontage/"
description: "pnmmontage – create a montage of portable anymaps"
---

<h2 class="name">NAME</h2>
<p> pnmmontage &#8211; create a montage of portable anymaps </p>
<h2>SYNOPSIS</h2>
<p> <code>pnmmontage</code> [<code>-?</code>|<code>-help</code>] [<code>-header=</code><i>headerfile</i>] [<code>-quality=</code><i>n</i>] [<code>-prefix=</code><i>prefix</i>] [<code>-0</code>|<code>-1</code>|<code>-2</code>|<code>&#8230;</code>|<code>-9</code>] pnmfile<i>&#8230;</i></p>
<h2>DESCRIPTION</h2>
<p> Packs images of differing sizes into a minimum-area composite image, optionally producing a C header file with the locations of the subimages within the composite image.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-?, -help</code></p>
<dd> Displays a (very) short usage message.</p>
<dt><code>-header</code></p>
<dd> Tells <code>pnmmontage</code> to write a C header file of the locations of the original images within the packed image. Each original image generates four #defines within the packed file: xxxX, xxxY, xxxSZX, and xxxSZY, where xxx is the name of the file, converted to all uppercase. The #defines OVERALLX and OVERALLY are also produced, specifying the total size of the montage image.</p>
<dt><code>-prefix</code></p>
<dd> Tells <code>pnmmontage</code> to use the specified prefix on all of the #defines it generates.</p>
<dt><code>-quality</code></p>
<dd> Before attempting to place the subimages, <code>pnmmontage</code> will calculate a minimum possible area for the montage; this is either the total of the areas of all the subimages, or the width of the widest subimage times the height of the tallest subimage, whichever is greater. <code>pnmmontage</code> then initiates a problem-space search to find the best packing; if it finds a solution that is (at least) as good as the minimum area times the quality as a percent, it will break out of the search. Thus, <code>-q 100</code> will find the best possible solution; however, it may take a very long time to do so. The default is <code>-q 200.</code></p>
<dt><code>-0, -1, &#8230; -9</code></p>
<dd> These options control the quality at a higher level than <code>-q;</code> <code>-0</code> is the worst quality (literally pick the first solution found), while <code>-9</code> is the best quality (perform an exhaustive search of problem space for the absolute best packing). The higher the number, the slower the computation. The default is <code>-5.</code></dl>
<h2>NOTES</h2>
<p> Using <code>-9</code> is excessively slow on all but the smallest image sets. If the anymaps differ in maxvals, then pnmmontage will pick the smallest maxval which is evenly divisible by each of the maxvals of the original images.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pnmcat/">pnmcat</a></code>(1), <code><a href="/docs/linux/man/1-pnmindex/">pnmindex</a></code>(1), <code><a href="/docs/linux/man/5-pnm/">pnm</a></code>(5), <code><a href="/docs/linux/man/5-pam/">pam</a></code>(5), <code><a href="/docs/linux/man/5-pbm/">pbm</a></code>(5), <code><a href="/docs/linux/man/5-pgm/">pgm</a></code>(5), <code><a href="/docs/linux/man/5-ppm/">ppm</a></code>(5) </p>
<h2>AUTHOR</h2>
<p> Copyright (C) 2000 by Ben Olmstead. </p>
<h2>Index</h2>
