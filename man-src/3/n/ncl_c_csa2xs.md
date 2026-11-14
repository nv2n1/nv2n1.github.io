---
title: "ncl_c_csa2xs(3)"
name: "ncl_c_csa2xs"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_c_csa2xs/"
---

c_csa2xs - cubic spline approximation, expanded entry for two-dimensional input, gridded output
<h2>Function Prototype</h2><pre>float *c_csa2xs(int, float [], float [], float [], float [], int [], float,
 int [], int, int, float [], float [], int *);</pre><h2>Synopsis</h2><pre>int c_csa2xs(int ni, float xi[], float yi[], float zi[], float wts[],
 int knots[2], float smth, int nderiv[2], int no, int mo, 
 float xo[], float yo[], int *ier);</pre><h2>Description</h2><dl COMPACT><dt>ni
<dd>(integer,input) The number of input data points. It must be that ni is greater than 3 and, depending on the size of knots below, n may have to be larger.
<dt>xi
<dd>(real, input) An array dimensioned for ni containing the X coordinate values for the input function.
<dt>yi
<dd>(real, input) An array dimensioned for ni containing the Y coordinate values for the input function.
<dt>zi
<dd>(real, input) An array containing the functional values of the input function -- zi[k] is the functional value at (xi[k], yi[k]) for k=0,ni-1.
<dt>wts
<dd>(real, input) An array containing weights for the zi values at the input xi values, that is, wts[l] is a weight for the value of zi[l] for l=0,ni-1. If you do not desire to weight the input zi values, then set wts[0] to -1. The weights in the wts array are relative and may be set to any non-negative value. When c_csa2xs is called, the weights are summed and the individual weights are normalized so that the weight sum is unity.
<dt>knots
<dd>(integer, input) The number of knots to be used in each coordinate direction in constructing the approximation spline. knots must be at least 4. The larger the value for knots, the closer the approximated curve will come to passing through the input function values.
<dt>smth
<dd>(real, input) A parameter that controls extrapolation into data sparse regions. If smth is zero, then nothing special is done in data sparse regions. A good first choice for smth is 1.
<dt>nderiv
<dd>(real, input) For each of the two coordinate direction, specifies whether you want functional values (nderiv=0), first derivative values (nderiv=1), or second derivative values (nderiv=2). For example, if nderiv[0]=1 and nderiv[1]=1, then the second order mixed partial would be computed.
<dt>no
<dd>(integer, input) The number of X coordinate values to be calculated for the output surface.
<dt>mo
<dd>(integer, input) The number of Y coordinate values to be calculated for the output surface.
<dt>xo
<dd>(real, input) An array dimensioned for no containing the X coordinate values for the output grid.
<dt>yo
<dd>(real, output) An array dimensioned for mo containing the Y coordinates of the output grid.
<dt>ier
<dd>(pointer to integer, output) An error return value. If *ier is returned as 0, then no errors were detected. If *ier is non-zero, then refer to the error list in the error table for details.</dl><h2>Usage</h2>c_csa2xs is called to find an approximating cubic spline surface for two-dimensional input data. c_csa2xs is called if you want to weight the input data values, calculate derivatives, or handle data sparse areas specially. If you do not want to do any of these three things, then use c_csa2s. 

 c_csa2xs returns a pointer to a linear array of data that is the approximated grid stored in row-major order. That is, if out is declared as 

 <pre> float *out;</pre>and we set: 

 <pre>out = c_csa2xs(ni, xi, yi, zi, wts, knots, smth, nderiv, 
 no, mo, xo, yo, &amp;ier);</pre>then out[i*mo+j] is the approximated function value at coordinate point (xo[i], yo[j]) for 0 &lt;= i &lt; no and 0 &lt;= j &lt; mo. The space for out is allocated internal to c_csa2xs and is no * mo floats in size.
<h2>Access</h2>To use c_csa2xs, load the NCAR Graphics library ngmath.
<h2>See Also</h2>csagrid, c_csa2s, c_csa2ls, c_csa2lxs 

 Complete documentation for Csagrid is available at URL 
 <a rel="nofollow" HREF="http://ngwww.ucar.edu/ngdoc/ng/ngmath/csagrid/csahome.html">http://ngwww.ucar.edu/ngdoc/ng/ngmath/csagrid/csahome.html</a>
<h2>Copyright</h2>Copyright (C) 2000 
 University Corporation for Atmospheric Research 
 

 The use of this Software is governed by a License Agreement.
