---
title: "xsettsorigin(3)"
name: "xsettsorigin"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xsettsorigin/"
description: "XSetTile, XSetStipple, XSetTSOrigin – GC convenience routines"
---

<p>XSetTile, XSetStipple, XSetTSOrigin &#8211; GC convenience routines </p>
<h2>Syntax</h2>
<dl COMPACT>
<dd>int XSetTile(Display *<i>display</i>, GC <i>gc</i>, Pixmap <i>tile</i>);</p>
<dd>int XSetStipple(Display *<i>display</i>, GC <i>gc</i>, Pixmap <i>stipple</i>);</p>
<dd>int XSetTSOrigin(Display *<i>display</i>, GC <i>gc</i>, int <i>ts_x_origin</i>, int <i>ts_y_origin</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>display</i></p>
<dd>Specifies the connection to the X server.</p>
<dt><i>gc</i></p>
<dd>Specifies the GC.</p>
<dt><i>stipple</i></p>
<dd>Specifies the stipple you want to set for the specified GC.</p>
<dt><i>tile</i></p>
<dd>Specifies the fill tile you want to set for the specified GC.</p>
<dt><i>ts_x_origin</i></p>
<dd>
<dt><i>ts_y_origin</i></p>
<dd>Specify the x and y coordinates of the tile and stipple origin.</dl>
<h2>Description</h2>
<p>The <code>XSetTile</code> function sets the fill tile in the specified GC. The tile and GC must have the same depth, or a <code>BadMatch</code> error results. </p>
<p> <code>XSetTile</code> can generate <code>BadAlloc</code>, <code>BadGC</code>, <code>BadMatch</code>, and <code>BadPixmap</code> errors. </p>
<p> The <code>XSetStipple</code> function sets the stipple in the specified GC. The stipple must have a depth of one, or a <code>BadMatch</code> error results. </p>
<p> <code>XSetStipple</code> can generate <code>BadAlloc</code>, <code>BadGC</code>, <code>BadMatch</code>, and <code>BadPixmap</code> errors. </p>
<p> The <code>XSetTSOrigin</code> function sets the tile/stipple origin in the specified GC. When graphics requests call for tiling or stippling, the parent&#8217;s origin will be interpreted relative to whatever destination drawable is specified in the graphics request. </p>
<p> <code>XSetTSOrigin</code> can generate <code>BadAlloc</code> and <code>BadGC</code> errors.</p>
<h2>Diagnostics</h2>
<dl COMPACT>
<dt><code>BadAlloc</code></p>
<dd>The server failed to allocate the requested resource or server memory.</p>
<dt><code>BadGC</code></p>
<dd>A value for a GContext argument does not name a defined GContext.</p>
<dt><code>BadMatch</code></p>
<dd>Some argument or pair of arguments has the correct type and range but fails to match in some other way required by the request.</p>
<dt><code>BadPixmap</code></p>
<dd>A value for a Pixmap argument does not name a defined Pixmap.</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-xcreategc/">XCreateGC</a>(3), <a href="/docs/linux/man/3-xquerybestsize/">XQueryBestSize</a>(3), <a href="/docs/linux/man/3-xsetarcmode/">XSetArcMode</a>(3), <a href="/docs/linux/man/3-xsetcliporigin/">XSetClipOrigin</a>(3), <a href="/docs/linux/man/3-xsetfillstyle/">XSetFillStyle</a>(3), <a href="/docs/linux/man/3-xsetfont/">XSetFont</a>(3), <a href="/docs/linux/man/3-xsetlineattributes/">XSetLineAttributes</a>(3), <a href="/docs/linux/man/3-xsetstate/">XSetState</a>(3)<br />
 <i>Xlib &#8211; C Language X Interface</i></p>
