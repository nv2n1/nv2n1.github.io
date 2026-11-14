---
title: "ncl_maptra(3)"
name: "ncl_maptra"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_maptra/"
---

MAPTRA - Projects points. 

<h2>Synopsis</h2>CALL MAPTRA (RLAT,RLON,UVAL,VVAL)
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/ncargC.h&gt; 

 void c_maptra (float rlat, float rlon, float *uval, 
 float *vval)
<h2>Description</h2><dl COMPACT><dt>RLAT and RLON
<dd>(input expressions, of type REAL) are the latitude and longitude, respectively, of a point on the globe. RLAT must be between -90. and +90., inclusive; RLON must be between -540. and +540., inclusive.
<dt>UVAL and VVAL
<dd>(output variables, of type REAL) define the point (UVAL,VVAL) that is the projection in the u/v plane of (RLAT,RLON). The units of UVAL and VVAL depend on the projection. <pre><code>If the point is not projectable or if it is outside the boundary of the
map (as defined by the last call to MAPSET and by the value of the
parameter 'EL'), UVAL is returned equal to 1.E12.</code></pre>
<h2>C-Binding Description</h2>The C-binding argument descriptions are the same as the FORTRAN argument descriptions.
<h2>Examples</h2>Use the ncargex command to see the following relevant examples: ccpmpxy, cmptra, fgkgtx, fngngdts.
<h2>Access</h2>To use MAPTRA or c_maptra, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.
<h2>See Also</h2>Online: ezmap, ezmap_params, mapaci, mapbla, mapblm, mapdrw, mapeod, mapfst, mapgci, mapgrd, mapgrm, mapgtc, mapgti, mapgtl, mapgtr, mapint, mapiq, mapiqa, mapiqd, mapiqm, mapit, mapita, mapitd, mapitm, maplbl, maplmb, maplot, mappos, maproj, maprs, maprst, mapsav, mapset, mapstc, mapsti, mapstl, mapstr, maptri, maptrn, mapusr, mapvec, mpchln, mpfnme, mpgetc, mpgeti, mpgetl, mpgetr, mpglty, mpiaty, mpifnb, mpilnb, mpiola, mpiosa, mpipai, mpipan, mpipar, mpisci, mplnam, mplndm, mplndr, mplnri, mpname, mprset, mpsetc, mpseti, mpsetl, mpsetr, supmap, supcon, ncarg_cbind 

 Hardcopy: NCAR Graphics Contouring and Mapping Tutorial
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
