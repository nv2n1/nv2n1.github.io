---
title: "ppmchange(1)"
name: "ppmchange"
section: "1"
letter: "p"
url: "/docs/linux/man/1-ppmchange/"
description: "ppmchange – change all pixels of one color to another in a portable pixmap"
---

<h2 class="name">NAME</h2>
<p> ppmchange &#8211; change all pixels of one color to another in a portable pixmap </p>
<h2>SYNOPSIS</h2>
<p> <code>ppmchange</code> [ <code>-closeness </code><i>closeness_percent</i> ] [ <code>-remainder </code><i>remainder_color</i> ] [ <i>oldcolor newcolor</i> ] &#8230; [<i>ppmfile</i>] </p>
<h2>DESCRIPTION</h2>
<p> Reads a portable pixmap as input. Changes all pixels of <i>oldcolor </i> to <i>newcolor</i>. You may specify up to 256 oldcolor/newcolor pairs on the command line. <code>ppmchange</code> leaves all colors not mentioned unchanged, unless you specify the <code>-remainder</code> option, in which case they are all changed to the single specified color. </p>
<p> You can specify that colors similar, but not identical, to the ones you specify get replaced by specifying a &quot;closeness&quot; factor. </p>
<p> The colors can be specified in five ways:</p>
<dl>
<dt>o</p>
<dd> A name, assuming that a pointer to an X11-style color names file was compiled in.</p>
<dt>o</p>
<dd> An X11-style hexadecimal specifier: rgb:r/g/b, where r g and b are each 1- to 4-digit hexadecimal numbers.</p>
<dt>o</p>
<dd> An X11-style decimal specifier: rgbi:r/g/b, where r g and b are floating point numbers between 0 and 1.</p>
<dt>o</p>
<dd> For backwards compatibility, an old-X11-style hexadecimal number: #rgb, #rrggbb, #rrrgggbbb, or #rrrrggggbbbb.</p>
<dt>o</p>
<dd> For backwards compatibility, a triplet of numbers separated by commas: r,g,b, where r g and b are floating point numbers between 0 and 1. (This style was added before MIT came up with the similar rgbi style.) </p>
<p> If a pixel matches two different <i>oldcolor</i>s, <code>ppmchange</code> replaces it with the <i>newcolor</i> of the leftmost specified one. </p>
</dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>-closeness </code><i>closeness_percent</i></p>
<dd> <i>closeness</i> is an integer per centage indicating how close to the color you specified a pixel must be to get replaced. By default, it is 0, which means the pixel must be the exact color you specified. </p>
<p> A pixel gets replaced if the distance in color between it and the color you specified is less than or equal to <i>closeness</i>. </p>
<p> The &quot;distance&quot; in color is defined as the cartesian sum of the individual differences in red, green, and blue intensities between the two pixels, normalized so that the difference between black and white is 100%. </p>
<p> This is probably simpler than what you want most the time. You probably would like to change colors that have similar chrominance, regardless of their intensity. So if there&#8217;s a red barn that is variously shadowed, you want the entire barn changed. But because the shadowing significantly changes the color according to <code>ppmchange</code>&#8216;s distance formula, parts of the barn are probably about as distant in color from other parts of the barn as they are from green grass next to the barn. </p>
<p> Maybe <code>ppmchange</code> will be enhanced some day to do chrominance analysis. </p>
<dt><code>-remainder </code><i>color</i></p>
<dd> <code>ppmchange</code> changes all pixels which are not of a color for which you specify an explicit replacement color on the command line to color <i>color</i>. </p>
<p> An example application of this is </p>
<p> <code>ppmchange -remainder=black red red</code> </p>
<p> to lift only the red portions from an image, or </p>
<p> <code>ppmchange -remainder=black red white | ppmtopgm</code> </p>
<p> to create a mask file for the red portions of the image. </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pgmtoppm/">pgmtoppm</a></code>(1), <code><a href="/docs/linux/man/1-ppmcolormask/">ppmcolormask</a></code>(1), <code><a href="/docs/linux/man/5-ppm/">ppm</a></code>(5) </p>
<h2>AUTHOR</h2>
<p> Wilson H. Bent. Jr. (whb [at] usc.edu) with modifications by Alberto Accomazzi (alberto [at] cfa.harvard.edu) </p>
<h2>Index</h2>
