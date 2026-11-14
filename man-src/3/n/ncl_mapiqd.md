---
title: "ncl_mapiqd(3)"
name: "ncl_mapiqd"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_mapiqd/"
---

MAPIQD - Terminates a string of calls to MAPITD. 

<h2>Synopsis</h2>CALL MAPIQD
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/ncargC.h&gt; 

 void c_mapiqd()
<h2>Description</h2>MAPIQD has no arguments.
<h2>Usage</h2>MAPIQD flushes MAPITD's buffers. It is particularly important that this be done before a STOP or a CALL FRAME, and before changing the color index, dash pattern, etc. 

 For more information, see the man page for MAPITD.
<h2>Examples</h2>Use the ncargex command to see the following relevant examples: cmpgci, cmptra, mpexfi.
<h2>Access</h2>To use MAPIQD or c_mapiqd, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.
<h2>See Also</h2>Online: ezmap, ezmap_params, mapaci, mapbla, mapblm, mapdrw, mapeod, mapfst, mapgci, mapgrd, mapgrm, mapgtc, mapgti, mapgtl, mapgtr, mapint, mapiq, mapiqa, mapiqm, mapit, mapita, mapitd, mapitm, maplbl, maplmb, maplot, mappos, maproj, maprs, maprst, mapsav, mapset, mapstc, mapsti, mapstl, mapstr, maptra, maptri, maptrn, mapusr, mapvec, mpchln, mpfnme, mpgetc, mpgeti, mpgetl, mpgetr, mpglty, mpiaty, mpifnb, mpilnb, mpiola, mpiosa, mpipai, mpipan, mpipar, mpisci, mplnam, mplndm, mplndr, mplnri, mpname, mprset, mpsetc, mpseti, mpsetl, mpsetr, supmap, supcon, ncarg_cbind 

 Hardcopy: NCAR Graphics Contouring and Mapping Tutorial
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
