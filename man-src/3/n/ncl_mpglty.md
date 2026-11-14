---
title: "ncl_mpglty(3)"
name: "ncl_mpglty"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_mpglty/"
---

MPGLTY - Retrieves the type of the line currently being drawn by MPLNDM. 

<h2>Synopsis</h2>CALL MPGLTY (ILTY)
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/ncargC.h&gt; 

 void c_mpglty (int *ilty)
<h2>Description</h2><pre><code>ILTY
(an output variable of type INTEGER) is the type of the line: 1 =&gt; a line
separating land from water, 2 =&gt; a line separating one &quot;continent&quot; from another
(as, for example, Africa from Eurasia, North America from Central America, or
Central America from South America), 3 =&gt; a line separating one country from
another, 4 =&gt; a line separating one state from another, and 5 =&gt; a line
separating one county from another.  If the current line is used on more than
one level (as, for example, a portion of the California coastline, which is
used on all five levels), then the value of ILTY will be the smallest of the
numerical values that apply.</code></pre>
<h2>C-Binding Description</h2>The C-binding argument description is the same as the FORTRAN argument description.
<h2>Usage</h2>MPGLTY may be called from within a line-processing routine whose name is used in a call to MPLNDM to retrieve, in ILTY, the type of the line being processed. This information may be used to determine how the line is to be drawn.
<h2>Examples</h2>Use the ncargex command to see the following relevant example: mpex11.
<h2>Access</h2>To use MPGLTY or c_mpglty, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.
<h2>See Also</h2>Online: ezmap, ezmap_params, mapaci, mapbla, mapblm, mapdrw, mapeod, mapfst, mapgci, mapgrd, mapgrm, mapgtc, mapgti, mapgtl, mapgtr, mapint, mapiq, mapiqa, mapiqd, mapiqm, mapit, mapita, mapitd, mapitm, maplbl, maplmb, maplot, mappos, maproj, maprs, maprst, mapsav, mapset, mapstc, mapsti, mapstl, mapstr, maptra, maptri, maptrn, mapusr, mapvec, mpchln, mpfnme, mpgetc, mpgeti, mpgetl, mpgetr, mpiaty, mpifnb, mpilnb, mpiola, mpiosa, mpipai, mpipan, mpipar, mpisci, mplnam, mplndm, mplndr, mplnri, mpname, mprset, mpsetc, mpseti, mpsetl, mpsetr, supmap, supcon, ncarg_cbind
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
