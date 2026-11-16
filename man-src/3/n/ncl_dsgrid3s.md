---
title: "ncl_dsgrid3s(3)"
name: "ncl_dsgrid3s"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_dsgrid3s/"
---

DSGRID3S - single precision Fortran entry for 3D gridding
<h2>Synopsis</h2>CALL DSGRID3S (NPNTS, X, Y, Z, U, NUMXOUT, NUMYOUT, NUMZOUT, XO, YO, ZO, UO, IER)
<h2>Description</h2><dl COMPACT><dt>NPNTS
</dt><dd>(Integer, Input) - The number of input data points.
</dd><dt>X
</dt><dd>(Real, Input) - An array containing the X coordinates of the input data points.
</dd><dt>Y
</dt><dd>(Real, Input) - An array containing the Y coordinates of the input data points.
</dd><dt>Z
</dt><dd>(Real, Input) - An array containing the Z coordinates of the input data points.
</dd><dt>U
</dt><dd>(Real, Input) - An array containing the functional values of the input data points. That is, U(L) is the value of the input function at coordinate (X(L),Y(L),Z(L)), for L=1,NPNTS.
</dd><dt>NUMXOUT
</dt><dd>(Integer, Input) - The number of X values in the output grid.
</dd><dt>NUMYOUT
</dt><dd>(Integer, Input) - The number of Y values in the output grid.
</dd><dt>NUMZOUT
</dt><dd>(Integer, Input) - The number of Z values in the output grid.
</dd><dt>XO
</dt><dd>(Real, Input) - An array of dimension NUMXOUT containing the X coordinates of the output data grid. The values in XO must be increasing, but need not be equally spaced.
</dd><dt>YO
</dt><dd>(Real, Input) - An array of dimension NUMYOUT containing the Y coordinates of the output data grid. The values in YO must be increasing, but need not be equally spaced.
</dd><dt>ZO
</dt><dd>(Real, Input) - An array of dimension NUMZOUT containing the Z coordinates of the output data grid. The values in ZO must be increasing, but need not be equally spaced.
</dd><dt>UO
</dt><dd>(Real, Output) - A three-dimensional array dimensioned as UO(NUMXOUT,NUMYOUT,NUMZOUT) containing the interpolated functional values. UO(I,J,K) is the interpolated value at grid point (XO(I),YO(J),ZO(K)).
</dd><dt>IER
</dt><dd>(Integer, Output) - An error return value. If IER is returned as 0, then no errors were detected. If IER is non-zero, then refer to the man page for dsgrid_errors for details.</dd></dl><h2>Usage</h2>DSGRID3S is the single precision gridding function in the Dsgrid package. The behavior of DSGRID3S is controlled by values set for the various parameters described in dsgrid_params. Values for these parameters can be set using the subroutines DSSETI, DSSETR, and DSSETC.
<h2>Access</h2>To use DSGRID3S, load the NCAR Graphics library ngmath.
<h2>See Also</h2>dsgrid, dsgrid_params, dsseti, dsgeti, dssetr, dsgetr, dssetc, dsgetc. 

 Complete documentation for Dsgrid is available at URL 

 <a rel="nofollow" HREF="http://ngwww.ucar.edu/ngdoc/ng/ngmath/dsgrid/dshome.html">http://ngwww.ucar.edu/ngdoc/ng/ngmath/dsgrid/dshome.html</a>
<h2>Copyright</h2>Copyright (C) 2000 
 University Corporation for Atmospheric Research 
 

 The use of this Software is governed by a License Agreement.
