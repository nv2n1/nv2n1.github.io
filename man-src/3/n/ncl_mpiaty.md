---
title: "ncl_mpiaty(3)"
name: "ncl_mpiaty"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_mpiaty/"
---

MPIATY - Given the area identifier of one of the areas defined by whatever database was last read by one of the EZMAPB routines MPLNAM, MPLNDM, MPLNDR, and MPLNRI, this function returns the area type of the area. 

<h2>Synopsis</h2>IATY=MPIATY(IAIN)
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/ncargC.h&gt; 

 int c_mpiaty (int iain)
<h2>Description</h2><dl COMPACT><dt>IAIN
<dd>is an input expression of type INTEGER, specifying the area identifier of a particular area of interest.</dl><h2>C-Binding Description</h2>The C-binding argument description is the same as the FORTRAN argument description.
<h2>Usage</h2>The statement &quot;IATY=MPIATY(IAIN)&quot; retrieves in IATY the area type of the area with area identifier IAIN. For example, if IMAD is the area identifier of the little island in Lake Superior called &quot;Lake Madeline&quot;, then MPIATY(IMAD) is 4, implying that this island is a portion of a state.
<h2>Examples</h2>Use the ncargex command to see the following relevant example: mpex12.
<h2>Access</h2>To use MPIATY or c_mpiaty, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.
<h2>See Also</h2>Online: ezmap, ezmap_params, mapaci, mapbla, mapblm, mapdrw, mapeod, mapfst, mapgci, mapgrd, mapgrm, mapgtc, mapgti, mapgtl, mapgtr, mapint, mapiq, mapiqa, mapiqd, mapiqm, mapit, mapita, mapitd, mapitm, maplbl, maplmb, maplot, mappos, maproj, maprs, maprst, mapsav, mapset, mapstc, mapsti, mapstl, mapstr, maptra, maptri, maptrn, mapusr, mapvec, mpchln, mpfnme, mpgetc, mpgeti, mpgetl, mpgetr, mpglty, mpifnb, mpilnb, mpiola, mpiosa, mpipai, mpipan, mpipar, mpisci, mplnam, mplndm, mplndr, mplnri, mpname, mprset, mpsetc, mpseti, mpsetl, mpsetr, supmap, supcon, ncarg_cbind
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
