---
title: "ncl_c_ftcurvs(3)"
name: "ncl_c_ftcurvs"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_c_ftcurvs/"
---

c_ftcurvs - compute a smoothing spline
<h2>Function Prototype</h2>int c_ftcurvs (int, float [], float [], int, float [], int, float [], float []);
<h2>Synopsis</h2>int c_ftcurvs (n, xi, yi, dflg, d, m, xo, yo);
<h2>Description</h2><dl COMPACT><dt>n
<dd>The number of input data points. (n &gt; 1)
<dt>xi
<dd>An array containing the abscissae for the input function.
<dt>yi
<dd>An array containing the functional values of the input function (yi[k] is the functional value at x[k] for k=0,n-1).
<dt>dflg
<dd>A switch for interpreting the value of d (as described below). If dflg=0, then d is an array of length n (an error estimate for each input data value); if dflg=1, then d is a scalar that serves as an error estimate for every single data item.
<dt>d
<dd>A user-specified value containing the observed weights. d may either be an array or a scalar, depending on the value of dflg.
<dt>m
<dd>The number of output values.
<dt>xo
<dd>Contains the abscissae for the output values.
<dt>yo
<dd>Contains the functional values for the smoothing spline ((yo[k] is the functional value at xo[k] for k=0,n-1).</dl><h2>Return Value</h2>c_ftcurvs returns an error value as per: 
 

 = 1 if n is less than 2. 
 = 2 if smt is negative. 
 = 3 if eps is negative or greater than 1. 
 = 4 if x values are not strictly increasing. 
 = 5 if d is negative. 

<h2>Usage</h2>This function computes an interpolatory smoothing spline under tension through a sequence of functional values. 

 Two parameters and one function argument used to control the degree of smoothness -- the parameters are smt, and eps and the function argument is d. 

 The argument d is a value indicating the degree of confidence in the accuracy of the input function values -- it should be an approximation of the standard deviation of error. Effectively the value of d controls how close the smoothed curve comes to the input data points. If d is small, then the interpolated curve will pass close to the input data. The larger the value of d, the more freedom the smooth curve has in how close it comes to the input data values. 

 The parameter smt is a more subtle global smoothing parameter; smt must be non-negative. For small values of smt, the curve approximates the tension spline and for larger values of smt, the curve is smoother. A reasonable value for smt is (float) n. 

 The parameter eps controls the precision to which smt is interpreted; eps must be between 0. and 1. inclusive. A reasonable value for eps sqrt( 2./(float) n ). 

 c_ftcurvs is called after all of the desired values for control parameters have been set using the procedures c_ftseti, c_ftsetr, c_ftsetc. Control parameters that apply to c_ftcurvs are: sig, smt, eps, sf2. 

 The value for the parameter sig specifies the tension factor. Values near zero result in a cubic spline; large values (e.g. 50) result in nearly a polygonal line. A typical value is 1. (the default).
<h2>Access</h2>To use c_ftcurvs, load the NCAR Graphics library ngmath.
<h2>See Also</h2>fitgrid_params, c_ftseti, c_ftsetr, c_ftsetc. 

 Complete documentation for Fitgrid is available at URL 
 <a rel="nofollow" HREF="http://ngwww.ucar.edu/ngdoc/ng/ngmath/fitgrid/fithome.html">http://ngwww.ucar.edu/ngdoc/ng/ngmath/fitgrid/fithome.html</a>
<h2>Copyright</h2>Copyright (C) 2000 
 University Corporation for Atmospheric Research 
 

 The use of this Software is governed by a License Agreement.
