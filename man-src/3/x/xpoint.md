---
title: "xpoint(3)"
name: "xpoint"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xpoint/"
description: "XDrawPoint, XDrawPoints, XPoint – draw points and points structure"
---

<p>XDrawPoint, XDrawPoints, XPoint &#8211; draw points and points structure </p>
<h2>Syntax</h2>
<dl COMPACT>
<dd>int XDrawPoint(Display *<i>display</i>, Drawable <i>d</i>, GC <i>gc</i>, int <i>x</i>, int <i>y</i>);</p>
<dd>int XDrawPoints(Display *<i>display</i>, Drawable <i>d</i>, GC <i>gc</i>, XPoint *<i>points</i>, int <i>npoints</i>, int <i>mode</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>d</i></p>
<dd>Specifies the drawable.</p>
<dt><i>display</i></p>
<dd>Specifies the connection to the X server.</p>
<dt><i>gc</i></p>
<dd>Specifies the GC.</p>
<dt><i>mode</i></p>
<dd>Specifies the coordinate mode. You can pass <code>CoordModeOrigin</code> or <code>CoordModePrevious</code>.</p>
<dt><i>npoints</i></p>
<dd>Specifies the number of points in the array.</p>
<dt><i>points</i></p>
<dd>Specifies an array of points.</p>
<dt><i>x</i></p>
<dd>
<dt><i>y</i></p>
<dd>Specify the x and y coordinates where you want the point drawn.</dl>
<h2>Description</h2>
<p>The <code>XDrawPoint</code> function uses the foreground pixel and function components of the GC to draw a single point into the specified drawable; <code>XDrawPoints</code> draws multiple points this way. <code>CoordModeOrigin</code> treats all coordinates as relative to the origin, and <code>CoordModePrevious</code> treats all coordinates after the first as relative to the previous point. <code>XDrawPoints</code> draws the points in the order listed in the array. </p>
<p> Both functions use these GC components: function, plane-mask, foreground, subwindow-mode, clip-x-origin, clip-y-origin, and clip-mask. </p>
<p> <code>XDrawPoint</code> can generate <code>BadDrawable</code>, <code>BadGC</code>, and <code>BadMatch</code> errors. <code>XDrawPoints</code> can generate <code>BadDrawable</code>, <code>BadGC</code>, <code>BadMatch</code>, and <code>BadValue</code> errors.</p>
<h2>Structures</h2>
<p>The <code>XPoint</code> structure contains: </p>
<p> typedef struct {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;short x, y; } XPoint; </p>
<p> All x and y members are signed integers. The width and height members are 16-bit unsigned integers. You should be careful not to generate coordinates and sizes out of the 16-bit ranges, because the protocol only has 16-bit fields for these values.</p>
<h2>Diagnostics</h2>
<dl COMPACT>
<dt><code>BadDrawable</code></p>
<dd>A value for a Drawable argument does not name a defined Window or Pixmap.</p>
<dt><code>BadGC</code></p>
<dd>A value for a GContext argument does not name a defined GContext.</p>
<dt><code>BadMatch</code></p>
<dd>An <code>InputOnly</code> window is used as a Drawable.</p>
<dt><code>BadMatch</code></p>
<dd>Some argument or pair of arguments has the correct type and range but fails to match in some other way required by the request.</p>
<dt><code>BadValue</code></p>
<dd>Some numeric value falls outside the range of values accepted by the request. Unless a specific range is specified for an argument, the full range defined by the argument&#8217;s type is accepted. Any argument defined as a set of alternatives can generate this error.</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-xdrawarc/">XDrawArc</a>(3), <a href="/docs/linux/man/3-xdrawline/">XDrawLine</a>(3), <a href="/docs/linux/man/3-xdrawrectangle/">XDrawRectangle</a>(3)<br />
 <i>Xlib &#8211; C Language X Interface</i></p>
