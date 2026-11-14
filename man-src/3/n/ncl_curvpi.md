---
title: "ncl_curvpi(3)"
name: "ncl_curvpi"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_curvpi/"
---

CURVPI - integrate a periodic spline curve
<h2>Synopsis</h2>FUNCTION CURVPI (XL, XU, N, X, Y, P, YP, SIGMA) 

 This function calculates an integral between two specified limits. CURVP1 must be called prior to calling CURVPI, and the values thus obtained used as input to CURVPI. The value of the integral is returned.
<h2>Description</h2><dl COMPACT><dt>XL
<dd>(real, input) The lower limit of the integration.
<dt>XR
<dd>(real, input) The upper limit of the integration.
<dt>N
<dd>(real, input) The number of input data values. (N &gt; 1)
<dt>X
<dd>(real, input) An array containing the abscissae for the input function.
<dt>Y
<dd>(real, input) An array containing the functional values of the input function -- Y(K) is the (real, input) functional value at X(K) for K=1,N.
<dt>P
<dd>(real, input) The period of the function.
<dt>YP
<dd>(real, input) Contains values for the second derivative (as calculated by CURV1).
<dt>SIGMA
<dd>(real, input) Tension factor. Values near zero result in a cubic spline; large values (e.g. 50) result in nearly a polygonal line. A typical value is 1.</dl><h2>Return Value</h2>CURVPI returns the integral of the interpolated curve between the specified limits.
<h2>Access</h2>To use CURVPI, load the NCAR Graphics library ngmath.
<h2>See Also</h2>curv1, fitgrid_params. 

 Complete documentation for Fitgrid is available at URL 
 <a rel="nofollow" HREF="http://ngwww.ucar.edu/ngdoc/ng/ngmath/fitgrid/fithome.html">http://ngwww.ucar.edu/ngdoc/ng/ngmath/fitgrid/fithome.html</a>
<h2>Copyright</h2>Copyright (C) 2000 
 University Corporation for Atmospheric Research 
 

 The use of this Software is governed by a License Agreement.
