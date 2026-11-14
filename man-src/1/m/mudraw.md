---
title: "mudraw(1)"
name: "mudraw"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mudraw/"
description: "mudraw – render PDF/XPS/CBZ/EPUB documents"
---

<h2 class="name">NAME</h2>
<p> mudraw &#8211; render PDF/XPS/CBZ/EPUB documents</p>
<h2>SYNOPSIS</h2>
<p> <code>mudraw</code> [<i>options</i>] file [<i>pages]</i> </p>
<h2>DESCRIPTION</h2>
<p> <code>mudraw</code> will render a document of a supported document format to image files, convert to another vector format, or extract the text content. </p>
<p> The supported input document formats are: pdf, xps, cbz, and epub. </p>
<p> The supported output image formats are: pbm, pgm, ppm, pam, png, tga, pwg, and pcl. The supported output vector formats are: svg, pdf, and debug trace (as xml). The supported output text formats are: plain text, html, and structured text (as xml). </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-p password</code></p>
<dd> Use the specified password if the file is encrypted.</p>
<dt><code>-o output</code></p>
<dd> The output format is inferred from the output file name. Embed %d in the name to indicate the page number (for example: &quot;page%d.png&quot;). Printf modifiers are supported, for example &quot;%03d&quot;. If no output is specified, the output will go to stdout.</p>
<dt><code>-F format</code></p>
<dd> Enforce a specific output format. Use this when outputting to stdout.</p>
<dt><code>-R angle</code></p>
<dd> Rotate clockwise by given number of degrees.</p>
<dt><code>-r resolution</code></p>
<dd> Render the page at the specified resolution. The default resolution is 72 dpi.</p>
<dt><code>-w width</code></p>
<dd> Render the page at the specified width (or, if the -r flag is used, render with a maximum width).</p>
<dt><code>-h height</code></p>
<dd> Render the page at the specified height (or, if the -r flag is used, render with a maximum height).</p>
<dt><code>-f</code></p>
<dd> Fit exactly; ignore the aspect ratio when matching specified width/heights.</p>
<dt><code>-W width</code></p>
<dd> Page width in points for EPUB layout.</p>
<dt><code>-H height</code></p>
<dd> Page height in points for EPUB layout.</p>
<dt><code>-S size</code></p>
<dd> Font size in points for EPUB layout.</p>
<dt><code>-c colorspace</code></p>
<dd> Render in the specified colorspace. Supported colorspaces are: mono, gray, grayalpha, rgb, rgbalpha, cmyk, cmykalpha. Some abbreviations are allowed: m, g, ga, rgba, cmyka. The default is chosen based on the output format.</p>
<dt><code>-G gamma</code></p>
<dd> Apply gamma correction. Some typical values are 0.7 or 1.4 to thin or darken text rendering.</p>
<dt><code>-I</code></p>
<dd> Invert colors.</p>
<dt><code>-s [mft5]</code></p>
<dd> Show various bits of information: memory use, features, timings, and/or md5 checksum.</p>
<dt><code>-A bits</code></p>
<dd> Specify how many bits of anti-aliasing to use. The default is 8.</p>
<dt><code>-D</code></p>
<dd> Disable use of display lists. May cause slowdowns, but should reduce the amount of memory used. <code>-i</code> Ignore errors.</p>
<dt><code>pages</code></p>
<dd> Comma separated list of page numbers and ranges (for example: 1,5,10-15). If no pages are specified, then all pages will be rendered. </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-mupdf/">mupdf</a></code>(1), <code><a href="/docs/linux/man/1-mutool/">mutool</a></code>(1). </p>
<h2>AUTHOR</h2>
<p> MuPDF is Copyright 2006-2015 Artifex Software, Inc. </p>
<h2>Index</h2>
