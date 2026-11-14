---
title: "ncl_mpfnme(3)"
name: "ncl_mpfnme"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_mpfnme/"
---

MPFNME - Given the area identifier of one of the areas defined by whatever database was last read by one of the EZMAPB routines MPLNAM, MPLNDM, MPLNDR, and MPLNRI, this function returns the full name of the area, including the prepended names of all containing (parent) areas, up to and including a specified level. 

<h2>Synopsis</h2>CHARACTER*128 MPFNME,FNME 

 FNME=MPFNME(IAIN,ILVL)
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/ncargC.h&gt; 

 char *c_mpfnme (int iain, int ilvl)
<h2>Description</h2><dl COMPACT><dt>IAIN
<dd>is an input expression of type INTEGER, specifying the area identifier of a particular area of interest.
<dt>ILVL
<dd>is an input expression of type INTEGER, specifying the highest level of containing (parent) name to be included in the returned full name.</dl><h2>C-Binding Description</h2>The C-binding argument description is the same as the FORTRAN argument description.
<h2>Usage</h2>Given the declaraion &quot;CHARACTER*128 MPFNME,FNME&quot;, the executable statement &quot;FNME=MPFNME(IAIN,ILVL)&quot; will retrieve in FNME the full name of the area with area identifier IAIN, including the prepended names of containing (parent) areas, up to the level ILVL. For example, if IMAD is the area identifier of the little island in Lake Superior called &quot;Lake Madeline&quot;, a level-4 area whose name in the database is actually &quot;Madeline Island (Lake Superior)&quot; and whose parent (also at level 4) is an area called &quot;Wisconsin&quot;, then MPFNME(IMAD,4) = 'Wisconsin - Madeline Island (Lake Superior)'. Note the use of a dash surrounded by blanks as a separator.
<h2>Examples</h2>Use the ncargex command to see the following relevant example: mpex12.
<h2>Access</h2>To use MPFNME or c_mpfnme, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.
<h2>See Also</h2>Online: ezmap, ezmap_params, mapaci, mapbla, mapblm, mapdrw, mapeod, mapfst, mapgci, mapgrd, mapgrm, mapgtc, mapgti, mapgtl, mapgtr, mapint, mapiq, mapiqa, mapiqd, mapiqm, mapit, mapita, mapitd, mapitm, maplbl, maplmb, maplot, mappos, maproj, maprs, maprst, mapsav, mapset, mapstc, mapsti, mapstl, mapstr, maptra, maptri, maptrn, mapusr, mapvec, mpchln, mpgetc, mpgeti, mpgetl, mpgetr, mpglty, mpiaty, mpifnb, mpilnb, mpiola, mpiosa, mpipai, mpipan, mpipar, mpisci, mplnam, mplndm, mplndr, mplnri, mpname, mprset, mpsetc, mpseti, mpsetl, mpsetr, supmap, supcon, ncarg_cbind
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
