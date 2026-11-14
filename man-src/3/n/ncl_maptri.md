---
title: "ncl_maptri(3)"
name: "ncl_maptri"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_maptri/"
---

MAPTRI - Performs inverse transformations. 

<h2>Synopsis</h2>CALL MAPTRI (UVAL,VVAL,RLAT,RLON)
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/ncargC.h&gt; 

 void c_maptri (float uval, float vval, float *rlat, 
 float *rlon)
<h2>Description</h2><dl COMPACT><dt>UVAL and VVAL
<dd>(input expressions, of type REAL) define the point (UVAL,VVAL) that is the projection in the u/v plane of the point whose latitude and longitude are desired. The units of UVAL and VVAL depend on the projection.
<dt>RLAT and RLON
<dd>(output variables, of type REAL) are the latitude and longitude, respectively, of the point, in degrees. RLAT will be between -90. and +90., inclusive; RLON will be between -180. and +180., inclusive. 

 If the point (UVAL,VVAL) is not the projection of some point of the globe or is outside the boundary of the map, RLAT and RLON are returned equal to 1.E12.</dl><h2>C-Binding Description</h2>The C-binding argument descriptions are the same as the FORTRAN argument descriptions.
<h2>Examples</h2>Use the ncargex command to see the following relevant examples: ccpmpxy, mpex10.
<h2>Access</h2>To use MAPTRI or c_maptri, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.
<h2>See Also</h2>Online: ezmap, ezmap_params, mapaci, mapbla, mapblm, mapdrw, mapeod, mapfst, mapgci, mapgrd, mapgrm, mapgtc, mapgti, mapgtl, mapgtr, mapint, mapiq, mapiqa, mapiqd, mapiqm, mapit, mapita, mapitd, mapitm, maplbl, maplmb, maplot, mappos, maproj, maprs, maprst, mapsav, mapset, mapstc, mapsti, mapstl, mapstr, maptra, maptrn, mapusr, mapvec, mpchln, mpfnme, mpgetc, mpgeti, mpgetl, mpgetr, mpglty, mpiaty, mpifnb, mpilnb, mpiola, mpiosa, mpipai, mpipan, mpipar, mpisci, mplnam, mplndm, mplndr, mplnri, mpname, mprset, mpsetc, mpseti, mpsetl, mpsetr, supmap, supcon, ncarg_cbind 

 Hardcopy: NCAR Graphics Contouring and Mapping Tutorial
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
