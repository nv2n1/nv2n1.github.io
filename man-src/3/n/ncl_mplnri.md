---
title: "ncl_mplnri(3)"
name: "ncl_mplnri"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_mplnri/"
---

MPLNRI - Reads information from a specified EZMAP database. 

<h2>Synopsis</h2>CALL MPLNRI (FLNM)
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/ncargC.h&gt; 

 void c_mplnri (char *flnm)
<h2>Description</h2><pre><code>FLNM
(an input expression of type CHARACTER) specifies the name of the database to
be used.  MPLNRI will first look for the files of the specified database in
the current working directory;
if the files are not found there, MPLNRI will
look for them in the NCAR Graphics database directory.  The database created in
1998 and provided as part of Version 4.1 of NCAR Graphics is named &quot;Earth..1&quot;.</code></pre>
<h2>C-Binding Description</h2>The C-binding argument description is the same as the FORTRAN argument description.
<h2>Usage</h2>Calling MPLNRI causes information about the database whose name is specified by FLNM to be read into EZMAPB common blocks. Subsequent references to functions like MPIOAR, MPISCI, and so on make use of this data.
<h2>Examples</h2>Use the ncargex command to see the following relevant example: mpex12.
<h2>Access</h2>To use MPLNRI or c_mplnri, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.
<h2>See Also</h2>Online: ezmap, ezmap_params, mapaci, mapbla, mapblm, mapdrw, mapeod, mapfst, mapgci, mapgrd, mapgrm, mapgtc, mapgti, mapgtl, mapgtr, mapint, mapiq, mapiqa, mapiqd, mapiqm, mapit, mapita, mapitd, mapitm, maplbl, maplmb, maplot, mappos, maproj, maprs, maprst, mapsav, mapset, mapstc, mapsti, mapstl, mapstr, maptra, maptri, maptrn, mapusr, mapvec, mpchln, mpfnme, mpgetc, mpgeti, mpgetl, mpgetr, mpglty, mpiaty, mpifnb, mpilnb, mpiola, mpiosa, mpipai, mpipan, mpipar, mpisci, mplnam, mplndm, mplndr, mpname, mprset, mpsetc, mpseti, mpsetl, mpsetr, supmap, supcon, ncarg_cbind
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
