---
title: "ncl_cssgrid(3)"
name: "ncl_cssgrid"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_cssgrid/"
---

CSSGRID - tension spline interpolation on a sphere.
<h2>Synopsis</h2>CALL CSSGRID (N, RLAT, RLON, F, NI, NJ, PLAT, PLON, FF, IWK, RWK, IER)
<h2>Description</h2><dl COMPACT><dt>N
<dd>(integer,input) The number of input data points (N &gt; 2).
<dt>RLAT
<dd>(real, input) An array containing the latitudes of the input data, expressed in degrees. The first three points must not be collinear (lie on a common great circle).
<dt>RLON
<dd>(real, input) An array containing the longitudes of the input data, expressed in degrees.
<dt>F
<dd>(real, input) An array containing data values. F(I) is a functional value at (RLAT(I),RLON(I)) for I = 1 to N.
<dt>NI
<dd>(integer, input) The number of rows in the uniform output grid. NI can be 1.
<dt>NJ
<dd>(integer, input) The number of columns in the uniform output grid. NJ can be 1.
<dt>PLAT
<dd>(real, intput) An array of length NI containing the latitudes the output grid lines. The values in PLAT should be in degrees.
<dt>PLON
<dd>(real, intput) An array of length NJ containing the longitudes the output grid lines. The value in PLON should be in degrees.
<dt>FF
<dd>(real, output) An NI by NJ array containing the desired interpolated values. FF(I,J) is the interpolated value at the coordinate specified by PLAT(I) and PLON(J) for I = 1 to NI and J = 1 to NJ.
<dt>IWK
<dd>(integer, input) An integer workspace of length 27*N.
<dt>RWK
<dd>(double precision, input) A work array dimensioned for 13*N. Note that RWK must be typed DOUBLE PRECISION.
<dt>IER
<dd>(integer, output) An error return value. If IER is returned as 0, then no errors were detected. If IER is non-zero, then refer to the man page for cssgrid_errors for details.</dl><h2>Usage</h2>CSSGRID is called to find an interpolating tension spline for data randomly positioned on a sphere.
<h2>Access</h2>To use CSSGRID, load the NCAR Graphics library ngmath.
<h2>See Also</h2>css_overview, csstri, cssgrid_errors 

 Complete documentation for Cssgrid is available at URL 
 <a rel="nofollow" HREF="http://ngwww.ucar.edu/ngdoc/ng/ngmath/cssgrid/csshome.html">http://ngwww.ucar.edu/ngdoc/ng/ngmath/cssgrid/csshome.html</a>
<h2>Copyright</h2>Copyright (C) 2000 
 University Corporation for Atmospheric Research 
 

 The use of this Software is governed by a License Agreement.
