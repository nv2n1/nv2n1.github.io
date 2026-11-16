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
</dt><dd>(integer, input) The number of grid lines in the X direction. (M &gt; 1)
</dd><dt>N
</dt><dd>(integer, input) The number of grid lines in the Y direction. (N &gt; 1)
</dd><dt>X
</dt><dd>(real, input) An array containing M X coordinates for grid lines in the X direction. These values must be strictly increasing.
</dd><dt>Y
</dt><dd>(real, input) An array containing N Y coordinates for grid lines in the Y direction. These values must be strictly increasing.
</dd><dt>Z
</dt><dd>(real, input) An array containing M x N functional values at the grid points; Z(I,J) contains the functional value at (X(I),Y(J)) for I=1,M and J=1,N.
</dd><dt>IZ
</dt><dd>(integer, input) The row dimension of the matrix Z (IZ is greater than or equal to M).
</dd><dt>ZX1
</dt><dd>(real, input) An array containing N X-partial derivatives of the function along the line X(1), that is ZX1(J) is the X-partial derivative at point (X(1),Y(J)) for J=1,N. This parameter may be defaulted by setting ISLPSW appropriately.
</dd><dt>ZXM
</dt><dd>(real, input) An array containing N X-partial derivatives of the function along the line X(M), that is ZXM(J) is the X-partial derivative at point (X(M),Y(J)) for J=1,N. This parameter may be defaulted by setting ISLPSW appropriately.
</dd><dt>ZY1
</dt><dd>(real, input) An array containing M Y-partial derivatives of the function along the line Y(1), that is ZY1(I) is the Y-partial derivative at point (X(I),Y(1)) for I=1,M. This parameter may be defaulted by setting ISLPSW appropriately.
</dd><dt>ZYN
</dt><dd>(real, input) An array containing M Y-partial derivatives of the function along the line Y(N), that is ZY1(I) is the Y-partial derivative at point (X(I),Y(N)) for I=1,M. This parameter may be defaulted by setting ISLPSW appropriately.
</dd><dt>ZXY11
</dt><dd>(real, input) The X-Y-partial derivative at (X(1),Y(1). This parameter may be defaulted by setting ISLPSW appropriately.
</dd><dt>ZXYM1
</dt><dd>(real, input) The X-Y-partial derivative at (X(M),Y(1). This parameter may be defaulted by setting ISLPSW appropriately.
</dd><dt>ZXY1N
</dt><dd>(real, input) The X-Y-partial derivative at (X(1),Y(N). This parameter may be defaulted by setting ISLPSW appropriately.
</dd><dt>ZXYMN
</dt><dd>(real, input) The X-Y-partial derivative at (X(M),Y(N). This parameter may be defaulted by setting ISLPSW appropriately.
</dd><dt>ISLPSW
</dt><dd>(integer, input) A switch to indicate which boundary derivatives are user supplied and which should be estimated internally. Where I1 = 0 if ZX1 is user-supplied and 1 otherwise. 
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
 = 2 if X or Y values are not strictly increasing.</dd></dl>

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
