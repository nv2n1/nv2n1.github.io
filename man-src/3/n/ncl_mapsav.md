---
title: "ncl_mapsav(3)"
name: "ncl_mapsav"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_mapsav/"
---

<pre><code>MAPSAV - Saves the current state of EZMAP for later restoration
by MAPRST.</code></pre>
<h2>Synopsis</h2>CALL MAPSAV (INFO)
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/ncargC.h&gt; 

 void c_mapsav (int info)
<h2>Description</h2><dl COMPACT><dt>INFO
<dd>(an input expression, of type INTEGER) is the number of a unit to which a single unformatted record is to be written. It is the user's responsibility to position this unit. MAPSAV does not rewind it, either before or after writing the record.</dl><h2>C-Binding Description</h2>The C-binding argument description is the same as the FORTRAN argument description.
<h2>Usage</h2>This routine allows you to save internal parameter values to a file. For a complete list of parameters available in this utility, see the ezmap_params man page.
<h2>Examples</h2><pre><code>No example is available for MAPSAV.</code></pre>
<h2>Access</h2>To use MAPSAV or c_mapsav, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.
<h2>Messages</h2>See the ezmap man page for a description of all EZMAP error messages and/or informational messages.
<h2>See Also</h2>Online: ezmap, ezmap_params, mapaci, mapbla, mapblm, mapdrw, mapeod, mapfst, mapgci, mapgrd, mapgrm, mapgtc, mapgti, mapgtl, mapgtr, mapint, mapiq, mapiqa, mapiqd, mapiqm, mapit, mapita, mapitd, mapitm, maplbl, maplmb, maplot, mappos, maproj, maprs, maprst, mapset, mapstc, mapsti, mapstl, mapstr, maptra, maptri, maptrn, mapusr, mapvec, mpchln, mpfnme, mpgetc, mpgeti, mpgetl, mpgetr, mpglty, mpiaty, mpifnb, mpilnb, mpiola, mpiosa, mpipai, mpipan, mpipar, mpisci, mplnam, mplndm, mplndr, mplnri, mpname, mprset, mpsetc, mpseti, mpsetl, mpsetr, supmap, supcon, ncarg_cbind 

 Hardcopy: NCAR Graphics Contouring and Mapping Tutorial
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
