---
title: "ncl_csvoro(3)"
name: "ncl_csvoro"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_csvoro/"
---

CSVORO - calculate Voronoi polygons for data on a sphere.
<h2>Synopsis</h2>CALL CSVORO (NPTS, RLATI, RLONI, NI, NF, IWK, RWK, 
 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>NC, RLATO, RLONO, RC,&nbsp;<wbr> 
 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>NCA, NUMV, NV, IER)
<h2>Description</h2><dl COMPACT><dt>NPTS
<dd>(integer,input) The number of input data points (NPTS &gt; 3).
<dt>RLATI
<dd>(real, input) An array containing the latitudes of the input data, expressed in degrees. The first three points must not be collinear (lie on a common great circle).
<dt>RLONI
<dd>(real, input) An array containing the longitudes of the input data, expressed in degrees.
<dt>NI
<dd>(integer, input) The index of the input coordinate for which you want to determine the Voronoi polygon (1 .LE. NI .LE. NPTS).
<dt>NF
<dd>(integer, input) Flag indicating if this is the first call to CSVORO to retrieve Voronoi polygons for this dataset (1=yes, 0=no). Calls subsequent to the first call for a given dataset are much faster than the first call.
<dt>IWK
<dd>(integer, input) Integer work space dimensioned for 27*NPTS.
<dt>RWK
<dd>(double precision, input) A work space dimensioned for 9*NPTS. Note that RWK must be typed DOUBLE PRECISION.
<dt>NC
<dd>(integer, input) The maximum size of the output arrays RLATO, RLONO, and RC. NC should be 2*NPTS.
<dt>RLATO
<dd>(real, output) The latitudes for the vertices of the Voronoi polygons. These are circumcenters of circles passing through the Delaunay triangles. If a coordinate is a boundary point, then the circle may pass through certain &quot;pseudo points&quot; that have been added to the original dataset in order to complete the Voronoi polygon.
<dt>RLONO
<dd>(real, output) The longitudes for the vertices of the Voronoi polygons.
<dt>RC
<dd>(real, output) Array containing circumradii (arc lengths in degrees of the angle between a circumcenter and its associated triangle vertices).
<dt>NCA
<dd>(integer, output) The actual number of circumcenters returned in RLATO and RLONO. This number may be larger than NPTS if the input dataset has boundary points since certain &quot;pseudo points&quot; may have been added to the original dataset in order to complete the Voronoi polygon set.
<dt>NUMV
<dd>(integer, output) The number of vertices in the Voronoi polygon enclosing the coordinate (RLATI(NI),RLONI(NI)).
<dt>NV
<dd>(integer, output) An array (dimensioned for NPTS) containing NUMV indices for the Voronoi polygon enclosing the coordinate (RLATI(NI),RLONI(NI)). The indices returned in this array refer to the coordinates returned in RLATO, RLONO, and RC. For example, if the integer &quot;J&quot; is an element of the NV array, then (RLATO(J),RLONO(J)) is a vertex of the Voronoi polygon enclosing (RLATI(NI),RLONI(NI)). The indices in NV list out the vertices of the Voronoi polygon in counter-clockwise order.
<dt>IER
<dd>(integer, output) An error return value. If IER is returned as 0, then no errors were detected. If IER is non-zero, then refer to the man page for cssgrid_errors for details.</dl><h2>Usage</h2>CSVORO is called if you want to determine the Voronoi polygons for data randomly positioned on a sphere. Each call to CSVORO calculates the vertices for the Voronoi polygon surrounding a specified input point.
<h2>Access</h2>To use CSVORO, load the NCAR Graphics library ngmath.
<h2>See Also</h2>css_overview, csstri, cssgrid. 

 Complete documentation for Cssgrid is available at URL 
 <a rel="nofollow" HREF="http://ngwww.ucar.edu/ngdoc/ng/ngmath/cssgrid/csshome.html">http://ngwww.ucar.edu/ngdoc/ng/ngmath/cssgrid/csshome.html</a>
<h2>Copyright</h2>Copyright (C) 2000 
 University Corporation for Atmospheric Research 
 

 The use of this Software is governed by a License Agreement.
