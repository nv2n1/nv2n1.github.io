---
title: "pnmhistmap(1)"
name: "pnmhistmap"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pnmhistmap/"
description: "pnmhistmap – draw a histogram for a PGM or PPM file"
---

<h2 class="name">NAME</h2>
<p> pnmhistmap &#8211; draw a histogram for a PGM or PPM file </p>
<h2>SYNOPSIS</h2>
<p> <code>pnmhistmap</code> [<code>-black</code>] [<code>-white</code>] [<code>-max</code> <i>N</i>] [<code>-verbose</code>] [<i>pnmfile</i>]</p>
<h2>DESCRIPTION</h2>
<p> Reads a portable anymap as input, although bitmap (PBM) input produces an error message and no image. Produces an image showing a histogram of the color (or gray) values in the input. A graymap (PGM) input produces a bitmap output. A pixmap (PPM) input produces pixmap output with three overlaid histograms: a red one for the red input, a green one for the green input, and a blue one for the blue input. The output is fixed in size: 256 pixels wide by 200 pixels high.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-black </code></p>
<dd> Ignores the count of black pixels when scaling the histogram.</p>
<dt><code>-white</code></p>
<dd> Ignores the count of white pixels when scaling the histogram.</dl>
<p> The -black and -white options, which can be used seperately or together, are useful for images with a large percentage of pixels whose value is zero or 255, which can cause the remaining histogram data to become unreadbaly small. Note that, for pixmap inputs, these options apply to all colors; if, for example, the input has a large number of bright-red areas, you will probably want to use the -white option.</p>
<dl>
<dt><code>-max N</code></p>
<dd> Force the scaling of the histogram to use N as the largest-count value. This is useful for inputs with a large percentage of single-color pixels which are not black or white.</p>
<dt><code>-verbose</code></p>
<dd> Report the progress of making the histogram, including the largest-count value used to scale the output.</dl>
<p> All flags can be abbreviated to their shortest unique prefix.</p>
<h2>BUGS</h2>
<p> Assumes maxval is always 255. Images with a smaller maxval will only use the lower-value side of the histogram. This can be overcome either by piping the input through &quot;pnmdepth 255&quot; or by cutting and scaling the lower-value side of the histogram. Neither is a particularly elegant solution. </p>
<p> Should allow the output size to be specified.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-pgmhist/">pgmhist</a>(1), <a href="/docs/linux/man/1-ppmhist/">ppmhist</a>(1), <a href="/docs/linux/man/5-pgm/">pgm</a>(5), <a href="/docs/linux/man/5-ppm/">ppm</a>(5)</p>
<h2>AUTHOR</h2>
<p> Wilson H. Bent. Jr. (whb [at] usc.edu). </p>
<h2>Index</h2>
