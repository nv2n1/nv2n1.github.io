---
title: "ncl_mapint(3)"
name: "ncl_mapint"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_mapint/"
---

MAPINT - Initialization. 

<h2>Synopsis</h2>CALL MAPINT
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/ncargC.h&gt; 

 void c_mapint()
<h2>Description</h2>MAPINT has no arguments.
<h2>Usage</h2>MAPINT is required initially and again after a call to any of the routines MAPPOS, MAPROJ, or MAPSET. The flag 'IN', which may be retrieved by a call to MAPGTI or MAPGTL, indicates whether or not initialization is required at a given time. No parameter change by means of a call to MAPSTx forces reinitialization; reinitialization is forced only by calls to MAPPOS, MAPROJ, and MAPSET. (&quot;MAPSTx&quot; refers to any routine that starts with the characters &quot;MAPST&quot;.)
<h2>Examples</h2>Use the ncargex command to see the following relevant examples: ccpcica, ccpmovi, ccppole, colcon, cmpclr, cmpdd, cmpel, cmpfil, cmpgrd, cmpgrp, cmpita, cmpitm, cmplab, cmplbl, cmplot, cmpmsk, cmpou, cmptit, cpex08, mpex09, mpex10, eezmpa, epltch, tezmpa, fcover, ffex00, ffex02, ffex03, ffex05, fpchiqu.
<h2>Access</h2>To use MAPINT or c_mapint, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.
<h2>Messages</h2>See the ezmap man page for a description of all EZMAP error messages and/or informational messages.
<h2>See Also</h2>Online: ezmap, ezmap_params, mapaci, mapbla, mapblm, mapdrw, mapeod, mapfst, mapgci, mapgrd, mapgrm, mapgtc, mapgti, mapgtl, mapgtr, mapiq, mapiqa, mapiqd, mapiqm, mapit, mapita, mapitd, mapitm, maplbl, maplmb, maplot, mappos, maproj, maprs, maprst, mapsav, mapset, mapstc, mapsti, mapstl, mapstr, maptra, maptri, maptrn, mapusr, mapvec, mpchln, mpfnme, mpgetc, mpgeti, mpgetl, mpgetr, mpglty, mpiaty, mpifnb, mpilnb, mpiola, mpiosa, mpipai, mpipan, mpipar, mpisci, mplnam, mplndm, mplndr, mplnri, mpname, mprset, mpsetc, mpseti, mpsetl, mpsetr, supmap, supcon, ncarg_cbind 

 Hardcopy: NCAR Graphics Contouring and Mapping Tutorial
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
