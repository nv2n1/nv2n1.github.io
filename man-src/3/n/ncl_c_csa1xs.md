---
title: "ncl_c_csa1xs(3)"
name: "ncl_c_csa1xs"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_c_csa1xs/"
---

c_csa1xs - cubic spline approximation, expanded entry for one-dimensional input
<h2>Function Prototype</h2><pre>float *c_csa1xs(int, float [], float [], float [], int,
 float, int, int, float [], int *);</pre><h2>Synopsis</h2><pre>float *c_csa1xs(int n, float xi[], float yi[], float wts[],
 int knots, float smth, int nderiv,
 int m, float xo[], int *ier);</pre><h2>Description</h2><dl COMPACT><dt>n
<dd>(integer,input) The number of input data points. It must be that n is greater than 3 and, depending on the size of knots below, n may have to be larger.
<dt>xi
<dd>(real, input) An array dimensioned for n containing the abscissae for the input function.
<dt>yi
<dd>(real, input) An array dimensioned for n containing the functional values of the input function -- yi[k] is the functional value at xi[k] for k=0,n-1.
<dt>wts
<dd>(real, input) An array dimensioned for n containing weights for the yi values at the input xi values, that is, wts[l] is a weight for the value of yi[l] for l=0,n-1. If you do not desire to weight the input yi values, then set wts[0] to -1. The weights in the wts array are relative and may be set to any non-negative value. When c_csa1xs is called, the weights are summed and the individual weights are normalized so that the weight sum is unity.
<dt>knots
<dd>(integer, input) The number of knots to be used in constructing the approximation spline. knots must be at least 4. The larger the value for knots, the closer the approximated curve will come to passing through the input function values.
<dt>smth
<dd>(real, input) A parameter that controls extrapolation into data sparse regions. If smth is zero, then nothing special is done in data sparse regions. A good first choice for smth is 1.
<dt>nderiv
<dd>(integer, input) Specifies whether you want functional values (nderiv=0), first derivative values (nderiv=1), or second derivative values (nderiv=2).
<dt>m
<dd>(integer, input) The number of values to be calculated for the output curve.
<dt>xo
<dd>(real, input) An array dimensioned for m containing the X coordinates of the output curve.
<dt>ier
<dd>(pointer to integer, output) An error return value. If *ier is returned as 0, then no errors were detected. If *ier is non-zero, then refer to the error list in the error table for details.</dl><h2>Usage</h2>c_csa1xs is called to find an approximating cubic spline for one-dimensional input data. c_csa1xs is called if you want to weight the input data values, calculate derivatives, or handle data sparse areas specially. If you do not want to do any of these three things, then use c_csa1s. 

 c_csa1s returns a pointer to a linear array of data that is the approximated curve.
<h2>Access</h2>To use c_csa1xs, load the NCAR Graphics library ngmath.
<h2>See Also</h2>csagrid, c_csa1s, c_csa1ls, c_csa1lxs 

 Complete documentation for Csagrid is available at URL 
 <a rel="nofollow" HREF="http://ngwww.ucar.edu/ngdoc/ng/ngmath/csagrid/csahome.html">http://ngwww.ucar.edu/ngdoc/ng/ngmath/csagrid/csahome.html</a>
<h2>Copyright</h2>Copyright (C) 2000 
 University Corporation for Atmospheric Research 
 

 The use of this Software is governed by a License Agreement.
