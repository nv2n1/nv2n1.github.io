---
title: "psimage(1)"
name: "psimage"
section: "1"
letter: "p"
url: "/docs/linux/man/1-psimage/"
description: "psimage – Place images or EPS files on maps"
---

<h2>NAME</h2>
<p> psimage &#8211; Place images or EPS files on maps</p>
<h2>SYNOPSIS</h2>
<p> <code>psimage</code> <i>imagefile</i> [ <i>refpoint</i> ] [ <i>box</i> ] [ [<code>b</code>|<code>f</code>|<code>t</code>]<i>color</i> ] [ ] [ <i>parameters</i> ] [ <code>z</code>|<code>Z</code><i>parameters</i> ] [ ] [ ] [ ] [ ] [ <i>west</i>/<i>east</i>/<i>south</i>/<i>north</i>[/<i>zmin</i>/<i>zmax</i>][<code>r</code>] ] [ [<i>just</i>/<i>dx</i>/<i>dy</i>/][<code>c</code>|<i>label</i>] ] [ [<i>level</i>] ] [ <i>x_offset</i> ] [ <i>y_offset</i> ] [ <code>-c</code><i>copies</i> ] [ <code>-p</code><i>&lt;flags&gt;</i> ] [ <code>-t</code><i>&lt;transp&gt;</i> ] </p>
<p> <code>Note:</code> No space is allowed between the option flag and the associated arguments.</p>
<h2>DESCRIPTION</h2>
<p> <code>psimage</code> reads an Encapsulated PostScript file or a raster image file and plots it on a map. The image can be scaled arbitrarily, and 1-bit raster images can be (1) inverted, i.e., black pixels (on) becomes white (off) and vice versa, or (2) colorized, by assigning different foreground and background colors, and (3) made transparent where one of back- or foreground is painted only. As an option, the user may choose to convert colored raster images to grayscale using TV&#8217;s YIQ-transformation. For raster files, the user can select which color to be made transparent. The user may also choose to replicate the image which, when preceded by appropriate clip paths, may allow larger custom-designed fill patterns to be implemented (the <code>-Gp</code> mechanism offered in most GMT programs is limited to rasters smaller than 146 by 146).</p>
<h2>REQUIRED ARGUMENTS</h2>
<dl>
<dt><i>imagefile</i></p>
<dd> This must be an Encapsulated PostScript (EPS) file or a raster image. An EPS file must contain an appropriate BoundingBox. A raster file can have a depth of 1, 8, 24, or 32 bits and is read via GDAL. Note: If GDAL was not configured during GMT installation then only Sun raster files are supported natively. You must then convert other formats to Sun raster files before use.</dl>
<h2>OPTIONAL ARGUMENTS</h2>
<dl>
<dt><code>-D</code>[<code>g</code>|<code>j</code>|<code>J</code>|<code>n</code>|<code>x</code>]<i>refpoint</i><code>+e</code><i>dpi</i><code>+w</code>[<code>&#8211;</code>]<i>width</i>[/<i>height</i>][<code>+j</code><i>justify</i>][<code>+n</code><i>nx</i>[/<i>ny</i>] ][<code>+o</code><i>dx</i>[/<i>dy</i>]]</p>
<dd> Sets reference point on the map for the image using one of four coordinate systems: (1) Use <code>-Dg</code> for map (user) coordinates, (2) use <code>-Dj</code> or <code>-DJ</code> for setting <i>refpoint</i> via a 2-char justification code that refers to the (invisible) map domain rectangle, (3) use <code>-Dn</code> for normalized (0-1) coordinates, or (4) use <code>-Dx</code> for plot coordinates (inches, cm, etc.). All but <code>-Dx</code> requires both <code>-R</code> and <code>-J</code> to be specified. By default, the anchor point on the scale is assumed to be the bottom left corner (BL), but this can be changed by appending <code>+j</code> followed by a 2-char justification code <i>justify</i> (see <code>pstext</code>). Note: If <code>-Dj</code> is used then <i>justify</i> defaults to the same as <i>refpoint</i>, if <code>-DJ</code> is used then <i>justify</i> defaults to the mirror opposite of <i>refpoint</i>. Add <code>+o</code> to offset the color scale by <i>dx</i>/<i>dy</i> away from the <i>refpoint</i> point in the direction implied by <i>justify</i> (or the direction implied by <code>-Dj</code> or <code>-DJ</code>). Specify image size in one of two ways: Use <code>+e</code><i>dpi</i> to set the dpi of the image in dots per inch, or use <code>+w</code>[<code>&#8211;</code>]<i>width</i>[/<i>height</i>] to set the width (and height) of the image in plot coordinates (inches, cm, etc.). If <i>height</i> is not given, the original aspect ratio of the image is maintained. If <i>width</i> is negative we use the absolute value and interpolate image to the device resolution using the PostScript image operator. Optionally, use <code>+n</code><i>nx</i>[/<i>ny</i>] to replicate the image <i>nx</i> times horizontally and <i>ny</i> times vertically. If <i>ny</i> is omitted, it will be identical to <i>nx</i> [Default is 1/1].</p>
<dt><code>-F</code>[<code>+c</code><i>clearances</i>][<code>+g</code><i>fill</i>][<code>+i</code>[[<i>gap</i>/]<i>pen</i>]][<code>+p</code>[<i>pen</i>]][<code>+r</code>[<i>radius</i>]][<code>+s</code>[[<i>dx</i>/<i>dy</i>/][<i>shade</i>]]]</p>
<dd> Without further options, draws a rectangular border around the image using <code>MAP_FRAME_PEN</code>; specify a different pen with <code>+p</code><i>pen</i>. Add <code>+g</code><i>fill</i> to fill the image box [no fill]. Append <code>+c</code><i>clearance</i> where <i>clearance</i> is either <i>gap</i>, <i>xgap</i>/<i>ygap</i>, or <i>lgap</i>/<i>rgap</i>/<i>bgap</i>/<i>tgap</i> where these items are uniform, separate in x- and y-direction, or individual side spacings between scale and border. Append <code>+i</code> to draw a secondary, inner border as well. We use a uniform <i>gap</i> between borders of 2<code>p</code> and the <code>MAP_DEFAULTS_PEN</code> unless other values are specified. Append <code>+r</code> to draw rounded rectangular borders instead, with a 6<code>p</code> corner radius. You can override this radius by appending another value. Finally, append <code>+s</code> to draw an offset background shaded region. Here, <i>dx</i>/<i>dy</i> indicates the shift relative to the foreground frame [4<code>p</code>/-4<code>p</code>] and <i>shade</i> sets the fill style to use for shading [gray50].</p>
<dt><code>-J</code><i>parameters</i> <i>(more &#8230;)</i></p>
<dd> Select map projection. (Used only with <code>-p</code>)</p>
<dt><code>-Jz</code>|<code>Z</code><i>parameters</i> <i>(more &#8230;)</i></p>
<dd> Set z-axis scaling; same syntax as <code>-Jx</code>.</p>
<dt><code>-K</code> <i>(more &#8230;)</i></p>
<dd> Do not finalize the PostScript plot.</p>
<dt><code>-M</code></p>
<dd> Convert color image to monochrome grayshades using the (television) YIQ-transformation.</p>
<dt><code>-O</code> <i>(more &#8230;)</i></p>
<dd> Append to existing PostScript plot.</p>
<dt><code>-P</code> <i>(more &#8230;)</i></p>
<dd> Select &quot;Portrait&quot; plot orientation.</p>
<dt><code>-R</code>[<i>unit</i>]<i>xmin</i>/<i>xmax</i>/<i>ymin</i>/<i>ymax</i>[<code>r</code>] <i>(more &#8230;)</i></p>
<dd> Specify the region of interest. (Used only with <code>-p</code>) </p>
<p> For perspective view <code>p</code>, optionally append /<i>zmin</i>/<i>zmax</i>. <i>(more &#8230;)</i></p>
<dt><code>-U</code>[<i>just</i>/<i>dx</i>/<i>dy</i>/][<code>c</code>|<i>label</i>] <i>(more &#8230;)</i></p>
<dd> Draw GMT time stamp logo on plot.</p>
<dt><code>-V</code>[<i>level</i>] <i>(more &#8230;)</i></p>
<dd> Select verbosity level [c]. </p>
<p> <code>-X</code>[<code>a</code>|<code>c</code>|<code>f</code>|<code>r</code>][<i>x-shift</i>[<code>u</code>]]</p>
<dt><code>-Y</code>[<code>a</code>|<code>c</code>|<code>f</code>|<code>r</code>][<i>y-shift</i>[<code>u</code>]] <i>(more &#8230;)</i></p>
<dd> Shift plot origin.</p>
<dt><code>-c</code><i>copies</i> <i>(more &#8230;)</i></p>
<dd> Specify number of plot copies [Default is 1]. </p>
<p> These options are for 1-bit images only. They have no effect when plotting other images or PostScript files.</p>
<dt><code>-G</code>[<code>b</code>|<code>f</code>|<code>t</code>]<i>color</i></p>
<dd>
<dt><code>-Gb</code></p>
<dd> Sets background color (replace white pixel) of 1-bit images. Use &#8211; for transparency (and set <code>-Gf</code> to the desired color).</p>
<dt><code>-Gf</code></p>
<dd> Sets foreground color (replace black pixel) of 1-bit images. Use &#8211; for transparency (and set <code>-Gb</code> to the desired color).</p>
<dt><code>-I</code></p>
<dd> Invert 1-bit image before plotting. This is what is done when you use <code>-GP</code> in other GMT programs. </p>
<p> These options are for 8-, 24-, and 32-bit raster images only. They have no effect when plotting 1-bit images or PostScript files.</p>
<dt><code>-Gt</code></p>
<dd> Assigns the color that is to be made transparent. Sun Raster files do not support transparency, so indicate here which color to be made transparent.</p>
<dt><code>-p</code>[<code>x</code>|<code>y</code>|<code>z</code>]<i>azim</i>/<i>elev</i>[/<i>zlevel</i>][<code>+w</code><i>lon0</i>/<i>lat0</i>[/<i>z0</i>]][<code>+v</code><i>x0</i>/<i>y0</i>] <i>(more &#8230;)</i></p>
<dd> Select perspective view. (Requires <code>-R</code> and <code>-J</code> for proper functioning).</p>
<dt><code>-t</code>[<i>transp</i>] <i>(more &#8230;)</i></p>
<dd> Set PDF transparency level in percent.</p>
<dt><code>-^</code> or just <code>&#8211;</code></p>
<dd> Print a short message about the syntax of the command, then exits (NOTE: on Windows use just <code>&#8211;</code>).</p>
<dt><code>-+</code> or just <code>+</code></p>
<dd> Print an extensive usage (help) message, including the explanation of any module-specific option (but not the GMT common options), then exits.</p>
<dt><code>-?</code> or no arguments</p>
<dd> Print a complete usage (help) message, including the explanation of options, then exits.</p>
<dt><code>&#8211;</code><code>-version</code></p>
<dd> Print GMT version and exit.</p>
<dt><code>&#8211;</code><code>-show-datadir</code></p>
<dd> Print full path to GMT share directory and exit. </p>
<p> <code>gmt</code>, <code>pslegend</code>, To plot the image logo.jpg, scaling it be 1 inch wide (height is scaled accordingly), and outline with a thin, blue pen, use </p>
<pre>
gmt psimage logo.jpg -Dx0/0+w1i -F+pthin,blue &gt; image.ps
</pre>
<p> To include an Encapsulated PostScript file tiger.eps with its upper right corner 2 inch to the right and 1 inch up from the current location, and have its width scaled to 3 inches, while keeping the aspect ratio, use </p>
<pre>
gmt psimage tiger.eps -Dx2i/1i+jTR+w3i &gt; image.ps
</pre>
<p> To replicate the 1-bit raster image template 1_bit.ras, colorize it (brown background and red foreground), and setting each of 5 by 5 tiles to be 1 cm wide, use </p>
<pre>
gmt psimage 1_bit.ras -Gbbrown -Gfred -Dx0/0+w1c+n5 &gt; image.ps
</pre>
</dl>
<h2>SEE ALSO</h2>
<p> <code>gmt</code>, <code>gmtcolors</code>, <code>gmtlogo</code> <code>pslegend</code>, <code>psscale</code> <code>psxy</code>, <i><a href="/docs/linux/man/1-convert/">convert</a>(1)</i></p>
<h2>COPYRIGHT</h2>
<p> 2015, P. Wessel, W. H. F. Smith, R. Scharroo, J. Luis, and F. Wobbe </p>
<h2>Index</h2>
