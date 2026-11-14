---
title: "ncl_mapgci(3)"
name: "ncl_mapgci"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_mapgci/"
---

MAPGCI - Returns a set of points on the shortest great circle route between two user-specified points on the globe. 

<h2>Synopsis</h2>CALL MAPGCI(ALAT,ALON,BLAT,BLON,NOPI,RLTI,RLNI)
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/ncargC.h&gt; 

 void c_mapgci( float alat, float alon, float blat, 
 float blon, int nopi, float *rlti, float *rlni)
<h2>Description</h2><dl COMPACT><dt>ALAT and ALON
<dd>(input expressions, of type REAL) are the latitude and longitude of the point at the beginning of a great circle route.
<dt>BLAT and BLON
<dd>(input expressions, of type REAL) are the latitude and longitude of the point at the end of a great circle route.
<dt>NOPI
<dd>(an input expression, of type INTEGER) is the number of equally-spaced points to be interpolated along the great circle route.
<dt>RLTI and RLNI
<dd>(output arrays of type REAL, each dimensioned at least NOPI) are arrays containing the latitudes and longitudes of points interpolated along the great circle route. Each lat/lon pair defines one of the points; they appear in order of increasing distance along the great circle route. The positions of the first point and the last point are not returned in these arrays; only the interpolated points are.</dl><h2>C-Binding Description</h2>The C-binding argument descriptions are the same as the FORTRAN argument descriptions.
<h2>Usage</h2>The statement:
<dl COMPACT><dd>CALL MAPGCI (ALAT,ALON,BLAT,BLON,NOPI,RLTI,RLNI)</dl>
 

 defines the positions of two points, A and B, on the globe and the number of equally-spaced points, NOPI, to be interpolated along the great circle route from A to B. The latitudes and longitudes of the interpolated points are returned to the caller in the arrays RLTI and RLNI. If the points A and B are exactly opposite one another on the globe, the code does not fail, but the direction of the great circle route will be somewhat unpredictable (since, in that case, there is more than one great circle route joining the two points).
<h2>Examples</h2>Use the ncargex command to see the following relevant example: cmpgci.
<h2>Access</h2>To use MAPGCI or c_mapgci, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.
<h2>See Also</h2>Online: ezmap, ezmap_params, mapaci, mapbla, mapblm, mapdrw, mapeod, mapfst, mapgrd, mapgrm, mapgtc, mapgti, mapgtl, mapgtr, mapint, mapiq, mapiqa, mapiqd, mapiqm, mapit, mapita, mapitd, mapitm, maplbl, maplmb, maplot, mappos, maproj, maprs, maprst, mapsav, mapset, mapstc, mapsti, mapstl, mapstr, maptra, maptri, maptrn, mapusr, mapvec, mpchln, mpfnme, mpgetc, mpgeti, mpgetl, mpgetr, mpglty, mpiaty, mpifnb, mpilnb, mpiola, mpiosa, mpipai, mpipan, mpipar, mpisci, mplnam, mplndm, mplndr, mplnri, mpname, mprset, mpsetc, mpseti, mpsetl, mpsetr, supmap, supcon, ncarg_cbind 

 Hardcopy: NCAR Graphics Contouring and Mapping Tutorial
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
