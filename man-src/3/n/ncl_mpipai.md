---
title: "ncl_mpipai(3)"
name: "ncl_mpipai"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_mpipai/"
---

<pre><code>MPIPAI - Given the area identifiers of two of the areas defined by whatever
database was last read by the EZMAPB routines MPLNAM, MPLNDM, MPLNDR, and
MPLNRI, this function has a non-zero value if and only if the first area is
a part of the second.</code></pre>
<h2>Synopsis</h2>IPRT=MPIPAI(IAIN,IAIP)
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/ncargC.h&gt; 

 int c_mpipai (int iain, int iaip)
<h2>Description</h2><dl COMPACT><dt>IAIN
<dd>is an input expression of type INTEGER, specifying the area identifier of a particular area of interest.
<dt>IAIP
<dd>is an input expression of type INTEGER, specifying the area identifier of a second area of interest.</dl><h2>C-Binding Description</h2>The C-binding argument description is the same as the FORTRAN argument description.
<h2>Usage</h2>The statement &quot;IPRT=MPIPAI(IAIN,IAIP)&quot; sets IPRT non-zero if and only if the area having area identifier IAIN is a part of the area having area identifier IAIP. For example, if IMAD is the area identifier of the little island in Lake Superior called &quot;Lake Madeline&quot;, ICUS is the area identifier of the area called 'Conterminous US', and IRUS is the area identifier of the area called 'Russia', then MPIPAI(IMAD,ICUS) has a non-zero value, but MPIPAI(IMAD,IRUS) does not.
<h2>Examples</h2>None.
<h2>Access</h2>To use MPIPAI or c_mpipai, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.
<h2>See Also</h2>Online: ezmap, ezmap_params, mapaci, mapbla, mapblm, mapdrw, mapeod, mapfst, mapgci, mapgrd, mapgrm, mapgtc, mapgti, mapgtl, mapgtr, mapint, mapiq, mapiqa, mapiqd, mapiqm, mapit, mapita, mapitd, mapitm, maplbl, maplmb, maplot, mappos, maproj, maprs, maprst, mapsav, mapset, mapstc, mapsti, mapstl, mapstr, maptra, maptri, maptrn, mapusr, mapvec, mpchln, mpfnme, mpgetc, mpgeti, mpgetl, mpgetr, mpglty, mpiaty, mpifnb, mpilnb, mpiola, mpiosa, mpipan, mpipar, mpisci, mplnam, mplndm, mplndr, mplnri, mpname, mprset, mpsetc, mpseti, mpsetl, mpsetr, supmap, supcon, ncarg_cbind
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
