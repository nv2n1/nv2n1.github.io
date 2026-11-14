---
title: "pamtosvg(1)"
name: "pamtosvg"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pamtosvg/"
description: "pamtosvg – convert a Netpbm image to a SVG (Scalable Vector Graphics) image"
---

<h2 class="name">NAME</h2>
<p> pamtosvg &#8211; convert a Netpbm image to a SVG (Scalable Vector Graphics) image</p>
<h2>SYNOPSIS</h2>
<p> <code>pamtosvg</code> </p>
<p> [<code>-background-color=</code><i>colorname</i>] [<code>-centerline</code>] [<code>-corner-threshold=</code><i>angle</i>] [<code>-corner-always-threshold=</code><i>angle</i>] [<code>-corner-surround=</code><i>integer</i>] [<code>-tangent-surround=</code><i>integer</i>] [<code>-error-threshold=</code><i>float</i>] [<code>-filter-iterations=</code><i>count</i>] [<code>-line-reversion-threshold=</code><i>float</i>] [<code>-line-threshold=</code><i>float</i>] [<code>-width-weight-factor=</code><i>float</i>] [<code>-preserve-width</code>] [<code>-remove-adjacent-corners</code>] [<code>-log</code>] [<code>-report-progress</code>] [<i>pnmfile</i>] </p>
<p> Minimum unique abbreviation of option is acceptable. You may use double hyphens instead of single hyphen to denote options. You may use white space in place of the equals sign to separate an option name from its value. </p>
<h2>DESCRIPTION</h2>
<p> This program is part of <code><a href="/docs/linux/man/1-netpbm/">Netpbm</a></code>(1) </p>
<p> <code>pamtosvg</code> reads a PNM image as input and produce an SVG (Scalable Vector Graphics) image as output. Thus, it traces curves in the input image and creates a set of splines that represent the image. </p>
<p> SVG is a vector image format, which means it describes curves that compose an image. By contrast, PNM is a raster format, which means it describes dots that compose an image. The main practical difference between the two types is that you can scale vector images better. A vector image also takes a lot less data to describe an image if the image is composed of simple curves. </p>
<p> That means it is really an understatement to say that <code>pamtosvg</code> is an image format converter. It&#8217;s really an image tracer. Its main job is to trace a raster image and find the lines in it. It then represents its findings in SVG format. </p>
<p> <code>pamtosvg</code> does the same kind of thing that StreamLine, CorelTrace, and Autotrace do. It is in fact derived from Autotrace. </p>
<p> SVG is a gigantic format, capable of amazing things. <code>pamtosvg</code> exploits only a morsel of it. The SVG image produced by <code>pamtosvg</code> consists of a single &lt;svg&gt; element, which has a &#8216;width&#8217; attribute and a &#8216;height&#8217; attribute. The value of that element is composed of &lt;path&gt; elements. That&#8217;s it. </p>
<p> In the SVG output, distances are unitless, with one unit corresponding to one pixel of the input. </p>
<p> So that <code>pamtosvg</code> will find simple curves in the image, you may want to remove speckles from it with <code>pbmclean</code> and consolidate multiple shades into single colors with <code>pnmquant</code> first. </p>
<p> For more information on SVG, see the Worldwide Web Consortium&#8217;s SVG web page . </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-background-color=</code><i>colorname</i></p>
<dd> Treat the specified color as the background color and ignore it. </p>
<p> If you don&#8217;t specify this option, <code>pamtosvg</code> does not recognize any background color. </p>
<p> Specify the color (<i>colorname</i>) as described for the argument of the <code>ppm_parsecolor()</code> library routine . </p>
<dt><code>-centerline</code></p>
<dd> Trace an object&#8217;s centerline. </p>
<p> By default, <code>pamtosvg</code> traces an object&#8217;s outline. </p>
<dt><code>-corner-always-threshold=</code><i>angle</i></p>
<dd> Consider any angle at a pixel which falls below angle <i>angle</i> (in decimal floating point degrees) as a corner, even if it is bordered by other corner pixels. Default is 60 degrees. </p>
<dt><code>-corner-surround=</code><i>integer</i></p>
<dd> Consider the specified number of pixels on either side of a point when determining if that point is a corner. Default is 4. </p>
<dt><code>-corner-threshold=</code><i>angle</i></p>
<dd> Consider any pixel which forms an angle with its predecessors and successors that is smaller than <i>angle</i> (in decimal floating point degrees) as a corner. Default is 100. </p>
<dt><code>-error-threshold=</code><i>float</i></p>
<dd> Subdivide fitted curves that are offset by a number of pixels exceeding the specified number. Default is 2.0. </p>
<dt><code>-filter-iterations=</code><i>integer</i></p>
<dd> Smooth the curve the specified number of times prior to fitting Default is 4. </p>
<dt><code>-line-reversion-threshold=</code><i>float</i></p>
<dd> When a spline is closer to a straight line than the specified real number weighted by the square of the curve length, maintain it as a straight line, even if it is a list with curves. </p>
<p> Default is .01. </p>
<dt><code>-line-threshold=</code><i>float</i></p>
<dd> If a spline does not deviate from the straight line defined by its endpoints by more than the specified number of pixels, then treat it as a straight line. </p>
<p> Default is 1. </p>
<dt><code>-log</code></p>
<dd> Create a log of the curve tracing process (suitable for debugging). Put it in the file named <i>inputfile</i><code>.log</code> in the current directory, where <i>inputfile</i> is the root of the input file name, or &#8216;pamtosvg&#8217; if the input is from Standard Input or a file with a weird name. </p>
<dt><code>-preserve-width</code></p>
<dd> Preserve line width prior to thinning. Meaningful only with <code>-centerline</code>. </p>
<dt><code>remove-adjacent-corners</code></p>
<dd> Remove adjacent corners. </p>
<dt><code>-report-progress</code></p>
<dd> Report the progress of the tracing to Standard Error as it happens. </p>
<dt><code>-tangent-surround</code></p>
<dd> Consider the specified number of points to either side of a point when computing the tangent at that point. Default is 3. </p>
<dt><code>-width-weight-factor</code></p>
<dd> Weight factor for fitting the linewidth. </p>
</dl>
<h2>Application Notes</h2>
<p> A convenient way to view an SVG document is with a web browser. Many understand a file whose name ends in &#8216;.svg&#8217; to be an SVG image and can render it. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pnmquant/">pnmquant</a></code>(1) , <code><a href="/docs/linux/man/1-pbmclean/">pbmclean</a></code>(1) , <code><a href="/docs/linux/man/1-pnm/">pnm</a></code>(1) , Autotrace </p>
<h2>HISTORY</h2>
<p> <code>pamtosvg</code> was added to Netpbm in Version 10.33 (March 2006). </p>
<p> The core of <code>pamtosvg</code> &#8212; the curve tracing logic &#8212; was taken nearly unmodified from Martin Weber&#8217;s Autotrace program. That program duplicates a lot of Netpbm function, so <code>pamtosvg</code> is a much leaner program. </p>
<p> Bryan Henderson created <code>pamtosvg</code>, basically just by adapting Autotrace to Netpbm. </p>
<p> Autotrace was first released in 2000 and updates were released through 2002. A number of people wrote the code in it, but Masatake Yamato and Martin Weber appear to be the principal creators of it. </p>
<p> As of June 2006, there was a Sourceforge project for it. </p>
<h2>Index</h2>
