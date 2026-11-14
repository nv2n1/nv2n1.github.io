---
title: "ncl_mpifnb(3)"
name: "ncl_mpifnb"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_mpifnb/"
---

MPIFNB - A simple utility function that finds the index of the first non-blank character in a character string. 

<h2>Synopsis</h2>IFNB=MPIFNB(CHRS)
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/ncargC.h&gt; 

 int c_mpifnb (char *chrs)
<h2>Description</h2><dl COMPACT><dt>CHRS
<dd>is an input expression of type CHARACTER.</dl><h2>C-Binding Description</h2>The C-binding argument description is the same as the FORTRAN argument description.
<h2>Usage</h2>The statement &quot;IFNB=MPIFNB(CHRS)&quot; sets the value of IFNB to the index (between 1 and LEN(CHRS)) of the first non-blank character in the character string CHRS.
<h2>Examples</h2>None.
<h2>Access</h2>To use MPIFNB or c_mpifnb, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.
<h2>See Also</h2>Online: ezmap, ezmap_params, mapaci, mapbla, mapblm, mapdrw, mapeod, mapfst, mapgci, mapgrd, mapgrm, mapgtc, mapgti, mapgtl, mapgtr, mapint, mapiq, mapiqa, mapiqd, mapiqm, mapit, mapita, mapitd, mapitm, maplbl, maplmb, maplot, mappos, maproj, maprs, maprst, mapsav, mapset, mapstc, mapsti, mapstl, mapstr, maptra, maptri, maptrn, mapusr, mapvec, mpchln, mpfnme, mpgetc, mpgeti, mpgetl, mpgetr, mpglty, mpiaty, mpilnb, mpiola, mpiosa, mpipai, mpipan, mpipar, mpisci, mplnam, mplndm, mplndr, mplnri, mpname, mprset, mpsetc, mpseti, mpsetl, mpsetr, supmap, supcon, ncarg_cbind
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
