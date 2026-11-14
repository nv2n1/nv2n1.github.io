---
title: "ncl_surf1(3)"
name: "ncl_surf1"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_surf1/"
---

SURF1 - calculate values for SURF2 usage.

<h2>Synopsis</h2>

CALL SURF1 (M, N, X, Y, Z, IZ, ZX1, ZXM, ZY1, ZYN, ZXY11, ZXYM1, ZXY1N, ZXYMN, ISLPSW, ZP, TEMP, SIGMA, IER) 

 This subroutine calculates certain values that are used by SURF2 in order to compute an interpolatory surface passing through a rectangular grid of function values. The surface computed is a tensor product of splines under tension. To calculate actual interpolated values, SURF2 must be called.

<h2>Description</h2>

<dl><dt>M
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
<dt>ZX1
<dd>(real, input) An array containing N X-partial derivatives of the function along the line <a HREF="/docs/linux/man/1-x/">X</a>(1), that is ZX1(J) is the X-partial derivative at point (<a HREF="/docs/linux/man/1-x/">X</a>(1),Y(J)) for J=1,N. This parameter may be defaulted by setting ISLPSW appropriately.
<dt>ZXM
<dd>(real, input) An array containing N X-partial derivatives of the function along the line X(M), that is ZXM(J) is the X-partial derivative at point (X(M),Y(J)) for J=1,N. This parameter may be defaulted by setting ISLPSW appropriately.
<dt>ZY1
<dd>(real, input) An array containing M Y-partial derivatives of the function along the line <a HREF="/docs/linux/man/1-y/">Y</a>(1), that is ZY1(I) is the Y-partial derivative at point (X(I),<a HREF="/docs/linux/man/1-y/">Y</a>(1)) for I=1,M. This parameter may be defaulted by setting ISLPSW appropriately.
<dt>ZYN
<dd>(real, input) An array containing M Y-partial derivatives of the function along the line Y(N), that is ZY1(I) is the Y-partial derivative at point (X(I),Y(N)) for I=1,M. This parameter may be defaulted by setting ISLPSW appropriately.
<dt>ZXY11
<dd>(real, input) The X-Y-partial derivative at (<a HREF="/docs/linux/man/1-x/">X</a>(1),<a HREF="/docs/linux/man/1-y/">Y</a>(1). This parameter may be defaulted by setting ISLPSW appropriately.
<dt>ZXYM1
<dd>(real, input) The X-Y-partial derivative at (X(M),<a HREF="/docs/linux/man/1-y/">Y</a>(1). This parameter may be defaulted by setting ISLPSW appropriately.
<dt>ZXY1N
<dd>(real, input) The X-Y-partial derivative at (<a HREF="/docs/linux/man/1-x/">X</a>(1),Y(N). This parameter may be defaulted by setting ISLPSW appropriately.
<dt>ZXYMN
<dd>(real, input) The X-Y-partial derivative at (X(M),Y(N). This parameter may be defaulted by setting ISLPSW appropriately.
<dt>ISLPSW
<dd>(integer, input) A switch to indicate which boundary derivatives are user supplied and which should be estimated internally. Where I1 = 0 if ZX1 is user-supplied and 1 otherwise. 
 I2 = 0 if ZXM is user-supplied and 1 otherwise. 
 I3 = 0 if ZY1 is user-supplied and 1 otherwise. 
 I4 = 0 if ZYN is user-supplied and 1 otherwise. 
 I5 = 0 if ZXY11 is user-supplied and 1 otherwise. 
 I6 = 0 if ZXYM1 is user-supplied and 1 otherwise. 
 I7 = 0 if ZXY1N is user-supplied and 1 otherwise. 
 I8 = 0 if ZXYMN is user-supplied and 1 otherwise. <pre><code>set ISLPSW = I1 + 2*I2 + 4*I3 +8*I4 +16*I5 +32*I6 + 64*I7 +
128*I8. Then, for example, if ISLPSW=0, then all derivative
information is user-supplied and if ISLPSW=255, then all
derivative information is to be internally estimated.
ZP
(real, output) An array of size M x N x 3. On output this contains partial
derivatives of the surface at the given nodes. ZP is used by
SURF2.
TEMP
(real, input) Scratch space.
SIGMA
(real, input) Tension factor. Values near zero result in a cubic spline;
large values(e.g.50) result in nearly a polygonal line.A typical value
    is 1. IER(integer, output) An error return value.If IER is returned as 0,
    then no errors
    were detected.</code></pre> = 1 if N is less than 2. 
 = 2 if X or Y values are not strictly increasing.</dl>

<h2>Access</h2>

To use SURF1, load the NCAR Graphics library ngmath.

<h2>See Also</h2>

surf2, fitgrid_params. 

 Complete documentation for Fitgrid is available at URL 
 <a rel="nofollow" HREF="http://ngwww.ucar.edu/ngdoc/ng/ngmath/fitgrid/fithome.html">http://ngwww.ucar.edu/ngdoc/ng/ngmath/fitgrid/fithome.html</a>

<h2>Copyright</h2>

Copyright (C) 2000 
 University Corporation for Atmospheric Research 
 

 The use of this Software is governed by a License Agreement.
