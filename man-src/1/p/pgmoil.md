---
title: "pgmoil(1)"
name: "pgmoil"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pgmoil/"
description: "pamoil – turn a PAM image into an oil painting"
---

<h2 class="name">NAME</h2>
<p> pamoil &#8211; turn a PAM image into an oil painting</p>
<h2>SYNOPSIS</h2>
<p> <code>pamoil</code> [<code>-n</code> <i>N</i>] [<i>pamfile</i>] </p>
<h2>DESCRIPTION</h2>
<p> Reads a Netpbm image as input. Does an &quot;oil transfer&quot;, and writes the same type of Netpbm image as output. </p>
<p> The oil transfer is described in &quot;Beyond Photography&quot; by Holzmann, chapter 4, photo 7. It&#8217;s a sort of localized smearing. </p>
<p> The smearing works like this: First, assume a grayscale image. For each pixel in the image, <code>pamoil</code> looks at a square neighborhood around it. <code>pamoil</code> determines what is the most common pixel intensity in the neighborhood, and puts a pixel of that intensity into the output in the same position as the input pixel. </p>
<p> For color images, or any arbitrary multi-channel image, <code>pamoil</code> computes each channel (e.g. red, green, and blue) separately the same way as the grayscale case above. </p>
<p> At the edges of the image, where the regular neighborhood would run off the edge of the image, <code>pamoil</code> uses a clipped neighborhood. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-n </code><i>size</i></p>
<dd> This is the size of the neighborhood used in the smearing. The neighborhood is this many pixels in all four directions. </p>
<p> The default is 3. </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pgmbentley/">pgmbentley</a></code>(1), <code><a href="/docs/linux/man/1-ppmrelief/">ppmrelief</a></code>(1), <code><a href="/docs/linux/man/5-ppm/">ppm</a></code>(5) </p>
<h2>AUTHOR</h2>
<p> Based on pgmoil Copyright (C) 1990 by Wilson Bent (whb [at] hoh-2.att.com) </p>
<p> Modified to ppm by Chris Sheppard, June 25, 2001 </p>
<p> Modified to pnm, using pam functions, by Bryan Henderson June 28, 2001. </p>
<h2>Index</h2>
