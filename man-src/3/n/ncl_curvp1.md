---
title: "ncl_curvp1(3)"
name: "ncl_curvp1"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_curvp1/"
---

CURVP1 - calculate values for CURVP2 usage.
<h2>Synopsis</h2>CALL CURVP1 (N, X, Y, P, YP, TEMP, SIGMA, IER) 

 This subroutine calculates certain values that are used by CURVP2 in order to compute an interpolatory spline under tension through a sequence of functional values for a periodic function. The actual computation of the interpolated values must be done using CURVP2 .
<h2>Description</h2><dl COMPACT><dt>N
<dd>(integer, input) The number of input data values. (N &gt; 1)
<dt>X
<dd>(real, input) An array containing the abscissae for the input function.
<dt>Y
<dd>(real, input) An array containing the functional values of the input function -- Y(K) is the functional value at X(K) for K=1,N.
<dt>P
<dd>(real, input) The period of the function. P must be greater than X(N)<a HREF="/docs/linux/man/1--x/">-X</a>(1).
<dt>YP
<dd>(real, output) Contains values for the second derivative (these are calculated by CURVP1).
<dt>TEMP
<dd>(real, input) Scratch space.
<dt>SIGMA
<dd>(integer, input) Tension factor. Values near zero result in a cubic spline; large values (e.g. 50) result in nearly a polygonal line. A typical value is 1.
<dt>IER
<dd>(integer, output) An error return value. If IER is returned as 0, then no errors were detected. 

 
 = 1 if N is less than 2. 
 = 2 if P is less than or equal to X(N)<a HREF="/docs/linux/man/1--x/">-X</a>(1). 
 = 3 if the X values are not strictly increasing.</dl><h2>Access</h2>To use CURVP1, load the NCAR Graphics library ngmath.
<h2>See Also</h2>curvp2, fitgrid_params. 

 Complete documentation for Fitgrid is available at URL 
 <a rel="nofollow" HREF="http://ngwww.ucar.edu/ngdoc/ng/ngmath/fitgrid/fithome.html">http://ngwww.ucar.edu/ngdoc/ng/ngmath/fitgrid/fithome.html</a>
<h2>Copyright</h2>Copyright (C) 2000 
 University Corporation for Atmospheric Research 
 

 The use of this Software is governed by a License Agreement.
