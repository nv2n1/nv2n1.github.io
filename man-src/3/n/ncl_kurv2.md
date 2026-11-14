---
title: "ncl_kurv2(3)"
name: "ncl_kurv2"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_kurv2/"
---

KURV2 - does interpolation for parametric curves
<h2>Synopsis</h2>CALL KURV2 (T, XS, YS, N, X, Y, XP, YP, S, SIGMA) 

 The interpolated curve is parameterized by mapping points in the interval [0.,1.] onto the interpolated curve. The resulting curve has a parametric representation both of whose components are splines under tension and functions of the polygonal arc length. The value 0. is mapped onto (X[1],Y[1]) and the value 1. is mapped onto (X[N],Y[N]). KURV1 must be called before calling KURV2.
<h2>Description</h2><dl COMPACT><dt>T
<dd>(real, input) A value to be mapped to a point on the curve. The interval [0.,1.] is mapped onto the curve such that 0. is mapped to (<a HREF="/docs/linux/man/1-x/">X</a>(1),<a HREF="/docs/linux/man/1-y/">Y</a>(1)) and 1. is mapped to (X(N),Y(N)). Values outside of [0.,1.] result in extrapolation.
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
<dd>(real, input) An array of length N as computed by KURV1.
<dt>YP
<dd>(real, input) An array of length N as computed by KURV1.
<dt>S
<dd>(real, input) An array of length N containing the polygonal arc lengths of the curve.
<dt>SIGMA
<dd>(real, input) Tension factor. Values near zero result in a cubic spline; large values (e.g. 50) result in nearly a polygonal line. A typical value is 1.</dl><h2>Access</h2>To use KURV2, load the NCAR Graphics library ngmath.
<h2>See Also</h2>kurv1, fitgrid_params. 

 Complete documentation for Fitgrid is available at URL 
 <a rel="nofollow" HREF="http://ngwww.ucar.edu/ngdoc/ng/ngmath/fitgrid/fithome.html">http://ngwww.ucar.edu/ngdoc/ng/ngmath/fitgrid/fithome.html</a>
<h2>Copyright</h2>Copyright (C) 2000 
 University Corporation for Atmospheric Research 
 

 The use of this Software is governed by a License Agreement.
