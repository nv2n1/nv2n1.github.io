---
title: "ncl_c_css2cd(3)"
name: "ncl_c_css2cd"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_c_css2cd/"
---

c_css2cd - convert from lat/lon coordinates to Cartesian coordinates.
<h2>Function Prototype</h2><pre> void c_css2cd(int, double *, double *, double *, double *, double *);</pre><h2>Synopsis</h2><pre> c_css2cd(n, rlat, rlon, x, y, z);</pre><h2>Description</h2><dl COMPACT><dt>n
<dd>The number of input lat/lon coordinates.
<dt>rlat
<dd>An array containing the latitudes of the input coordinates, in degrees.
<dt>rlon
<dd>An array containing the longitudes of the input coordinates, in degrees.
<dt>x
<dd>An array containing the X component of the Cartesian coordinates of the output data. (x[i],y[i],z[i]) is the Cartesian coordinate corresponding to the lat/lon coordinate (rlat[i],rlon[i]) for i=0 to n-1.
<dt>y
<dd>An array containing the Y component of the Cartesian coordinates of the output data. (x[i],y[i],z[i]) is the Cartesian coordinate corresponding to the lat/lon coordinate (rlat[i],rlon[i]) for i=0 to n-1.
<dt>z
<dd>An array containing the Z component of the Cartesian coordinates of the output data. (x[i],y[i],z[i]) is the Cartesian coordinate corresponding to the lat/lon coordinate (rlat[i],rlon[i]) for i=0 to n-1.</dl><h2>Usage</h2>c_css2cd is called to find the equivalent Cartesian coordinates on a unit sphere to specified latitude and longitude coordinates. The coordinate of 0. latitude and 0. longitude is converted to Cartesian coordinate (1.,0.,0.). Latitudes and longitudes are assumed to be in degrees. c_css2cd is a double precision version of c_css2c.
<h2>Return Value</h2>c_css2cd does not return a value.
<h2>Access</h2>To use c_css2cd, load the NCAR Graphics library ngmath.
<h2>See Also</h2>css_overview, c_cssgrid, c_csc2sd. 

 Complete documentation for Cssgrid is available at URL 
 <a rel="nofollow" HREF="http://ngwww.ucar.edu/ngdoc/ng/ngmath/cssgrid/csshome.html">http://ngwww.ucar.edu/ngdoc/ng/ngmath/cssgrid/csshome.html</a>
<h2>Copyright</h2>Copyright (C) 2000 
 University Corporation for Atmospheric Research 
 

 The use of this Software is governed by a License Agreement.
