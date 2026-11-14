---
title: "ncl_kurv1(3)"
name: "ncl_kurv1"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_kurv1/"
---

KURV1 - calculate values for KURV2 usage
<h2>Synopsis</h2>CALL KURV1 (N, X, Y, SLP1, SLPN, ISLPSW, XP, YP, TEMP, S, SIGMA, IER) 

 This subroutine calculates certain values that are used by KURV2 in order to compute an interpolatory spline under tension through a sequence of points in the plane. The actual computation of the interpolated values must be done using KURV2.
<h2>Description</h2><dl COMPACT><dt>N
<dd>(integer, input) The number of input data values. (N &gt; 1)
<dt>X
<dd>(real, input) An array containing the X values of the points.
<dt>Y
<dd>(real, input) An array containing the Y values of the points. Adjacent pairs of points must be distinct.
<dt>SLP1
<dd>(real, input) A value (in radians) containing the slope at (<a HREF="/docs/linux/man/1-x/">X</a>(1),<a HREF="/docs/linux/man/1-y/">Y</a>(1)). The angles are measured counter-clockwise from the X axis and the positive sense of the curve is assumed to be that moving from point 1 to point N. A value for SLP1 may be omitted as indicated by the switch ISLPSW.
<dt>SLPN
<dd>(real, input) A value (in radians) containing the slope at (X(N),Y(N)). The angles are measured counter-clockwise from the X axis and the positive sense of the curve is assumed to be that moving from point 1 to point N. A value for SLP2 may be omitted as indicated by the switch ISLPSW.
<dt>ISLPSW
<dd>(integer, input) A switch to indicate whether the slopes at the end points should be calculated internally. 

 = 0 if SLP1 and SLPN are user-specified. 
 = 1 if SLP1 is user-specified, but SLPN calculated internally. 
 = 2 if SLPN is user-specified, but SLP1 calculated internally. 
 = 3 if SLP1 and SLPN are internally calculated.
<dt>XP
<dd>(real, output) An array of length N.
<dt>YP
<dd>(real, output) An array of length N.
<dt>TEMP
<dd>(real, input) Scratch space.
<dt>S
<dd>(real, input) An array of length N. On output, S contains the polygonal arclengths of the curve.
<dt>SIGMA
<dd>(real, input) Tension factor. Values near zero result in a cubic spline; large values (e.g. 50) result in nearly a polygonal line. A typical value is 1.
<dt>IER
<dd>(integer, output) An error return value. If IER is returned as 0, then no errors were detected. 

 = 1 if N is less than 2. 
 = 2 if a pair of adjacent points coincide.</dl><h2>Access</h2>To use KURV1, load the NCAR Graphics library ngmath.
<h2>See Also</h2>kurv2, fitgrid_params. 

 Complete documentation for Fitgrid is available at URL 
 <a rel="nofollow" HREF="http://ngwww.ucar.edu/ngdoc/ng/ngmath/fitgrid/fithome.html">http://ngwww.ucar.edu/ngdoc/ng/ngmath/fitgrid/fithome.html</a>
<h2>Copyright</h2>Copyright (C) 2000 
 University Corporation for Atmospheric Research 
 

 The use of this Software is governed by a License Agreement.
