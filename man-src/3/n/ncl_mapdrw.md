---
title: "ncl_mapdrw(3)"
name: "ncl_mapdrw"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_mapdrw/"
---

MAPDRW - Draws the complete map described by the current values of the internal parameters of EZMAP. Note that this routine uses whichever old outline dataset is selected by the value of the internal parameter 'OU'; to access the new map database &quot;Earth..1&quot;, which was created in 1998, one must call instead the routines that MAPDRW would have called, but call MPLNDR instead of MAPLOT. 

<h2>Synopsis</h2>CALL MAPDRW
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/ncargC.h&gt; 

 void c_mapdrw()
<h2>Description</h2>MAPDRW does not use any arguments.
<h2>Usage</h2>MAPDRW calls MAPINT (if the value of the internal parameter 'IN' indicates that initialization is required), MAPGRD, MAPLBL, and MAPLOT, in that order. The user may wish to call these routines directly.
<h2>Examples</h2>Use the ncargex command to see the following relevant examples: ccpmap, ccpvp, cezmap1, cezmap2, cezmap3, cmpdrw, cmppos, cmpsat, cmptra, cmpusr, cpex01, cpex03, cpex09, mpex01, mpex02, mpex04, mpex05, mpex06, mpex07, mpex10, tezmap, fgkgpl, fgkgtx, fngngdts.
<h2>Access</h2>To use MAPDRW or c_mapdrw, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.
<h2>See Also</h2>Online: ezmap, ezmap_params, mapaci, mapbla, mapblm, mapeod, mapfst, mapgci, mapgrd, mapgrm, mapgtc, mapgti, mapgtl, mapgtr, mapint, mapiq, mapiqa, mapiqd, mapiqm, mapit, mapita, mapitd, mapitm, maplbl, maplmb, maplot, mappos, maproj, maprs, maprst, mapsav, mapset, mapstc, mapsti, mapstl, mapstr, maptra, maptri, maptrn, mapusr, mapvec, mpchln, mpfnme, mpgetc, mpgeti, mpgetl, mpgetr, mpglty, mpiaty, mpifnb, mpilnb, mpiola, mpiosa, mpipai, mpipan, mpipar, mpisci, mplnam, mplndm, mplndr, mplnri, mpname, mprset, mpsetc, mpseti, mpsetl, mpsetr, supmap, supcon, ncarg_cbind 

 Hardcopy: NCAR Graphics Contouring and Mapping Tutorial
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
