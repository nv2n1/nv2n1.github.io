---
title: "ncl_curvs1(3)"
name: "ncl_curvs1"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_curvs1/"
---

CURVS1 - calculate values for a smoothing spline for data in the plane.
<h2>Synopsis</h2>CALL CURVS1 (N,X,Y,D,ISW,S,EPS,PARAM,XS,YS,XSP,YSP, 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>SIGMA,TEMP,IERR) 

 This subroutine calculates certain values that are used by CURVS2 in order to compute an interpolatory smoothing spline under tension through a sequence of data values in the plane. In general this curve will not pass through the original data points. The actual computation of the interpolated values must be done using CURVS2. 

 Three parameters are used to control the degree of smoothness -- D, S, and EPS. 

 The parameter D is a value indicating the degree of confidence in the accuracy of the input function values -- it should be an approximation of the standard deviation of error. Effectively the value of D controls how close the smoothed curve comes to the input data points. If D is small then the interpolated curve will pass close to the input data. The larger the value of D, the more freedom the smooth curve has in how close it comes to the input data values. 

 S is a more subtle global smoothing parameter. S must be non-negative. For small values of S, the interpolated curve approximates the tension spline and for larger values of S, the curve is smoother. A reasonable value for S is REAL(N). 

 EPS controls the precision to which S is interpreted; EPS must be between 0. and 1. inclusive. A reasonable value for EPS is SQRT(2./REAL(N)).
<h2>Description</h2><dl COMPACT><dt>N
<dd>(integer, input) The number of input data values. (N &gt; 1)
<dt>X
<dd>(integer, input) An array containing the X-coordinates for the input data. These need not be increasing.
<dt>Y
<dd>(integer, input) An array containing the Y-coordinates for the input data.
<dt>D
<dd>(integer, input) A user-specified value containing the observed weights. D may be either an array or a scalar, depending on the value of ISW (as described below).
<dt>ISW
<dd>(integer, input) A switch for interpreting the value of D. If ISW=0, then D is an array of length N (D contains an individual error estimate for each input data value); if ISW=1, then D is a scalar that serves as an error estimate for every single data item.
<dt>S
<dd>(integer, input) Contains the value for smoothing. S must be non-negative. Larger values for S yield greater smoothing. A reasonable value is REAL(N).
<dt>EPS
<dd>(integer, input) Contains a tolerance value for the relative precision to which S should be interpreted. EPS must be between 0. and 1. inclusive. A reasonable value is SQRT(2./REAL(N)).
<dt>PARAM
<dd>(integer, output) PARAM(I) is the arc length of the curve up through point (X(I),Y(I)), divided by the total arc length.
<dt>XS
<dd>(integer, output) An array of length N. Contains the smoothed values.
<dt>XSP
<dd>(integer, output) An array of length N. Contains second derivative information for the X-coordinate values.
<dt>YS
<dd>(integer, output) An array of length N. Contains the smoothed values.
<dt>YSP
<dd>(integer, output) An array of length N. Contains second derivative information for the X-coordinate values.
<dt>SIGMA
<dd>(integer, input) Tension factor. Values near zero result in a cubic spline; large values (e.g. 50) result in nearly a polygonal line. A typical value is 1.
<dt>TEMP
<dd>(integer, input) Scratch space of length at least 19*N.
<dt>IER
<dd>(integer, output) An error return value. If IER is returned as 0, then no errors were detected. 

 = 1 if N is less than 2. 
 = 2 if S is negative. 
 = 3 if EPS is negative or greater than 1. 
 = 5 if D is negative.</dl><h2>Access</h2>To use CURVS1, load the NCAR Graphics library ngmath.
<h2>See Also</h2>curvs2, fitgrid_params. 

 Complete documentation for Fitgrid is available at URL 
 <a rel="nofollow" HREF="http://ngwww.ucar.edu/ngdoc/ng/ngmath/fitgrid/fithome.html">http://ngwww.ucar.edu/ngdoc/ng/ngmath/fitgrid/fithome.html</a>
<h2>Copyright</h2>Copyright (C) 2000 
 University Corporation for Atmospheric Research 
 

 The use of this Software is governed by a License Agreement.
