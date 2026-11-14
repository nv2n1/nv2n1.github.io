---
title: "ncl_kurvp2(3)"
name: "ncl_kurvp2"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_kurvp2/"
---

KURVP2 - does interpolation for closed parametric curves
<h2>Synopsis</h2>CALL KURVP2 (T, XS, YS, N, X, Y, XP, YP, S, SIGMA) 

 The interpolated curve is parameterized by mapping points in the interval [0.,1.] onto an interpolated closed curve. The resulting curve has a parametric representation both of whose components are splines under tension and functions of the polygonal arc length. The value 0. is mapped onto (X[1],Y[1]) and the value 1. is also mapped onto (X[1],Y[1]), since the interpolated curve is closed. KURVP1 must be called before calling KURVP2.
<h2>Description</h2><dl COMPACT><dt>T
<dd>(real,input) A value to be mapped to a point on the curve. The interval [0.,1.] is mapped onto the curve such that 0. is mapped to (<a HREF="/docs/linux/man/1-x/">X</a>(1),<a HREF="/docs/linux/man/1-y/">Y</a>(1)) and 1. is mapped to (<a HREF="/docs/linux/man/1-x/">X</a>(1),<a HREF="/docs/linux/man/1-y/">Y</a>(1)), since the interpolated curve is closed. Any interval [TT,TT+1.] maps onto the entire curve.
<dt>XS
<dd>(real, oputput) Contains the X coordinate of the interpolated point that T maps to.
<dt>YS
<dd>(real, oputput) Contains the Y coordinate of the interpolated point that T maps to.
<dt>N
<dd>(integer, input) The number of input data points. (N &gt; 1)
<dt>X
<dd>(real, input) An array containing the X values of the input points.
<dt>Y
<dd>(real, input) An array containing the Y values of the input points. Adjacent pairs of points must be distinct.
<dt>XP
<dd>(real, input) An array of length N as computed by KURVP1.
<dt>YP
<dd>(real, input) An array of length N as computed by KURVP1.
<dt>S
<dd>(real, input) An array of length N containing the polygonal arc lengths of the curve.
<dt>SIGMA
<dd>(real, input) Tension factor. Values near zero result in a cubic spline; large values (e.g. 50) result in nearly a polygonal line. A typical value is 1.</dl><h2>Access</h2>To use KURVP2, load the NCAR Graphics library ngmath.
<h2>See Also</h2>kurvp1, fitgrid_params. 

 Complete documentation for Fitgrid is available at URL 
 <a rel="nofollow" HREF="http://ngwww.ucar.edu/ngdoc/ng/ngmath/fitgrid/fithome.html">http://ngwww.ucar.edu/ngdoc/ng/ngmath/fitgrid/fithome.html</a>
<h2>Copyright</h2>Copyright (C) 2000 
 University Corporation for Atmospheric Research 
 

 The use of this Software is governed by a License Agreement.
