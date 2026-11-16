---
title: "ncl_curvs2(3)"
name: "ncl_curvs2"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_curvs2/"
---

CURVS2 - calculates an interpolated value for a smoothing spline under tension at a given point.
<h2>Synopsis</h2>FUNCTION CURVS2(T,N,PARAM,X,Y,XP,YP,SIGMA,XO,YO) 

 This subroutine is a companion to CURV1S which must be called before calling this subroutine. CURV2S calculates an interpolated value for a smoothing spline under tension at a given point.
<h2>Description</h2><dl COMPACT><dt>T
</dt><dd>(real, input) A real value to be mapped onto the interpolating curve. Values of T between zero and one interpolate the original data; any values of T outside this range result in extrapolation.
</dd><dt>N
</dt><dd>(integer, input) The number of points which were specified to determine the curve in CURVS1.
</dd><dt>PARAM
</dt><dd>(real, input) The arc lengths as computed by CURVS1.
</dd><dt>X
</dt><dd>(real, input) An array containing the X-coordinate values of the specified points.
</dd><dt>Y
</dt><dd>(real, input) An array containing the Y-coordinate values of the specified points.
</dd><dt>XP
</dt><dd>(real, input) An array of second derivative values as calculated by CURVS1.
</dd><dt>YP
</dt><dd>(real, input) An array of second derivative values as calculated by CURVS1.
</dd><dt>SIGMA
</dt><dd>(real, input) Tension factor. Values near zero result in a cubic spline; large values (e.g. 50) result in nearly a polygonal line. A typical value is 1.
</dd><dt>XO
</dt><dd>(real, output) The interpolated X value.
</dd><dt>YO
</dt><dd>(real, output) The interpolated Y value.</dd></dl><h2>Access</h2>To use CURV2, load the NCAR Graphics library ngmath.
<h2>See Also</h2>curvs1, fitgrid_params. 

 Complete documentation for Fitgrid is available at URL 
 <a rel="nofollow" HREF="http://ngwww.ucar.edu/ngdoc/ng/ngmath/fitgrid/fithome.html">http://ngwww.ucar.edu/ngdoc/ng/ngmath/fitgrid/fithome.html</a>
<h2>Copyright</h2>Copyright (C) 2000 
 University Corporation for Atmospheric Research 
 

 The use of this Software is governed by a License Agreement.
