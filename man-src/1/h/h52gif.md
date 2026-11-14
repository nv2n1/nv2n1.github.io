---
title: "h52gif(1)"
name: "h52gif"
section: "1"
letter: "h"
url: "/docs/linux/man/1-h52gif/"
description: "h52gif – Converts an HDF5 file to a GIF file."
---

<h2>NAME</h2>
<p> h52gif &#8211; Converts an HDF5 file to a GIF file.</p>
<h2>SYNOPSIS</h2>
<p> <code>h52gif </code> h5_file gif_file <code>-i </code> h5_image [ <code>-p </code> h5_palette ]</p>
<h2>DESCRIPTION</h2>
<p> h52gif accepts as input the HDF5 file h5_file and the names of images and associated palettes within that file as input and produces the GIF file gif_file, containing those images, as output. </p>
<p> h52gif expects at least one h5_image. You may repeat</p>
<dl>
<dt>
<dd> -i h5_image [-p h5_palette]</dl>
<p> up to 50 times, for a maximum of 50 images.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-i h5_image</code></p>
<dd> Image option, specifying the name of an HDF5 image or dataset containing an image to be converted</p>
<dt><code>-p h5_palette</code></p>
<dd> Palette option, specifying the name of an HDF5 dataset containing a palette to be used in an image conversion</dl>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-h5dump/">h5dump</a></i>(1), <i><a href="/docs/linux/man/1-h5ls/">h5ls</a></i>(1), <i><a href="/docs/linux/man/1-h5diff/">h5diff</a></i>(1), <i><a href="/docs/linux/man/1-h5repart/">h5repart</a></i>(1), <i><a href="/docs/linux/man/1-h5import/">h5import</a></i>(1), <i><a href="/docs/linux/man/1-gif2h5/">gif2h5</a></i>(1), <i><a href="/docs/linux/man/1-h5perf/">h5perf</a></i>(1) </p>
<h2>Index</h2>
