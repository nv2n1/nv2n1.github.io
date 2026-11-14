---
title: "ncl_mapset(3)"
name: "ncl_mapset"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_mapset/"
---

MAPSET - Specifies the rectangular portion of the u/v plane to be drawn. 

<h2>Synopsis</h2>CALL MAPSET (JLTS, PLM1, PLM2, PLM3, PLM4)
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/ncargC.h&gt; 

 void c_mapset (char *jlts, float *plm1, float *plm2, 
 float *plm3, float *plm4)
<h2>Description</h2><dl COMPACT><dt>JLTS
<dd>(an input expression, of type CHARACTER) is a character string specifying how the limits of the map are to be chosen. There are six possibilities, as follows: <pre><code>&amp;bull;
JLTS = 'MA'(MAXIMUM).The maximum useful area produced by the projection
           is plotted.PLM1,
    PLM2, PLM3, and PLM4 are not used.&amp; bull;
JLTS = 'CO'(CORNERS).The points(PLM1, PLM2) and (PLM3, PLM4) are to be at opposite corners of the map.PLM1 and PLM3 are latitudes, in degrees.PLM2 and PLM4 are longitudes, in degrees.If a cylindrical projection is being used, the first point should be on the left edge of the map and the second point on the right edge;
otherwise, the order makes no difference.
               &amp;bull;
JLTS = 'PO'(POINTS).PLM1, PLM2, PLM3, and PLM4 are two - element arrays giving the latitudes and longitudes, in degrees, of four points which are to be on the edges of the rectangular map.If a cylindrical projection is being used, the first point should be on the left edge and the second point on the right edge;
otherwise, the order makes no difference.
               &amp;bull;
JLTS = 'AN'(ANGLES).PLM1, PLM2, PLM3, and PLM4 are positive angles, in degrees, representing angular distances from a point on the map to the left, right, bottom, and top edges of the map, respectively.For most projections, these angles are measured with the center of the earth at the vertex and represent angular distances from the point which projects to the origin of the u / v plane; on a satellite-view projection, they are
measured with the satellite at the vertex and represent angular
deviations from the line of sight. Angular limits are particularly useful
for polar projections and for the satellite-view projection; they are not
appropriate for the Lambert conformal conic and an error will result if
one attempts to use JLTS='AN' with JPRJ='LC'.
&amp;bull;
JLTS = 'LI'(LIMITS).PLM1, PLM2, PLM3, and PLM4 specify the minimum value of u, the maximum value of u, the minimum value of v, and the maximum value of v, respectively.Knowledge of the projection equations is necessary in order to use this option correctly.&amp;bull;
JLTS = 'GR'(GRID).PLM1, PLM2, PLM3, and PLM4 specify the minimum value of latitude, the minimum value of longitude, the maximum value of latitude,
    and the maximum value of longitude, in degrees, on a lat / lon grid.The limits will be determined in such a way as to ensure that the entire grid will be visible on the map.

                                                               PLM1,
    PLM2, PLM3, and PLM4(input arrays, dimensioned 2, of type REAL) are as described above, depending on the value of JLTS.Note that each is a two - element array.Strictly speaking, the FORTRAN standard requires that they be declared as such, even when only the first element of each array is used.</code></pre>
<h2>C-Binding Description</h2>The C-binding argument descriptions are the same as the FORTRAN argument descriptions.
<h2>Usage</h2>This routine allows you to set the current values of the EZMAP parameters 'AR', 'P1', 'P2', ... 'P7', and 'P8'. For a complete list of parameters available in this utility, see the ezmap_params man page.
<h2>Examples</h2>Use the ncargex command to see the following relevant examples: ccpcica, ccpmap, ccpmovi, ccppole, ccpvp, colcon, cezmap1, cezmap2, cezmap3, cmpclr, cmpdd, cmpdrw, cmpfil, cmpgrd, cmpgrp, cmpita, cmpitm, cmplab, cmplbl, cmplot, cmpmsk, cmpou, cmptra, cpex01, cpex03, cpex08, cpex09, mpex01, mpex02, mpex04, mpex07, mpex09, mpex10, eezmpa, tezmap, tezmpa, fcover, ffex00, ffex02, ffex03, ffex05, fgkgpl, fgkgtx, fngngdts.
<h2>Access</h2>To use MAPSET or c_mapset, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.
<h2>Messages</h2>See the ezmap man page for a description of all EZMAP error messages and/or informational messages.
<h2>See Also</h2>Online: ezmap, ezmap_params, mapaci, mapbla, mapblm, mapdrw, mapeod, mapfst, mapgci, mapgrd, mapgrm, mapgtc, mapgti, mapgtl, mapgtr, mapint, mapiq, mapiqa, mapiqd, mapiqd, mapiqm, mapit, mapita, mapitd, mapitd, mapitm, maplbl, maplmb, maplot, mappos, maproj, maprs, maprst, mapsav, mapstc, mapsti, mapstl, mapstr, maptra, maptri, maptrn, mapusr, mapvec, mpchln, mpfnme, mpgetc, mpgeti, mpgetl, mpgetr, mpglty, mpiaty, mpifnb, mpilnb, mpiola, mpiosa, mpipai, mpipan, mpipar, mpisci, mplnam, mplndm, mplndr, mplnri, mpname, mprset, mpsetc, mpseti, mpsetl, mpsetr, supmap, supcon, ncarg_cbind 

 Hardcopy: NCAR Graphics Contouring and Mapping Tutorial
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
