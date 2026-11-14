---
title: "ncl_c_dspnt2s(3)"
name: "ncl_c_dspnt2s"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_c_dspnt2s/"
---

c_dspnt2s - Interpolate at a single point (or points) in 2D in single precision 

<h2>Function Prototype</h2><pre>void c_dspnt2s(int, float [], float [], float [],
<br>
 int, float [], float [], float *, int *);</pre><h2>Synopsis</h2><pre>void c_dspnt2s (int n, float x[], float y[], float z[], 
<br>
 int m, float xo[], float yo[], float zo, int *ier); </pre><h2>Description</h2><dl COMPACT><dt>n
<dd>The number of input data points.
<dt>x
<dd>An array containing the X coordinates of the input data points.
<dt>y
<dd>An array containing the Y coordinates of the input data points.
<dt>z
<dd>An array containing the functional values of the input data points. That is, z[l] is the value of the input function at coordinate (x[l],y[l]), for 0 &lt;= l &lt; n .
<dt>m
<dd>The number of output data points (this may be &quot;1&quot;).
<dt>xo
<dd>An array of dimension m containing the X coordinates of the output data. The values in xo may be in any order.
<dt>yo
<dd>An array of dimension m containing the Y coordinates of the output data. The values in xo may be in any order.
<dt>zo
<dd>A pointer to a float. Space for m floats is allocated for zo by dspnt2s. zo[i] is the interpolated value at point (xo[i],yo[i]) for 0 &lt;= i &lt; n .
<dt>ier
<dd>An error return value. If *ier is returned as 0, then no errors were detected. If *ier is non-zero, then refer to the man page for dsgrid_errors.</dl><h2>Usage</h2>This function is called when you want to interpolate 2D data at an individual point or points.
<h2>Access</h2>To use c_dspnt2s, load the NCAR Graphics library ngmath.
<h2>See Also</h2>dsgrid, dsgrid_params. 

 Complete documentation for Dsgrid is available at URL 
 <a rel="nofollow" HREF="http://ngwww.ucar.edu/ngdoc/ng/ngmath/dsgrid/dshome.html">http://ngwww.ucar.edu/ngdoc/ng/ngmath/dsgrid/dshome.html</a>
<h2>Copyright</h2>Copyright (C) 2000 
 University Corporation for Atmospheric Research 
 

 The use of this Software is governed by a License Agreement.
