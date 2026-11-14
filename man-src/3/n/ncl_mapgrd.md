---
title: "ncl_mapgrd(3)"
name: "ncl_mapgrd"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_mapgrd/"
---

MAPGRD - Draws a lat/lon grid. 

<h2>Synopsis</h2>CALL MAPGRD
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/ncargC.h&gt; 

 void c_mapgrd()
<h2>Description</h2>MAPGRD has no arguments.
<h2>Usage</h2>The statement:
<dl COMPACT><dd>CALL MAPGRD</dl>
 

 draws a grid consisting of lines of constant latitude (parallels) and lines of constant longitude (meridians), spaced as specified by the value of the internal parameter 'GR'. If EZMAP needs initialization or if the value of 'GR' is less than or equal to zero or if there is an uncleared NCAR Graphics error, MAPGRD does nothing. 

 The grid is drawn using calls to MAPIT and MAPIQ. By default, MAPGRD temporarily forces the value of the internal parameter 'DL' to zero, so that the grid will be drawn using calls to the routines FRSTD and VECTD, in the dash package. MAPGRD also temporarily forces the use of the dash pattern defined by the internal parameter 'DA'. A user version of the routine MAPUSR may be supplied to change the way in which grid lines are drawn. Before returning control to the user, MAPGRD restores the original value of 'DL' and resets the current dash pattern to be used by the dash package.
<h2>Examples</h2>Use the ncargex command to see the following relevant examples: ccpcica, ccpmovi, cmpclr, cmpdd, cmpgrd, cmplbl, cmplot, cmptit, epltch, ffex02, fpchiqu.
<h2>Access</h2>To use MAPGRD or c_mapgrd, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.
<h2>See Also</h2>Online: ezmap, ezmap_params, mapaci, mapbla, mapblm, mapdrw, mapeod, mapfst, mapgci, mapgrm, mapgtc, mapgti, mapgtl, mapgtr, mapint, mapiq, mapiqa, mapiqd, mapiqm, mapit, mapita, mapitd, mapitm, maplbl, maplmb, maplot, mappos, maproj, maprs, maprst, mapsav, mapset, mapstc, mapsti, mapstl, mapstr, maptra, maptri, maptrn, mapusr, mapvec, mpchln, mpfnme, mpgetc, mpgeti, mpgetl, mpgetr, mpglty, mpiaty, mpifnb, mpilnb, mpiola, mpiosa, mpipai, mpipan, mpipar, mpisci, mplnam, mplndm, mplndr, mplnri, mpname, mprset, mpsetc, mpseti, mpsetl, mpsetr, supmap, supcon, ncarg_cbind 

 Hardcopy: NCAR Graphics Contouring and Mapping Tutorial
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
