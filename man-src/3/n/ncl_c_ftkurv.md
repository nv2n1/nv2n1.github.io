---
title: "ncl_c_ftkurv(3)"
name: "ncl_c_ftkurv"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_c_ftkurv/"
---

c_ftkurv - interpolation for parametric curves
<h2>Function Prototype</h2>int c_ftkurv (int, float [], float [], int, float [], float [], float []);
<h2>Synopsis</h2>int c_ftkurv (n, xi, yi, m, t, xo, yo);
<h2>Description</h2><dl COMPACT><dt>n
<dd>The number of input data values. (n &gt; 1)
<dt>xi
<dd>An array containing the abscissae for the input function.
<dt>yi
<dd>An array containing the functional values (y[k] is the functional value at x[k] for k=0,n-1).
<dt>m
<dd>The number of desired interpolated values.
<dt>t
<dd>Contains an array of values for the parameter mapping onto the interpolated curve.
<dt>xo
<dd>An array containing the X values for the interpolated points. t[k] maps to (xo[k],yo[k]) for k=0,m-1.
<dt>yo
<dd>An array containing the Y values for the interpolated points. t[k] maps to (xo[k],yo[k]) for k=0,m-1.</dl><h2>Return Value</h2>c_ftkurv returns an error value as per: 
 

 = 0 -- no error. 
 = 1 -- if n is less than 2. 
 = 2 -- if adjacent coordinate pairs coincide. 

<h2>Usage</h2>This function calculates an interpolatory spline under tension through a sequence of points in the plane. 

 Given a sequence of input points ( (x[0],y[0]), ... , (x[n-1],y[n-1]), the interpolated curve is parameterized by mapping points in the interval [0.,1.] onto the interpolated curve. The resulting curve has a parametric representation both of whose components are splines under tension and functions of the polygonal arc length. The value 0. is mapped onto (x[0],y[0]) and the value 1. is mapped onto (x[n-1],y[n-1]). 

 c_ftkurv is called after all of the desired values for control parameters have been set using the procedures c_ftseti, c_ftsetr, c_ftsetc. Control parameters that apply to c_ftkurv are: sig, sl1, sln, sf1. 

 The value for the parameter sig specifies the tension factor. Values near zero result in a cubic spline; large values (e.g. 50) result in nearly a polygonal line. A typical value is 1. (the default). 

 The value for parameter sl1 is in radians and contains the slope at (x[0],y[0]). The angle is measured counter-clockwise from the X axis and the positive sense of the curve is assumed to be that moving from point 0 to point n-1. A value for sl1 may be omitted as indicated by the switch sf1. 

 The value for parameter sln is in radians and contains the slope at (x[n-1],y[n-1]). The angle is measured counter-clockwise from the X axis and the positive sense of the curve is assumed to be that moving from point 0 to point n-1. A value for sln may be omitted as indicated by the switch sf1. 

 The value of sf1 controls whether to use the values for sl1 and sln, or compute those values internally. Specifically, sf1 

 = 0 if sl1 and sln are user-specified. 
 = 1 if sl1 is user-specified, but sln is internally calculated. 
 = 2 if sln is user-specified, but sl1 is internally calculated. 
 = 3 if sl1 and sln are internally calculated. 

<h2>Access</h2>To use c_ftkurv, load the NCAR Graphics library ngmath.
<h2>See Also</h2>fitgrid_params, c_ftseti, c_ftsetr, c_ftsetc. 

 Complete documentation for Fitgrid is available at URL 
 <a rel="nofollow" HREF="http://ngwww.ucar.edu/ngdoc/ng/ngmath/fitgrid/fithome.html">http://ngwww.ucar.edu/ngdoc/ng/ngmath/fitgrid/fithome.html</a>
<h2>Copyright</h2>Copyright (C) 2000 
 University Corporation for Atmospheric Research 
 

 The use of this Software is governed by a License Agreement.
