---
title: "pnmcomp(1)"
name: "pnmcomp"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pnmcomp/"
description: "pnmcomp – composite (overlay) two portable anymap files together"
---

<h2 class="name">NAME</h2>
<p> pnmcomp &#8211; composite (overlay) two portable anymap files together </p>
<h2>SYNOPSIS</h2>
<p> <code>pnmcomp</code> [<code>-xoff=</code><i>X</i> | <code>-align=</code>{<code>left</code>,<code>center</code>,<code>right</code>}]<br />
 [<code>-yoff=</code><i>Y</i> | <code>-valign=</code>{<code>top</code>,<code>middle</code>,<code>bottom</code>}]<br />
 [<code>-alpha=</code><i>alpha-pgmfile</i>] [<code>-invert</code>]<br />
 <i>overlay</i> [<i>pnm-input</i>] [<i>pnm-output</i>] </p>
<p> Minimum unique abbreviations are acceptable. </p>
<h2>DESCRIPTION</h2>
<p> <code>pnmcomp</code> reads two images and produces a composite image with one of the images overlayed on top of the other. The images need not be the same size. The input and outputs are PNM format image files. </p>
<p> In its simplest use, <code>pnmcomp</code> simply places the <i>overlay</i> file on top of the <i>pnm-input</i> file, blocking out the part of the <i>pnm-input</i> file beneath it. If you specify the <i>alpha-pgmfile</i>, <code>pnmcomp</code> uses it as an alpha mask, which means it determines the level of transparency of each point in the overlay image. The alpha mask must have the same dimensions as the overlay image. In places where the alpha mask defines the overlay image to be opaque, the composite output contains only the contents of the overlay image; the underlying image is totally blocked out. In places where the alpha mask defines the overlay image to be transparent, the composite output contains none of the overlay image; the underlying image shows through completely. In places where the alpha mask shows a value in between opaque and transparent (translucence), the composite image contains a mixture of the overlay image and the underlying image and the level of translucence determines how much of each. </p>
<p> The alpha mask is a PGM file in which a white pixel represents opaqueness and a black pixel transparency. Anything in between is translucent. </p>
<p> In some image file formats (PNG, for example), transparency information (the alpha mask) is part of the definition of the image. In the PNM formats, transparency is always embodied in a separate companion file. The PNM converter programs that convert from an image format such as PNG have options that allow you to extract the transparency information to a separate file, which you can then use as input to <code>pnmcomp</code>. </p>
<p> The output image is always of the same dimensions as the underlying image. <code>pnmcomp</code> only uses parts of the overlay image that fit within the underlying image. </p>
<p> To specify where on the underlying image to place the overlay image, use the <code>-xoff</code>, <code>-yoff</code>, <code>-align</code>, and <code>-valign</code> options. Without these options, the default horizontal position is flush left and the default vertical position is flush top. </p>
<p> The overlay and underlying images may be of different formats (e.g. overlaying a PBM text image over a full color PPM image) and have different maxvals. The output image has the more general of the two input formats and a maxval that is the least common multiple the two maxvals (or the maximum maxval allowable by the format, if the LCM is more than that). </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-invert</code></p>
<dd> This option inverts the sense of the values in the alpha mask, which effectively switches the roles of the overlay image and the underlying image in places where the two intersect.</p>
<dt><code>-xoff </code><i>X</i></p>
<dd>
<dt><code>-yoff </code><i>Y</i></p>
<dd> These options position the overlay image with respect to the underlying image. <i>X</i> and <i>Y</i> are the horizontal and vertical displacements of the top left corner of the overlay image from the top left corner of the underlying image, in pixels. A positive value means right or down; a negative value means left or up. The overlay need not fit entirely (or at all) on the underlying image. <code>pnmcomp</code> uses only the parts that lie over the underlying image.</p>
<dt><code>-align=</code>[<code>left</code>,<code>center</code>,<code>right</code>]</p>
<dd> This option is an alternative to <code>-xoff</code>, in the style of HTML. It selects the horizontal position of the overlay image so that it is flush left, centered, or flush right on the underlying image.</p>
<dt><code>-valign=</code>[<code>top</code>,<code>middle</code>,<code>bottom</code>]</p>
<dd> This option is an alternative to <code>-yoff</code>, in the style of HTML. It selects the vertical position of the overlay image so that it is flush top, centered, or flush bottom on the underlying image. </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-ppmmix/">ppmmix</a></code>(1) and <code><a href="/docs/linux/man/1-pnmpaste/">pnmpaste</a></code>(1) are simpler, less general versions of the same tool. </p>
<p> <code><a href="/docs/linux/man/5-pnm/">pnm</a></code>(5), <code><a href="/docs/linux/man/1-pbmmask/">pbmmask</a></code>(1)</p>
<h2>AUTHOR</h2>
<p> Copyright (C) 1992 by David Koblas (koblas [at] mips.com). </p>
<h2>Index</h2>
