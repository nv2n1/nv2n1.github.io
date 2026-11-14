---
title: "ncl_c_csa3ls(3)"
name: "ncl_c_csa3ls"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_c_csa3ls/"
---

c_csa3ls - cubic spline approximation, simple entry for three-dimensional input, list output
<h2>Function Prototype</h2><pre>float *c_csa3ls(int, float [], float [], float [], float [],
 int [], int, float [], float [], float[], int *);</pre><h2>Synopsis</h2><pre>float *c_csa3ls(int n, float xi[], float yi[], float zi[], float ui[],
 int knots[3], int no, float xo[], float yo[], float zo[], 
 int *);</pre><h2>Description</h2><dl COMPACT><dt>n
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
<dd>(integer, input) The number of knots to be used in constructing the approximation spline. knots[0], knots[1], and knots[2] must be at least 4. The larger the value for knots, the closer the approximated curve will come to passing through the input function values.
<dt>no
<dd>(integer, input) The number of X - Y coordinate values to be calculated for the output array.
<dt>xo
<dd>(real, input) An array dimensioned for no containing the X coordinates of the output list.
<dt>yo
<dd>(real, output) An array dimensioned for no containing the Y coordinates of the output list.
<dt>zo
<dd>(real, output) An array dimensioned for no containing the Z coordinates of the output list.
<dt>ier
<dd>(pointer to integer, output) An error return value. If *ier is returned as 0, then no errors were detected. If *ier is non-zero, then refer to the error list in the error table for details.</dl><h2>Usage</h2>c_csa3ls is called to find values of an approximating cubic spline at specified three-dimensional coordinates. If you want to weight the input data values, calculate derivatives, or handle data sparse areas specially, then you will need to use c_csa3lxs. 

 c_csa3ls returns a pointer to a linear array of data that contains the approximated values calculated at the input list of coordinate values. That is, if out is declared as 

 <pre> float *out;</pre>and we set: 

 <pre> out = c_csa3ls(n, x, y, z, u, knots, no, xo, yo, zo, &amp;ier);</pre>then out[i] is the approximated function value at coordinate point (xo[i], yo[i], zo[i]) for 0 &lt;= i &lt; no. The space for out is allocated internal to c_csa3ls and is no floats in size.
<h2>Access</h2>To use c_csa3ls, load the NCAR Graphics library ngmath.
<h2>See Also</h2>csagrid, c_csa3s, c_csa3xs, c_csa3lxs 

 Complete documentation for Csagrid is available at URL 
 <a rel="nofollow" HREF="http://ngwww.ucar.edu/ngdoc/ng/ngmath/csagrid/csahome.html">http://ngwww.ucar.edu/ngdoc/ng/ngmath/csagrid/csahome.html</a>
<h2>Copyright</h2>Copyright (C) 2000 
 University Corporation for Atmospheric Research 
 

 The use of this Software is governed by a License Agreement.
