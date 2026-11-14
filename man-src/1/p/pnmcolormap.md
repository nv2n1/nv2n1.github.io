---
title: "pnmcolormap(1)"
name: "pnmcolormap"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pnmcolormap/"
description: "pnmcolormap – create quantization color map for a portable anymap"
---

<h2 class="name">NAME</h2>
<p> pnmcolormap &#8211; create quantization color map for a portable anymap</p>
<h2>SYNOPSIS</h2>
<p> <code>pnmcolormap</code> [<code>-center</code>|<code>-meancolor</code>|<code>-meanpixel</code>] [<code>-spreadbrightness</code>|<code>-spreadluminosity</code>] [<code>-sort</code>] [<code>-square</code>] <i>ncolors</i>|<i></i><code>all</code> [<i>pnmfile</i>] </p>
<p> All options can be abbreviated to their shortest unique prefix. You may use two hyphens instead of one to designate an option. You may use either white space or an equals sign between an option name and its value. </p>
<h2>DESCRIPTION</h2>
<p> Reads a PNM image as input. Chooses <i>ncolors</i> colors to best represent the image, maps the existing colors to the new ones, and writes a PNM color map defining them as output. </p>
<p> You can use this map as input to <code>pnmremap</code> on the same input image to quantize the colors in that image, I.e. produce a similar image with fewer colors. <code>pnmquant</code> does both the <code>pnmcolormap</code> and <code>pnmremap</code> steps for you. </p>
<p> A PNM colormap is a PNM image of any dimensions that contains at least one pixel of each color in the set of colors it represents. </p>
<p> The quantization method is Heckbert&#8217;s &quot;median cut&quot;. See the section QUANTIZATION METHOD. </p>
<p> If the input image is a PPM, the output image is a PPM. If the input image is a PBM or PGM, the output colormap is a PGM. Note that a colormap of a PBM image is not very interesting. </p>
<p> The colormap generally has the same maxval as the input image, but <code>pnmcolormap</code> may reduce it if there are too many colors in the input, as part of its quantization algorithm. </p>
<p> If you want to create a colormap without basing it on the colors in an input image, see <code>ppmcolors</code>. </p>
<h2>PARAMETERS</h2>
<p> The single parameter, which is required, is the number of colors you want in the output colormap. <code>pnmcolormap</code> may produce a color map with slightly fewer colors than that. You may specify <code>all</code> to get a colormap of every color in the input image (no quantization). </p>
<p> <code>OPTIONS</code></p>
<dl>
<dt><code>-sort</code></p>
<dd> This option causes the output colormap to be sorted by the red component intensity, then the green, then the blue in ascending order. This is an insertion sort, so it is not very fast on large colormaps. Sorting is useful because it allows you to compare two sets of colors.</p>
<dt><code>-square</code></p>
<dd> By default, <code>pnmcolormap</code> produces as the color map a PPM image with one row and one column for each color in the colormap. This option causes <code>pnmcolormap</code> instead to produce a PPM image that is within one row or column of being square, with multiple pixels of the same color as necessary to create a number of pixels which is a perfect square.</p>
<dt><code>-verbose</code></p>
<dd> This option causes <code>pnmcolormap</code> to display messages to Standard Error about the quantization.</p>
<dt><code>-center</code></p>
<dd>
<dt><code>-meancolor</code></p>
<dd>
<dt><code>-meanpixel</code></p>
<dd>
<dt><code>-spreadbrightness</code></p>
<dd>
<dt><code>-spreadluminosity</code></p>
<dd> These options control the quantization algorithm. See QUANTIZATION METHOD below. </p>
</dl>
<h2>QUANTIZATION METHOD</h2>
<p> A quantization method is a way to choose which colors, being fewer in number than in the input, you want in the output. <code>pnmcolormap</code> uses Heckbert&#8217;s &quot;median cut&quot; quantization method. </p>
<p> This method involves separating all the colors into &quot;boxes,&quot; each holding colors that represent about the same number of pixels. You start with one box and split boxes in two until the number of boxes is the same as the number of colors you want in the output, and choose one color to represent each box. </p>
<p> When you split a box, you do it so that all the colors in one sub-box are &quot;greater&quot; than all the colors in the other. &quot;Greater,&quot; for a particular box, means it is brighter in the color component (red, green, blue) which has the largest spread in that box. <code>pnmcolormap</code> gives you two ways to define &quot;largest spread.&quot;: 1) largest spread of brightness; 2) largest spread of contribution to the luminosity of the color. E.g. red is weighted much more than blue. Select among these with the <code>-spreadbrightness</code> and <code>-spreadluminosity</code> options. The default is <code>-spreadbrightness</code>. </p>
<p> <code>pnmcut</code> provides three ways of choosing a color to represent a box: 1) the center color &#8211; the color halfway between the greatest and least colors in the box, using the above definition of &quot;greater&quot;; 2) the mean of the colors (each component averaged separately by brightness) in the box; 3) the mean weighted by the number of pixels of a color in the image. </p>
<p> Note that in all three methods, there may be colors in the output which do not appear in the input at all. </p>
<p> Select among these with the <code>-center</code>, <code>-meancolor</code>, and <code>-meanpixel</code> options. The default is <code>-center</code>. </p>
<h2>REFERENCES</h2>
<p> &quot;Color Image Quantization for Frame Buffer Display&quot; by Paul Heckbert, SIGGRAPH &#8217;82 Proceedings, page 297. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pnmremap/">pnmremap</a></code>(1), <code><a href="/docs/linux/man/1-pnmquant/">pnmquant</a></code>(1), <code><a href="/docs/linux/man/1-ppmquantall/">ppmquantall</a></code>(1), <code><a href="/docs/linux/man/1-pnmdepth/">pnmdepth</a></code>(1), <code><a href="/docs/linux/man/1-ppmdither/">ppmdither</a></code>(1), <code><a href="/docs/linux/man/1-ppmquant/">ppmquant</a></code>(1), <code><a href="/docs/linux/man/5-ppm/">ppm</a></code>(5) </p>
<h2>AUTHOR</h2>
<p> Copyright (C) 1989, 1991 by Jef Poskanzer. Copyright (C) 2001 by Bryan Henderson. </p>
<h2>Index</h2>
