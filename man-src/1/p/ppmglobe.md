---
title: "ppmglobe(1)"
name: "ppmglobe"
section: "1"
letter: "p"
url: "/docs/linux/man/1-ppmglobe/"
description: "ppmglobe – generate strips to glue onto a sphere"
---

<h2 class="name">NAME</h2>
<p> ppmglobe &#8211; generate strips to glue onto a sphere</p>
<h2>SYNOPSIS</h2>
<p> <code>ppmglobe</code> [<code>-background=</code><i>colorname</i>] [<code>-closeok</code>] <i>stripcount</i> [<i>filename</i>] </p>
<p> Minimum unique abbreviation of option is acceptable. You may use double hyphens instead of single hyphen to denote options. You may use white space in place of the equals sign to separate an option name from its value. </p>
<h2>DESCRIPTION</h2>
<p> This program is part of <code><a href="/docs/linux/man/1-netpbm/">Netpbm</a></code>(1) </p>
<p> <code>ppmglobe</code> does the inverse of a cylindrical projection of a sphere. Starting with a cylindrical projection, it produces an image you can cut up and glue onto a sphere to obtain the spherical image of which it is the cylindrical projection. </p>
<p> What is a cylindrical projection? Imagine a map of the Earth on flat paper. There are lots of different ways cartographers show the three dimensional information in such a two dimensional map. The cylindrical projection is one. You could make a cylindrical projection by tracing as folows: wrap a rectangular sheet of paper around the globe, touching the globe at the Equator. For each point of color on the globe, run a horizontal line from the axis of the globe through that point and out to the paper. Mark the same color on the paper there. Lay the paper out flat and you have a cylindrical projection. </p>
<p> Here&#8217;s where <code>ppmglobe</code> comes in: Pass the image on that paper through <code>ppmglobe</code> and what comes out the other side looks something like this: </p>
<p> <code>Example of map of the earth run through ppmglobe</code> </p>
<p> You could cut out the strips and glue it onto a sphere and you&#8217;d have a copy of the original globe. </p>
<p> Note that cylindrical projections are not what you normally see as maps of the Earth. You&#8217;re more likely to see a Mercator projection. In the Mercator projection, the Earth gets stretched North-South as well as East-West as you move away from the Equator. It was invented for use in navigation, because you can draw straight compass courses on it, but is used today because it is pretty. </p>
<p> You can find maps of planets at maps.jpl.nasa.gov . </p>
<h2>PARAMETERS</h2>
<p> <i>stripcount</i> is the number of strips <code>ppmglobe</code> is to generate in the output. More strips makes it easier to fit onto a sphere (less stretching, tearing, and crumpling of paper), but makes you do more cutting out of the strips. </p>
<p> The strips are all the same width. If the number of columns of pixels in the image doesn&#8217;t evenly divide by the number of strips, <code>ppmglobe</code> truncates the image on the right to create nothing but whole strips. In the pathological case that there are fewer columns of pixels than the number of strips you asked for, <code>ppmglobe</code> fails. </p>
<p> Before Netpbm 10.32 (February 2006), instead of truncating the image on the right, <code>ppmglobe</code> produces a fractional strip on the right. </p>
<p> <i>filename</i> is the name of the input file. If you don&#8217;t specify this, <code>ppmglobe</code> reads the image from Standard Input. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-background=</code><i>colorname</i></p>
<dd> This specifies the color that goes between the strips. </p>
<p> Specify the color (<i>color</i>) as described for the argument of the <code>ppm_parsecolor()</code> library routine . </p>
<p> The default is black. </p>
<p> This option was new in Netpbm 10.31 (December 2005). Before that, the background is always black. </p>
<dt><code>-closeok</code></p>
<dd> This means it is OK if the background isn&#8217;t exactly the color you specify. Sometimes, it is impossible to represent a named color exactly due to the precision (i.e. maxval) of the image&#8217;s color space. If you specify <code>-closeok</code> and <code>ppmglobe</code> can&#8217;t represent the color you name exactly, it will use instead the closest color to it that is possible. If you don&#8217;t specify <code>closeok</code>, <code>ppmglobe</code> fails in that situation. </p>
<p> This option was new in Netpbm 10.31 (December 2005). </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-ppm/">ppm</a></code>(1) </p>
<p> <code><a href="/docs/linux/man/1-pnmmercator/">pnmmercator</a></code>(1) </p>
<h2>HISTORY</h2>
<p> <code>ppmglobe</code> was new in Netpbm 10.16 (June 2003). </p>
<p> It is derived from Max Gensthaler&#8217;s <code>ppmglobemap</code>. </p>
<h2>AUTHORS</h2>
<p> <i>Max Gensthaler</i> wrote a program he called <code>ppmglobemap</code> in June 2003 and suggested it for inclusion in Netpbm. Bryan Henderson modified the code slightly and included it in Netpbm as <code>ppmglobe</code>. </p>
<h2>Index</h2>
