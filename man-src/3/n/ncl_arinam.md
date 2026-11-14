---
title: "ncl_arinam(3)"
name: "ncl_arinam"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_arinam/"
---

ARINAM - Initializes an area map. 

<h2>Synopsis</h2>CALL ARINAM (MAP,LMAP)
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/ncargC.h&gt; 

 void c_arinam (int *map, int lmap)
<h2>Description</h2><dl COMPACT><dt>MAP
<dd>(output array, of type INTEGER, dimensioned at least LMAP) - An integer array in which an area map is to be constructed. Each vertex for an edge segment in your area map requires ten words in the array MAP. Remember that the total number of vertices includes those added at each intersection of edges, and those added when long edge segments are broken into shorter edge segments.
<dt>LMAP
<dd>(an input expression of type INTEGER) - Length of the MAP array. As part of the initialization process, the value of LMAP is stored in <a HREF="/docs/linux/man/1-map/">MAP</a>(1); that way, it need not be given as an argument in calls to other routines that use the area map.</dl><h2>C-Binding Description</h2>The C-binding argument descriptions are the same as the FORTRAN argument descriptions.
<h2>Examples</h2>Use the ncargex command to see the following relevant examples: cardb1, cardb2, carfill, carline, carmap, ccpcldm, ccpfil, ccplbam, ccpllb, ccpllc, ccplll, ccpllo, ccpllp, ccpllt, ccpllw, ccppc, ccppc1, ccppc2, ccppc3, ccppc4, ccprc, ccpscam, ccpvs, colcon, cmpfil, cmpgrp, cmpita, cmpitm, cmplab, cmpmsk, cmptit, cpex01, cpex02, cpex03, cpex04, cpex05, cpex06, cpex07, cpex08, eezmpa, arex01, cbex01, vvex01, tareas, tconpa, tezmpa, fcover, ffex00, ffex03, ffex05, fcirc, fsfsgfa, fsppoint.
<h2>Access</h2>To use ARINAM or c_arinam, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.
<h2>See Also</h2>Online: areas, areas_params, ardbpa, ardrln, aredam, argeti, argetr, argtai, armvam, arpram, arscam, arseti, arsetr, ncarg_cbind 

 Hardcopy: NCAR Graphics Contouring and Mapping Tutorial
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
