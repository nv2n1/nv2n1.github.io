---
title: "gimpsvg(1)"
name: "gimpsvg"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gimpsvg/"
description: "gimpsvg – convert a GIMP gradient (ggr) to the SVG format."
---

<h2 class="name">NAME</h2>
<p> gimpsvg &#8211; convert a GIMP gradient (ggr) to the SVG format. </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>gimpsvg</code> [-g&nbsp;<wbr><i>geometry</i>] [-h] [-o&nbsp;<wbr><i>file</i>] [-p] [-s&nbsp;<wbr><i>samples</i>] [-v] [-V] [<i>file</i>]</dl>
<h2>DESCRIPTION</h2>
<dd>The <code>gimpsvg</code> utility converts gradient files from the <code><a href="/docs/linux/man/1-gimp/">GIMP</a></code>(1), the GNU Image Manipulation Program, to the SVG (scalar vector graphics) format. </p>
<p> The program will read from stdin if a file is not specified as the final argument, and write to stdout if the <code>-o</code> option is not specified. </p>
<p> The output is formatted for machines to read, rather than humans. A post-processor such as <code><a href="/docs/linux/man/1-tidy/">tidy</a></code>(1) could be used in the latter case.</p>
<h2>OPTIONS</h2>
<p> <code>-g</code>, <code>&#8211;geometry</code> <i>width</i>x<i>height</i></p>
<dl>
<dt>
<dd> Specify the size of the SVG preview in pixels.</dl>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Brief help.</dl>
<p> <code>-o</code>, <code>&#8211;output</code> <i>file</i></p>
<dl>
<dt>
<dd> Write the output to <i>file</i>, rather than stdout.</dl>
<p> <code>-p</code>, <code>&#8211;preview</code></p>
<dl>
<dt>
<dd> Include a preview in the SVG output. See also the <code>&#8211;geometry</code> option.</dl>
<p> <code>-s</code>, <code>&#8211;samples</code> <i>number</i></p>
<dl>
<dt>
<dd> Specify the maximum <i>number</i> of samples. <code>GIMP</code> gradients allow for complex curves in a number of colour-space co-ordinate systems. In order that these can be converted into SVG&#8217;s simple RGB linear splines we must sample these complex curves quite densely. The <code>-s</code> option specifies (roughly) the maximum number of samples. In the case that the GIMP gradient is an RGB linear spline gradient the option has no effect, since we can then convert the segments without loss.</dl>
<p> <code>-v</code>, <code>&#8211;verbose</code></p>
<dl>
<dt>
<dd> Verbose operation.</dl>
<p> <code>-V</code>, <code>&#8211;version</code></p>
<dl>
<dt>
<dd> Version information.</dl>
<h2>AUTHOR</h2>
<p> J.J. Green</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-gimp/">GIMP</a></code>(1), <code><a href="/docs/linux/man/1-tidy/">tidy</a></code>(1), <code><a href="/docs/linux/man/1-svggimp/">svggimp</a></code>(1). </p>
<h2>Index</h2>
