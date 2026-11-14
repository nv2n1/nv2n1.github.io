---
title: "ncl_c_natgridd(3)"
name: "ncl_c_natgridd"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_c_natgridd/"
---

c_natgrids - primary double precision C entry for natural neighbor gridding
<h2>Function Prototype</h2>double *c_natgridd(int, double [], double [], double [], 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>int, int, double&nbsp;<wbr>[], double&nbsp;<wbr>[], int&nbsp;<wbr>*);
<h2>Synopsis</h2>double *c_natgridd (npnts, x, y, z, numxout, numyout, xi, yi, ier);
<h2>Description</h2><dl COMPACT><dt>npnts
<dd>The number of input data points. (npnts &gt; 3).
<dt>x
<dd>An array containing the x coordinates of the input data points.
<dt>y
<dd>An array containing the y coordinates of the input data points.
<dt>z
<dd>An array containing the functional values of the input data points. That is, z[m] is the value of the input function at coordinate (x[m],y[m]), for 0 &lt;= m &lt; npnts.
<dt>numxout
<dd>The number of x values in the output grid.
<dt>numyout
<dd>The number of y values in the output grid.
<dt>xi
<dd>An array of dimension numxout containing the x coordinates of the output data grid. The values in xi must be increasing, but need not be equally spaced.
<dt>yi
<dd>An array of dimension numyout containing the y coordinates of the output data grid. The values in yi must be increasing, but need not be equally spaced.
<dt>ier
<dd>An error value. If *ier is 0, then no errors were detected. If *ier is non-zero, then refer to the man page for natgrid_errors for details.</dl><h2>Usage</h2>c_natgridd returns a pointer to a linear array of data that is is the interpolated grid stored in row-major order. That is, if out is declared as 

 double *out; 

 and we set: 

 
&nbsp;<wbr>&nbsp;<wbr>out&nbsp;<wbr>=&nbsp;<wbr>c_natgridd(numin, x, y, z, numxout, numyout, xo, yo,&nbsp;<wbr>&amp;ier); 

 then out[i*numyout+j] is the interpolated function value at coordinate point (xo[i],yo[j]) for 0 &lt;= i &lt; numxout and 0 &lt;= j &lt; numyout. The space for out is allocated internal to c_natgrids and is numxout*numyout double values in size.
<h2>Access</h2>To use c_natgridd, load the NCAR Graphics library ngmath.
<h2>See Also</h2>natgrid, natgrid_params, c_nnseti, c_nngeti, c_nnsetrd, c_nngetrd, c_nnsetc, c_nngetc. 

 Complete documentation for Natgrid is available at URL 
 <a rel="nofollow" HREF="http://ngwww.ucar.edu/ngdoc/ng/ngmath/natgrid/nnhome.html">http://ngwww.ucar.edu/ngdoc/ng/ngmath/natgrid/nnhome.html</a>
<h2>Copyright</h2>Copyright (C) 2000 
 University Corporation for Atmospheric Research 
 

 The use of this Software is governed by a License Agreement.
