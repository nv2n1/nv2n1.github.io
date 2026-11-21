---

title: "mupdf(1)"
name: "mupdf"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mupdf/"
description: "mupdf – MuPDF is a lightweight PDF viewer written in portable C"
---

<p> <code>mupdf</code> [<i>options</i>]<i> PDFfile</i> </p>
<p> This manual page briefly describes the <code>mupdf</code> command. </p>
<h2>OPTIONS</h2>
<p> A description of each of the supported options is included below. </p>
<dl>
<dt><code>-p password</code></dt>
<dd> Uses the given password to open an encrypted PDF file. The password is tried both as user and owner password.</dd>
<dt><code>-r resolution</code></dt>
<dd> Changes the initial zoom level, specified as the resolution in dpi. The default value is 72.</dd>
<dt><code>-A bits</code></dt>
<dd> Changes the anti-aliasing quality, specified as a number of bits between 0 (off) and 8 (best). The default value is 8.</dd>
<dt><code>-C RRGGBB</code></dt>
<dd> Sets the full-page tint using hexadecimal color syntax. The default value is FFFAF0.</dd>
<dt><code>-W width</code></dt>
<dd> Page width in points for EPUB layout.</dd>
<dt><code>-H height</code></dt>
<dd> Page height in points for EPUB layout.</dd>
<dt><code>-S size</code></dt>
<dd> Font size in points for EPUB layout. </dd>
</dl>
<h2>MOUSE BEHAVIOR</h2>
<dl>
<dt><code>Left mouse button click</code></dt>
<dd> A left click on a hyper link follows the link.</dd>
<dt><code>Left mouse button drag</code></dt>
<dd> Pan the page. Panning beyond the bottom or top edge will go to the next or previous page.</dd>
<dt><code>Right mouse button drag</code></dt>
<dd> Select text in an area. On X11, the selected text can be pasted in another application with a middle click. Press Ctl+C to copy the selected text to the clipboard. On windows, the selected text will automatically be copied to the clipboard.</dd>
<dt><code>Scroll wheel</code></dt>
<dd> Pan page up or down. Does not change page when reaching the bottom or top edge.</dd>
<dt><code>Shift + Scroll wheel</code></dt>
<dd> Pan page left or right.</dd>
<dt><code>Control + Scroll wheel</code></dt>
<dd> Zoom in or out. </dd>
</dl>
<h2>KEY BINDINGS</h2>
<dl>
<dt><code>L, R</code></dt>
<dd> Rotate page left (counter-clockwise) or right (clockwise).</dd>
<dt><code>h, j, k, l</code></dt>
<dd> Pan page left, down, up, or right.</dd>
<dt><code>+, &#8211;</code></dt>
<dd> Zoom in or out.</dd>
<dt><code>W, H</code></dt>
<dd> Zoom page to exactly fit width or height of window.</dd>
<dt><code>w</code></dt>
<dd> Shrinkwrap window to fit the page.</dd>
<dt><code>r</code></dt>
<dd> Reload file.</dd>
<dt><code>. pgdn right space</code></dt>
<dd> Go to the next page</dd>
<dt><code>, pgup left b backspace</code></dt>
<dd> Go to the previous page</dd>
<dt><code>&lt;, &gt;</code></dt>
<dd> Skip back/forth 10 pages at a time.</dd>
<dt><code>m</code></dt>
<dd> Mark current page for snap back. Up to 256 pages can be marked.</dd>
<dt><code>t</code></dt>
<dd> Pop back to the latest mark.</dd>
<dt><code>[0-9]m</code></dt>
<dd> Save the current page number in the numbered register.</dd>
<dt><code>[0-9]t</code></dt>
<dd> Go to the page saved in the numbered register.</dd>
<dt><code>123g</code></dt>
<dd> Go to page 123.</dd>
<dt><code>g, G</code></dt>
<dd> Go to the first or last page.</dd>
<dt><code>/, ?</code></dt>
<dd> Search for text forwards or backwards.</dd>
<dt><code>n, N</code></dt>
<dd> Find the next/previous search result.</dd>
<dt><code>f</code></dt>
<dd> Toggles fullscreen mode.</dd>
<dt><code>p</code></dt>
<dd> Toggle presentation mode.</dd>
<dt><code>c</code></dt>
<dd> Toggle between color and grayscale rendering.</dd>
<dt><code>C</code></dt>
<dd> Toggle full-page color tinting. <code>i</code> Toggle between normal and inverted color rendering.</dd>
<dt><code>q</code></dt>
<dd> Quit. </dd>
</dl>
<h2>SIGNALS</h2>
<dl>
<dt><code>SIGHUP</code></dt>
<dd> Sending a <code>SIGHUP</code> signal to the mupdf process will also cause the viewed file to be reloaded automatically, for use in e.g. build scripts. </dd>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-mudraw/">mudraw</a></code>(1), <code><a href="/docs/linux/man/1-mutool/">mutool</a></code>(1). </p>
<h2>AUTHOR</h2>
<p> MuPDF is Copyright 2006-2014 Artifex Software, Inc. </p>
