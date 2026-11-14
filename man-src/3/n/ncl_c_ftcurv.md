---
title: "ncl_c_ftcurv(3)"
name: "ncl_c_ftcurv"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_c_ftcurv/"
---

c_ftcurv - 1D interpolation for non-periodic functions
<h2>Function Prototype</h2>int c_ftcurv (int, float [], float [], int, float [], float []);
<h2>Synopsis</h2>int c_ftcurv (n, xi, yi, m, xo, yo);
<h2>Description</h2><dl COMPACT><dt>n
<dd>The number of input data points. (n &gt; 1)
<dt>xi
<dd>An array containing the abscissae for the input function.
<dt>yi
<dd>An array containing the functional values of the input function -- y(k) is the functional value at x(k) for k=0,n.
<dt>m
<dd>The number of desired interpolated values.
<dt>xo
<dd>An array containing the abscissae for the interpolated values.
<dt>yo
<dd>An array containing the interpolated functional values -- yo(k) is the functional value at xo(k) for k=0,n.</dl><h2>Return Value</h2>c_ftcurv returns an error value as per: 
 

 = 0 -- no error. 
 = 1 -- if n is less than 2. 
 = 2 -- if X values are not strictly increasing. 

<h2>Usage</h2>c_ftcurv is called after all of the desired values for control parameters have been set using the procedures c_ftseti, c_ftsetr, c_ftsetc. Control parameters that apply to c_ftcurv are: sig, sl1, sln, sf1.
<h2>Access</h2>To use c_ftcurv, load the NCAR Graphics library ngmath.
<h2>See Also</h2>fitgrid_params, c_ftseti, c_ftsetr, c_ftsetc. 

 Complete documentation for Fitgrid is available at URL 
 <a rel="nofollow" HREF="http://ngwww.ucar.edu/ngdoc/ng/ngmath/fitgrid/fithome.html">http://ngwww.ucar.edu/ngdoc/ng/ngmath/fitgrid/fithome.html</a>
<h2>Copyright</h2>Copyright (C) 2000 
 University Corporation for Atmospheric Research 
 

 The use of this Software is governed by a License Agreement.
