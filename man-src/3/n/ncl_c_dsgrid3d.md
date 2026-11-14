---
title: "ncl_c_dsgrid3d(3)"
name: "ncl_c_dsgrid3d"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_c_dsgrid3d/"
---

c_dsgrid3d - primary double precision C entry for 3D gridding
<h2>Function Prototype</h2><pre>double *c_dsgrid3d(int, double [], double [], double [], double [],
<br>
 int, int, int, double [], double [], double [], int *);</pre><h2>Synopsis</h2><pre>double *c_dsgrid3d(int n, double x[], double y[], double z[], 
<br>
 double u[], int nx, int ny, int nz, double xo[], 
<br>
 double yo[], double zo[], int *ier);</pre><h2>Description</h2><dl COMPACT><dt>n
<dd>The number of input data points.
<dt>x
<dd>An array containing the X coordinates of the input data points.
<dt>y
<dd>An array containing the Y coordinates of the input data points.
<dt>z
<dd>An array containing the Z coordinates of the input data points.
<dt>u
<dd>An array of size n containing the functional values of the input data points. That is, z[m] is the value of the input function at coordinate (x[m],y[m],z[m]), for 0 &lt;= m &lt; n.
<dt>nx
<dd>The number of X values in the output grid.
<dt>ny
<dd>The number of Y values in the output grid.
<dt>nz
<dd>The number of Z values in the output grid.
<dt>xo
<dd>An array of size nx containing the X coordinates of the output data grid. The values in xo must be increasing, but need not be equally spaced.
<dt>yo
<dd>An array of size ny containing the Y coordinates of the output data grid. The values in yo must be increasing, but need not be equally spaced.
<dt>zo
<dd>An array of size nz containing the Z coordinates of the output data grid. The values in zo must be increasing, but need not be equally spaced.
<dt>ier
<dd>An error return value. If *ier is returned as 0, then no errors were detected. If *ier is non-zero, then refer to the man page for dsgrid_errors.</dl><h2>Usage</h2>c_dsgrid3d returns a pointer to a linear array of data that is the interpolated grid stored in row-major order. That is, if out is declared as 

 
&nbsp;<wbr>&nbsp;<wbr>double&nbsp;<wbr>*out; 

 and we set: 

 
&nbsp;<wbr>&nbsp;<wbr>out&nbsp;<wbr>=&nbsp;<wbr>*c_dsgrid3d(n, x, y, z, u, nx, ny, nz, xo, yo, zo, ier); 

 then out[nz*ny*i + nz*j + k] is the interpolated function value at coordinate point (xo[i],yo[j],zo[k]) for 0 &lt;= i &lt; nx, 0 &lt;= j &lt; ny, and 0 &lt;= k &lt; nz. The space for out is allocated internal to c_dsgrid3d and is nx*ny*nz doubles in size.
<h2>Access</h2>To use c_dsgrid3d, load the NCAR Graphics library ngmath.
<h2>See Also</h2>dsgrid, dsgrid_params, c_dsseti, c_dsgeti, c_dssetrd, c_dsgetrd, c_dssetc, c_dsgetc. 

 Complete documentation for Dsgrid is available at URL 
 <a rel="nofollow" HREF="http://ngwww.ucar.edu/ngdoc/ng/ngmath/dsgrid/dshome.html">http://ngwww.ucar.edu/ngdoc/ng/ngmath/dsgrid/dshome.html</a>
<h2>Copyright</h2>Copyright (C) 2000 
 University Corporation for Atmospheric Research 
 

 The use of this Software is governed by a License Agreement.
