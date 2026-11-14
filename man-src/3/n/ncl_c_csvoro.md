---
title: "ncl_c_csvoro(3)"
name: "ncl_c_csvoro"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_c_csvoro/"
---

c_csvoro - calculate Voronoi polygons for points on a sphere.
<h2>Function Prototype</h2><pre>void c_csvoro(int, float [], float [], 
<br>
 int, int, float [], float [], float [], 
<br>
 int *, int *, int [], int *);</pre><h2>Synopsis</h2><pre>void *c_csvoro (n, rlat, rlon, ni, nf, plat, plon, rc,
<br>
 nca, numv, nv, ier);</pre><h2>Description</h2><dl COMPACT><dt>n
<dd>The number of input data points, n &gt; 2.
<dt>rlat
<dd>An array containing the latitudes of the input data, expressed in degrees. The first three points must not be collinear (lie on a common great circle).
<dt>rlon
<dd>An array containing the longitudes of the input data, expressed in degrees.
<dt>ni
<dd>The index of the input coordinate for which you want to determine the Voronoi polygon (0 &lt;= ni &lt; n).
<dt>nf
<dd>Flag indicating if this is the first call to c_csvoro to retrieve Voronoi polygons for this dataset (1=yes, 0=no). Calls subsequent to the first call for a given dataset are much faster than the first call.
<dt>plat
<dd>The latitudes for the vertices of the Voronoi polygons. These are circumcenters of circles passing through the Delaunay triangles. If a coordinate is a boundary point, then the circle may pass through certain &quot;pseudo points&quot; that have been added to the original dataset in order to complete the Voronoi polygon.
<dt>plon
<dd>The longitudes for the vertices of the Voronoi polygons.
<dt>rc
<dd>Array containing circumradii (arc lengths in degrees of the angle between a circumcenter and its associated triangle vertices).
<dt>nca
<dd>*nca is the actual number of circumcenters returned in plat and plon. This number may be larger than n if the input dataset has boundary points, since certain &quot;pseudo points&quot; may have been added to the original dataset in order to complete the Voronoi polygon set.
<dt>numv
<dd>*numv is the number of vertices in the Voronoi polygon enclosing the coordinate (rlat[ni],rlon[ni]).
<dt>nv
<dd>An array containing numv indices for the Voronoi polygon enclosing the coordinate (rlat[ni],rlon[ni]). The indices returned in this array refer to the coordinates returned in plat and plon. For example, if the integer &quot;j&quot; is an element of the nv array, then (plat[j],plon[j]) is a vertex of the Voronoi polygon enclosing (rlat[ni],rlon[ni]). The indices in nv list out the vertices of the Voronoi polygon in counter-clockwise order.
<dt>ier
<dd>An error return value. If *ier is returned as 0, then no errors were detected. If *ier is non-zero, then refer to the error list in the error table for details.</dl><h2>Usage</h2>c_csvoro is called if you want to determine the Voronoi polygons for data randomly positioned on a sphere. Each call to c_csvoro calculates the vertices for the Voronoi polygon surrounding a specified input point.
<h2>Access</h2>To use c_csvoro, load the NCAR Graphics library ngmath.
<h2>See Also</h2>css_overview, c_cssgrid, cssgrid_errors 

 Complete documentation for Cssgrid is available at URL 
 <a rel="nofollow" HREF="http://ngwww.ucar.edu/ngdoc/ng/ngmath/cssgrid/csshome.html">http://ngwww.ucar.edu/ngdoc/ng/ngmath/cssgrid/csshome.html</a>
<h2>Copyright</h2>Copyright (C) 2000 
 University Corporation for Atmospheric Research 
 

 The use of this Software is governed by a License Agreement.
