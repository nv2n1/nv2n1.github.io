---
title: "ncl_dsgrid2s(3)"
name: "ncl_dsgrid2s"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_dsgrid2s/"
---

DSGRID2S - primary single precision Fortran entry for 2D gridding
<h2>Synopsis</h2>CALL DSGRID2S (NPNTS, X, Y, Z, NUMXOUT, NUMYOUT, XO, YO, ZO, IER)
<h2>Description</h2><dl COMPACT><dt>NPNTS
<dd>(Integer, Input) - The number of input data points.
<dt>X
<dd>(Real, Input) - An array containing the X coordinates of the input data points.
<dt>Y
<dd>(Real, Input) - An array containing the Y coordinates of the input data points.
<dt>Z
<dd>(Real, Input) - An array containing the functional values of the input data points. That is, Z(L) is the value of the input function at coordinate (X(L),Y(L)), for L=1,NPNTS.
<dt>NUMXOUT
<dd>(Integer, Input) - The number of X values in the output grid.
<dt>NUMYOUT
<dd>(Integer, Input) - The number of Y values in the output grid.
<dt>XO
<dd>(Real, Input) - An array of dimension NUMXOUT containing the X coordinates of the output data grid. The values in XO must be increasing, but need not be equally spaced.
<dt>YO
<dd>(Real, Input) - An array of dimension NUMYOUT containing the Y coordinates of the output data grid. The values in YO must be increasing, but need not be equally spaced.
<dt>ZO
<dd>(Real, Output) - A two-dimensional array of dimension NUMXOUT x NUMYOUT containing the interpolated functional values. ZO(I,J) is the interpolated value at grid point (XO(I),YO(J)).
<dt>IER
<dd>(Integer, Output) - An error return value. If IER is returned as 0, then no errors were detected. If IER is non-zero, then refer to the man page for dsgrid_errors for details.</dl><h2>Usage</h2>DSGRID2S is the single precision gridding function for 2D data in the Dsgrid package. The behavior of DSGRID2S is controlled by values set for the various parameters described in dsgrid_params. Values for these parameters can be set using the subroutines DSSETI, DSSETR, and DSSETC. 

 In almost all cases the ngmath function NATGRIDS is superior to DSGRID2S for 2D interpolation. See the man page for NATGRIDS for details.
<h2>Access</h2>To use DSGRID2S, load the NCAR Graphics library ngmath.
<h2>See Also</h2>dsgrid, dsgrid_params, dsseti, dsgeti, dssetr, dsgetr, dssetc, dsgetc. 

 Complete documentation for Dsgrid is available at URL 
 <a rel="nofollow" HREF="http://ngwww.ucar.edu/ngdoc/ng/ngmath/dsgrid/dshome.html">http://ngwww.ucar.edu/ngdoc/ng/ngmath/dsgrid/dshome.html</a>
<h2>Copyright</h2>Copyright (C) 2000 
 University Corporation for Atmospheric Research 
 

 The use of this Software is governed by a License Agreement.
