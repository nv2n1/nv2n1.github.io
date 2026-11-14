---
title: "calc_spline(3)"
name: "calc_spline"
section: "3"
letter: "c"
url: "/docs/linux/man/3-calc_spline/"
description: "calc_spline – Calculates a series of values along a Bezier spline. Allegro game programming library."
---

<h2>NAME</h2>
<p> calc_spline &#8211; Calculates a series of values along a Bezier spline. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>void calc_spline(const int points[8], int npts, int *x, int *y);</code></p>
<h2>DESCRIPTION</h2>
<p> Calculates a series of npts values along a Bezier spline, storing them in the output x and y arrays. The Bezier curve is specified by the four x/y control points in the points array: points[0] and points[1] contain the coordinates of the first control point, points[2] and points[3] are the second point, etc. Control points 0 and 3 are the ends of the spline, and points 1 and 2 are guides. The curve probably won&#8217;t pass through points 1 and 2, but they affect the shape of the curve between points 0 and 3 (the lines p0-p1 and p2-p3 are tangents to the spline). The easiest way to think of it is that the curve starts at p0, heading in the direction of p1, but curves round so that it arrives at p3 from the direction of p2. In addition to their role as graphics primitives, spline curves can be useful for constructing smooth paths around a series of control points, as in exspline.c. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-spline/">spline</a></code>(3), <code><a href="/docs/linux/man/3-exspline/">exspline</a></code>(3) </p>
<h2>Index</h2>
