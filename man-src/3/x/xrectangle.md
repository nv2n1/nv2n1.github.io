---
title: "xrectangle(3)"
name: "xrectangle"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xrectangle/"
description: "XDrawRectangle, XDrawRectangles, XRectangle – draw rectangles and rectangles structure"
---

<p>XDrawRectangle, XDrawRectangles, XRectangle &#8211; draw rectangles and rectangles structure </p>
<h2>Syntax</h2>
<dl COMPACT>
<dd>int XDrawRectangle(Display *<i>display</i>, Drawable <i>d</i>, GC <i>gc</i>, int <i>x</i>, int <i>y</i>, unsigned int <i>width</i>, unsigned int <i>height</i>);</p>
<dd>int XDrawRectangles(Display *<i>display</i>, Drawable <i>d</i>, GC <i>gc</i>, XRectangle <i>rectangles</i>[], int <i>nrectangles</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>d</i></p>
<dd>Specifies the drawable.</p>
<dt><i>display</i></p>
<dd>Specifies the connection to the X server.</p>
<dt><i>gc</i></p>
<dd>Specifies the GC.</p>
<dt><i>nrectangles</i></p>
<dd>Specifies the number of rectangles in the array.</p>
<dt><i>rectangles</i></p>
<dd>Specifies an array of rectangles.</p>
<dt><i>width</i></p>
<dd>
<dt><i>height</i></p>
<dd>Specify the width and height, which specify the dimensions of the rectangle.</p>
<dt><i>x</i></p>
<dd>
<dt><i>y</i></p>
<dd>Specify the x and y coordinates, which specify the upper-left corner of the rectangle.</dl>
<h2>Description</h2>
<p>The <code>XDrawRectangle</code> and <code>XDrawRectangles</code> functions draw the outlines of the specified rectangle or rectangles as if a five-point <code>PolyLine</code> protocol request were specified for each rectangle:</p>
<dl COMPACT>
<dd>[x,y] [x+width,y] [x+width,y+height] [x,y+height] [x,y]</dl>
<p> For the specified rectangle or rectangles, these functions do not draw a pixel more than once. <code>XDrawRectangles</code> draws the rectangles in the order listed in the array. If rectangles intersect, the intersecting pixels are drawn multiple times. </p>
<p> Both functions use these GC components: function, plane-mask, line-width, line-style, cap-style, join-style, fill-style, subwindow-mode, clip-x-origin, clip-y-origin, and clip-mask. They also use these GC mode-dependent components: foreground, background, tile, stipple, tile-stipple-x-origin, tile-stipple-y-origin, dash-offset, and dash-list. </p>
<p> <code>XDrawRectangle</code> and <code>XDrawRectangles</code> can generate <code>BadDrawable</code>, <code>BadGC</code>, and <code>BadMatch</code> errors.</p>
<h2>Structures</h2>
<p>The <code>XRectangle</code> structure contains: </p>
<p> typedef struct {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;short x, y;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned short width, height; } XRectangle; </p>
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
<dd>Some argument or pair of arguments has the correct type and range but fails to match in some other way required by the request.</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-xdrawarc/">XDrawArc</a>(3), <a href="/docs/linux/man/3-xdrawline/">XDrawLine</a>(3), <a href="/docs/linux/man/3-xdrawpoint/">XDrawPoint</a>(3)<br />
 <i>Xlib &#8211; C Language X Interface</i></p>
