---
title: "ncl_dspnt2d(3)"
name: "ncl_dspnt2d"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_dspnt2d/"
---

DSPNT2D- Interpolate at a single point (or points) in 2D in double precision
<h2>Synopsis</h2>CALL DSPNT2D (N, X, Y, Z, M, XO, YO, ZO, IER)
<h2>Description</h2><dl COMPACT><dt>N
<dd>(Integer, Input) - The number of input data points.
<dt>X
<dd>(Double precision, Input) - An array containing the X coordinates of the input data points.
<dt>Y
<dd>(Double precision, Input) - An array containing the Y coordinates of the input data points.
<dt>Z
<dd>(Double precision, Input) - An array containing the functional values of the input data points. That is, Z(L) is the value of the input function at coordinate (X(L),Y(L)), for L=1,N.
<dt>M
<dd>(Integer, Input) - The number of output data points (this may be &quot;1&quot;).
<dt>XO
<dd>(Double precision, Input) - An array of dimension M containing the X coordinates of the output data. The values in XO may be in any order.
<dt>YO
<dd>(Double precision, Input) - An array of dimension M containing the Y coordinates of the output data. The values in YO may be in any order.
<dt>ZO
<dd>(Double precision, Output) - An array of dimension M containing the interpolated values. ZO(I) is the interpolated value at point (XO(I),YO(I)) for I=1,M.
<dt>IER
<dd>(Integer, Output) - An error return value. If IER is returned as 0, then no errors were detected. If IER is non-zero, then refer to the man page for dsgrid_errors for details.</dl><h2>Usage</h2>This subroutine is called when you want to interpolate at an individual point or points.
<h2>Access</h2>To use DSPNT2D, load the NCAR Graphics library ngmath.
<h2>See Also</h2>dsgrid, dsgrid_params. 

 Complete documentation for Dsgrid is available at URL 
 <a rel="nofollow" HREF="http://ngwww.ucar.edu/ngdoc/ng/ngmath/dsgrid/dshome.html">http://ngwww.ucar.edu/ngdoc/ng/ngmath/dsgrid/dshome.html</a>
<h2>Copyright</h2>Copyright (C) 2000 
 University Corporation for Atmospheric Research 
 

 The use of this Software is governed by a License Agreement.
