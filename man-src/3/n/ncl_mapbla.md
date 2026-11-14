---
title: "ncl_mapbla(3)"
name: "ncl_mapbla"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_mapbla/"
---

MAPBLA - Adds to the area map in the array IAMA the set of boundary lines, of projected geographical entities, determined by the current state of the internal parameters of EZMAP. Note that this routine uses whichever old outline dataset is selected by the value of the internal parameter 'OU'; to access the new map database &quot;Earth..1&quot;, which was created in 1998, one must call instead the EZMAPB routine MPLNAM. 

<h2>Synopsis</h2>CALL MAPBLA (IAMA)
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/ncargC.h&gt; 

 void c_mapbla (int *iama)
<h2>Description</h2><dl COMPACT><dt>IAMA
<dd>(an input/output array of type INTEGER) is the area map array to which boundary lines are to be added.</dl><h2>C-Binding Description</h2>The C-binding argument description is the same as the FORTRAN argument description.
<h2>Usage</h2>One or two groups of boundary lines are added to the area map by a call to MAPBLA. The first group has the group identifier 'G1', which has a default value of 1. The group 'G1' consists of a perimeter (either rectangular or elliptical, depending on the value of the EZMAP parameter 'EL') and the set of projected boundary lines implied by your selection of an EZMAP dataset (some combination of continental, U.S. state, and international political outlines). For certain projections a limb line may also be included. (The limb is the boundary between a projectable region and an unprojectable one.) 

 If the EZMAP parameter 'VS' has a value greater than zero, a second group, with the group identifier 'G2', is added to the area map. (The default value of 'VS' is 1; the default value of 'G2' is 2.) The purpose of the group 'G2' is to split up areas and thus reduce the number of points required to define a typical area. This may be necessary because some hardware devices fail if the number of points defining an area is too large. The group 'G2' consists of a copy of the perimeter and the limb line (if any), plus a set of vertical lines that split the area inside the perimeter into 'VS' vertical strips. 

 The perimeter and the limb in the groups 'G1' and 'G2' have the following left and right area identifiers:
<dl COMPACT><dd><dl COMPACT><dt>0
<dd>Identifies the area inside the perimeter or limb.
<dt>-1
<dd>Identifies the area outside the perimeter or limb.</dl></dl>
 

 The vertical lines in the group 'G2' have left and right area identifiers of 0. 

 To set the values of 'G1', 'G2', and 'VS', call the EZMAP routine MAPSTI. To get the current values of 'G1', 'G2', and 'VS', call the EZMAP routine MAPGTI. See the man pages for MAPSTI and MAPGTI.
<h2>Examples</h2>Use the ncargex command to see the following relevant examples: ccppole, colcon, cmpfil, cmpgrp, cmpita, cmpitm, cmplab, cmpmsk, cmptit, cpex08, eezmpa, tezmpa, fcover, ffex00.
<h2>Access</h2>To use MAPBLA or c_mapbla, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.
<h2>See Also</h2>Online: ezmap, ezmap_params, mapaci, mapblm, mapdrw, mapeod, mapfst, mapgci, mapgrd, mapgrm, mapgtc, mapgti, mapgtl, mapgtr, mapint, mapiq, mapiqa, mapiqd, mapiqm, mapit, mapita, mapitd, mapitm, maplbl, maplmb, maplot, mappos, maproj, maprs, maprst, mapsav, mapset, mapstc, mapsti, mapstl, mapstr, maptra, maptri, maptrn, mapusr, mapvec, mpchln, mpfnme, mpgetc, mpgeti, mpgetl, mpgetr, mpglty, mpiaty, mpifnb, mpilnb, mpiola, mpiosa, mpipai, mpipan, mpipar, mpisci, mplnam, mplndm, mplndr, mplnri, mpname, mprset, mpsetc, mpseti, mpsetl, mpsetr, supmap, supcon, ncarg_cbind 

 Hardcopy: NCAR Graphics Contouring and Mapping Tutorial
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
