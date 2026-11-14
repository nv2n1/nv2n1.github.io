---
title: "ncl_nggsog(3)"
name: "ncl_nggsog"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_nggsog/"
---

NGGSOG - Returns the latitudes and longitudes of six points defining a five-pointed star at a given point on the surface of the globe. 

<h2>Synopsis</h2>CALL NGGSOG (SLAT,SLON,SRAD,ALAT,ALON)
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/ncargC.h&gt; 

 void c_nggsog(float slat, float slon, float srad, float *alat, 
 float *alon)
<h2>Description</h2><dl COMPACT><dt>SLAT
<dd>(an input expression of type REAL) is the latitude, in degrees, of a point on the globe defining the center of the star.
<dt>SLON
<dd>(an input expression of type REAL) is the longitude, in degrees, of a point on the globe defining the center of the star.
<dt>SRAD
<dd>(an input expression of type REAL) specifies the great-circle distance, in degrees, from the center of the star to the end of one of its points.
<dt>ALAT
<dd>(an output array, of type REAL, dimensioned 6) is an array in which the latitudes of points on the star are to be returned.
<dt>ALON
<dd>(an output array, of type REAL, dimensioned 6) is an array in which the longitudes of points on the star are to be returned.</dl><h2>C-Binding Description</h2>The C binding argument descriptions are the same as the FORTRAN argument descriptions.
<h2>Usage</h2>Let C represent (CLAT,CLON), let O represent the center of the globe, and let P represent the end of one point of the star. Then, the angle POC has the magnitude specified by SRAD. 

 SIN, COS, and TAN are used to generate points representing a star having the desired radius and centered at the the point with latitude 0 and longitude 0. These points are then subjected to two rotations - one that brings the star up to the desired latitude, and another that carries it to the desired longitude. 

 NGGSOG is intended to be used for relatively small stars marking points of interest on the surface of the globe; using SRAD = 90 degrees is guaranteed to get you into trouble and SRAD &lt; 10 degrees is recommended.
<h2>Examples</h2>Use the ncargex command to see the following relevant example: cpex10.
<h2>Access</h2>To use NGGSOG or c_nggsog, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.
<h2>Messages</h2>None.
<h2>See Also</h2>Online: nggcog(3NCARG), ngritd(3NCARG).
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
