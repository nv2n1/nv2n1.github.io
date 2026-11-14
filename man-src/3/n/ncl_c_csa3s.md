---
title: "ncl_c_csa3s(3)"
name: "ncl_c_csa3s"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_c_csa3s/"
---

c_csa3s - cubic spline approximation, simple entry for three-dimensional input, gridded output
<h2>Function Prototype</h2><pre>float *c_csa3s(int, float [], float [], float [], float [], int [], int, int,
 int, float [], float [], float [], int *);</pre><h2>Synopsis</h2><pre>float *c_csa3s (int n, float xi[], float yi[], float zi[],
 float ui[], int knots[3], int nxo, int nyo,
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
<dt>knots
<dd>(integer, input) The number of knots to be used in constructing the approximation spline. knots[0], knots[1] and knots[2] must each be at least 4. The larger the value for knots, the closer the approximated curve will come to passing through the input function values.
<dt>nxo
<dd>(integer, input) The number of X coordinate values to be calculated for the output surface.
<dt>nyo
<dd>(integer, input) The number of Y coordinate values to be calculated for the output surface.
<dt>nzo
<dd>The number of Z coordinate values to be calculated for the output grid.
<dt>xo
<dd>(real, input) An array dimensioned for nxo containing the X coordinates of the output grid.
<dt>yo
<dd>(real, output) An array dimensioned for nyo containing the Y coordinates of the output grid.
<dt>zo
<dd>(real, output) An array dimensioned for nzo containing the Z coordinates of the output grid.
<dt>ier
<dd>(pointer to integer, output) An error return value. If *ier is returned as 0, then no errors were detected. If *ier is non-zero, then refer to the error list in the error table for details.</dl><h2>Usage</h2>c_csa3s is called to find an approximating cubic spline for three-dimensional input data. If you want to weight the input data values, calculate derivatives, or handle data sparse areas specially, then you will need to use c_csa3xs. 

 c_csa3s returns a pointer to a linear array of data that is the approximation spline stored in row-major order. That is, if out is declared as 

 <pre> float *out;</pre>and we set: 

 <pre> out = c_csa3s(n, x, y, z, u, nx, ny, nz, xo, yo, zo, &amp;ier);</pre>then out[nz*ny*i + nz*j + k] is the approximation function value at coordinate point (xo[i], yo[j], zo[k]) for 0 &lt;= i &lt; nx, 0 &lt;= j &lt; ny, and 0 &lt;= k &lt; nz. The space for out is allocated internal to c_csa3s and is nx*ny*nz floats in size.
<h2>Access</h2>To use c_csa3s, load the NCAR Graphics library ngmath.
<h2>See Also</h2>csagrid, c_csa3xs, c_csa3ls, c_csa3lxs 

 Complete documentation for Csagrid is available at URL 
 <a rel="nofollow" HREF="http://ngwww.ucar.edu/ngdoc/ng/ngmath/csagrid/csahome.html">http://ngwww.ucar.edu/ngdoc/ng/ngmath/csagrid/csahome.html</a>
<h2>Copyright</h2>Copyright (C) 2000 
 University Corporation for Atmospheric Research 
 

 The use of this Software is governed by a License Agreement.
