---
title: "ncl_c_csa3xs(3)"
name: "ncl_c_csa3xs"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_c_csa3xs/"
---

c_csa3xs - cubic spline approximation, expanded entry for three-dimensional input, gridded output
<h2>Function Prototype</h2><pre>loat *c_csa3xs(int, float [], float [], float [], float [], float [],
 int [], float, int [], int, int, int, float [],
 float [], float [], int *);</pre><h2>Synopsis</h2><pre>float *c_csa3xs (int n, float xi[], float yi[], float zi[],
 float ui[], float wts[], int knots[3], float smth,
 int nderiv[3], int nxo, int nyo,
 int nzo, float xo[], float yo[], float zo[], 
 int *ier);</pre><h2>Description</h2><dl COMPACT><dt>n
<dd>(integer,input) The number of input data points. It must be that n is greater than 3 and, depending on the size of knots below, n may have to be larger.
<dt>xi
<dd>(real, input) An array dimensioned for n containing the X coordinate values for the input function.
<dt>yi
<dd>(real, input) An array dimensioned for n containing the Y coordinate values for the input function.
<dt>zi
<dd>(real, input) An array dimensioned for n containing the Z coordinate values for the input function.
<dt>ui
<dd>(real, input) An array containing the functional values of the input function -- ui[k] is the functional value at (xi[k], yi[k], zi[k]) for k=0,n-1.
<dt>wts
<dd>(real, input) An array containing weights for the ui values at the input values, that is, wts[l] is a weight for the value of ui[l] for l=0,n-1. If you do not desire to weight the input ui values, then set wts[0] to -1. The weights in the wts array are relative and may be set to any non-negative value. When c_csa3xs is called, the weights are summed and the individual weights are normalized so that the weight sum is unity.
<dt>knots
<dd>(integer, input) The number of knots to be used in constructing the approximation spline. knots[0], knots[1] and knots[2] must each be at least 4. The larger the value for knots, the closer the approximated curve will come to passing through the input function values.
<dt>smth
<dd>(real, input) A parameter that controls extrapolation into data sparse regions. If smth is zero, then nothing special is done in data sparse regions. A good first choice for smth is 1.
<dt>nderiv
<dd>(integer, input) For each of the two coordinate direction, specifies whether you want functional values (nderiv=0), first derivative values (nderiv=1), or second derivative values (nderiv=2). For example, if nderiv[0]=1 and nderiv[1]=1, then the second order mixed partial would be computed.
<dt>nxo
<dd>(integer, input) The number of X coordinate values to be calculated for the output spline.
<dt>nyo
<dd>(integer, input) The number of Y coordinate values to be calculated for the output spline.
<dt>nzo
<dd>(integer, input) The number of Z coordinate values to be calculated for the output spline.
<dt>xo
<dd>(real, input) An array dimensioned for nxo containing the X coordinates of the output spline.
<dt>yo
<dd>(real, output) An array dimensioned for nyo containing the Y coordinates of the output spline.
<dt>zo
<dd>(real, output) An array dimensioned for nzo containing the Z coordinates of the output spline.
<dt>ier
<dd>(pointer to integer, output) An error return value. If *ier is returned as 0, then no errors were detected. If *ier is non-zero, then refer to the error list in the error table for details.</dl><h2>Usage</h2>c_csa3xs is called to find an approximating cubic spline for three-dimensional input data. c_csa3xs is called if you want to weight the input data values, calculate derivatives, or handle data sparse areas specially. If you do not want to do any of these three things, then use c_csa3s. 

 c_csa3xs returns a pointer to a linear array of data that is the approximation spline stored in row-major order. That is, if out is declared as <pre> float *out;</pre>and we set: 

 <pre>out = c_csa3xs(ni, xi, yi, zi, ui, wts, knots, smth, nderiv,
 nx, ny, nz, xo, yo, zo, &amp;ier)</pre>then out[nz*ny*i + nz*j + k] is the approximation function value at coordinate point (xo[i], yo[j], zo[k]) for 0 &lt;= i &lt; nx, 0 &lt;= j &lt; ny, and 0 &lt;= k &lt; nz. The space for out is allocated internal to c_csa3xs and is nx*ny*nz floats in size. 

<h2>Access</h2>To use c_csa3xs, load the NCAR Graphics library ngmath.
<h2>See Also</h2>csagrid, c_csa3s, c_csa3ls, c_csa3lxs 

 Complete documentation for Csagrid is available at URL 
 <a rel="nofollow" HREF="http://ngwww.ucar.edu/ngdoc/ng/ngmath/csagrid/csahome.html">http://ngwww.ucar.edu/ngdoc/ng/ngmath/csagrid/csahome.html</a>
<h2>Copyright</h2>Copyright (C) 2000 
 University Corporation for Atmospheric Research 
 

 The use of this Software is governed by a License Agreement.
