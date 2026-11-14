---
title: "ncl_mpipan(3)"
name: "ncl_mpipan"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_mpipan/"
---

<pre><code>MPIPAN - Given the area identifier of one of the areas defined by whatever
database was last read by the EZMAPB routines MPLNAM, MPLNDM, MPLNDR, and
MPLNRI and a name, this function has a non-zero value if and only if the
area with the specified area identifier is part of some area with the
specified name.</code></pre>
<h2>Synopsis</h2>IPRT=MPIPAN(IAIN,ANME)
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/ncargC.h&gt; 

 int c_mpipan (int iain, char *anme)
<h2>Description</h2><dl COMPACT><dt>IAIN
<dd>is an input expression of type INTEGER, specifying the area identifier of a particular area of interest.
<dt>ANME
<dd>is an input expression of type CHARACTER, specifying a name of interest.</dl><h2>C-Binding Description</h2>The C-binding argument description is the same as the FORTRAN argument description.
<h2>Usage</h2>The statement &quot;IPRT=MPIPAN(IAIN,ANME)&quot; sets IPRT non-zero if and only if the area having area identifier IAIN is a part of some area having the name ANME. For example, if IMAD is the area identifier of the little island in Lake Superior called &quot;Lake Madeline&quot;, then MPIPAN(IMAD,'Conterminous US') has a non-zero value, but MPIPAN(IMAD,'Russia') does not.
<h2>Examples</h2>None.
<h2>Access</h2>To use MPIPAN or c_mpipan, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.
<h2>See Also</h2>Online: ezmap, ezmap_params, mapaci, mapbla, mapblm, mapdrw, mapeod, mapfst, mapgci, mapgrd, mapgrm, mapgtc, mapgti, mapgtl, mapgtr, mapint, mapiq, mapiqa, mapiqd, mapiqm, mapit, mapita, mapitd, mapitm, maplbl, maplmb, maplot, mappos, maproj, maprs, maprst, mapsav, mapset, mapstc, mapsti, mapstl, mapstr, maptra, maptri, maptrn, mapusr, mapvec, mpchln, mpfnme, mpgetc, mpgeti, mpgetl, mpgetr, mpglty, mpiaty, mpifnb, mpilnb, mpiola, mpiosa, mpipai, mpipar, mpisci, mplnam, mplndm, mplndr, mplnri, mpname, mprset, mpsetc, mpseti, mpsetl, mpsetr, supmap, supcon, ncarg_cbind
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
