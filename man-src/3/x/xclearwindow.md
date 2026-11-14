---
title: "xclearwindow(3)"
name: "xclearwindow"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xclearwindow/"
description: "XClearArea, XClearWindow – clear area or window"
---

<p>XClearArea, XClearWindow &#8211; clear area or window </p>
<h2>Syntax</h2>
<dl COMPACT>
<dd>int XClearArea(Display *<i>display</i>, Window <i>w</i>, int <i>x</i>, int <i>y</i>, unsigned <i>width</i>, unsigned <i>height</i>, Bool <i>exposures</i>);</p>
<dd>int XClearWindow(Display *<i>display</i>, Window <i>w</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>display</i></p>
<dd>Specifies the connection to the X server.</p>
<dt><i>exposures</i></p>
<dd>Specifies a Boolean value that indicates if <code>Expose</code> events are to be generated.</p>
<dt><i>w</i></p>
<dd>Specifies the window.</p>
<dt><i>width</i></p>
<dd>
<dt><i>height</i></p>
<dd>Specify the width and height, which are the dimensions of the rectangle.</p>
<dt><i>x</i></p>
<dd>
<dt><i>y</i></p>
<dd>Specify the x and y coordinates, which are relative to the origin of the window and specify the upper-left corner of the rectangle.</dl>
<h2>Description</h2>
<p>The <code>XClearArea</code> function paints a rectangular area in the specified window according to the specified dimensions with the window&#8217;s background pixel or pixmap. The subwindow-mode effectively is <code>ClipByChildren</code>. If width is zero, it is replaced with the current width of the window minus x. If height is zero, it is replaced with the current height of the window minus y. If the window has a defined background tile, the rectangle clipped by any children is filled with this tile. If the window has background <code>None</code>, the contents of the window are not changed. In either case, if exposures is <code>True</code>, one or more <code>Expose</code> events are generated for regions of the rectangle that are either visible or are being retained in a backing store. If you specify a window whose class is <code>InputOnly</code>, a <code>BadMatch</code> error results. </p>
<p> <code>XClearArea</code> can generate <code>BadMatch</code>, <code>BadValue</code>, and <code>BadWindow</code> errors. </p>
<p> The <code>XClearWindow</code> function clears the entire area in the specified window and is equivalent to <code>XClearArea</code> (display, w, 0, 0, 0, 0, <code>False</code>). If the window has a defined background tile, the rectangle is tiled with a plane-mask of all ones and <code>GXcopy</code> function. If the window has background <code>None</code>, the contents of the window are not changed. If you specify a window whose class is <code>InputOnly</code>, a <code>BadMatch</code> error results. </p>
<p> <code>XClearWindow</code> can generate <code>BadMatch</code> and <code>BadWindow</code> errors.</p>
<h2>Diagnostics</h2>
<dl COMPACT>
<dt><code>BadMatch</code></p>
<dd>An <code>InputOnly</code> window is used as a Drawable.</p>
<dt><code>BadValue</code></p>
<dd>Some numeric value falls outside the range of values accepted by the request. Unless a specific range is specified for an argument, the full range defined by the argument&#8217;s type is accepted. Any argument defined as a set of alternatives can generate this error.</p>
<dt><code>BadWindow</code></p>
<dd>A value for a Window argument does not name a defined Window.</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-xcopyarea/">XCopyArea</a>(3)<br />
 <i>Xlib &#8211; C Language X Interface</i></p>
