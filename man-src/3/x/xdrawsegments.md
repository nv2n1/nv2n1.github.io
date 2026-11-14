---
title: "xdrawsegments(3)"
name: "xdrawsegments"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xdrawsegments/"
description: "XDrawLine, XDrawLines, XDrawSegments, XSegment – draw lines, polygons, and line structure"
---

<p>XDrawLine, XDrawLines, XDrawSegments, XSegment &#8211; draw lines, polygons, and line structure </p>
<h2>Syntax</h2>
<dl COMPACT>
<dd>int XDrawLine(Display *<i>display</i>, Drawable <i>d</i>, GC <i>gc</i>, int <i>x1</i>, int <i>y1</i>, int <i>x2</i>, int <i>y2</i>);</p>
<dd>int XDrawLines(Display *<i>display</i>, Drawable <i>d</i>, GC <i>gc</i>, XPoint *<i>points</i>, int <i>npoints</i>, int <i>mode</i>);</p>
<dd>int XDrawSegments(Display *<i>display</i>, Drawable <i>d</i>, GC <i>gc</i>, XSegment *<i>segments</i>, int <i>nsegments</i>);</dl>
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
<dt><i>nsegments</i></p>
<dd>Specifies the number of segments in the array.</p>
<dt><i>points</i></p>
<dd>Specifies an array of points.</p>
<dt><i>segments</i></p>
<dd>Specifies an array of segments.</p>
<dt><i>x1</i></p>
<dd>
<dt><i>y1</i></p>
<dd>
<dt><i>x2</i></p>
<dd>
<dt><i>y2</i></p>
<dd>Specify the points (x1, y1) and (x2, y2) to be connected.</dl>
<h2>Description</h2>
<p>The <code>XDrawLine</code> function uses the components of the specified GC to draw a line between the specified set of points (x1, y1) and (x2, y2). It does not perform joining at coincident endpoints. For any given line, <code>XDrawLine</code> does not draw a pixel more than once. If lines intersect, the intersecting pixels are drawn multiple times. </p>
<p> The <code>XDrawLines</code> function uses the components of the specified GC to draw npoints-1 lines between each pair of points (point[i], point[i+1]) in the array of <code>XPoint</code> structures. It draws the lines in the order listed in the array. The lines join correctly at all intermediate points, and if the first and last points coincide, the first and last lines also join correctly. For any given line, <code>XDrawLines</code> does not draw a pixel more than once. If thin (zero line-width) lines intersect, the intersecting pixels are drawn multiple times. If wide lines intersect, the intersecting pixels are drawn only once, as though the entire <code>PolyLine</code> protocol request were a single, filled shape. <code>CoordModeOrigin</code> treats all coordinates as relative to the origin, and <code>CoordModePrevious</code> treats all coordinates after the first as relative to the previous point. </p>
<p> The <code>XDrawSegments</code> function draws multiple, unconnected lines. For each segment, <code>XDrawSegments</code> draws a line between (x1, y1) and (x2, y2). It draws the lines in the order listed in the array of <code>XSegment</code> structures and does not perform joining at coincident endpoints. For any given line, <code>XDrawSegments</code> does not draw a pixel more than once. If lines intersect, the intersecting pixels are drawn multiple times. </p>
<p> All three functions use these GC components: function, plane-mask, line-width, line-style, cap-style, fill-style, subwindow-mode, clip-x-origin, clip-y-origin, and clip-mask. The <code>XDrawLines</code> function also uses the join-style GC component. All three functions also use these GC mode-dependent components: foreground, background, tile, stipple, tile-stipple-x-origin, tile-stipple-y-origin, dash-offset, and dash-list. </p>
<p> <code>XDrawLine</code>, <code>XDrawLines</code>, and <code>XDrawSegments</code> can generate <code>BadDrawable</code>, <code>BadGC</code>, and <code>BadMatch</code> errors. <code>XDrawLines</code> can also generate a <code>BadValue</code> error.</p>
<h2>Structures</h2>
<p>The <code>XSegment</code> structure contains: </p>
<p> typedef struct {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;short x1, y1, x2, y2; } XSegment; </p>
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
<p><a href="/docs/linux/man/3-xdrawarc/">XDrawArc</a>(3), <a href="/docs/linux/man/3-xdrawpoint/">XDrawPoint</a>(3), <a href="/docs/linux/man/3-xdrawrectangle/">XDrawRectangle</a>(3)<br />
 <i>Xlib &#8211; C Language X Interface</i></p>
