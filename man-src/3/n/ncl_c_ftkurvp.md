---
title: "ncl_c_ftkurvp(3)"
name: "ncl_c_ftkurvp"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_c_ftkurvp/"
---

c_ftkurvp - interpolation for closed parametric curves
<h2>Function Prototype</h2>int c_ftkurvp (int, float [], float [], int, float [], float [], float []);
<h2>Synopsis</h2>int c_ftkurvp (n, xi, yi, m, t, xo, yo);
<h2>Description</h2><dl COMPACT><dt>n
<dd>The number of input data values. (n &gt; 1)
<dt>xi
<dd>An array containing the abscissae for the input function.
<dt>yi
<dd>An array containing the functional values (y[k] is the functional value at x[k] for k=0,n-1).
<dt>m
<dd>The number of desired interpolated values.
<dt>t
<dd>Contains an array of values for the parameter mapping onto the interpolated curve. Any interval [tt,tt+1.] maps onto the entire curve.
<dt>xo
<dd>An array containing the X values for the interpolated points. t[k] maps to (xo[k],yo[k]) for k=0,m-1.
<dt>yo
<dd>An array containing the Y values for the interpolated points. t[k] maps to (xo[k],yo[k]) for k=0,m-1.</dl><h2>Return Value</h2>c_ftkurvp returns an error value as per: 
 

 = 0 -- no error. 
 = 1 -- if n is less than 2. 
 = 2 -- if adjacent coordinate pairs coincide. 

<h2>Usage</h2>This procedure calculates an interpolatory spline under tension through a sequence of points in the plane forming a closed curve. 

 Given a sequence of distinct input points ( (x[0],y[0]), ... , (x[n-1],y[n-1]), the interpolated curve is parameterized by mapping points in the interval [0.,1.] onto the interpolated curve. The resulting curve has a parametric representation both of whose components are splines under tension and functions of the polygonal arc length. The value 0. is mapped onto (x[0],y[0]) and the value 1. is mapped onto (x[0],y[0]) as well (completing the closed curve). 

 c_ftkurvp is called after all of the desired values for control parameters have been set using the procedures c_ftseti, c_ftsetr, c_ftsetc. The only control parameter that applies to c_ftkurvp is: sig. 

 The value for the parameter sig specifies the tension factor. Values near zero result in a cubic spline; large values (e.g. 50) result in nearly a polygonal line. A typical value is 1. (the default).
<h2>Access</h2>To use c_ftkurvp, load the NCAR Graphics library ngmath.
<h2>See Also</h2>fitgrid_params, c_ftseti, c_ftsetr, c_ftsetc. 

 Complete documentation for Fitgrid is available at URL 
 <a rel="nofollow" HREF="http://ngwww.ucar.edu/ngdoc/ng/ngmath/fitgrid/fithome.html">http://ngwww.ucar.edu/ngdoc/ng/ngmath/fitgrid/fithome.html</a>
<h2>Copyright</h2>Copyright (C) 2000 
 University Corporation for Atmospheric Research 
 

 The use of this Software is governed by a License Agreement.
