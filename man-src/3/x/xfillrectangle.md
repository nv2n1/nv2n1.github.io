---
title: "xfillrectangle(3)"
name: "xfillrectangle"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xfillrectangle/"
description: "XFillRectangle, XFillRectangles, XFillPolygon, XFillArc, XFillArcs – fill rectangles, polygons, or arcs"
---

<p>XFillRectangle, XFillRectangles, XFillPolygon, XFillArc, XFillArcs &#8211; fill rectangles, polygons, or arcs </p>
<h2>Syntax</h2>
<dl COMPACT>
<dd>int XFillRectangle(Display *<i>display</i>, Drawable <i>d</i>, GC <i>gc</i>, int <i>x</i>, int <i>y</i>, unsigned int <i>width</i>, unsigned int <i>height</i>);</p>
<dd>int XFillRectangles(Display *<i>display</i>, Drawable <i>d</i>, GC <i>gc</i>, XRectangle *<i>rectangles</i>, int <i>nrectangles</i>);</p>
<dd>int XFillPolygon(Display *<i>display</i>, Drawable <i>d</i>, GC <i>gc</i>, XPoint *<i>points</i>, int <i>npoints</i>, int <i>shape</i>, int <i>mode</i>);</p>
<dd>int XFillArc(Display *<i>display</i>, Drawable <i>d</i>, GC <i>gc</i>, int <i>x</i>, int <i>y</i>, unsigned int <i>width</i>, unsigned int <i>height</i>, int <i>angle1</i>, int <i>angle2</i>);</p>
<dd>int XFillArcs(Display *<i>display</i>, Drawable <i>d</i>, GC <i>gc</i>, XArc *<i>arcs</i>, int <i>narcs</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>angle1</i></p>
<dd>Specifies the start of the arc relative to the three-o&#8217;clock position from the center, in units of degrees * 64.</p>
<dt><i>angle2</i></p>
<dd>Specifies the path and extent of the arc relative to the start of the arc, in units of degrees * 64.</p>
<dt><i>arcs</i></p>
<dd>Specifies an array of arcs.</p>
<dt><i>d</i></p>
<dd>Specifies the drawable.</p>
<dt><i>display</i></p>
<dd>Specifies the connection to the X server.</p>
<dt><i>gc</i></p>
<dd>Specifies the GC.</p>
<dt><i>mode</i></p>
<dd>Specifies the coordinate mode. You can pass <code>CoordModeOrigin</code> or <code>CoordModePrevious</code>.</p>
<dt><i>narcs</i></p>
<dd>Specifies the number of arcs in the array.</p>
<dt><i>npoints</i></p>
<dd>Specifies the number of points in the array.</p>
<dt><i>nrectangles</i></p>
<dd>Specifies the number of rectangles in the array.</p>
<dt><i>points</i></p>
<dd>Specifies an array of points.</p>
<dt><i>rectangles</i></p>
<dd>Specifies an array of rectangles.</p>
<dt><i>shape</i></p>
<dd>Specifies a shape that helps the server to improve performance. You can pass <code>Complex</code>, <code>Convex</code>, or <code>Nonconvex</code>.</p>
<dt><i>width</i></p>
<dd>
<dt><i>height</i></p>
<dd>Specify the width and height, which are the dimensions of the rectangle to be filled or the major and minor axes of the arc.</p>
<dt><i>x</i></p>
<dd>
<dt><i>y</i></p>
<dd>Specify the x and y coordinates, which are relative to the origin of the drawable and specify the upper-left corner of the rectangle.</dl>
<h2>Description</h2>
<p>The <code>XFillRectangle</code> and <code>XFillRectangles</code> functions fill the specified rectangle or rectangles as if a four-point <code>FillPolygon</code> protocol request were specified for each rectangle: </p>
<p> [x,y] [x+width,y] [x+width,y+height] [x,y+height] </p>
<p> Each function uses the x and y coordinates, width and height dimensions, and GC you specify. </p>
<p> <code>XFillRectangles</code> fills the rectangles in the order listed in the array. For any given rectangle, <code>XFillRectangle</code> and <code>XFillRectangles</code> do not draw a pixel more than once. If rectangles intersect, the intersecting pixels are drawn multiple times. </p>
<p> Both functions use these GC components: function, plane-mask, fill-style, subwindow-mode, clip-x-origin, clip-y-origin, and clip-mask. They also use these GC mode-dependent components: foreground, background, tile, stipple, tile-stipple-x-origin, and tile-stipple-y-origin. </p>
<p> <code>XFillRectangle</code> and <code>XFillRectangles</code> can generate <code>BadDrawable</code>, <code>BadGC</code>, and <code>BadMatch</code> errors. </p>
<p> <code>XFillPolygon</code> fills the region closed by the specified path. The path is closed automatically if the last point in the list does not coincide with the first point. <code>XFillPolygon</code> does not draw a pixel of the region more than once. <code>CoordModeOrigin</code> treats all coordinates as relative to the origin, and <code>CoordModePrevious</code> treats all coordinates after the first as relative to the previous point. </p>
<p> Depending on the specified shape, the following occurs:</p>
<dl COMPACT>
<dt>&bull;</p>
<dd>If shape is <code>Complex</code>, the path may self-intersect. Note that contiguous coincident points in the path are not treated as self-intersection.</p>
<dt>&bull;</p>
<dd>If shape is <code>Convex</code>, for every pair of points inside the polygon, the line segment connecting them does not intersect the path. If known by the client, specifying <code>Convex</code> can improve performance. If you specify <code>Convex</code> for a path that is not convex, the graphics results are undefined.</p>
<dt>&bull;</p>
<dd>If shape is <code>Nonconvex</code>, the path does not self-intersect, but the shape is not wholly convex. If known by the client, specifying <code>Nonconvex</code> instead of <code>Complex</code> may improve performance. If you specify <code>Nonconvex</code> for a self-intersecting path, the graphics results are undefined.</dl>
<p> The fill-rule of the GC controls the filling behavior of self-intersecting polygons. </p>
<p> This function uses these GC components: function, plane-mask, fill-style, fill-rule, subwindow-mode, clip-x-origin, clip-y-origin, and clip-mask. It also uses these GC mode-dependent components: foreground, background, tile, stipple, tile-stipple-x-origin, and tile-stipple-y-origin. </p>
<p> <code>XFillPolygon</code> can generate <code>BadDrawable</code>, <code>BadGC</code>, <code>BadMatch</code>, and <code>BadValue</code> errors. </p>
<p> For each arc, <code>XFillArc</code> or <code>XFillArcs</code> fills the region closed by the infinitely thin path described by the specified arc and, depending on the arc-mode specified in the GC, one or two line segments. For <code>ArcChord</code>, the single line segment joining the endpoints of the arc is used. For <code>ArcPieSlice</code>, the two line segments joining the endpoints of the arc with the center point are used. <code>XFillArcs</code> fills the arcs in the order listed in the array. For any given arc, <code>XFillArc</code> and <code>XFillArcs</code> do not draw a pixel more than once. If regions intersect, the intersecting pixels are drawn multiple times. </p>
<p> Both functions use these GC components: function, plane-mask, fill-style, arc-mode, subwindow-mode, clip-x-origin, clip-y-origin, and clip-mask. They also use these GC mode-dependent components: foreground, background, tile, stipple, tile-stipple-x-origin, and tile-stipple-y-origin. </p>
<p> <code>XFillArc</code> and <code>XFillArcs</code> can generate <code>BadDrawable</code>, <code>BadGC</code>, and <code>BadMatch</code> errors.</p>
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
