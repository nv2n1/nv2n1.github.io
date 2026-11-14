---
title: "ncl_cssgrid_errors(3)"
name: "ncl_cssgrid_errors"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_cssgrid_errors/"
---

cssgrid_errors - This document briefly describes all the errors reported from Cssgrid. 

<h2>Description</h2>Each entry below includes the error number and its meaning.
<dl COMPACT><dt> 1
<dd>Invalid number of input points (must be greater than 3).
<dt> 2
<dd>Invalid dimension for latitudes in the output grid.
<dt> 3
<dd>Invalid dimension for longitudes in the output grid.
<dt> 4
<dd>First three nodes of input array are collinear.
<dt> 5
<dd>Extrapolation failed due to the uniform grid extending too far beyond the triangulation boundary.
<dt> 6
<dd>Internal algorithm error - please report this.
<dt> 7
<dd>Vertex of a triangle containing an interpolation point is outside its valid range.
<dt> 8
<dd>The angular distance between an interpolated point and the nearest point of the triangulation is at least 90 degrees.
<dt> 9
<dd>Not enough input points to calculate a gradient.
<dt>10
<dd>Insufficient space for the triangulation (must be &gt;= number of boundary nodes minus 2).
<dt>11
<dd>Degenerate triangle (two vertices lie on same geodesic).
<dt>-L
<dd>Coordinates L and M coincide for some M &gt; L &gt;= 1 (coordinate numbering starting at 1).</dl><h2>See Also</h2>css_overview, cssgrid, csstri, csscoord, cstrans, csvoro, c_cssgrid, c_csstri, c_csscoord, c_cstrans, c_csvoro 

 Complete documentation for Cssgrid is available at URL 
 <a rel="nofollow" HREF="http://ngwww.ucar.edu/ngdoc/ng/ngmath/cssgrid/csshome.html">http://ngwww.ucar.edu/ngdoc/ng/ngmath/cssgrid/csshome.html</a>
<h2>Copyright</h2>Copyright (C) 2000 
 University Corporation for Atmospheric Research 
 

 The use of this Software is governed by a License Agreement.
