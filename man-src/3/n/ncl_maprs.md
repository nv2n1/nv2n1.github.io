---
title: "ncl_maprs(3)"
name: "ncl_maprs"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_maprs/"
---

MAPRS - Re-calls SET. 

<h2>Synopsis</h2>CALL MAPRS
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/ncargC.h&gt; 

 void c_maprs()
<h2>Description</h2>MAPRS has no arguments.
<h2>Usage</h2>This routine allows you to have the SPPS routine SET re-called with the same arguments that MAPINT would use, but executes a little faster than MAPINT. This is useful when you are about to call one of the routines MAPBLA, MAPDRW, MAPFST, MAPGRD, MAPGRM, MAPIQ, MAPIQA, MAPIQM, MAPIT, MAPITA, MAPITM, MAPLBL, MAPLOT, or MAPVEC (all of which depend on the proper SET call's having been done), and there has been some intervening, inappropriate, call to SET.
<h2>Examples</h2><pre><code>No example is available for MAPRS.</code></pre>
<h2>Access</h2>To use MAPRS or c_maprs, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.
<h2>See Also</h2>Online: ezmap, ezmap_params, mapaci, mapbla, mapblm, mapdrw, mapeod, mapfst, mapgci, mapgrd, mapgrm, mapgtc, mapgti, mapgtl, mapgtr, mapint, mapiq, mapiqa, mapiqd, mapiqm, mapit, mapita, mapitd, mapitm, maplbl, maplmb, maplot, mappos, maproj, maprst, mapsav, mapset, mapstc, mapsti, mapstl, mapstr, maptra, maptri, maptrn, mapusr, mapvec, mpchln, mpfnme, mpgetc, mpgeti, mpgetl, mpgetr, mpglty, mpiaty, mpifnb, mpilnb, mpiola, mpiosa, mpipai, mpipan, mpipar, mpisci, mplnam, mplndm, mplndr, mplnri, mpname, mprset, mpsetc, mpseti, mpsetl, mpsetr, supmap, supcon, ncarg_cbind 

 Hardcopy: NCAR Graphics Contouring and Mapping Tutorial
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
