---
title: "ncl_maproj(3)"
name: "ncl_maproj"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_maproj/"
---

MAPROJ - Sets the map projection to be used. 

<h2>Synopsis</h2>CALL MAPROJ (JPRJ, PLAT, PLON, ROTA)
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/ncargC.h&gt; 

 void c_maproj (char *jprj, float plat, float plon, 
 float rota)
<h2>Description</h2><dl COMPACT><dt>JPRJ
<dd>(an input expression, of type CHARACTER) defines the desired projection type. All the possible values are two characters in length; these are the possibilities: 

<dl COMPACT><dd>The conic projection:
<dl COMPACT><dd><dl COMPACT><dt>'LC' -
<dd>Lambert conformal conic with two standard parallels.</dl></dl>
 

 The azimuthal projections:
<dl COMPACT><dd><dl COMPACT><dt>'ST' -
<dd>Stereographic.
<dt>'OR' -
<dd>Orthographic. The EZMAP parameter 'SA' will be zeroed. See the note below.
<dt>'LE' -
<dd>Lambert equal area.
<dt>'GN' -
<dd>Gnomonic.
<dt>'AE' -
<dd>Azimuthal equidistant.
<dt>'SV' -
<dd>Satellite-view. If the EZMAP parameter 'SA' is less than or equal to 1., it will be reset to 6.631 (the value for a satellite in a geosynchronous orbit). See the note below.</dl></dl>
 

 The cylindrical projections:
<dl COMPACT><dd><dl COMPACT><dt>'CE' -
<dd>Cylindrical equidistant.
<dt>'ME' -
<dd>Mercator.
<dt>'MO' -
<dd>Mollweide-type.</dl></dl>
 

 Note: The orthographic and satellite-view projections have the same internal identifier. The EZMAP parameter 'SA' determines which will be used. If a call to MAPROJ selecting one or the other is followed by a call to MAPSTR resetting 'SA', it may have the effect of causing the other to be used.</dl><dt>PLAT,PLON,ROTA
<dd>(input expressions, of type REAL) are angular quantities, in degrees. How they are used depends on the value of JPRJ, as follows:
<dl COMPACT><dd><dl COMPACT><dt>&bull;
<dd>If JPRJ is not equal to 'LC': PLAT and PLON define the latitude and longitude of the pole of the projection, the point on the globe which is to project to the origin of the u/v plane. PLAT must be between -90. and +90., inclusive, positive in the northern hemisphere, negative in the southern. PLON must be between -180. and +180., inclusive, positive to the east, and negative to the west, of Greenwich. ROTA is the angle between the v axis and north at the origin. It is taken to be positive if the angular movement from north to the v axis is counter-clockwise, negative otherwise. If the origin is at the north pole, &quot;north&quot; is considered to be in the direction of PLON+180. If the origin is at the south pole, &quot;north&quot; is considered to be in the direction of PLON. For the cylindrical projections, the axis of the projection is parallel to the v axis.
<dt>&bull;
<dd>If JPRJ is equal to 'LC': PLON defines the central meridian of the projection, and PLAT and ROTA define the two standard parallels. If PLAT and ROTA are equal, a simpler conic projection, with one standard parallel, is used.</dl></dl>
</dl><h2>C-Binding Description</h2>The C-binding argument descriptions are the same as the FORTRAN argument descriptions.
<h2>Usage</h2>This routine allows you to set the current values of the EZMAP parameters 'PR', 'PT', 'PN', and 'RO'. For a complete list of parameters available in this utility, see the ezmap_params man page.
<h2>Examples</h2>Use the ncargex command to see the following relevant examples: ccpcica, ccpmap, ccpmovi, ccppole, ccpvp, colcon, cezmap1, cezmap2, cezmap3, cmpclr, cmpdd, cmpdrw, cmpel, cmpfil, cmpgrd, cmpgrp, cmpita, cmpitm, cmplab, cmplbl, cmplot, cmpmsk, cmpou, cmpsat, cmptit, cmptra, cmpusr, cpex01, cpex03, cpex08, cpex09, mpex01, mpex02, mpex04, mpex05, mpex06, mpex07, mpex09, mpex10, eezmpa, epltch, tezmap, tezmpa, fcover, ffex00, ffex02, ffex03, ffex05, fgkgtx, fngngdts, fpchiqu.
<h2>Access</h2>To use MAPROJ or c_maproj, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.
<h2>Messages</h2>See the ezmap man page for a description of all EZMAP error messages and/or informational messages.
<h2>See Also</h2>Online: ezmap, ezmap_params, mapaci, mapbla, mapblm, mapdrw, mapeod, mapfst, mapgci, mapgrd, mapgrm, mapgtc, mapgti, mapgtl, mapgtr, mapint, mapiq, mapiqa, mapiqd, mapiqm, mapit, mapita, mapitd, mapitm, maplbl, maplmb, maplot, mappos, maprs, maprst, mapsav, mapset, mapstc, mapsti, mapstl, mapstr, maptra, maptri, maptrn, mapusr, mapvec, mpchln, mpfnme, mpgetc, mpgeti, mpgetl, mpgetr, mpglty, mpiaty, mpifnb, mpilnb, mpiola, mpiosa, mpipai, mpipan, mpipar, mpisci, mplnam, mplndm, mplndr, mplnri, mpname, mprset, mpsetc, mpseti, mpsetl, mpsetr, supmap, supcon, ncarg_cbind 

 Hardcopy: NCAR Graphics Contouring and Mapping Tutorial
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
