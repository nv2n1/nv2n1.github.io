---
title: "ncl_mapita(3)"
name: "ncl_mapita"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_mapita/"
---

MAPITA - Adds to an area map the projections of lines defined by a series of lat/lon coordinates. 

<h2>Synopsis</h2>CALL MAPITA (RLAT,RLON,IFST,IAMA,IGID,IAIL,IAIR) 

 CALL MAPIQA (IAMA,IGID,IAIL,IAIR)
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/ncargC.h&gt; 

 void c_mapita (float rlat, float rlon, int ifst, 
 int *iama, int igid, int iail, int iair) 

 void c_mapiqa (int *iama, int igid, int iail, int iair)
<h2>Description</h2><pre><code>RLAT and RLON(input expressions, of type REAL) specify the latitude and longitude of a point to which the &quot;pen&quot; is to be moved.Both are given in
        degrees.RLAT must be between
        - 90. and
    +90.,
    inclusive;
RLON must be
            between -
        540. and
    +540.,
    inclusive.IFST(an input expression, of type INTEGER) is 0 to do a &quot;pen-up&quot; move, 1 to do a &quot;pen-down&quot; move only if the distance from the last point to the new point is greater than 'MV' plotter units, and2 or greater to do a &quot;pen-down&quot; move regardless of the distance from the last point to the new one.IAMA(an input / output array of type INTEGER, dimensioned as specified in a call to the AREAS initialization routine ARINAM) is the area map to which lines in MAPITA's buffer are to be added. IGID(an input expression of type INTEGER) is the group identifier to be passed to the AREAS routine AREDAM when the lines in MAPITA's buffer are added to the area map in IAMA.IAIL(an input expression of type INTEGER) is the left area identifier to be passed to the AREAS routine AREDAM when the lines in MAPITA's buffer are added to the area map in IAMA.IAIR(an input expression of type INTEGER) is the right area identifier to be passed to the AREAS routine AREDAM when the lines in MAPITA's buffer are added to the area map in IAMA.</code></pre>
<h2>C-Binding Description</h2>The C-binding argument descriptions are the same as the FORTRAN argument descriptions.
<h2>Usage</h2>The routines MAPITA and MAPIQA may be used to add lines defined by a set of user-specified latitudes and longitudes to an area map; they attempt to omit non-visible portions of lines and to handle &quot;cross-over&quot;, in the same way that MAPIT does. 

 MAPITA is called like the EZMAP routine MAPIT, but it has some additional arguments: 

<dl COMPACT><dd>CALL MAPITA (RLAT,RLON,IFST,IAMA,IGID,IAIL,IAIR)</dl>
 

 Additional arguments are the area map array IAMA, a group identifier IGID, and left and right area identifiers IAIL and IAIR. MAPIQA is called like the EZMAP routine MAPIQ, to terminate a series of calls to MAPITA and to flush the buffers; it has the same additional arguments: 

<dl COMPACT><dd>CALL MAPIQA (IAMA,IGID,IAIL,IAIR)</dl>
 

 The additional arguments are passed by MAPITA and MAPIQA to the routine AREDAM, in the package named AREAS. 

 For more information, see the man page for the routine MAPIT.
<h2>Examples</h2>Use the ncargex command to see the following relevant examples: cmpita, cpex08.
<h2>Access</h2>To use MAPITA or c_mapita, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.
<h2>See Also</h2>Online: ezmap, ezmap_params, mapaci, mapbla, mapblm, mapdrw, mapeod, mapfst, mapgci, mapgrd, mapgrm, mapgtc, mapgti, mapgtl, mapgtr, mapint, mapiq, mapiqa, mapiqd, mapiqm, mapit, mapitd, mapitm, maplbl, maplmb, maplot, mappos, maproj, maprs, maprst, mapsav, mapset, mapstc, mapsti, mapstl, mapstr, maptra, maptri, maptrn, mapusr, mapvec, mpchln, mpfnme, mpgetc, mpgeti, mpgetl, mpgetr, mpglty, mpiaty, mpifnb, mpilnb, mpiola, mpiosa, mpipai, mpipan, mpipar, mpisci, mplnam, mplndm, mplndr, mplnri, mpname, mprset, mpsetc, mpseti, mpsetl, mpsetr, supmap, supcon, ncarg_cbind 

 Hardcopy: NCAR Graphics Contouring and Mapping Tutorial
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
