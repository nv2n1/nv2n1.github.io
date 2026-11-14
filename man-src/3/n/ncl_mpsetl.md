---
title: "ncl_mpsetl(3)"
name: "ncl_mpsetl"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_mpsetl/"
---

MAPSTL - Sets the values of certain EZMAP parameters of type LOGICAL. <pre><code>MPSETL is an alternate name for the routine MAPSTL.</code></pre>
<h2>Synopsis</h2>CALL MAPSTL (PNAM,LVAL)
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/ncargC.h&gt; 

 void c_mapstl (char *pnam, int lval)
<h2>Description</h2><dl COMPACT><dt>PNAM
<dd>(an input expression, of type CHARACTER*2) specifies the name of an internal parameter whose value is to be set. Only the first two characters of this string are examined.
<dt>LVAL
<dd>(an input expression of type LOGICAL) contains the value to be given to the parameter specified by PNAM.</dl><h2>C-Binding Description</h2>The C-binding argument descriptions are the same as the FORTRAN argument descriptions.
<h2>Usage</h2>This routine allows you to set the value of EZMAP parameters. For a complete list of parameters available in this utility, see the ezmap_params man page.
<h2>Examples</h2>The capabilities offered by the MAPSTL or MPSETL routines are also offered by the MAPSTI or MPSETI routines. See the examples listed on the MAPSTI or MPSETI man page.
<h2>Access</h2>To use MAPSTL, MPSETL, or c_mapstl, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.
<h2>Messages</h2>See the ezmap man page for a description of all EZMAP error messages and/or informational messages.
<h2>See Also</h2>Online: ezmap, ezmap_params, mapaci, mapbla, mapblm, mapdrw, mapeod, mapfst, mapgci, mapgrd, mapgrm, mapgtc, mapgti, mapgtl, mapgtr, mapint, mapiq, mapiqa, mapiqd, mapiqm, mapit, mapita, mapitd, mapitm, maplbl, maplmb, maplot, mappos, maproj, maprs, maprst, mapsav, mapset, mapstc, mapsti, mapstr, maptra, maptri, maptrn, mapusr, mapvec, mpchln, mpfnme, mpgetc, mpgeti, mpgetl, mpgetr, mpglty, mpiaty, mpifnb, mpilnb, mpiola, mpiosa, mpipai, mpipan, mpipar, mpisci, mplnam, mplndm, mplndr, mplnri, mpname, mprset, mpsetc, mpseti, mpsetl, mpsetr, supmap, supcon, ncarg_cbind
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
