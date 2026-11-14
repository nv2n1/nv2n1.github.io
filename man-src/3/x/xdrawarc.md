---
title: "xdrawarc(3)"
name: "xdrawarc"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xdrawarc/"
description: "XDrawArc, XDrawArcs, XArc – draw arcs and arc structure"
---

<p>XDrawArc, XDrawArcs, XArc &#8211; draw arcs and arc structure </p>
<h2>Syntax</h2>
<dl COMPACT>
<dd>int XDrawArc(Display *<i>display</i>, Drawable <i>d</i>, GC <i>gc</i>, int <i>x</i>, int <i>y</i>, unsigned int <i>width</i>, unsigned int <i>height</i>, int <i>angle1</i>, int <i>angle2</i>);</p>
<dd>int XDrawArcs(Display *<i>display</i>, Drawable <i>d</i>, GC <i>gc</i>, XArc *<i>arcs</i>, int <i>narcs</i>);</dl>
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
<dt><i>narcs</i></p>
<dd>Specifies the number of arcs in the array.</p>
<dt><i>width</i></p>
<dd>
<dt><i>height</i></p>
<dd>Specify the width and height, which are the major and minor axes of the arc.</p>
<dt><i>x</i></p>
<dd>
<dt><i>y</i></p>
<dd>Specify the x and y coordinates, which are relative to the origin of the drawable and specify the upper-left corner of the bounding rectangle.</dl>
<h2>Description</h2>
<p>delim %% <code>XDrawArc</code> draws a single circular or elliptical arc, and <code>XDrawArcs</code> draws multiple circular or elliptical arcs. Each arc is specified by a rectangle and two angles. The center of the circle or ellipse is the center of the rectangle, and the major and minor axes are specified by the width and height. Positive angles indicate counterclockwise motion, and negative angles indicate clockwise motion. If the magnitude of angle2 is greater than 360 degrees, <code>XDrawArc</code> or <code>XDrawArcs</code> truncates it to 360 degrees. </p>
<p> For an arc specified as %[ ~x, ~y, ~width , ~height, ~angle1, ~angle2 ]%, the origin of the major and minor axes is at % [ x +^ {width over 2} , ~y +^ {height over 2} ]%, and the infinitely thin path describing the entire circle or ellipse intersects the horizontal axis at % [ x, ~y +^ {height over 2} ]% and % [ x +^ width , ~y +^ { height over 2 }] % and intersects the vertical axis at % [ x +^ { width over 2 } , ~y ]% and % [ x +^ { width over 2 }, ~y +^ height ]%. These coordinates can be fractional and so are not truncated to discrete coordinates. The path should be defined by the ideal mathematical path. For a wide line with line-width lw, the bounding outlines for filling are given by the two infinitely thin paths consisting of all points whose perpendicular distance from the path of the circle/ellipse is equal to lw/2 (which may be a fractional value). The cap-style and join-style are applied the same as for a line corresponding to the tangent of the circle/ellipse at the endpoint. </p>
<p> For an arc specified as % [ ~x, ~y, ~width, ~height, ~angle1, ~angle2 ]%, the angles must be specified in the effectively skewed coordinate system of the ellipse (for a circle, the angles and coordinate systems are identical). The relationship between these angles and angles expressed in the normal coordinate system of the screen (as measured with a protractor) is as follows: </p>
<pre>% roman &quot;skewed-angle&quot; ~ = ~ atan left ( tan ( roman &quot;normal-angle&quot; )
 * width over height right ) +^ adjust%</pre>
<p>The skewed-angle and normal-angle are expressed in radians (rather than in degrees scaled by 64) in the range % [ 0 , ~2 pi ]% and where atan returns a value in the range % [ &#8211; pi over 2 , ~pi over 2 ] % and adjust is: </p>
<table>
<tr VALIGN=top>
<td>%0%</td>
<td>for normal-angle in the range % [ 0 , ~pi over 2 ]%
</td>
</tr>
<tr VALIGN=top>
<td>%pi%</td>
<td>for normal-angle in the range % [ pi over 2 , ~{3 pi} over 2 ]%
</td>
</tr>
<tr VALIGN=top>
<td>%2 pi%</td>
<td>for normal-angle in the range % [ {3 pi} over 2 , ~2 pi ]%
</td>
</tr>
</table>
<p> For any given arc, <code>XDrawArc</code> and <code>XDrawArcs</code> do not draw a pixel more than once. If two arcs join correctly and if the line-width is greater than zero and the arcs intersect, <code>XDrawArc</code> and <code>XDrawArcs</code> do not draw a pixel more than once. Otherwise, the intersecting pixels of intersecting arcs are drawn multiple times. Specifying an arc with one endpoint and a clockwise extent draws the same pixels as specifying the other endpoint and an equivalent counterclockwise extent, except as it affects joins. </p>
<p> If the last point in one arc coincides with the first point in the following arc, the two arcs will join correctly. If the first point in the first arc coincides with the last point in the last arc, the two arcs will join correctly. By specifying one axis to be zero, a horizontal or vertical line can be drawn. Angles are computed based solely on the coordinate system and ignore the aspect ratio. </p>
<p> Both functions use these GC components: function, plane-mask, line-width, line-style, cap-style, join-style, fill-style, subwindow-mode, clip-x-origin, clip-y-origin, and clip-mask. They also use these GC mode-dependent components: foreground, background, tile, stipple, tile-stipple-x-origin, tile-stipple-y-origin, dash-offset, and dash-list. </p>
<p> <code>XDrawArc</code> and <code>XDrawArcs</code> can generate <code>BadDrawable</code>, <code>BadGC</code>, and <code>BadMatch</code> errors.</p>
<h2>Structures</h2>
<p>The <code>XArc</code> structure contains: </p>
<pre>typedef struct {
 short x, y;
 unsigned short width, height;
 short angle1, angle2; /* Degrees * 64 */
} XArc;</pre>
<p>All x and y members are signed integers. The width and height members are 16-bit unsigned integers. You should be careful not to generate coordinates and sizes out of the 16-bit ranges, because the protocol only has 16-bit fields for these values.</p>
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
<p><a href="/docs/linux/man/3-xdrawline/">XDrawLine</a>(3), <a href="/docs/linux/man/3-xdrawpoint/">XDrawPoint</a>(3), <a href="/docs/linux/man/3-xdrawrectangle/">XDrawRectangle</a>(3)<br />
 <i>Xlib &#8211; C Language X Interface</i></p>
