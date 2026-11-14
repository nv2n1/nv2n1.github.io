---
title: "ncl_mapitm(3)"
name: "ncl_mapitm"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_mapitm/"
---

MAPITM - Draws lines on a map, masked by a specified area map. 

<h2>Synopsis</h2>&nbsp;<wbr>CALL MAPITM&nbsp;<wbr>(RLAT,RLON,IFST,IAMA,XCRA,YCRA,MCRA,IAAI,IAGI, + NOGI,ULPR) 

 CALL MAPIQM (IAMA,XCRA,YCRA,MCRA,IAAI,IAGI,NOGI,ULPR)
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/ncargC.h&gt; 

 void c_mapitm (float rlat, float rlon, int ifst, 
 int *iama, float *xcra, float *ycra, int mcra, 
 int *iaai, int *iagi, int nogi, 
 int (*ulpr)(float *xcra, float *ycra, int *mcra, 
 int *iaai, int *iagi, int *nogi)) 

 void c_mapiqm (int *iama, float *xcra, float *ycra, 
 int mcra, int *iaai, int *iagi, int nogi, 
 int ulpr(float *xcra, float *ycra, int *mcra, 
 int *iaai, int *iagi , int *nogi))
<dl COMPACT><dt>RLAT and RLON
<dd>(input expressions, of type REAL) specify the latitude and longitude of a point to which the &quot;pen&quot; is to be moved. Both are given in degrees. RLAT must be between -90. and +90., inclusive; RLON must be between -540. and +540., inclusive.
<dt>IFST
<dd>(an input expression, of type INTEGER) is 0 to do a &quot;pen-up&quot; move, 1 to do a &quot;pen-down&quot; move only if the distance from the last point to the new point is greater than 'MV' plotter units, and 2 or greater to do a &quot;pen-down&quot; move regardless of the distance from the last point to the new one.
<dt>IAMA
<dd>(an input/output array of type INTEGER, dimensioned as specified in a call to the AREAS initialization routine ARINAM) is the array containing the area map against which lines drawn by MAPIQM will be masked.
<dt>XCRA and YCRA
<dd>(scratch arrays of type REAL, each dimensioned MCRA) are to be passed by MAPIQM to the AREAS routine ARDRLN, which uses them in calls to the user line-processing routine ULPR. They will hold the X and Y coordinates of points in the fractional coordinate system defining some portion of the projection of a user-defined polyline on the globe.
<dt>MCRA
<dd>(an input expression of type INTEGER) is the size of each of the arrays XCRA and YCRA. The value of MCRA must be at least two. For most applications, the value 100 works nicely.
<dt>IAAI and IAGI
<dd>(scratch arrays of type INTEGER, each dimensioned NOGI) are to be passed by MAPIQM to the AREAS routine ARDRLN, which uses them in calls to the user line-processing routine ULPR. They will hold area identifier/group identifier pairs for the area containing the polyline fragment defined by XCRA and YCRA.
<dt>NOGI
<dd>(an input expression of type INTEGER) is the size of each of the arrays IAAI and IAGI. The value of NOGI must be greater than or equal to the number of groups of edges placed in the area map in IAMA.
<dt>ULPR
<dd>is the name of a user-provided line-processing routine. This name must appear in an EXTERNAL statement in the routine that calls MAPITM, so that the compiler and loader will know that it is the name of a routine to be called, rather than the name of a variable.</dl><h2>C-Binding Description</h2>The C-binding argument descriptions are the same as the FORTRAN argument descriptions.
<h2>Usage</h2>The routines MAPITM and MAPIQM may be used to draw lines defined by a series of user-specified latitudes and longitudes on a map, masked by the areas defined by an area map (perhaps one created by a call to MAPBLA or perhaps one created by a set of calls to routines in the package AREAS); like MAPIT and MAPIQ, they attempt to omit non-visible portions of lines and to handle &quot;cross-over&quot;. 

 MAPITM is called like the EZMAP routine MAPIT (which see, above) but has some additional arguments: 

<dl COMPACT><dd>&nbsp;<wbr>CALL MAPITM&nbsp;<wbr>(RLAT,RLON,IFST,IAMA,XCRA,YCRA,MCRA,IAAI,&nbsp;<wbr> 
 + IAGI,NOGI,ULPR)</dl>
 

 Additional arguments are the area-map array IAMA, coordinate arrays XCRA and YCRA, dimensioned MCRA, integer arrays IAAI and IAGI, dimensioned NOGI, and a user-provided line-processing routine named ULPR. MAPIQM is called like the EZMAP routine MAPIQ, to terminate a series of calls to MAPITM and to flush the buffers; it has the same additional arguments: 

<dl COMPACT><dd>CALL MAPIQM (IAMA,XCRA,YCRA,MCRA,IAAI,IAGI,NOGI,ULPR)</dl>
 

 The additional arguments are passed by MAPITM and MAPIQM to the routine ARDRLN, in the package named AREAS. 

 For more information, see the man page for the routine MAPIT.
<h2>Examples</h2>Use the ncargex command to see the following relevant example: cmpitm.
<h2>Access</h2>To use MAPITM or c_mapitm, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.
<h2>See Also</h2>Online: ezmap, ezmap_params, mapaci, mapbla, mapblm, mapdrw, mapeod, mapfst, mapgci, mapgrd, mapgrm, mapgtc, mapgti, mapgtl, mapgtr, mapint, mapiq, mapiqa, mapiqd, mapiqm, mapit, mapita, mapitd, maplbl, maplmb, maplot, mappos, maproj, maprs, maprst, mapsav, mapset, mapstc, mapsti, mapstl, mapstr, maptra, maptri, maptrn, mapusr, mapvec, mpchln, mpfnme, mpgetc, mpgeti, mpgetl, mpgetr, mpglty, mpiaty, mpifnb, mpilnb, mpiola, mpiosa, mpipai, mpipan, mpipar, mpisci, mplnam, mplndm, mplndr, mplnri, mpname, mprset, mpsetc, mpseti, mpsetl, mpsetr, supmap, supcon, ncarg_cbind 

 Hardcopy: NCAR Graphics Contouring and Mapping Tutorial
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
