---
title: "xpstopdf(1)"
name: "xpstopdf"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xpstopdf/"
description: "xpstopdf – XPS to PDF converter"
---

<h2 class="name">NAME</h2>
<p> xpstopdf &#8211; XPS to PDF converter </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>xpstopdf</code> [<i>OPTION</i>&#8230;] FILE [<i>OUTPUT FILE</i>]</dl>
<h2>DESCRIPTION</h2>
<p> <code>xpstopdf</code></p>
<dd>converts XPS documents to PDF format. <code>xpstopdf</code> reads the XPS file, <i>FILE</i>, and writes a PDF file, <i>OUTPUT FILE</i>. If <i>OUTPUT FILE</i> is not specified the output filename will be derived from the <i>OUTPUT FILE</i> filename.</p>
<h2>OPTIONS</h2>
<p> <code>-?</code>, <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Show help options.</dl>
<p> <code>-d</code> <i>DOCUMENT</i>, <code>&#8211;document</code>=<i>DOCUMENT</i></p>
<dl>
<dt>
<dd> The document inside the XPS file to convert. By default, the first document of the XPS file is used.</dl>
<p> <code>-f</code> <i>PAGE</i>, <code>&#8211;first</code>=<i>PAGE</i></p>
<dl>
<dt>
<dd> The first page to convert.</dl>
<p> <code>-l</code> <i>PAGE</i>, <code>&#8211;last</code>=<i>PAGE</i></p>
<dl>
<dt>
<dd> The last page to convert.</dl>
<p> <code>-o</code>, <code>&#8211;odd</code></p>
<dl>
<dt>
<dd> Convert only odd pages.</dl>
<p> <code>-e</code>, <code>&#8211;even</code></p>
<dl>
<dt>
<dd> Convert only even pages.</dl>
<p> <code>-r</code> <i>RESOLUTION</i>, <code>&#8211;resolution</code>=<i>RESOLUTION</i></p>
<dl>
<dt>
<dd> Horizontal and vertical resolution in PPI (Pixels Per Inch). The default is 150 PPI.</dl>
<p> <code>&#8211;rx</code>=<i>RESOLUTION</i></p>
<dl>
<dt>
<dd> Horizontal resolution in PPI (Pixels Per Inch). The default is 150 PPI.</dl>
<p> <code>&#8211;ry</code>=<i>RESOLUTION</i></p>
<dl>
<dt>
<dd> Vertical resolution in PPI (Pixels Per Inch). The default is 150 PPI.</dl>
<p> <code>-x</code> <i>X</i>, <code>&#8211;crop-x</code>=<i>X</i></p>
<dl>
<dt>
<dd> The x-coordinate of the crop area top left corner.</dl>
<p> <code>-y</code> <i>Y</i>, <code>&#8211;crop-y</code>=<i>Y</i></p>
<dl>
<dt>
<dd> The y-coordinate of the crop area top left corner.</dl>
<p> <code>-w</code> <i>WIDTH</i>, <code>&#8211;crop-width</code>=<i>WIDTH</i></p>
<dl>
<dt>
<dd> The width of crop area.</dl>
<p> <code>-h</code> <i>HEIGHT</i>, <code>&#8211;crop-height</code>=<i>HEIGHT</i></p>
<dl>
<dt>
<dd> The height of crop area.</dl>
<p> <code>&#8211;paper-width</code>=<i>WIDTH</i></p>
<dl>
<dt>
<dd> The paper width.</dl>
<p> <code>&#8211;paper-height</code>=<i>HEIGHT</i></p>
<dl>
<dt>
<dd> The paper height.</dl>
<p> <code>&#8211;expand</code></p>
<dl>
<dt>
<dd> Expand pages smaller than the paper to fill the paper. By default, pages are not scaled.</dl>
<p> <code>&#8211;no-shrink</code></p>
<dl>
<dt>
<dd> Don&#8217;t scale pages which are larger than the paper. By default, pages larger than the paper are shrunk to fit.</dl>
<p> <code>&#8211;no-center</code></p>
<dl>
<dt>
<dd> Don&#8217;t center on the paper pages smaller than the paper (after any scaling). By default, pages smaller than the paper are aligned to the lower-left corner.</dl>
<h2>BUGS</h2>
<p> Please send bug reports to m[blue]<code><a rel="nofollow" href="https://bugzilla.gnome.org/enter_bug.cgi?product=libgxps">https://bugzilla.gnome.org/enter_bug.cgi?product=libgxps</a></code>m[].</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-xpstojpeg/">xpstojpeg</a></code>(1) <code><a href="/docs/linux/man/1-xpstopng/">xpstopng</a></code>(1) <code><a href="/docs/linux/man/1-xpstops/">xpstops</a></code>(1) <code><a href="/docs/linux/man/1-xpstosvg/">xpstosvg</a></code>(1) </p>
<h2>Index</h2>
