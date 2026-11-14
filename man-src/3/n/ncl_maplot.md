---
title: "ncl_maplot(3)"
name: "ncl_maplot"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_maplot/"
---

MAPLOT - Draws geographical outlines. Note that this routine uses whichever old outline dataset is selected by the value of the internal parameter 'OU'; to access the new map database &quot;Earth..1&quot;, which was created in 1998, one must call instead the EZMAPB routine MPLNDR. 

<h2>Synopsis</h2>CALL MAPLOT
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/ncargC.h&gt; 

 void c_maplot()
<h2>Description</h2>MAPLOT has no arguments.
<h2>Usage</h2>MAPLOT draws the continental and/or political outlines selected by the EZMAP parameter 'OU'; the parameter 'DO' determines whether solid lines or dotted lines are drawn. If EZMAP needs initialization or if there is an uncleared NCAR Graphics error, MAPLOT does nothing.
<h2>Examples</h2>Use the ncargex command to see the following relevant examples: ccpcica, ccpmovi, ccppole, colcon, cmpclr, cmpel, cmpfil, cmpgrp, cmpita, cmpitm, cmplab, cmplot, cmpmsk, cmpou, cmptit, cpex08, mpex09, eezmpa, epltch, tezmpa, fcover, ffex00, ffex02, ffex03, ffex05, fpchiqu.
<h2>Access</h2>To use MAPLOT or c_maplot, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.
<h2>See Also</h2>Online: ezmap, ezmap_params, mapaci, mapbla, mapblm, mapdrw, mapeod, mapfst, mapgci, mapgrd, mapgrm, mapgtc, mapgti, mapgtl, mapgtr, mapint, mapiq, mapiqa, mapiqd, mapiqm, mapit, mapita, mapitd, mapitm, maplbl, maplmb, mappos, maproj, maprs, maprst, mapsav, mapset, mapstc, mapsti, mapstl, mapstr, maptra, maptri, maptrn, mapusr, mapvec, mpchln, mpfnme, mpgetc, mpgeti, mpgetl, mpgetr, mpglty, mpiaty, mpifnb, mpilnb, mpiola, mpiosa, mpipai, mpipan, mpipar, mpisci, mplnam, mplndm, mplndr, mplnri, mpname, mprset, mpsetc, mpseti, mpsetl, mpsetr, supmap, supcon, ncarg_cbind 

 Hardcopy: NCAR Graphics Contouring and Mapping Tutorial
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
