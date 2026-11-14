---
title: "ncl_c_nnpntinits(3)"
name: "ncl_c_nnpntinits"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_c_nnpntinits/"
---

c_nnpntinits - Enter single point mode 

<h2>Function Prototype</h2>void c_nnpntinits(int, float [], float [], float []);
<h2>Synopsis</h2>void c_nnpntinits (npnts, x, y, z);
<h2>Description</h2><dl COMPACT><dt>npnts
<dd>The number of input data points. (npnts &gt; 2)
<dt>x
<dd>An array of size npnts containing the X coordinates of the input data points.
<dt>y
<dd>An array of size npnts containing the Y coordinates of the input data points.
<dt>z
<dd>An array of size npnts containing the functional values of the input data points. That is, z[n] is the value of the input function at coordinate (x[n],y[n]), for 0 &lt;= n &lt; npnts.</dl><h2>Usage</h2>This function is invoked when you want to interpolate at individal points. It is an initialization routine that sets up some internal variables and does this initial triangulation. To actually do the interplation, use function c_nnpnts. To terminate single point mode, use the function c_nnpntend.
<h2>Access</h2>To use c_nnpntinits, load the NCAR Graphics library ngmath.
<h2>See Also</h2>natgrid, natgrid_params, c_natgrids, c_nnpnts, c_nnpntend. 

 Complete documentation for Natgrid is available at URL 
 <a rel="nofollow" HREF="http://ngwww.ucar.edu/ngdoc/ng/ngmath/natgrid/nnhome.html">http://ngwww.ucar.edu/ngdoc/ng/ngmath/natgrid/nnhome.html</a>
<h2>Copyright</h2>Copyright (C) 2000 
 University Corporation for Atmospheric Research 
 

 The use of this Software is governed by a License Agreement.
