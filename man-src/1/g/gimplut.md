---
title: "gimplut(1)"
name: "gimplut"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gimplut/"
description: "gimplut – convert GIMP gradient (ggr) files to binary lookup tables (lut)."
---

<h2 class="name">NAME</h2>
<p> gimplut &#8211; convert GIMP gradient (ggr) files to binary lookup tables (lut). </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>gimplut</code> [-h] [-o&nbsp;<wbr><i>file</i>] [-s&nbsp;<wbr><i>samples</i>] [-v] [-V] [<i>file</i>]</dl>
<h2>DESCRIPTION</h2>
<dd>The <code>gimplut</code> utility converts gradient files from the <code><a href="/docs/linux/man/1-gimp/">GIMP</a></code>(1), the GNU Image Manipulation Program, to a binary lookup table format commonly used by medical imaging software; in particular the <code><a href="/docs/linux/man/1-medcon/">Medcon</a></code>(1) package. </p>
<p> The LUT format consists of <code>n</code> red, <code>n</code> green and <code>n</code> blue bytes, interpreted as integers from 0 to 255. </p>
<p> The program will read from stdin if a file is not specified as the final argument, and write to stdout if the <code>-o</code> option is not specified.</p>
<h2>OPTIONS</h2>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Brief help.</dl>
<p> <code>-o</code>, <code>&#8211;output</code> <i>file</i></p>
<dl>
<dt>
<dd> Write the output to <i>file</i>, rather than stdout.</dl>
<p> <code>-s</code>, <code>&#8211;samples</code> <i>number</i></p>
<dl>
<dt>
<dd> Use the specified <i>number</i> of samples rather than 256.</dl>
<p> <code>-v</code>, <code>&#8211;verbose</code></p>
<dl>
<dt>
<dd> Verbose operation.</dl>
<p> <code>-V</code>, <code>&#8211;version</code></p>
<dl>
<dt>
<dd> Version information.</dl>
<h2>CAVEATS</h2>
<p> The alpha channel of the input is completely ignored in the output. </p>
<p> At some point in the future the functionality of this program will be transferred to the <code><a href="/docs/linux/man/1-svgx/">svgx</a></code>(1) program.</p>
<h2>AUTHOR</h2>
<p> J.J. Green</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-gimp/">GIMP</a></code>(1), <code><a href="/docs/linux/man/1-medcon/">medcon</a></code>(1). </p>
<h2>Index</h2>
