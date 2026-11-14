---
title: "mupdf(1)"
name: "mupdf"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mupdf/"
description: "mupdf – MuPDF is a lightweight PDF viewer written in portable C"
---

<h2 class="name">NAME</h2>
<p> mupdf &#8211; MuPDF is a lightweight PDF viewer written in portable C</p>
<h2>SYNOPSIS</h2>
<p> <code>mupdf</code> [<i>options</i>]<i> PDFfile</i> </p>
<h2>DESCRIPTION</h2>
<p> This manual page briefly describes the <code>mupdf</code> command. </p>
<h2>OPTIONS</h2>
<p> A description of each of the supported options is included below. </p>
<dl>
<dt><code>-p password</code></p>
<dd> Uses the given password to open an encrypted PDF file. The password is tried both as user and owner password.</p>
<dt><code>-r resolution</code></p>
<dd> Changes the initial zoom level, specified as the resolution in dpi. The default value is 72.</p>
<dt><code>-A bits</code></p>
<dd> Changes the anti-aliasing quality, specified as a number of bits between 0 (off) and 8 (best). The default value is 8.</p>
<dt><code>-C RRGGBB</code></p>
<dd> Sets the full-page tint using hexadecimal color syntax. The default value is FFFAF0.</p>
<dt><code>-W width</code></p>
<dd> Page width in points for EPUB layout.</p>
<dt><code>-H height</code></p>
<dd> Page height in points for EPUB layout.</p>
<dt><code>-S size</code></p>
<dd> Font size in points for EPUB layout. </p>
</dl>
<h2>MOUSE BEHAVIOR</h2>
<dl>
<dt><code>Left mouse button click</code></p>
<dd> A left click on a hyper link follows the link.</p>
<dt><code>Left mouse button drag</code></p>
<dd> Pan the page. Panning beyond the bottom or top edge will go to the next or previous page.</p>
<dt><code>Right mouse button drag</code></p>
<dd> Select text in an area. On X11, the selected text can be pasted in another application with a middle click. Press Ctl+C to copy the selected text to the clipboard. On windows, the selected text will automatically be copied to the clipboard.</p>
<dt><code>Scroll wheel</code></p>
<dd> Pan page up or down. Does not change page when reaching the bottom or top edge.</p>
<dt><code>Shift + Scroll wheel</code></p>
<dd> Pan page left or right.</p>
<dt><code>Control + Scroll wheel</code></p>
<dd> Zoom in or out. </p>
</dl>
<h2>KEY BINDINGS</h2>
<dl>
<dt><code>L, R</code></p>
<dd> Rotate page left (counter-clockwise) or right (clockwise).</p>
<dt><code>h, j, k, l</code></p>
<dd> Pan page left, down, up, or right.</p>
<dt><code>+, &#8211;</code></p>
<dd> Zoom in or out.</p>
<dt><code>W, H</code></p>
<dd> Zoom page to exactly fit width or height of window.</p>
<dt><code>w</code></p>
<dd> Shrinkwrap window to fit the page.</p>
<dt><code>r</code></p>
<dd> Reload file.</p>
<dt><code>. pgdn right space</code></p>
<dd> Go to the next page</p>
<dt><code>, pgup left b backspace</code></p>
<dd> Go to the previous page</p>
<dt><code>&lt;, &gt;</code></p>
<dd> Skip back/forth 10 pages at a time.</p>
<dt><code>m</code></p>
<dd> Mark current page for snap back. Up to 256 pages can be marked.</p>
<dt><code>t</code></p>
<dd> Pop back to the latest mark.</p>
<dt><code>[0-9]m</code></p>
<dd> Save the current page number in the numbered register.</p>
<dt><code>[0-9]t</code></p>
<dd> Go to the page saved in the numbered register.</p>
<dt><code>123g</code></p>
<dd> Go to page 123.</p>
<dt><code>g, G</code></p>
<dd> Go to the first or last page.</p>
<dt><code>/, ?</code></p>
<dd> Search for text forwards or backwards.</p>
<dt><code>n, N</code></p>
<dd> Find the next/previous search result.</p>
<dt><code>f</code></p>
<dd> Toggles fullscreen mode.</p>
<dt><code>p</code></p>
<dd> Toggle presentation mode.</p>
<dt><code>c</code></p>
<dd> Toggle between color and grayscale rendering.</p>
<dt><code>C</code></p>
<dd> Toggle full-page color tinting. <code>i</code> Toggle between normal and inverted color rendering.</p>
<dt><code>q</code></p>
<dd> Quit. </p>
</dl>
<h2>SIGNALS</h2>
<dl>
<dt><code>SIGHUP</code></p>
<dd> Sending a <code>SIGHUP</code> signal to the mupdf process will also cause the viewed file to be reloaded automatically, for use in e.g. build scripts. </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-mudraw/">mudraw</a></code>(1), <code><a href="/docs/linux/man/1-mutool/">mutool</a></code>(1). </p>
<h2>AUTHOR</h2>
<p> MuPDF is Copyright 2006-2014 Artifex Software, Inc. </p>
<h2>Index</h2>
