---
title: "ncl_curv1(3)"
name: "ncl_curv1"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_curv1/"
---

CURV1 - does set-up for CURV2.
<h2>Synopsis</h2>CALL CURV1 (N, X, Y, SLP1, SLPN, ISLPSW, YP, TEMP, SIGMA, IER)
<h2>Description</h2><dl COMPACT><dt>N
<dd>(integer,input) The number of input data values. (N &gt; 1)
<dt>X
<dd>(real, input) An array containing the abscissae for the input function.
<dt>Y
<dd>(real, input) An array containing the functional values of the input data -- (Y(K) is the functional value at X(K) for K=1,N).
<dt>SLP1
<dd>(real, input) A user-specified value for the desired slope at <a HREF="/docs/linux/man/1-x/">X</a>(1). See ISLPSW below if you want to have a value calculated internally.
<dt>SLPN
<dd>(real, input) A user-specified value for the desired slope at X(N). See ISLPSW below if you want to have a value calculated internally.
<dt>ISLPSW
<dd>(integer, input) A switch to indicate whether the slopes at the end points should be calculated internally. 
 

 = 0 if SLP1 and SLPN are user-specified. 
 = 1 if SLP1 is user-specified, but SLPN is internally calculated. 
 = 2 if SLPN is user-specified, but SLP1 is internally calculated. 
 = 3 if SLP1 and SLPN are internally calculated. 
 

<dt>YP
<dd>(real, output) Contains values for the second derivative (CURV1 computes these).
<dt>TEMP
<dd>(real, input) Scratch space.
<dt>SIGMA
<dd>(real, input) Tension factor. Values near zero result in a cubic spline; large values (e.g. 50) result in nearly a polygonal line. A typical value is 1.
<dt>IER
<dd>(integer, output) An error return value. If IER is returned as 0, then no errors were detected. 
 

 = 1 if N is less than 2. 
 = 2 if X values are not strictly increasing.</dl><h2>Access</h2>To use CURV1, load the NCAR Graphics library ngmath.
<h2>See Also</h2>curv2, fitgrid_params. 

 Complete documentation for Fitgrid is available at URL 
 <a rel="nofollow" HREF="http://ngwww.ucar.edu/ngdoc/ng/ngmath/fitgrid/fithome.html">http://ngwww.ucar.edu/ngdoc/ng/ngmath/fitgrid/fithome.html</a>
<h2>Copyright</h2>Copyright (C) 2000 
 University Corporation for Atmospheric Research 
 

 The use of this Software is governed by a License Agreement.
