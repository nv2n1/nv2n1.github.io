---
title: "ncl_curvd(3)"
name: "ncl_curvd"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_curvd/"
---

CURVD - derivatives for 1D functions.
<h2>Synopsis</h2>FUNCTION CURVD (T, N, X, Y, YP, SIGMA) 

 This function calculates a derivative at a specified point using a spline under tension. CURV1 must be called prior to calling CURVD, and the values thus obtained used as input to CURVD. The derivative value is returned.
<h2>Description</h2><dl COMPACT><dt>T
</dt><dd>(real, input) The abscissa for which an interpolated function value is desired.
</dd><dt>N
</dt><dd>(integer, input) The number of input data values. (N &gt; 1)
</dd><dt>X
</dt><dd>(real, input) An array containing the abscissae for the input function.
</dd><dt>Y
</dt><dd>(real, input) An array containing the functional values of the input data -- Y(K) is the functional value at X(K) for K=1,N.
</dd><dt>YP
</dt><dd>(real, input) Contains values for the second derivative (as calculated by CURV1).
</dd><dt>SIGMA
</dt><dd>(real, input) Tension factor. Values near zero result in a cubic spline; large values (e.g. 50) result in nearly a polygonal line. A typical value is 1.</dd></dl><h2>Return Value</h2>CURVD returns the derivative value of the interpolated curve at the specified point T.
<h2>Access</h2>To use CURVD, load the NCAR Graphics library ngmath.
<h2>See Also</h2>curv1, fitgrid_params. 

 Complete documentation for Fitgrid is available at URL 
 <a rel="nofollow" HREF="http://ngwww.ucar.edu/ngdoc/ng/ngmath/fitgrid/fithome.html">http://ngwww.ucar.edu/ngdoc/ng/ngmath/fitgrid/fithome.html</a>
<h2>Copyright</h2>Copyright (C) 2000 
 University Corporation for Atmospheric Research 
 

 The use of this Software is governed by a License Agreement.
