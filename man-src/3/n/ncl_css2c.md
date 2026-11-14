---
title: "ncl_css2c(3)"
name: "ncl_css2c"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_css2c/"
---

CSS2C - convert from Cartesian to lat/lon coordinates
<h2>Synopsis</h2>CALL CSS2C (N, RLAT, RLON, X, Y, Z)
<h2>Description</h2><dl COMPACT><dt>N
<dd>(integer, input) The number of coordinates to convert.
<dt>RLAT
<dd>(real, input) The latitudes of the input coordinates, in degrees.
<dt>RLON
<dd>(real, input) The longitudes of the input coordinates, in degrees.
<dt>X,Y,Z
<dd>(real, output) The Cartesian coordinates of the output points.</dl><h2>Usage</h2>CSS2C is called to find equivalent Cartesian coordinates on the unit sphere to latitude and longitude coordinates. The coordinate 0. degrees latitude and 0. degrees longitude is mapped to the Cartesian coordinate (1., 0.,0.).
<h2>Access</h2>To use CSS2C, load the NCAR Graphics library ngmath.
<h2>See Also</h2>css_overview, cssgrid, csc2s. 

 Complete documentation for Cssgrid is available at URL 
 <a rel="nofollow" HREF="http://ngwww.ucar.edu/ngdoc/ng/ngmath/cssgrid/csshome.html">http://ngwww.ucar.edu/ngdoc/ng/ngmath/cssgrid/csshome.html</a>
<h2>Copyright</h2>Copyright (C) 2000 
 University Corporation for Atmospheric Research 
 

 The use of this Software is governed by a License Agreement.
