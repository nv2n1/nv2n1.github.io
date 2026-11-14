---
title: "xsetsubwindowmode(3)"
name: "xsetsubwindowmode"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xsetsubwindowmode/"
description: "XSetArcMode, XSetSubwindowMode, XSetGraphicsExposure – GC convenience routines"
---

<p>XSetArcMode, XSetSubwindowMode, XSetGraphicsExposure &#8211; GC convenience routines </p>
<h2>Syntax</h2>
<dl COMPACT>
<dd>int XSetArcMode(Display *<i>display</i>, GC <i>gc</i>, int <i>arc_mode</i>);</p>
<dd>int XSetSubwindowMode(Display *<i>display</i>, GC <i>gc</i>, int <i>subwindow_mode</i>);</p>
<dd>int XSetGraphicsExposures(Display *<i>display</i>, GC <i>gc</i>, Bool <i>graphics_exposures</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>arc_mode</i></p>
<dd>Specifies the arc mode. You can pass <code>ArcChord</code> or <code>ArcPieSlice</code>.</p>
<dt><i>display</i></p>
<dd>Specifies the connection to the X server.</p>
<dt><i>gc</i></p>
<dd>Specifies the GC.</p>
<dt><i>graphics_exposures</i></p>
<dd>Specifies a Boolean value that indicates whether you want <code>GraphicsExpose</code> and <code>NoExpose</code> events to be reported when calling <code>XCopyArea</code> and <code>XCopyPlane</code> with this GC.</p>
<dt><i>subwindow_mode</i></p>
<dd>Specifies the subwindow mode. You can pass <code>ClipByChildren</code> or <code>IncludeInferiors</code>.</dl>
<h2>Description</h2>
<p>The <code>XSetArcMode</code> function sets the arc mode in the specified GC. </p>
<p> <code>XSetArcMode</code> can generate <code>BadAlloc</code>, <code>BadGC</code>, and <code>BadValue</code> errors. </p>
<p> The <code>XSetSubwindowMode</code> function sets the subwindow mode in the specified GC. </p>
<p> <code>XSetSubwindowMode</code> can generate <code>BadAlloc</code>, <code>BadGC</code>, and <code>BadValue</code> errors. </p>
<p> The <code>XSetGraphicsExposures</code> function sets the graphics-exposures flag in the specified GC. </p>
<p> <code>XSetGraphicsExposures</code> can generate <code>BadAlloc</code>, <code>BadGC</code>, and <code>BadValue</code> errors.</p>
<h2>Diagnostics</h2>
<dl COMPACT>
<dt><code>BadAlloc</code></p>
<dd>The server failed to allocate the requested resource or server memory.</p>
<dt><code>BadGC</code></p>
<dd>A value for a GContext argument does not name a defined GContext.</p>
<dt><code>BadValue</code></p>
<dd>Some numeric value falls outside the range of values accepted by the request. Unless a specific range is specified for an argument, the full range defined by the argument&#8217;s type is accepted. Any argument defined as a set of alternatives can generate this error.</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-xcopyarea/">XCopyArea</a>(3), <a href="/docs/linux/man/3-xcreategc/">XCreateGC</a>(3), <a href="/docs/linux/man/3-xquerybestsize/">XQueryBestSize</a>(3), <a href="/docs/linux/man/3-xsetcliporigin/">XSetClipOrigin</a>(3), <a href="/docs/linux/man/3-xsetfillstyle/">XSetFillStyle</a>(3), <a href="/docs/linux/man/3-xsetfont/">XSetFont</a>(3), <a href="/docs/linux/man/3-xsetlineattributes/">XSetLineAttributes</a>(3), <a href="/docs/linux/man/3-xsetstate/">XSetState</a>(3), <a href="/docs/linux/man/3-xsettile/">XSetTile</a>(3)<br />
 <i>Xlib &#8211; C Language X Interface</i></p>
