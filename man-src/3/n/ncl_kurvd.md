---
title: "ncl_kurvd(3)"
name: "ncl_kurvd"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_kurvd/"
---

KURVD - interpolation and derivatives for parametric curves
<h2>Synopsis</h2>CALL KURVD (T, XS, YS, XST, YST, XSTT, YSTT, N, X, Y, XP, YP, S, SIGMA) 

 This subroutine behaves like KURV2 except that in addition it returns the first and second derivatives of the component functions in the parameterization. The interval [0.,1.] maps onto a curve in the plane. The resulting curve has a parametric representation both of whose components are splines under tension and functions of the polygonal arc length. KURV1 must be called before calling KURVD.
<h2>Description</h2><dl COMPACT><dt>T
<dd>(real,input) A value to be mapped to a point on the curve. The interval [0.,1.] is mapped onto the curve such that 0. is mapped to (<a HREF="/docs/linux/man/1-x/">X</a>(1),<a HREF="/docs/linux/man/1-y/">Y</a>(1)) and 1. is mapped to (X(N),Y(N)). Values outside of [0.,1.] result in extrapolation.
<dt>XS
<dd>(real,output) Contains the X coordinate of the point that T maps to.
<dt>YS
<dd>(real,output) Contains the Y coordinate of the point that T maps to.
<dt>XST
<dd>(real,output) Contains the first derivatives of the X component with respect to T.
<dt>YST
<dd>(real,output) Contains the first derivatives of the Y component with respect to T.
<dt>XSTT
<dd>(real,output) Contains the second derivatives of the X component with respect to T.
<dt>YSTT
<dd>(real,output) Contains the second derivatives of the X component with respect to T.
<dt>N
<dd>(integer,input) The number of input data points. (N &gt; 1)
<dt>X
<dd>(real,input) An array containing the X values of the input points.
<dt>Y
<dd>(real,input) An array containing the Y values of the input points. Adjacent pairs of points must be distinct.
<dt>XP
<dd>(real,input) An array of length N as computed by KURV1.
<dt>YP
<dd>(real,input) An array of length N as computed by KURV1.
<dt>S
<dd>(real,input) An array of length N containing the polygonal arc lengths of the curve, as computed by KURV1.
<dt>SIGMA
<dd>(real,input) Tension factor. Values near zero result in a cubic spline; large values (e.g. 50) result in nearly a polygonal line. A typical value is 1.</dl><h2>Access</h2>To use KURVD, load the NCAR Graphics library ngmath.
<h2>See Also</h2>kurv1,kurv2, fitgrid_params. 

 Complete documentation for Fitgrid is available at URL 
 <a rel="nofollow" HREF="http://ngwww.ucar.edu/ngdoc/ng/ngmath/fitgrid/fithome.html">http://ngwww.ucar.edu/ngdoc/ng/ngmath/fitgrid/fithome.html</a>
<h2>Copyright</h2>Copyright (C) 2000 
 University Corporation for Atmospheric Research 
 

 The use of this Software is governed by a License Agreement.
