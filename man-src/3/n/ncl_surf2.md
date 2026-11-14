---
title: "ncl_surf2(3)"
name: "ncl_surf2"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_surf2/"
---

SURF2 - 2D interpolation for gridded data

<h2>Synopsis</h2>

FUNCTION SURF2 (XX, YY, M, N, X, Y, Z, IZ, ZP, SIGMA) 

 This function interpolates a surface value at a specified coordinate using bi-splines under tension. SURF1 must be called before invoking SURF2. The desired interpolated value is returned as the value of the function.

<h2>Description</h2>

<dl><dt>XX
<dd>(real, input) Contains the X coordinate of a point to be mapped onto the interpolated surface.
<dt>YY
<dd>(real, input) Contains the Y coordinate of a point to be mapped onto the interpolated surface.
<dt>M
<dd>(integer, input) The number of grid lines in the X direction. (M &gt; 1)
<dt>N
<dd>(integer, input) The number of grid lines in the Y direction. (N &gt; 1)
<dt>X
<dd>(real, input) An array containing M X coordinates for grid lines in the X direction. These values must be strictly increasing.
<dt>Y
<dd>(real, input) An array containing N Y coordinates for grid lines in the Y direction. These values must be strictly increasing.
<dt>Z
<dd>(real, input) An array containing M x N functional values at the grid points; Z(I,J) contains the functional value at (X(I),Y(J)) for I=1,M and J=1,N.
<dt>IZ
<dd>(integer, input) The row dimension of the matrix Z (IZ is greater than or equal to M).
<dt>ZP
<dd>(real, input) An array of size M x N x 3.
<dt>SIGMA
<dd>(real, input) Tension factor. Values near zero result in a cubic spline; large values (e.g. 50) result in nearly a polygonal line. A typical value is 1.</dl>

<h2>Return Value</h2>

SURF2 returns the interpolated value at the specified point T.

<h2>Access</h2>

To use SURF2, load the NCAR Graphics library ngmath.

<h2>See Also</h2>

surf1, fitgrid_params. 

 Complete documentation for Fitgrid is available at URL 
 <a rel="nofollow" HREF="http://ngwww.ucar.edu/ngdoc/ng/ngmath/fitgrid/fithome.html">http://ngwww.ucar.edu/ngdoc/ng/ngmath/fitgrid/fithome.html</a>

<h2>Copyright</h2>

Copyright (C) 2000 
 University Corporation for Atmospheric Research 
 

 The use of this Software is governed by a License Agreement.
