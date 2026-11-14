---
title: "ncl_natgridd(3)"
name: "ncl_natgridd"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_natgridd/"
---

<pre><code>NATGRIDD - primary double precision Fortran entry for natural neighbor gridding</code></pre>
<h2>Synopsis</h2>CALL NATGRIDD (NPNTS, X, Y, Z, NUMXOUT, NUMYOUT, XI, YI, ZI, IER)
<h2>Description</h2>NPNTS
(Integer, Input) - The number of input data points. (NPNTS &gt; 3).
X
(Double precision, Input) - An array containing the
X coordinates of the input data points.
Y
(Double precision, Input) - An array containing the Y
coordinates of the input data points.
Z
(Double precision, Input) - An array containing the functional values
of the input data points. That is, Z(L) is the value of the input function at
coordinate (X(L),Y(L)), for L=1,NPNTS.
NUMXOUT
(Integer, Input) - The number of X values in the output grid.
NUMYOUT
(Integer, Input) - The number of Y values in the output grid.
XI
(Double precision, Input) - An array of dimension NUMXOUT containing the X
coordinates of the output data grid. The values in XI must be
increasing, but need not be equally spaced.
YI
(Double precision, Input) - An array of dimension NUMYOUT containing the Y
coordinates of the output data grid. The values in YI must be
increasing, but need not be equally spaced.
ZI
(Double precision, Output) -  A two-dimensional array of
dimension NUMXOUT x NUMYOUT
containing the interpolated functional values. ZI(I,J) is the interpolated
value at grid point (XI(I),YI(J)).
IER
(Integer, Output) - An error return value. If IER is returned as 0, then
no errors were detected. If IER is non-zero, then refer to the man
page for natgrid_errors for details.
<h2>Usage</h2>NATGRIDD is the double precision gridding function in the Natgrid package. The behavior of NATGRIDD is controlled by values set for the various parameters described in natgrid_params. Values for these parameters can be set using the subroutines NNSETI, NNSETRD, and NNSETC.
<h2>Access</h2>To use NATGRIDD, load the NCAR Graphics library ngmath.
<h2>See Also</h2>natgrid, natgrid_params, nnseti, nngeti, nnsetrd, nngetrd, nnsetc, nngetc. <pre><code>Complete documentation for Natgrid is available at URL

http://ngwww.ucar.edu/ngdoc/ng/ngmath/natgrid/nnhome.html</code></pre>
<h2>Copyright</h2>Copyright (C) 2000 
 University Corporation for Atmospheric Research 
 

 The use of this Software is governed by a License Agreement.
