---
title: "ncl_c_cssgridd(3)"
name: "ncl_c_cssgridd"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_c_cssgridd/"
---

c_cssgridd - tension spline interpolation on a sphere
<h2>Function Prototype</h2><pre>double *c_cssgridd(int, double [], double [], double [],
<br>
 int, int, double [], double [], int *);</pre><h2>Synopsis</h2><pre>double *c_cssgridd (n, rlat, rlon, f, ni, nj, plat, plon, ier)</pre><h2>Description</h2><dl COMPACT><dt>n
<dd>The number of input data points, n &gt; 2.
<dt>rlat
<dd>An array containing the latitudes of the input data, expressed in degrees. The first three points must not be collinear (lie on a common great circle).
<dt>rlon
<dd>An array containing the longitudes of the input data, expressed in degrees.
<dt>f
<dd>Array containing data values. f[i] is the functional value at (rlat[i],rlon[i]) for i = 0 to n-1.
<dt>ni
<dd>The number of latitudes in the interpolated grid.
<dt>nj
<dd>The number of longitudes in the interpolated grid. ni and nj can both be 1, allowing for interpolation at a single point.
<dt>plat
<dd>An array containing the latitudes of the points where interpolated values are to be computed. The values in plat should be in degrees.
<dt>plon
<dd>An array of length nj containing the longitudes the output grid lines. The values in plon should be in degrees.
<dt>ier
<dd>An error return value. If *ier is returned as 0, then no errors were detected. If *ier is non-zero, then refer to the error list in cssgrid_errors for details.</dl><h2>Usage</h2>c_cssgridd is called to find an interpolating tension spline for randomly positioned data on a unit sphere. c_cssgridd is a double precision version of c_cssgrid.
<h2>Return Value</h2>c_cssgridd returns a pointer to a linear array of data that contains interpolated values at user-specified lat/lon pairs. The returned array stores its values as if they were a 2-dimensional C array with latitude being the first dimension and longitude the second dimension. That is, if out is declared as 

 <pre> double *out;</pre>and we set: 

 <pre> out = c_cssgridd(n, rlat, rlon, f, nlat, nlon, plat, plon, &amp;ier);</pre>then out[i*nlon+j] is the interpolated function value at coordinate point (plat[i], plon[j]) for 0 &lt;= i &lt; nlat and 0 &lt;= j &lt; nlon. The space for out is allocated internal to c_cssgridd and is nlat * nlon doubles in size.
<h2>Access</h2>To use c_cssgridd, load the NCAR Graphics library ngmath.
<h2>See Also</h2>c_cssgrid, css_overview, cssgrid_errors 

 Complete documentation for Cssgrid is available at URL 
 <a rel="nofollow" HREF="http://ngwww.ucar.edu/ngdoc/ng/ngmath/cssgrid/csshome.html">http://ngwww.ucar.edu/ngdoc/ng/ngmath/cssgrid/csshome.html</a>
<h2>Copyright</h2>Copyright (C) 2000 
 University Corporation for Atmospheric Research 
 

 The use of this Software is governed by a License Agreement.
