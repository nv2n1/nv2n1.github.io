---
title: "ncl_aredam(3)"
name: "ncl_aredam"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_aredam/"
---

AREDAM - Adds edge segments to an area map. 

<h2>Synopsis</h2>CALL AREDAM (MAP,XCA,YCA,LCA,IGI,IDL,IDR)
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/ncargC.h&gt; 

 void c_aredam (int *map, float *xca, float *yca, int lca, int igi, int idl, int idr)
<h2>Description</h2><dl COMPACT><dt>MAP
<dd>(an input/output array of type INTEGER) - An array containing an area map that has been initialized by a call to ARINAM. 

 Note: As part of initializing the area map, ARINAM stores the dimension of MAP in <a HREF="/docs/linux/man/1-map/">MAP</a>(1); therefore, the dimension does not have to be given as an argument in calls to AREDAM.)
<dt>XCA
<dd>(an input array, dimensioned LCA, of type REAL) - The X coordinates, in the user coordinate system, of the points defining an edge.
<dt>YCA
<dd>(an input array, dimensioned LCA, of type REAL) - The Y coordinates, in the user coordinate system, of the points defining an edge.
<dt>LCA
<dd>(an input expression of type INTEGER) - The number of coordinates in XCA and YCA.
<dt>IGI
<dd>(an input expression of type INTEGER) - Identifier of the group to which the edge belongs.
<dt>IDL
<dd>(an input expression of type INTEGER) - Identifier of the area that lies to the left of the edge.
<dt>IDR
<dd>(an input expression of type INTEGER) - Identifier of the area that lies to the right of the edge.</dl><h2>C-Binding Description</h2>The C-binding argument descriptions are the same as the FORTRAN argument descriptions.
<h2>Usage</h2>The area-map array MAP must have been initialized by a call to ARINAM. Each subsequent call to AREDAM adds to the area map the LCA-1 edge segments defined by the points whose user coordinates are in the arrays XCA and YCA. (Points 1 and 2 define the first edge segment, points 2 and 3 define the next edge segment, points 3 and 4 the next one, and so on.)
<h2>Examples</h2>Use the ncargex command to see the following relevant examples: cardb1, cardb2, carfill, carline, carmap, arex01, cbex01, tareas, fsppoint.
<h2>Access</h2>To use AREDAM or c_aredam, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.
<h2>Messages</h2>See the areas man page for a description of all Areas error messages and/or informational messages.
<h2>See Also</h2>Online: areas, areas_params, ardbpa, ardrln, argeti, argetr, argtai, arinam, armvam, arpram, arscam, arseti, arsetr, ncarg_cbind 

 Hardcopy: NCAR Graphics Contouring and Mapping Tutorial
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
