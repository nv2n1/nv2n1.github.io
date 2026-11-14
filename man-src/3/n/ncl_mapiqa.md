---
title: "ncl_mapiqa(3)"
name: "ncl_mapiqa"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_mapiqa/"
---

MAPIQA - Terminates a string of calls to MAPITA. 

<h2>Synopsis</h2>CALL MAPIQA (IAMA,IGID,IAIL,IAIR)
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/ncargC.h&gt; 

 void c_mapiqa (int *iama, int igid, int iail, int iair) 

 void c_mapita (float rlat, float rlon, int ifst, 
 int *iama, int igid, int iail, int iair)
<h2>Description</h2><dl COMPACT><dt>IAMA
<dd>(an input/output array of type INTEGER, dimensioned as specified in a call to the AREAS initialization routine ARINAM) is the area map to which lines in MAPITA's buffer are to be added.
<dt>IGID
<dd>(an input expression of type INTEGER) is the group identifier to be passed to the AREAS routine AREDAM when the lines in MAPITA's buffer are added to the area map in IAMA.
<dt>IAIL
<dd>(an input expression of type INTEGER) is the left area identifier to be passed to the AREAS routine AREDAM when the lines in MAPITA's buffer are added to the area map in IAMA.
<dt>IAIR
<dd>(an input expression of type INTEGER) is the right area identifier to be passed to the AREAS routine AREDAM when the lines in MAPITA's buffer are added to the area map in IAMA.</dl><h2>C-Binding Description</h2>The C-binding argument descriptions are the same as the FORTRAN argument descriptions.
<h2>Usage</h2>You must call MAPITA once for each point along the line. After your last call to MAPITA for a given line, you must call MAPIQA to signal the end of the line. 

 For more information, see the man pages for the routines MAPIT and MAPITA.
<h2>Examples</h2>Use the ncargex command to see the following relevant examples: cmpita, cpex08.
<h2>Access</h2>To use MAPIQA or c_mapiqa, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.
<h2>See Also</h2>Online: ezmap, ezmap_params, mapaci, mapbla, mapblm, mapdrw, mapeod, mapfst, mapgci, mapgrd, mapgrm, mapgtc, mapgti, mapgtl, mapgtr, mapint, mapiq, mapiqd, mapiqm, mapit, mapita, mapitd, mapitm, maplbl, maplmb, maplot, mappos, maproj, maprs, maprst, mapsav, mapset, mapstc, mapsti, mapstl, mapstr, maptra, maptri, maptrn, mapusr, mapvec, mpchln, mpfnme, mpgetc, mpgeti, mpgetl, mpgetr, mpglty, mpiaty, mpifnb, mpilnb, mpiola, mpiosa, mpipai, mpipan, mpipar, mpisci, mplnam, mplndm, mplndr, mplnri, mpname, mprset, mpsetc, mpseti, mpsetl, mpsetr, supmap, supcon, ncarg_cbind 

 Hardcopy: NCAR Graphics Contouring and Mapping Tutorial
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
