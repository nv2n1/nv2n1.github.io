---
title: "pnmscale(1)"
name: "pnmscale"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pnmscale/"
description: "pnmscale – scale a portable anymap"
---

<h2 class="name">NAME</h2>
<p> pnmscale &#8211; scale a portable anymap </p>
<h2>SYNOPSIS</h2>
<p> <code>pnmscale</code> <i>scale_factor</i> [<i>pnmfile</i>]<br />
 <code>pnmscale -reduce</code> <i>reduction_factor</i> [<i>pnmfile</i>]<br />
 <code>pnmscale</code> [{<code>-xsize=</code><i>cols</i> | <code>-width=</code><i>cols</i> | <code>-xscale=</code><i>factor</i>}] [{<code>-ysize=</code><i>rows</i> | <code>-height=</code><i>rows</i> | <code>-yscale=</code><i>factor</i>}] [<i>pnmfile</i>]<br />
 <code>pnmscale -xysize</code> <i>cols rows</i> [<i>pnmfile</i>]<br />
 <code>pnmscale -pixels</code> <i>n</i> [<i>pnmfile</i>] </p>
<p> Miscellaneous options:<br />
 <code>-verbose -nomix</code> </p>
<p> Minimum unique abbreviation of option is acceptable. You may use double hypens instead of single hyphen to denote options. You may use white space in place of the equals sign to separate an option name from its value. </p>
<h2>DESCRIPTION</h2>
<p> Reads a PBM, PGM, or PPM image as input, scales it by the specified factor or factors and produces a PGM or PPM image as output. If the input file is in color (PPM), the output will be too, otherwise it will be grayscale (PGM). This is true even if the input is a black and white bitmap (PBM), because the process of scaling can turn a combination of black and white pixels into a gray pixel. </p>
<p> If you want PBM output, use <code>pgmtopbm</code> to convert <code>pnmscale</code>&#8216;s output to PBM. Also consider <code>pbmreduce</code>. </p>
<p> You can both enlarge (scale factor &gt; 1) and reduce (scale factor &lt; 1). </p>
<p> When you specify an absolute size or scale factor for both dimensions, <code>pnmscale</code> scales each dimension independently without consideration of the aspect ratio. </p>
<p> If you specify one dimension as a pixel size and don&#8217;t specify the other dimension, <code>pnmscale</code> scales the unspecified dimension to preserve the aspect ratio. </p>
<p> If you specify one dimension as a scale factor and don&#8217;t specify the other dimension, <code>pnmscale</code> leaves the unspecified dimension unchanged from the input. </p>
<p> If you specify the <i>scale_factor</i> parameter instead of dimension options, that is the scale factor for both dimensions. It is equivalent to <code>-xscale=</code><i>scale_factor</i><code> -yscale=</code><i>scale_factor</i> . </p>
<p> Specifying the <code>-reduce</code> <i>reduction_factor</i> option is equivalent to specifying the <i>scale_factor </i> parameter, where <i>scale_factor</i> is the reciprocal of <i>reduction_factor</i>. </p>
<p> <code>-xysize</code> specifies a bounding box. <code>pnmscale</code> scales the input image to the largest size that fits within the box, while preserving its aspect ratio. </p>
<p> <code>-pixels</code> specifies a maximum total number of output pixels. <code>pnmscale</code> scales the image down to that number of pixels. If the input image is already no more than that many pixels, <code>pnmscale</code> just copies it as output; <code>pnmscale</code> does not scale up with <code>-pixels</code>. </p>
<p> If you enlarge by a factor of 3 or more, you should probably add a <i>pnmsmooth</i> step; otherwise, you can see the original pixels in the resulting image. </p>
<p> When the scale factor is not an integer (including all cases of scaling down), there are two ways to do the scaling. Which one <code>pnmscale </code> does is controlled by its <code>-nomix</code> option. </p>
<p> By default, <code>pnmscale</code> mixes the colors of adjacent pixels to produce output pixels that contain information from multiple input pixels. This makes the image look more like it would if it had infinite resolution. Note that it means the output may contain colors that aren&#8217;t in the input at all. </p>
<p> But if you specify <code>-nomix</code>, <code>pnmscale</code> never mixes pixels. Each output pixel is derived from one input pixel. If you&#8217;re scaling up, pixels get duplicated. If you&#8217;re scaling down, pixels get omitted. Note that this means the image is rather distorted. If you scale up by 1.5 horizontally, for example, the even numbered input pixels are doubled in the output and the odd numbered ones are copied singly. </p>
<p> When the scale factor is an integer (which means you&#8217;re scaling up), the <code>-nomix</code> option has no effect &#8212; output pixels are always just N copies of the input pixels. In this case, though, consider using <code>pamstretch</code> instead of <code>pnmscale</code> to get the added pixels interpolated instead of just copied and thereby get a smoother enlargement. </p>
<p> <code>pnmscale </code> with <code>-nomix</code> is faster than without, but <code>pnmenlarge</code> is faster still. <code>pnmenlarge</code> works only on integer enlargements. </p>
<p> A useful application of <code>pnmscale</code> is to blur an image. Scale it down (without <code>-nomix )</code> to discard some information, then scale it back up using <code>pamstretch</code>. </p>
<p> Or scale it back up with <code>pnmscale</code> and create a &quot;pixelized&quot; image, which is sort of a computer-age version of blurring. </p>
<h3>PRECISION</h3>
<p> <code>pnmscale </code> uses floating point arithmetic internally. There is a speed cost associated with this. For some images, you can get the acceptable results (in fact, sometimes identical results) faster with <code>pnmscalefixed</code>, which uses fixed point arithmetic. <code>pnmscalefixed</code> may, however, distort your image a little. See <code>pnmscalefixed</code>&#8216;s man page for a complete discussion of the difference. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pnmscalefixed/">pnmscalefixed</a></code>(1), <code><a href="/docs/linux/man/1-pamstretch/">pamstretch</a></code>(1), <code><a href="/docs/linux/man/1-pbmreduce/">pbmreduce</a></code>(1), <code><a href="/docs/linux/man/1-pnmenlarge/">pnmenlarge</a></code>(1), <code><a href="/docs/linux/man/1-pnmsmooth/">pnmsmooth</a></code>(1), <code><a href="/docs/linux/man/1-pnmcut/">pnmcut</a></code>(1), <code><a href="/docs/linux/man/5-pnm/">pnm</a>(5)</code> </p>
<h2>AUTHOR</h2>
<p> Copyright (C) 1989, 1991 by Jef Poskanzer. </p>
<h2>Index</h2>
