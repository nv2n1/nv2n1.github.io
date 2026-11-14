---
title: "ncl_natgrids(3)"
name: "ncl_natgrids"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_natgrids/"
---

<pre><code>NATGRIDS - primary single precision Fortran entry for natural neighbor gridding</code></pre>
<h2>Synopsis</h2>CALL NATGRIDS (NPNTS, X, Y, Z, NUMXOUT, NUMYOUT, XI, YI, ZI, IER)
<h2>Description</h2>NPNTS
(Integer, Input) - The number of input data points. (NPNTS &gt; 3).
X
(Real, Input) - An array containing the X coordinates of the input data
points.
Y
(Real, Input) - An array containing the Y coordinates of the input data
points.
Z
(Real, Input) - An array containing the functional values of the
input data points. That is, Z(L) is the value of the input function at
coordinate (X(L),Y(L)), for L=1,NPNTS.
NUMXOUT
(Integer, Input) - The number of X values in the output grid.
NUMYOUT
(Integer, Input) - The number of Y values in the output grid.
XI
(Real, Input) - An array of dimension NUMXOUT containing the X
coordinates of the output data grid. The values in XI must be
increasing, but need not be equally spaced.
YI
(Real, Input) - An array of dimension NUMYOUT containing the Y
coordinates of the output data grid. The values in YI must be
increasing, but need not be equally spaced.
ZI
(Real, Output) -  A two-dimensional array of dimension NUMXOUT x NUMYOUT
containing the interpolated functional values. ZI(I,J) is the interpolated
value at grid point (XI(I),YI(J)).
IER
(Integer, Output) - An error return value. If IER is returned as 0, then
no errors were detected. If IER is non-zero, then refer to the man
page for natgrid_errors for details.
<h2>Usage</h2>NATGRIDS is the single precision gridding function in the Natgrid package. The behavior of NATGRIDS is controlled by values set for the various parameters described in natgrid_params. Values for these parameters can be set using the subroutines NNSETI, NNSETR, and NNSETC.
<h2>Access</h2>To use NATGRIDS, load the NCAR Graphics library ngmath.
<h2>See Also</h2>natgrid, natgrid_params, nnseti, nngeti, nnsetr, nngetr, nnsetc, nngetc. <pre><code>Complete documentation for Natgrid is available at URL

http://ngwww.ucar.edu/ngdoc/ng/ngmath/natgrid/nnhome.html</code></pre>
<h2>Copyright</h2>Copyright (C) 2000 
 University Corporation for Atmospheric Research 
 

 The use of this Software is governed by a License Agreement.
