---
title: "ncl_mapfst(3)"
name: "ncl_mapfst"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_mapfst/"
---

MAPFST - Draws lines on a map - used in conjunction with MAPVEC. 

<h2>Synopsis</h2>CALL MAPFST (RLAT,RLON)
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/ncargC.h&gt; 

 void c_mapfst (float rlat, float rlon)
<h2>Description</h2><dl COMPACT><dt>RLAT and RLON
<dd>(input expressions, of type REAL) specify the latitude and longitude of a point to which the &quot;pen&quot; is to be moved. Both are given in degrees. RLAT must be between -90. and +90., inclusive; RLON must be between -540. and +540., inclusive.</dl><h2>C-Binding Description</h2>The C-binding argument descriptions are the same as the FORTRAN argument descriptions.
<h2>Usage</h2>The statement:
<dl COMPACT><dd>CALL MAPFST (RLAT, RLON) 

</dl>
 is equivalent to
<dl COMPACT><dd>CALL MAPIT (RLAT, RLON, 0)</dl>
 

 It moves the &quot;pen&quot; (in the &quot;up&quot; position) to the first point in a series of points. See the man page for MAPIT.
<h2>Access</h2>To use MAPFST or c_mapfst, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.
<h2>See Also</h2>Online: ezmap, ezmap_params, mapaci, mapbla, mapblm, mapdrw, mapeod, mapgci, mapgrd, mapgrm, mapgtc, mapgti, mapgtl, mapgtr, mapint, mapiq, mapiqa, mapiqd, mapiqm, mapit, mapita, mapitd, mapitm, maplbl, maplmb, maplot, mappos, maproj, maprs, maprst, mapsav, mapset, mapstc, mapsti, mapstl, mapstr, maptra, maptri, maptrn, mapusr, mapvec, mpchln, mpfnme, mpgetc, mpgeti, mpgetl, mpgetr, mpglty, mpiaty, mpifnb, mpilnb, mpiola, mpiosa, mpipai, mpipan, mpipar, mpisci, mplnam, mplndm, mplndr, mplnri, mpname, mprset, mpsetc, mpseti, mpsetl, mpsetr, supmap, supcon, ncarg_cbind
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
