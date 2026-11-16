---
title: "ncl_dspnt2s(3)"
name: "ncl_dspnt2s"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_dspnt2s/"
---

DSPNT2S- Interpolate at a single point (or points) in 2D in single precision
<h2>Synopsis</h2>CALL DSPNT2S (N, X, Y, Z, M, XO, YO, ZO, IER)
<h2>Description</h2><dl COMPACT><dt>N
</dt><dd>(Integer, Input) - The number of input data points.
</dd><dt>X
</dt><dd>(Real, Input) - An array containing the X coordinates of the input data points.
</dd><dt>Y
</dt><dd>(Real, Input) - An array containing the Y coordinates of the input data points.
</dd><dt>Z
</dt><dd>(Real, Input) - An array containing the functional values of the input data points. That is, Z(L) is the value of the input function at coordinate (X(L),Y(L)), for L=1,N.
</dd><dt>M
</dt><dd>(Integer, Input) - The number of output data points (this may be &quot;1&quot;).
</dd><dt>XO
</dt><dd>(Real, Input) - An array of dimension M containing the X coordinates of the output data. The values in XO may be in any order.
</dd><dt>YO
</dt><dd>(Real, Input) - An array of dimension M containing the Y coordinates of the output data. The values in YO may be in any order.
</dd><dt>ZO
</dt><dd>(Real, Output) - An array of dimension M containing the interpolated values. ZO(I) is the interpolated value at point (XO(I),YO(I)) for I=1,M.
</dd><dt>IER
</dt><dd>(Integer, Output) - An error return value. If IER is returned as 0, then no errors were detected. If IER is non-zero, then refer to the man page for dsgrid_errors for details.</dd></dl><h2>Usage</h2>This subroutine is called when you want to interpolate at an individual point or points.
<h2>Access</h2>To use DSPNT2S, load the NCAR Graphics library ngmath.
<h2>See Also</h2>dsgrid, dsgrid_params. 

 Complete documentation for Dsgrid is available at URL 
 <a rel="nofollow" HREF="http://ngwww.ucar.edu/ngdoc/ng/ngmath/dsgrid/dshome.html">http://ngwww.ucar.edu/ngdoc/ng/ngmath/dsgrid/dshome.html</a>
<h2>Copyright</h2>Copyright (C) 2000 
 University Corporation for Atmospheric Research 
 

 The use of this Software is governed by a License Agreement.
