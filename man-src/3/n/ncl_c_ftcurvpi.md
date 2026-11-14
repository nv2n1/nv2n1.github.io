---
title: "ncl_c_ftcurvpi(3)"
name: "ncl_c_ftcurvpi"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_c_ftcurvpi/"
---

c_ftcurvpi - calculate integrals for periodic functions
<h2>Function Prototype</h2>int c_ftcurvpi (float, float, float, int, float [], float [], float *);
<h2>Synopsis</h2>int c_ftcurvpi (xl, xr, p, m, xi, yi, integral);
<h2>Description</h2><dl COMPACT><dt>xl
<dd>The lower limit of the integration.
<dt>xr
<dd>The upper limit of the integration.
<dt>p
<dd>The period of the function; p must not be less than xi[n-1] - xi[0].
<dt>m
<dd>The number of input data points. (N &gt; 1)
<dt>xi
<dd>An array containing the abscissae for the input function.
<dt>yi
<dd>An array containing the functional values of the input function (y(k) is the functional value at x(k) for k=0,n).
<dt>integral
<dd>The integral of the function from xl to xr is given by *integral.</dl><h2>Return Value</h2>c_ftcurvpi returns an error value as per: 
 

 = 0 -- no error. 
 = 1 -- if n is less than 2. 
 = 2 -- if the period is strictly less than the span of the abscissae. 

<h2>Usage</h2>c_ftcurvpi is called after all of the desired values for control parameters have been set using the procedures c_ftseti, c_ftsetr, c_ftsetc. Control parameters that apply to c_ftcurvpi are: sig.
<h2>Access</h2>To use c_ftcurvpi, load the NCAR Graphics library ngmath.
<h2>See Also</h2>fitgrid_params, c_ftseti, c_ftsetr, c_ftsetc. 

 Complete documentation for Fitgrid is available at URL 
 <a rel="nofollow" HREF="http://ngwww.ucar.edu/ngdoc/ng/ngmath/fitgrid/fithome.html">http://ngwww.ucar.edu/ngdoc/ng/ngmath/fitgrid/fithome.html</a>
<h2>Copyright</h2>Copyright (C) 2000 
 University Corporation for Atmospheric Research 
 

 The use of this Software is governed by a License Agreement.
