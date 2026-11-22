---
title: "xsetstipple(3)"
name: "xsetstipple"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xsetstipple/"
description: "XSetTile, XSetStipple, XSetTSOrigin – GC convenience routines"
---

<p>XSetTile, XSetStipple, XSetTSOrigin &#8211; GC convenience routines </p>
<h2>Syntax</h2>
<dl COMPACT>
<dd>int XSetTile(Display *<i>display</i>, GC <i>gc</i>, Pixmap <i>tile</i>);</dd>
<dd>int XSetStipple(Display *<i>display</i>, GC <i>gc</i>, Pixmap <i>stipple</i>);</dd>
<dd>int XSetTSOrigin(Display *<i>display</i>, GC <i>gc</i>, int <i>ts_x_origin</i>, int <i>ts_y_origin</i>);</dd></dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>display</i></dt>
<dd>Specifies the connection to the X server.</dd>
<dt><i>gc</i></dt>
<dd>Specifies the GC.</dd>
<dt><i>stipple</i></dt>
<dd>Specifies the stipple you want to set for the specified GC.</dd>
<dt><i>tile</i></dt>
<dd>Specifies the fill tile you want to set for the specified GC.</dd>
<dt><i>ts_x_origin</i></dt>
<dd>
</dd><dt><i>ts_y_origin</i></dt>
<dd>Specify the x and y coordinates of the tile and stipple origin.</dd></dl>
<h2>Description</h2>
<p>The <code>XSetTile</code> function sets the fill tile in the specified GC. The tile and GC must have the same depth, or a <code>BadMatch</code> error results. </p>
<p> <code>XSetTile</code> can generate <code>BadAlloc</code>, <code>BadGC</code>, <code>BadMatch</code>, and <code>BadPixmap</code> errors. </p>
<p> The <code>XSetStipple</code> function sets the stipple in the specified GC. The stipple must have a depth of one, or a <code>BadMatch</code> error results. </p>
<p> <code>XSetStipple</code> can generate <code>BadAlloc</code>, <code>BadGC</code>, <code>BadMatch</code>, and <code>BadPixmap</code> errors. </p>
<p> The <code>XSetTSOrigin</code> function sets the tile/stipple origin in the specified GC. When graphics requests call for tiling or stippling, the parent&#8217;s origin will be interpreted relative to whatever destination drawable is specified in the graphics request. </p>
<p> <code>XSetTSOrigin</code> can generate <code>BadAlloc</code> and <code>BadGC</code> errors.</p>
<h2>Diagnostics</h2>
<dl COMPACT>
<dt><code>BadAlloc</code></dt>
<dd>The server failed to allocate the requested resource or server memory.</dd>
<dt><code>BadGC</code></dt>
<dd>A value for a GContext argument does not name a defined GContext.</dd>
<dt><code>BadMatch</code></dt>
<dd>Some argument or pair of arguments has the correct type and range but fails to match in some other way required by the request.</dd>
<dt><code>BadPixmap</code></dt>
<dd>A value for a Pixmap argument does not name a defined Pixmap.</dd></dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-xcreategc/">XCreateGC</a>(3), <a href="/docs/linux/man/3-xquerybestsize/">XQueryBestSize</a>(3), <a href="/docs/linux/man/3-xsetarcmode/">XSetArcMode</a>(3), <a href="/docs/linux/man/3-xsetcliporigin/">XSetClipOrigin</a>(3), <a href="/docs/linux/man/3-xsetfillstyle/">XSetFillStyle</a>(3), <a href="/docs/linux/man/3-xsetfont/">XSetFont</a>(3), <a href="/docs/linux/man/3-xsetlineattributes/">XSetLineAttributes</a>(3), <a href="/docs/linux/man/3-xsetstate/">XSetState</a>(3)<br/>
 <i>Xlib &#8211; C Language X Interface</i></p>
