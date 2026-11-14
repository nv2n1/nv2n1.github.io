---
title: "ncl_c_csc2s(3)"
name: "ncl_c_csc2s"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_c_csc2s/"
---

c_csc2s - convert from Cartesian coordinates to lat/lon coordinates.
<h2>Function Prototype</h2><pre> void c_csc2s(int, float *, float *, float *, float *, float *);</pre><h2>Synopsis</h2><pre> c_csc2s(n, x, y, z, rlat, rlon);</pre><h2>Description</h2><dl COMPACT><dt>n
<dd>The number of input Cartesian coordinates.
<dt>x
<dd>An array containing the X component of the Cartesian coordinates of the input data. (rlat[i],rlon[i]) is the lat/lon coordinate corresponding to the Cartesian coordinate (x[i],y[i],z[i]) for i=0 to n-1.
<dt>y
<dd>An array containing the Y component of the Cartesian coordinates of the input data. (rlat[i],rlon[i]) is the lat/lon coordinate corresponding to the Cartesian coordinate (x[i],y[i],z[i]) for i=0 to n-1.
<dt>z
<dd>An array containing the Z component of the Cartesian coordinates of the input data. (rlat[i],rlon[i]) is the lat/lon coordinate corresponding to the Cartesian coordinate (x[i],y[i],z[i]) for i=0 to n-1.
<dt>rlat
<dd>An array containing the latitudes of the output coordinates, in degrees.
<dt>rlon
<dd>An array containing the longitudes of the output coordinates, in degrees.</dl><h2>Usage</h2>c_csc2s is called to find the equivalent lat/lon coordinates to specified Cartesian coordinates on a unit sphere. The Cartesian coordinate (1.,0.,0.) is converted to lat/lon coordinate (0.,0.). Latitudes and longitudes are assumed to be in degrees.
<h2>Return Value</h2>c_csc2s does not return a value.
<h2>Access</h2>To use c_csc2s, load the NCAR Graphics library ngmath.
<h2>See Also</h2>css_overview, c_cssgrid, c_css2c. 

 Complete documentation for Cssgrid is available at URL 
 <a rel="nofollow" HREF="http://ngwww.ucar.edu/ngdoc/ng/ngmath/cssgrid/csshome.html">http://ngwww.ucar.edu/ngdoc/ng/ngmath/cssgrid/csshome.html</a>
<h2>Copyright</h2>Copyright (C) 2000 
 University Corporation for Atmospheric Research 
 

 The use of this Software is governed by a License Agreement.
