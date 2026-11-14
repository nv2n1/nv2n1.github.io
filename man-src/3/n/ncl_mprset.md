---
title: "ncl_mprset(3)"
name: "ncl_mprset"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_mprset/"
---

MPRSET - Reset the internal state of EZMAP/EZMAPA to the default. 

<h2>Synopsis</h2>CALL MPRSET
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/ncargC.h&gt; 

 void c_mprset()
<h2>Description</h2>MPRSET has no arguments.
<h2>Usage</h2>MPRSET - Calling this routine resets the internal parameters of EZMAP/EZMAPA to the default state and recalls the routine MAPINT to initialize the package.
<h2>Examples</h2><pre><code>No example is available for MPRSET.</code></pre>
<h2>Access</h2>To use MPRSET or c_mprset, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.
<h2>See Also</h2>Online: ezmap, ezmap_params, mapaci, mapbla, mapblm, mapdrw, mapeod, mapfst, mapgci, mapgrd, mapgrm, mapgtc, mapgti, mapgtl, mapgtr, mapint, mapiq, mapiqa, mapiqd, mapiqm, mapit, mapita, mapitd, mapitm, maplbl, maplmb, maplot, mappos, maproj, maprs, maprst, mapsav, mapset, mapstc, mapsti, mapstl, mapstr, maptra, maptri, maptrn, mapusr, mapvec, mpchln, mpfnme, mpgetc, mpgeti, mpgetl, mpgetr, mpglty, mpiaty, mpifnb, mpilnb, mpiola, mpiosa, mpipai, mpipan, mpipar, mpisci, mplnam, mplndm, mplndr, mplnri, mpname, mpsetc, mpseti, mpsetl, mpsetr, supmap, supcon, ncarg_cbind 

 Hardcopy: NCAR Graphics Contouring and Mapping Tutorial
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
