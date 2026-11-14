---
title: "ncl_maplbl(3)"
name: "ncl_maplbl"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_maplbl/"
---

MAPLBL - Labels the map. 

<h2>Synopsis</h2>CALL MAPLBL
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/ncargC.h&gt; 

 void c_maplbl()
<h2>Description</h2>MAPLBL has no arguments.
<h2>Usage</h2>If the parameter 'LA' is set appropriately, MAPLBL labels the international date line (ID), the equator (EQ), the Greenwich Meridian (GM), and the poles (NP and SP), and if the parameter 'PE' is set appropriately, it draws the perimeter of the map. If EZMAP needs initialization or if there is an uncleared NCAR Graphics error, MAPLBL does nothing.
<h2>Examples</h2>Use the ncargex command to see the following relevant examples: cmpclr, cmpel, cmpfil, cmpgrp, cmpita, cmpitm, cmplab, cmplbl, cmplot, cmpmsk, cmpou, cmptit, eezmpa, tezmpa, ffex00.
<h2>Access</h2>To use MAPLBL or c_maplbl, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.
<h2>See Also</h2>Online: ezmap, ezmap_params, mapaci, mapbla, mapblm, mapdrw, mapeod, mapfst, mapgci, mapgrd, mapgrm, mapgtc, mapgti, mapgtl, mapgtr, mapint, mapiq, mapiqa, mapiqd, mapiqm, mapit, mapita, mapitd, mapitm, maplmb, maplot, mappos, maproj, maprs, maprst, mapsav, mapset, mapstc, mapsti, mapstl, mapstr, maptra, maptri, maptrn, mapusr, mapvec, mpchln, mpfnme, mpgetc, mpgeti, mpgetl, mpgetr, mpglty, mpiaty, mpifnb, mpilnb, mpiola, mpiosa, mpipai, mpipan, mpipar, mpisci, mplnam, mplndm, mplndr, mplnri, mpname, mprset, mpsetc, mpseti, mpsetl, mpsetr, supmap, supcon, ncarg_cbind 

 Hardcopy: NCAR Graphics Contouring and Mapping Tutorial
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
