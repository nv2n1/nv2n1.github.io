---
title: "ncl_kurvp1(3)"
name: "ncl_kurvp1"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_kurvp1/"
---

KURVP1 - calculate values for KURVP2 usage
<h2>Synopsis</h2>CALL KURVP1 (N, X, Y, XP, YP, TEMP, S, SIGMA, IER) 

 This subroutine calculates certain values that are used by KURVP2 in order to compute an interpolatory spline under tension through a sequence of points in the plane that form a closed curve. The actual computation of the interpolated values must be done using KURVP2 .
<h2>Description</h2><dl COMPACT><dt>N
<dd>(integer,input) The number of input data points. (N &gt; 1)
<dt>X
<dd>(real,input) An array containing the X values of the points.
<dt>Y
<dd>(real,input) An array containing the Y values of the points. Adjacent pairs of points must be distinct.
<dt>XP
<dd>(real,output) An array of length N.
<dt>YP
<dd>(real,output) An array of length N.
<dt>TEMP
<dd>(real,input) Scratch space.
<dt>S
<dd>(real,output) An array of length N (this will be used to pass to KURVP2).
<dt>SIGMA
<dd>(real,input) Tension factor. Values near zero result in a cubic spline; large values (e.g. 50) result in nearly a polygonal line. A typical value is 1.
<dt>IER
<dd>(integer,output) An error return value. If IER is returned as 0, then no errors were detected. 

 = 1 if N is less than 2. 
 = 2 if a pair of adjacent points coincide.</dl><h2>Access</h2>To use KURVP1, load the NCAR Graphics library ngmath.
<h2>See Also</h2>kurvp2, fitgrid_params. 

 Complete documentation for Fitgrid is available at URL 
 <a rel="nofollow" HREF="http://ngwww.ucar.edu/ngdoc/ng/ngmath/fitgrid/fithome.html">http://ngwww.ucar.edu/ngdoc/ng/ngmath/fitgrid/fithome.html</a>
<h2>Copyright</h2>Copyright (C) 2000 
 University Corporation for Atmospheric Research 
 

 The use of this Software is governed by a License Agreement.
