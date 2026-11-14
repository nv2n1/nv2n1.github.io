---
title: "ncl_mapaci(3)"
name: "ncl_mapaci"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_mapaci/"
---

MAPACI - Normally used to pick colors for the areas created by the boundary lines added to an area map by a call to MAPBLA. Note that this function should not be used to select color indices for areas defined by the new map database &quot;Earth..1&quot;, which was created in 1998; for that purpose, use EZMAPB functions instead (in particular, MPISCI). 

<h2>Synopsis</h2>ICIR=MAPACI(IAID)
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/ncargC.h&gt; 

 int c_mapaci (int iaid)
<h2>Description</h2><dl COMPACT><dt>IAID
<dd>(an input expression of type INTEGER) is an area identifier for one of the areas defined by the set of boundary lines added to an area map by a call to MAPBLA.</dl><h2>C-Binding Description</h2>The C-binding argument description is the same as the FORTRAN argument description.
<h2>Usage</h2>Executing the statement &quot;ICIR=MAPACI(IAID)&quot; gives ICIR a value between 1 and 7, inclusive, that may be used to select a color index for the area whose area identifier is IAID. It is guaranteed that MAPACI will not return the same value for adjacent areas; this fact can be used to ensure that adjacent areas will have different colors. 

 Note that it is the responsibility of the user to define the colors associated with color indices used; this is done by calling the GKS routine GSCR.
<h2>Examples</h2>Use the ncargex command to see the following relevant example: eezmpa.
<h2>Access</h2>To use MAPACI or c_mapaci, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.
<h2>See Also</h2>Online: ezmap, ezmap_params, mapbla, mapblm, mapdrw, mapeod, mapfst, mapgci, mapgrd, mapgrm, mapgtc, mapgti, mapgtl, mapgtr, mapint, mapiq, mapiqa, mapiqd, mapiqm, mapit, mapita, mapitd, mapitm, maplbl, maplmb, maplot, mappos, maproj, maprs, maprst, mapsav, mapset, mapstc, mapsti, mapstl, mapstr, maptra, maptri, maptrn, mapusr, mapvec, mpchln, mpfnme, mpgetc, mpgeti, mpgetl, mpgetr, mpglty, mpiaty, mpifnb, mpilnb, mpiola, mpiosa, mpipai, mpipan, mpipar, mpisci, mplnam, mplndm, mplndr, mplnri, mpname, mprset, mpsetc, mpseti, mpsetl, mpsetr, supmap, supcon, ncarg_cbind 

 Hardcopy: NCAR Graphics Contouring and Mapping Tutorial
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
