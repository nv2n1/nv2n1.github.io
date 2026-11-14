---
title: "ncl_css2cd(3)"
name: "ncl_css2cd"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_css2cd/"
---

CSS2CD - convert from lat/lon coordinates to Cartesian coordinates.
<h2>Synopsis</h2>CALL CSS2CD (N, RLAT, RLON, X, Y, Z)
<h2>Description</h2><dl COMPACT><dt>N
<dd>(integer, input) The number of input lat/lon coordinates.
<dt>RLAT
<dd>(double precision, input) An array containing the latitudes of the input coordinates.
<dt>RLON
<dd>(double precision, input) An array containing the longitudes of the input coordinates.
<dt>X
<dd>(double precision, output) An array containing the X component of the Cartesian coordinates of the output data. (X(I),Y(I),Z(I)) is the Cartesian coordinate corresponding to the lat/lon coordinate (RLAT(I),RLON(I)) for I=1 to N.
<dt>Y
<dd>(double precision, output) An array containing the Y component of the Cartesian coordinates of the output data. (X(I),Y(I),Z(I)) is the Cartesian coordinate corresponding to the lat/lon coordinate (RLAT(I),RLON(I)) for I=1 to N.
<dt>Z
<dd>(double precision, output) An array containing the Z component of the Cartesian coordinates of the output data. (X(I),Y(I),Z(I)) is the Cartesian coordinate corresponding to the lat/lon coordinate (RLAT(I),RLON(I)) for I=1 to N.</dl><h2>Usage</h2>CSS2CD is called to find the equivalent Cartesian coordinates on a unit sphere to specified latitude and longitude coordinates. The coordinate of 0. latitude and 0. longitude is converted to Cartesian coordinate (1.,0.,0.). Latitudes and longitudes are assumed to be in degrees. CSS2CD is a double precision verson of CSS2C.
<h2>Access</h2>To use CSS2CD, load the NCAR Graphics library ngmath.
<h2>See Also</h2>css_overview, cssgrid, csc2sd, css2c. 

 Complete documentation for Cssgrid is available at URL 
 <a rel="nofollow" HREF="http://ngwww.ucar.edu/ngdoc/ng/ngmath/cssgrid/csshome.html">http://ngwww.ucar.edu/ngdoc/ng/ngmath/cssgrid/csshome.html</a>
<h2>Copyright</h2>Copyright (C) 2000 
 University Corporation for Atmospheric Research 
 

 The use of this Software is governed by a License Agreement.
