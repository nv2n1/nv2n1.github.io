---
title: "ncl_mpisci(3)"
name: "ncl_mpisci"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_mpisci/"
---

<pre><code>MPISCI - Given the area identifier of one of the areas defined by whatever
database was last read by one of the EZMAPB routines MPLNAM, MPLNDM, MPLNDR,
and MPLNRI, this function returns a suggested color index for that area.</code></pre>
<h2>Synopsis</h2>ISCI=MPISCI(IAIN)
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/ncargC.h&gt; 

 int c_mpisci (int iain)
<h2>Description</h2><dl COMPACT><dt>IAIN
<dd>is an input expression of type INTEGER, specifying the area identifier of a particular area of interest.</dl><h2>C-Binding Description</h2>The C-binding argument description is the same as the FORTRAN argument description.
<h2>Usage</h2>The statement &quot;ISCI=MPISCI(IAIN)&quot; retrieves in ISCI the suggested color index for the area with area identifier IAIN. For example, if IMAD is the area identifier of the little island in Lake Superior called &quot;Lake Madeline&quot;, then MPISCI(IMAD) has the value 6. The suggested color indices are defined in such a way as to ensure that areas that touch each other have different color indices. 

 To get a suggested color index for the area, at a specified level, that contains the area with a specified area identifier, use MPISCI in combination with MPIOAR (which see). For example, MPISCI(MPIOAR(IMAD,4)) has the value 6, which is the color index for &quot;Wisconsin&quot; or any portion thereof, and MPISCI(MPIOAR(IMAD,2)) = 5, which is the color index for &quot;North America&quot;.
<h2>Examples</h2>Use the ncargex command to see the following relevant examples: mpex11, mpex12.
<h2>Access</h2>To use MPISCI or c_mpisci, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.
<h2>See Also</h2>Online: ezmap, ezmap_params, mapaci, mapbla, mapblm, mapdrw, mapeod, mapfst, mapgci, mapgrd, mapgrm, mapgtc, mapgti, mapgtl, mapgtr, mapint, mapiq, mapiqa, mapiqd, mapiqm, mapit, mapita, mapitd, mapitm, maplbl, maplmb, maplot, mappos, maproj, maprs, maprst, mapsav, mapset, mapstc, mapsti, mapstl, mapstr, maptra, maptri, maptrn, mapusr, mapvec, mpchln, mpfnme, mpgetc, mpgeti, mpgetl, mpgetr, mpglty, mpiaty, mpifnb, mpilnb, mpiola, mpiosa, mpipai, mpipan, mpipar, mplnam, mplndm, mplndr, mplnri, mpname, mprset, mpsetc, mpseti, mpsetl, mpsetr, supmap, supcon, ncarg_cbind
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
