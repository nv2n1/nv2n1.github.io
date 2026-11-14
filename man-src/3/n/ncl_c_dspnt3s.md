---
title: "ncl_c_dspnt3s(3)"
name: "ncl_c_dspnt3s"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_c_dspnt3s/"
---

c_dspnt3s - interpolate single precision 3D data at specified points 

<h2>Function Prototype</h2><pre>void c_dspnt3s(int, float [], float [], float [], float[]
<br>
int, float [], float [], float [], float *, int *);</pre><h2>Synopsis</h2><pre>void c_dspnt3d(int n, float xi[], float yi[], float zi[], float ui[],
<br>
 int m, float xo[], float yo[], float zo[], float *uo,
<br>
 int *ier)</pre><h2>Description</h2><dl COMPACT><dt>n
<dd>The number of input data points.
<dt>xi
<dd>An array containing the X coordinates of the input data points.
<dt>yi
<dd>An array containing the Y coordinates of the input data points.
<dt>zi
<dd>An array containing the Z coordinates of the input data points.
<dt>ui
<dd>An array containing the functional values of the input data points. That is, ui[l] is the value of the input function at coordinate (xi[l],yi[l],zi[l]), for 0 &lt;= l &lt; n .
<dt>m
<dd>The number of output data points (this may be &quot;1&quot;).
<dt>xo
<dd>An array of dimension m containing the X coordinates of the output data. The values in xo may be in any order.
<dt>yo
<dd>An array of dimension m containing the Y coordinates of the output data. The values in xo may be in any order.
<dt>zo
<dd>An array of dimension m containing the Z coordinates of the output data. The values in xo may be in any order.
<dt>uo
<dd>A pointer to a float. Space for m floats is allocated for uo by dspnt3d. zo[i] is the interpolated value at point (xo[i],yo[i],zo[i]) for 0 &lt;= i &lt; n .
<dt>ier
<dd>An error return value. If *ier is returned as 0, then no errors were detected. If *ier is non-zero, then refer to the man page for dsgrid_errors.</dl><h2>Usage</h2>This function is called to interpolate single precision 3D data at a specified point or points.
<h2>Access</h2>To use c_dspnt3s, load the NCAR Graphics library ngmath.
<h2>See Also</h2>dsgrid, dsgrid_params. 

 Complete documentation for Dsgrid is available at URL 
 <a rel="nofollow" HREF="http://ngwww.ucar.edu/ngdoc/ng/ngmath/dsgrid/dshome.html">http://ngwww.ucar.edu/ngdoc/ng/ngmath/dsgrid/dshome.html</a>
<h2>Copyright</h2>Copyright (C) 2000 
 University Corporation for Atmospheric Research 
 

 The use of this Software is governed by a License Agreement.
