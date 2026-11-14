---
title: "ncl_csstri(3)"
name: "ncl_csstri"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_csstri/"
---

CSSTRI - calculates a Delaunay triangulation for data on a sphere
<h2>Synopsis</h2>CALL CSSTRI (N, RLAT, RLON, NT, NTRI, IWK, RWK, IER)
<h2>Description</h2><dl COMPACT><dt>N
<dd>(integer,input) The number of input data points (N &gt; 2).
<dt>RLAT
<dd>(real, input) An array containing the latitudes of the input data, expressed in degrees. The first three points must not be collinear (lie on a common great circle).
<dt>RLON
<dd>(real, input) An array containing the longitudes of the input data, expressed in degrees.
<dt>NT
<dd>(integer, output) The number of triangles in the triangulation, unless IER .NE. 0, in which case NT = 0. Where NB is the number of boundary points on the convex hull of the data, if NB .GE. 3, then NT = 2N-NB-2, otherwise NT=2N-4. The input data are considered to be bounded if they all lie in one hemisphere. Dimensioning NT for 2*N will always work.
<dt>NTRI
<dd>(integer, output) A two-dimensional integer array dimensioned for 3 x NT where NT is the number of triangles in the triangulation (NT is at most 2*N). NTRI contains the triangulation data. The vertices of the Kth triangle are: (PLAT(NTRI((1,K)),PLON(NTRI(1,K)), (PLAT(NTRI((2,K)),PLON(NTRI(2,K)), (PLAT(NTRI((3,K)),PLON(NTRI(3,K))
<dt>IWK
<dd>(integer, input) An integer workspace of length 27*N.
<dt>RWK
<dd>(double precision, input) A work array dimensioned for 13*N. Note that this work array must be typed DOUBLE PRECISION.
<dt>IER
<dd>(integer, output) An error return value. If IER is returned as 0, then no errors were detected. If IER is non-zero, then refer to the man page for cssgrid_errors for details.</dl><h2>Usage</h2>CSSTRI is called to find a Delaunay triangulation of data randomly positioned on the surface of a sphere.
<h2>Access</h2>To use CSSTRI, load the NCAR Graphics library ngmath.
<h2>See Also</h2>css_overview, cssgrid, csvoro. 

 Complete documentation for Cssgrid is available at URL 
 <a rel="nofollow" HREF="http://ngwww.ucar.edu/ngdoc/ng/ngmath/cssgrid/csshome.html">http://ngwww.ucar.edu/ngdoc/ng/ngmath/cssgrid/csshome.html</a>
<h2>Copyright</h2>Copyright (C) 2000 
 University Corporation for Atmospheric Research 
 

 The use of this Software is governed by a License Agreement.
