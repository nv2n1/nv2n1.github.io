---
title: "ncl_nggcog(3)"
name: "ncl_nggcog"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_nggcog/"
---

NGGCOG - Returns the latitudes and longitudes of a set of points approximating a circle at a given point on the surface of the globe. 

<h2>Synopsis</h2>CALL NGGCOG (CLAT,CLON,CRAD,ALAT,ALON,NPTS)
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/ncargC.h&gt; 

 void c_nggcog(float clat, float clon, float crad, float *alat, 
 float *alon, int npts)
<h2>Description</h2><dl COMPACT><dt>CLAT
<dd>(an input expression of type REAL) is the latitude, in degrees, of a point on the globe defining the center of the circle.
<dt>CLON
<dd>(an input expression of type REAL) is the longitude, in degrees, of a point on the globe defining the center of the circle.
<dt>CRAD
<dd>(an input expression of type REAL) specifies the radius of the circle. This is given as a great-circle distance, in degrees.
<dt>ALAT
<dd>(an output array, of type REAL, dimensioned NPTS) is an array in which the latitudes of points on the circle are to be returned.
<dt>ALON
<dd>(an output array, of type REAL, dimensioned NPTS) is an array in which the longitudes of points on the circle are to be returned.
<dt>NPTS
<dd>(an input expression, of type INTEGER) is the desired number of points to be used to represent the circle. Its value determines how accurately the circle will be represented.</dl><h2>C-Binding Description</h2>The C binding argument descriptions are the same as the FORTRAN argument descriptions.
<h2>Usage</h2>Let C represent (CLAT,CLON) and let O represent the center of the globe. The circle is the set of all points P on the globe such that the angle POC is of the size specified by CRAD. 

 SIN and COS are used to generate points representing a circle having the desired radius and centered at the North Pole. These points are then subjected to two rotations - one that brings the circle down to the desired latitude, and another that carries it to the desired longitude.
<h2>Examples</h2>Use the ncargex command to see the following relevant example: cpex10.
<h2>Access</h2>To use NGGCOG or c_nggcog, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.
<h2>Messages</h2>None.
<h2>See Also</h2>Online: nggsog(3NCARG), ngritd(3NCARG).
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
