---
title: "ncl_mapgti(3)"
name: "ncl_mapgti"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_mapgti/"
---

MAPGTI - Gets the current value of a specified EZMAP parameter of type INTEGER. 

 MPGETI is an alternate name for the routine MAPGTI. 

<h2>Synopsis</h2>CALL MAPGTI (PNAM,IVAL)
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/ncargC.h&gt; 

 void c_mapgti (char *pnam, int *ival)
<h2>Description</h2><dl COMPACT><dt>PNAM
<dd>(an input expression of type CHARACTER) specifies the name of the parameter to get. Only the first two characters of the string are examined.
<dt>IVAL
<dd>(an output variable of type INTEGER) receives the value of the parameter specified by PNAM.</dl><h2>C-Binding Description</h2>The C-binding argument descriptions are the same as the FORTRAN argument descriptions.
<h2>Usage</h2>This routine allows you to retrieve the current value of EZMAP parameters. For a complete list of parameters available in this utility, see the ezmap_params man page.
<h2>Examples</h2>Use the ncargex command to see the following relevant examples: mpex07, mpex08.
<h2>Access</h2>To use MAPGTI, MPGETI, or c_mapgti load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.
<h2>Messages</h2>See the ezmap man page for a description of all EZMAP error messages and/or informational messages.
<h2>See Also</h2>Online: ezmap, ezmap_params, mapaci, mapbla, mapblm, mapdrw, mapeod, mapfst, mapgci, mapgrd, mapgrm, mapgtc, mapgtl, mapgtr, mapint, mapiq, mapiqa, mapiqd, mapiqm, mapit, mapita, mapitd, mapitm, maplbl, maplmb, maplot, mappos, maproj, maprs, maprst, mapsav, mapset, mapstc, mapsti, mapstl, mapstr, maptra, maptri, maptrn, mapusr, mapvec, mpchln, mpfnme, mpgetc, mpgeti, mpgetl, mpgetr, mpglty, mpiaty, mpifnb, mpilnb, mpiola, mpiosa, mpipai, mpipan, mpipar, mpisci, mplnam, mplndm, mplndr, mplnri, mpname, mprset, mpsetc, mpseti, mpsetl, mpsetr, supmap, supcon, ncarg_cbind 

 Hardcopy: NCAR Graphics Contouring and Mapping Tutorial
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
