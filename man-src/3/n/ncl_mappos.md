---
title: "ncl_mappos(3)"
name: "ncl_mappos"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_mappos/"
---

MAPPOS - Positions the map on the plotter frame. 

<h2>Synopsis</h2>CALL MAPPOS (XLOW,XROW,YBOW,YTOW)
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/ncargC.h&gt; 

 void c_mappos (float xlow, float xrow, float ybow, 
 float ytow)
<h2>Description</h2><dl COMPACT><dt>XLOW
<dd>(an input expression, of type REAL) specifies the position of the left edge of the window. The default is .05.
<dt>XROW
<dd>(an input expression, of type REAL) specifies the position of the right edge of the window. The default is .95.
<dt>YBOW
<dd>(an input expression, of type REAL) specifies the position of the bottom edge of the window. The default is .05.
<dt>YTOW
<dd>(an input expression, of type REAL) specifies the position of the top edge of the window. The default is .95.</dl><h2>C-Binding Description</h2>The C-binding argument descriptions are the same as the FORTRAN argument descriptions.
<h2>Usage</h2>This routine allows you to set the current values of the four EZMAP parameters 'XL', 'XR', 'YB', and 'YT'. For a complete list of parameters available in this utility, see the ezmap_params man page.
<h2>Examples</h2>Use the ncargex command to see the following relevant examples: caredg, ccpcica, ccpmovi, ccppole, ccpvp, cmppos, cmptit, cpex03, cpex08, mpex04, mpex05, mpex06, mpex07, epltch, fgkgpl, fpchiqu.
<h2>Access</h2>To use MAPPOS or c_mappos, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.
<h2>Messages</h2>See the ezmap man page for a description of all EZMAP error messages and/or informational messages.
<h2>See Also</h2>Online: ezmap, ezmap_params, mapaci, mapbla, mapblm, mapdrw, mapeod, mapfst, mapgci, mapgrd, mapgrm, mapgtc, mapgti, mapgtl, mapgtr, mapint, mapiq, mapiqa, mapiqd, mapiqm, mapit, mapita, mapitd, mapitm, maplbl, maplmb, maplot, maproj, maprs, maprst, mapsav, mapset, mapstc, mapsti, mapstl, mapstr, maptra, maptri, maptrn, mapusr, mapvec, mpchln, mpfnme, mpgetc, mpgeti, mpgetl, mpgetr, mpglty, mpiaty, mpifnb, mpilnb, mpiola, mpiosa, mpipai, mpipan, mpipar, mpisci, mplnam, mplndm, mplndr, mplnri, mpname, mprset, mpsetc, mpseti, mpsetl, mpsetr, supmap, supcon, ncarg_cbind 

 Hardcopy: NCAR Graphics Contouring and Mapping Tutorial
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
