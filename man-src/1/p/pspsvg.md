---
title: "pspsvg(1)"
name: "pspsvg"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pspsvg/"
description: "pspsvg – convert PaintShop Pro® gradients (jgd, PspGradient) to the SVG format."
---

<h2 class="name">NAME</h2>
<p> pspsvg &#8211; convert PaintShop Pro&#174; gradients (jgd, PspGradient) to the SVG format. </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>pspsvg</code> [-g&nbsp;<wbr><i>geometry</i>] [-h] [-o&nbsp;<wbr><i>file</i>] [-p] [-v] [-V] [<i>file</i>]</dl>
<h2>DESCRIPTION</h2>
<dd>The <code>pspsvg</code> utility converts the gradient files used by PaintShop Pro (which usually have the extension jgd or PspGradient) to the Scalar Vector Graphics (SVG) format. </p>
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
<p> <code>-v</code>, <code>&#8211;verbose</code></p>
<dl>
<dt>
<dd> Verbose operation.</dl>
<p> <code>-V</code>, <code>&#8211;version</code></p>
<dl>
<dt>
<dd> Version information.</dl>
<h2>EXAMPLES</h2>
<p> Create a machine-readable SVG file: </p>
<dl>
<dt>
<dd>
<pre>
  pspsvg -v -o new.svg old.jgd
</pre>
</dl>
<p> Create a human-readable SVG file: </p>
<dl>
<dt>
<dd>
<pre>
  pspsvg old.jgd | tidy -xml -indent -o new.svg
</pre>
</dl>
<h2>NOTES</h2>
<p> The author could find no public documentation for the PaintShop Pro gradient file format and so has reverse-engineered it. A technical description of the format can be found in the file src/common/README.psp included in the cptutils source distribution. </p>
<p> The PaintShop Pro format can be read by Photoshop, but Photoshop&#8217;s native (grd) gradient format cannot be read by this program. To convert Photoshop gradients, see the <code><a href="/docs/linux/man/1-pssvg/">pssvg</a></code>(1) documentation. </p>
<p> PaintShop Pro&#174; is a trademark of the Corel Corporation. Adobe Photoshop&#174; is a trademark of Adobe Systems Inc.</p>
<h2>AUTHOR</h2>
<p> J.J. Green</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pssvg/">pssvg</a></code>(1), <code><a href="/docs/linux/man/1-svgpsp/">svgpsp</a></code>(1), <code><a href="/docs/linux/man/1-tidy/">tidy</a></code>(1). </p>
<h2>Index</h2>
