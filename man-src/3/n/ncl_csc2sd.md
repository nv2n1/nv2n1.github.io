---
title: "ncl_csc2sd(3)"
name: "ncl_csc2sd"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_csc2sd/"
---

CSC2SD - convert from Cartesian to lat/lon coordinates
<h2>Synopsis</h2>CALL CSC2SD (N, X, Y, Z, RLAT, RLON)
<h2>Description</h2><dl COMPACT><dt>N
</dt><dd>(integer, input) The number of coordinates to convert.
</dd><dt>X,Y,Z
</dt><dd>(double precision, input) The Cartesian coordinates of the input points.
</dd><dt>RLAT
</dt><dd>(double precision, output) The latitudes of the output coordinates, in degrees.
</dd><dt>RLON
</dt><dd>(double precision, output) The longitudes of the output coordinates, in degrees.</dd></dl><h2>Usage</h2>CSC2SD is called to find equivalent latitude and longitude coordinates to specified Cartesian coordinates on the unit sphere. The coordinate (1.,0.,0.) is mapped to the latitude/longitude coordinate (0.,0.). The latitude/longitude coordinates are returned in degrees. CSC2SD is a double precision version of CSC2S.
<h2>Access</h2>To use CSC2SD, load the NCAR Graphics library ngmath.
<h2>See Also</h2>css_overview, cssgrid, css2cd, csc2s. 

 Complete documentation for Cssgrid is available at URL 
 <a rel="nofollow" HREF="http://ngwww.ucar.edu/ngdoc/ng/ngmath/cssgrid/csshome.html">http://ngwww.ucar.edu/ngdoc/ng/ngmath/cssgrid/csshome.html</a>
<h2>Copyright</h2>Copyright (C) 2000 
 University Corporation for Atmospheric Research 
 

 The use of this Software is governed by a License Agreement.
