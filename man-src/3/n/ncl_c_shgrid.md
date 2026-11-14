---
title: "ncl_c_shgrid(3)"
name: "ncl_c_shgrid"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_c_shgrid/"
---

c_shgrid - interpolate random data in 3-space using a modified Shepard's algorithm
<h2>Function Prototype</h2><pre>float *c_shgrid(int, float [], float [], float [], float [],
 int, int, int, float [], float [], float [], int*);</pre><h2>Synopsis</h2><pre>float *c_shgrid (n, x[], y[], z[], f[], nxo, nyo, nzo, 
 xo[], yo[], zo[], ier);</pre><h2>Description</h2><dl COMPACT><dt>n
<dd>(integer,input) The number of input data points (n &gt; 9).
<dt>xi
<dd>(float, input) An array dimensioned for n containing the X coordinate values for the input function.
<dt>yi
<dd>(float, input) An array dimensioned for n containing the Y coordinate values for the input function.
<dt>zi
<dd>(float, input) An array dimensioned for n containing the Z coordinate values for the input function.
<dt>f
<dd>(float, input) An array containing the functional values of the input function -- f[k] is the functional value at (xi[k], yi[k], zi[k]) for k=0,n-1.
<dt>nxo
<dd>(integer, input) The number of X coordinate values to be calculated for the output grid.
<dt>nyo
<dd>(integer, input) The number of Y coordinate values to be calculated for the output grid.
<dt>nzo
<dd>The number of Z coordinate values to be calculated for the output grid.
<dt>xo
<dd>(float, input) An array dimensioned for nxo containing the X coordinates of the output grid.
<dt>yo
<dd>(float, output) An array dimensioned for nyo containing the Y coordinates of the output grid.
<dt>zo
<dd>(float, output) An array dimensioned for nzo containing the Z coordinates of the output grid.
<dt>ier
<dd>(pointer to integer, output) An error return value. If *ier is returned as 0, then no errors were detected. If *ier is non-zero, then refer to the error list in the error table for details.</dl><h2>Usage</h2>c_shgrid is called to interpolate randomly spaced data in 3-space. c_shgrid uses a modified Shepard's algorithm to construct an interpolatory surface. 

 c_shgrid returns a pointer to a linear array of data that is the interpolation grid stored in row-major order. That is, if out is declared as 

 <pre> float *out;</pre>and we set: 

 <pre> out = c_shgrid(n, x, y, z, f, nxo, nyo, nzo, xo, yo, zo, ier);</pre>then out[nz*ny*i + nz*j + k] is the approximation function value at coordinate point (xo[i], yo[j], zo[k]) for 0 &lt;= i &lt; nx, 0 &lt;= j &lt; ny, and 0 &lt;= k &lt; nz. The space for out is allocated internal to c_shgrid and is nx*ny*nz floats in size.
<h2>Access</h2>To use c_shgrid, load the NCAR Graphics library ngmath.
<h2>See Also</h2>shgrid_params, c_shseti, c_shgeti, c_shgetnp. 

 Complete documentation for Shgrid is available at URL 
 <a rel="nofollow" HREF="http://ngwww.ucar.edu/ngdoc/ng/ngmath/shgrid/shhome.html">http://ngwww.ucar.edu/ngdoc/ng/ngmath/shgrid/shhome.html</a>
<h2>Copyright</h2>Copyright (C) 1997-2000 
 University Corporation for Atmospheric Research 
 

 The use of this Software is governed by a License Agreement.
