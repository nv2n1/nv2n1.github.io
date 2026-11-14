---
title: "ncl_curv2(3)"
name: "ncl_curv2"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_curv2/"
---

CURV2 - 1D interpolation for non-periodic functions.
<h2>Synopsis</h2>FUNCTION CURV2 (T, N, X, Y, YP, SIGMA) 

 This function interpolates a value at a specified point using a spline under tension. CURV1 must be called prior to calling CURV2, and the values thus obtained used as input to CURV2. CURV2 returns the interpolated function value at the X-coordinate specified.
<h2>Description</h2><dl COMPACT><dt>T
<dd>(real, input) The abscissa for which an interpolated function value is desired.
<dt>N
<dd>(integer, input) The number of input data values. (N &gt; 1)
<dt>X
<dd>(real, input) An array containing the abscissae for the input function.
<dt>Y
<dd>(real, input) An array containing the functional values of the input data -- Y(K) is the functional value at X(K) for K=1,N.
<dt>YP
<dd>(real, input) Contains values for the second derivative (as calculated by CURV1).
<dt>SIGMA
<dd>(real, input) Tension factor. Values near zero result in a cubic spline; large values (e.g. 50) result in nearly a polygonal line. A typical value is 1.</dl><h2>Return Value</h2>CURV2 returns the interpolated value at the specified point T.
<h2>Access</h2>To use CURV2, load the NCAR Graphics library ngmath.
<h2>See Also</h2>curv1, fitgrid_params. 

 Complete documentation for Fitgrid is available at URL 
 <a rel="nofollow" HREF="http://ngwww.ucar.edu/ngdoc/ng/ngmath/fitgrid/fithome.html">http://ngwww.ucar.edu/ngdoc/ng/ngmath/fitgrid/fithome.html</a>
<h2>Copyright</h2>Copyright (C) 2000 
 University Corporation for Atmospheric Research 
 

 The use of this Software is governed by a License Agreement.
