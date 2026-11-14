---
title: "ncl_mapgrm(3)"
name: "ncl_mapgrm"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_mapgrm/"
---

MAPGRM - Draws lines of latitude and longitude masked against an existing area map. 

<h2>Synopsis</h2>CALL MAPGRM (IAMA,XCRA,YCRA,MCRA,IAAI,IAGI,MNOG,ULPR)
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/ncargC.h&gt; 

 void c_mapgrm (int *iama, float *xcra, float *ycra, 
 int mcra, int *iaai, int *iagi, int mnog, 
 int (*ulpr)(float *xcra, float *ycra, int *ncs, 
 int *iaai, int *iagi, int *nai))
<h2>Description</h2><dl COMPACT><dt>IAMA
<dd>(an input/output array, dimensioned as specified in a call to the AREAS routine ARINAM, of type INTEGER) is the array containing the area map against which lines of latitude and longitude are to be masked. The area map must have been initialized by a call to ARINAM; it may contain edges added to it by calling MAPBLA, as is the case in the example named &quot;eezmpa&quot;, or it may contain a different set of edges to create some other desired effect. For example, an area map might be created that defines a region of interest, within which user data is available and within which lines of latitude and longitude are to be drawn. For more details, see the reference document for the package named AREAS.
<dt>XCRA and YCRA
<dd>(scratch arrays, dimensioned at least MCRA, of type REAL) are to be used by MAPGRM in calls to the AREAS routine ARDRLN; they will eventually be used in calls to the user-provided line-processing routine ULPR.
<dt>MCRA
<dd>(an input expression of type INTEGER) is the dimension of the arrays XCRA and YCRA.
<dt>IAAI and IAGI
<dd>(scratch arrays, dimensioned at least NOGI, of type INTEGER) are to be used by MAPGRM in calls to the AREAS routine ARDRLN; they will eventually be used in calls to the user-provided line-processing routine ULPR. The mnemonics stand for &quot;Integer Array of Area Identifiers&quot; and &quot;Integer Array of Group Identifiers&quot;, respectively.
<dt>NOGI
<dd>(an input expression of type INTEGER) is the dimension of the arrays IAAI and IAGI. The mnemonic stands for &quot;Number Of Group Identifiers (of edges in the area map)&quot;, which determines the required dimension of IAAI and IAGI.
<dt>ULPR
<dd>is the name of the user-supplied line-processing routine. It must be declared EXTERNAL in the routine that calls MAPGRM, so that the compiler and loader will know that it is the name of a routine to be called instead of a variable. The user routine ULPR will be called once for each piece of a latitude/longitude line resulting from the masking process; it may decide to draw (or to not draw) each such piece. ULPR will be called using a FORTRAN statement like 

<dl COMPACT><dd>CALL ULPR (XCRA,YCRA,NCRA,IAAI,IAGI,NGPS)</dl><dd>where XCRA and YCRA are real arrays holding the normalized device coordinates of NCRA points defining a polyline which is part of some latitude/longitude line and IAAI and IAGI are integer arrays holding NGPS area-identifier/group-identifier pairs for the area within which that piece of the line lies. In writing ULPR, the user may rely upon a SET call's having been done which makes it possible to use normalized device coordinates in calls to routines like CURVE, CURVED, GPL, etc. For more details, see the reference document for the package named AREAS and, in particular, the description of the subroutine ARDRLN.</dl><h2>C-Binding Description</h2>The C-binding argument descriptions are the same as the FORTRAN argument descriptions.
<h2>Usage</h2>The statement
<dl COMPACT><dd>CALL MAPGRM (IAMA,XCRA,YCRA,MCRA,IAAI,IAGI,MNOG,ULPR)</dl>
 

 does the same thing as the statement
<dl COMPACT><dd>CALL MAPGRD</dl>
 

 except that the grid lines are drawn using calls to MAPITM and MAPIQM, which does the masking of the lines against the area map defined by the arguments in the call and passes the pieces resulting from the masking process to a user-provided line-drawing routine.
<h2>Examples</h2>Use the ncargex command to see the following relevant examples: ccppole, cmpfil, cmpgrp, cmpitm, cmplab, cmpmsk, cmptit, cpex08, eezmpa, tezmpa, fcover, ffex03, ffex05.
<h2>Access</h2>To use MAPGRM or c_mapgrm, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.
<h2>See Also</h2>Online: ezmap, ezmap_params, mapaci, mapbla, mapblm, mapdrw, mapeod, mapfst, mapgci, mapgrd, mapgtc, mapgti, mapgtl, mapgtr, mapint, mapiq, mapiqa, mapiqd, mapiqm, mapit, mapita, mapitm, mapitd, maplbl, maplmb, maplot, mappos, maproj, maprs, maprst, mapsav, mapset, mapstc, mapsti, mapstl, mapstr, maptra, maptri, maptrn, mapusr, mapvec, mpchln, mpfnme, mpgetc, mpgeti, mpgetl, mpgetr, mpglty, mpiaty, mpifnb, mpilnb, mpiola, mpiosa, mpipai, mpipan, mpipar, mpisci, mplnam, mplndm, mplndr, mplnri, mpname, mprset, mpsetc, mpseti, mpsetl, mpsetr, supmap, supcon, ncarg_cbind 

 Hardcopy: NCAR Graphics Contouring and Mapping Tutorial
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
