---
title: "ncl_c_csstrid(3)"
name: "ncl_c_csstrid"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_c_csstrid/"
---

c_csstrid - calculates a Delaunay triangulation for data on a sphere
<h2>Function Prototype</h2><pre> int *c_csstrid(int, double [], double [], int *, int *);</pre><h2>Synopsis</h2><pre> int *c_csstrid(n, rlat, rlon, nt, ier);</pre><h2>Description</h2><dl COMPACT><dt>n
<dd>The number of input data points, n &gt; 2.
<dt>rlat
<dd>An array containing the latitudes of the input data, expressed in degrees. The first three points must not be collinear (lie on a common great circle).
<dt>rlon
<dd>An array containing the longitudes of the input data, expressed in degrees.
<dt>nt
<dd>*nt is the number of triangles in the triangulation, unless *ier is non-zero, in which case *nt = 0. Where nb is the number of boundary points on the convex hull of the data, if nb is greater than 3, then *nt = 2n-nb-2, otherwise *nt = 2n-4. The input data are considered to be bounded if they all lie in one hemisphere.
<dt>ier
<dd>An error return value. If *ier is returned as 0, then no errors were detected. If *ier is non-zero, then refer to the error list in cssgrid_errors for details.</dl><h2>Usage</h2>c_csstrid is called to find a Delaunay triangulation of data randomly positioned on the surface of a sphere. c_csstrid is a double precision version of c_csstri.
<h2>Return Value</h2>c_csstrid returns a pointer to a linear array that contains a sequence of integer triples. The elements of a triple are indices of vertices of a triangle. Each index references an original data point as it occurs in sequence in the input data set (numbering starts at 0). For example, if the triple &lt;5,0,2&gt; were in the list of triples, then (rlat[5],rlon[5]), (rlat[0],rlon[0]), and (rlat[2],rlon[2]) would be vertices of a triangle in the Delaunay triangulation.
<h2>Access</h2>To use c_csstrid, load the NCAR Graphics library ngmath.
<h2>See Also</h2>css_overview, c_cssgrid, c_csstri, cssgrid_errors 

 Complete documentation for Cssgrid is available at URL 
 <a rel="nofollow" HREF="http://ngwww.ucar.edu/ngdoc/ng/ngmath/cssgrid/csshome.html">http://ngwww.ucar.edu/ngdoc/ng/ngmath/cssgrid/csshome.html</a>
<h2>Copyright</h2>Copyright (C) 2000 
 University Corporation for Atmospheric Research 
 

 The use of this Software is governed by a License Agreement.
