---
title: "ppmcie(1)"
name: "ppmcie"
section: "1"
letter: "p"
url: "/docs/linux/man/1-ppmcie/"
description: "ppmcie – draw a CIE color chart as a PPM image"
---

<h2 class="name">NAME</h2>
<p> ppmcie &#8211; draw a CIE color chart as a PPM image</p>
<h2>SYNOPSIS</h2>
<p> <code>ppmcie</code> [<code>-rec709</code>|<code>-cie</code>|<code>-ebu</code>|<code>-hdtv</code>|<code>-ntsc</code>|<code>-smpte</code>] [<code>-xy</code>|<code>-upvp</code>] [<code>-red</code> <i>rx</i> <i>ry</i>] [<code>-green</code> <i>gx</i> <i>gy</i>] [<code>-blue</code> <i>bx</i> <i>by</i>] [<code>-white</code> <i>wx</i> <i>wy</i>] [<code>-size</code> <i>edge</i>] [<code>-xsize</code>|<code>-width</code> <i>width</i>] [<code>-ysize</code>|<code>-height</code> <i>height</i>] [<code>-noblack</code>] [<code>-nowpoint</code>] [<code>-nolabel</code>] [<code>-noaxes</code>] [<code>-full</code>] </p>
<p> All options can be abbreviated to their shortest unique prefix. </p>
<h2>DESCRIPTION</h2>
<p> <code>ppmcie</code> creates a PPM file containing a plot of the CIE &#8220;tongue&#8221; color chart &#8212; to the extent possible in a PPM image. Alternatively, creates a pseudo-PPM image of the color tongue using RGB values from a color system of your choice. </p>
<p> The CIE color tongue is an image of all the hues that can be described by CIE X-Y chromaticity coordinates. They are arranged on a two dimensional coordinate plane with the X chromaticity on the horizontal axis and the Y chromaticity on the vertical scale. (You can choose alternatively to use CIE u&#8217;-v&#8217; chromaticity coordinates, but the general idea of the color tongue is the same). </p>
<p> Note that the PPM format specifies that the RGB values in the file are from CIE Rec. 709 color system, gamma-corrected. And positive. See <code><a href="/docs/linux/man/5-ppm/">ppm</a></code>(5) for details. If you use one of the color system options on <code>ppmcie</code>, what you get is not a true PPM image, but is very similar. If you display such <code>ppmcie</code> output using a device that expects PPM input (which includes just about any computer graphics display program), it will display the wrong colors. </p>
<p> However, you may have a device that expects one of these variations on PPM. </p>
<p> In every RGB color system you can specify, including the default (which produces a true PPM image) there are hues in the color tongue that can&#8217;t be represented. For example, monochromatic blue-green with a wavelength of 500nm cannot be represented in a PPM image. </p>
<p> For these hues, <code>ppmcie</code> substitutes a similar hue as follows: They are desaturated and rendered as the shade where the edge of the Maxwell triangle intersects a line drawn from the requested shade to the white point defined by the color system&#8217;s white point. Furthermore, unless you specify the <code>-full</code> option, <code>ppmcie</code> reduces their intensity by 25% compared to the true hues in the image. </p>
<p> <code>ppmcie</code> draws and labels the CIE X-Y coordinate axes unless you choose otherwise with options. </p>
<p> <code>ppmcie</code> draws the Maxwell triangle for the color system in use on the color tongue. The Maxwell triangle is the triangle whose vertices are the primary illuminant hues for the color system. The hues inside the triangle show the color gamut for the color system. They are also the only ones that are correct for the CIE X-Y chromaticity coordinates shown. (See explanation above). </p>
<p> <code>ppmcie</code> also places a mark at the color system&#8217;s white point and displays in text the CIE X-Y chromaticities of the primary illuminants and white point for the color system. You can turn this off with options, though. </p>
<p> <code>ppmcie</code> annotates the periphery of the color tongue with the wavelength, in nanometers of the monochromatic hues which appear there. </p>
<p> Finally, <code>ppmcie</code> displays the black body chromaticity curve for Planckian radiators from 1000 to 30000 kelvins on the image. </p>
<p> You can choose from several standard color systems, or specify one of your own numerically. </p>
<p> CIE charts, by their very nature, contain a very large number of colors. If you&#8217;re encoding the chart for a color mapped device or file format, you&#8217;ll need to use <code>ppmquant</code> or <code>ppmdither</code> to reduce the number of colors in the image. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-rec709</code>|<code>-cie</code>|<code>-ebu</code>|<code>-hdtv</code>|<code>-ntsc</code>|<code>-smpte</code></p>
<dd> Select a standard color system whose gamut to plot. The default is <code>-rec709</code>, which chooses CIE Rec. 709, gamma-corrected. This is the only color system for which <code>ppmcie</code>&#8216;s output is a true PPM image. See explanation above. <code>-ebu</code> chooses the primaries used in the PAL and SECAM broadcasting standards. <code>-ntsc</code> chooses the primaries specified by the NTSC broadcasting system (few modern monitors actually cover this range). <code>-smpte</code> selects the primaries recommended by the Society of Motion Picture and Television Engineers (SMPTE) in standards RP-37 and RP-145, and <code>-hdtv</code> uses the much broader <i>HDTV ideal</i> primaries. <code>-cie</code> chooses a color system that has the largest possible gamut within the spectrum of the chart. This is the same color system as you get with the <code>-cie</code> option to John Walker&#8217;s <code>cietoppm</code> program. </p>
<dt><code>-xy</code></p>
<dd> plot CIE 1931 x y chromaticities. This is the default.</p>
<dt><code>-upvp</code></p>
<dd> plot u&#8217; v&#8217; 1976 chromaticities rather than CIE 1931 x y chromaticities. The advantage of u&#8217; v&#8217; coordinates is that equal intervals of distance on the u&#8217; v&#8217; plane correspond roughly to the eye&#8217;s ability to discriminate colors.</p>
<dt><code>-red</code><i> rx ry</i></p>
<dd> specifies the CIE <i>x</i> and <i>y</i> co-ordinates of the red illuminant of a custom color system and selects the custom system.</p>
<dt><code>-green</code><i> gx gy</i></p>
<dd> specifies the CIE <i>x</i> and <i>y</i> co-ordinates of the green illuminant of the color system and selects the custom system.</p>
<dt><code>-blue</code><i> bx by</i></p>
<dd> specifies the CIE <i>x</i> and <i>y</i> co-ordinates of the blue illuminant of the color system and selects the custom system.</p>
<dt><code>-white</code><i> wx wy</i></p>
<dd> specifies the CIE <i>x</i> and <i>y</i> co-ordinates of the white point of the color system and selects the custom system.</p>
<dt><code>-size</code><i> edge</i></p>
<dd> Create a pixmap of <i>edge</i> by <i>edge</i> pixels. The default is 512&#215;512.</p>
<dt><code>-xsize|-width</code><i> width</i></p>
<dd> Sets the width of the generated image to <i>width</i> pixels. The default width is 512 pixels. If the height and width of the image are not the same, the CIE diagram will be stretched in the longer dimension.</p>
<dt><code>-ysize|-height</code><i> height</i></p>
<dd> Sets the height of the generated image to <i>height</i> pixels. The default height is 512 pixels. If the height and width of the image are not the same, the CIE diagram will be stretched in the longer dimension.</p>
<dt><code>-noblack</code></p>
<dd> Don&#8217;t plot the black body chromaticity curve.</p>
<dt><code>-nowpoint</code></p>
<dd> Don&#8217;t plot the color system&#8217;s white point.</p>
<dt><code>-nolabel</code></p>
<dd> Omit the label.</p>
<dt><code>-noaxes</code></p>
<dd> Don&#8217;t plot axes.</p>
<dt><code>-full</code></p>
<dd> Plot the entire CIE tongue in full intensity; don&#8217;t enhance the gamut of the specified color system. </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-ppmdither/">ppmdither</a></code>(1), <code><a href="/docs/linux/man/1-ppmquant/">ppmquant</a></code>(1), <code><a href="/docs/linux/man/5-ppm/">ppm</a></code>(5) </p>
<h2>AUTHOR</h2>
<p> <center> Copyright (C) 1995 by John Walker (kelvin [at] fourmilab.ch)<br />
 WWW home page: <a rel="nofollow" href="http://www.fourmilab.ch/">http://www.fourmilab.ch/</a><br />
 </center> </p>
<p> Permission to use, copy, modify, and distribute this software and its documentation for any purpose and without fee is hereby granted, without any conditions or restrictions. This software is provided &#8220;as is&#8221; without express or implied warranty. </p>
<h2>Index</h2>
