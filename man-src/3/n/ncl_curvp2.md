---
title: "ncl_curvp2(3)"
name: "ncl_curvp2"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_curvp2/"
---

CURVP2 - interpolate a periodic function at a specified point
<h2>Synopsis</h2>FUNCTION CURVP2 (T, N, X, Y, P, YP, SIGMA) 

 This function interpolates a value at a specified point using a spline under tension. CURVP1 must be called prior to calling CURVP2, and the values thus obtained used as input to CURVP2. CURVP2 returns the interpolated function value at the X-coordinate specified.
<h2>Description</h2><dl COMPACT><dt>T
</dt><dd>(real, input) The abscissa for which an interpolated function value is desired.
</dd><dt>N
</dt><dd>(integer, input) The number of input data values. (N &gt; 1)
</dd><dt>X
</dt><dd>(real, input) An array containing the abscissae for the input function.
</dd><dt>Y
</dt><dd>(real, input) An array containing the functional values of the input data -- Y(K) is the functional value at X(K) for K=1,N.
</dd><dt>X
</dt><dd>(real, input) The period of the function.
</dd><dt>YP
</dt><dd>(real, input) Contains values for the second derivative (as calculated by CURV1).
</dd><dt>SIGMA
</dt><dd>(real, input) Tension factor. Values near zero result in a cubic spline; large values (e.g. 50) result in nearly a polygonal line. A typical value is 1.</dd></dl><h2>Return Value</h2>CURVP2 returns the interpolated value at the specified point T.
<h2>Access</h2>To use CURVP2, load the NCAR Graphics library ngmath.
<h2>See Also</h2>curvp1, fitgrid_params. 

 Complete documentation for Fitgrid is available at URL 
 <a rel="nofollow" HREF="http://ngwww.ucar.edu/ngdoc/ng/ngmath/fitgrid/fithome.html">http://ngwww.ucar.edu/ngdoc/ng/ngmath/fitgrid/fithome.html</a>
<h2>Copyright</h2>Copyright (C) 2000 
 University Corporation for Atmospheric Research 
 

 The use of this Software is governed by a License Agreement.
