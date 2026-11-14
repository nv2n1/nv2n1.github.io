---
title: "ncl_c_csa2s(3)"
name: "ncl_c_csa2s"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_c_csa2s/"
---

c_csa2s - cubic spline approximation, simple entry for two-dimensional input, gridded output
<h2>Function Prototype</h2><pre>float *c_csa2s(int, float [], float [], float [], int [],
 int, int, float [], float [], int *);</pre><h2>Synopsis</h2><pre>int c_csa2s(int n, float xi[], float yi[], float zi[], int knots[2],
 int no, int mo, float xo[], float yo[], int *ier);</pre><h2>Description</h2><dl COMPACT><dt>n
<dd>(integer,input) The number of input data points. It must be that n is greater than 3 and, depending on the size of knots below, n may have to be larger.
<dt>xi
<dd>(real, input) An array dimensioned for n containing the X coordinate values for the input function.
<dt>yi
<dd>(real, input) An array dimensioned for n containing the Y coordinate values for the input function.
<dt>zi
<dd>(real, input) An array containing the functional values of the input function -- zi[k] is the functional value at (xi[k], yi[k]) for k=0,n-1.
<dt>knots
<dd>(integer, input) The number of knots to be used in each coordinate direction in constructing the approximation spline. knots[0] and knots[1] must be at least 4. The larger the value for knots, the closer the approximated curve will come to passing through the input function values.
<dt>no
<dd>(integer, input) The number of X coordinate values to be calculated for the output surface.
<dt>mo
<dd>(integer, input) The number of Y coordinate values to be calculated for the output surface.
<dt>xo
<dd>(real, input) An array dimensioned for no containing the X coordinates of the output grid.
<dt>yo
<dd>(real, output) An array dimensioned for mo containing the Y coordinates of the output grid.
<dt>ier
<dd>(pointer to integer, output) An error return value. If *ier is returned as 0, then no errors were detected. If *ier is non-zero, then refer to the error list in the error table for details.</dl><h2>Usage</h2>c_csa2s is called to find an approximating cubic spline surface for two-dimensional input data. If you want to weight the input data values, calculate derivatives, or handle data sparse areas specially, then you will need to use c_csa2xs. 

 c_csa2s returns a pointer to a linear array of data that is the approximated grid stored in row-major order. That is, if out is declared as 

 <pre> float *out;</pre>and we set: 

 <pre> out = c_csa2s(n, x, y, z, knots, no, mo, xo, yo, &amp;ier);</pre>then out[i*mo+j] is the approximated function value at coordinate point (xo[i], yo[j]) for 0 &lt;= i &lt; no and 0 &lt;= j &lt; mo. The space for out is allocated internal to c_csa2s and is no * mo floats in size.
<h2>Access</h2>To use c_csa2s, load the NCAR Graphics library ngmath.
<h2>See Also</h2>csagrid, c_csa2xs, c_csa2ls, c_csa2lxs 

 Complete documentation for Csagrid is available at URL 
 <a rel="nofollow" HREF="http://ngwww.ucar.edu/ngdoc/ng/ngmath/csagrid/csahome.html">http://ngwww.ucar.edu/ngdoc/ng/ngmath/csagrid/csahome.html</a>
<h2>Copyright</h2>Copyright (C) 2000 
 University Corporation for Atmospheric Research 
 

 The use of this Software is governed by a License Agreement.
