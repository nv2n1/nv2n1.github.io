---
title: "ncl_argtai(3)"
name: "ncl_argtai"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_argtai/"
---

ARGTAI - Returns the area identifiers associated with a given point. 

<h2>Synopsis</h2>CALL ARGTAI (MAP,XCD,YCD,IAI,IAG,MAI,NAI,ICF)
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/ncargC.h&gt; 

 void c_argtai (int *map, float xcd, float ycd, int *iai, int *iag, int mai, int *nai, int icf)
<h2>Description</h2><dl COMPACT><dt>MAP
<dd>(an input/output array of type INTEGER) - An array containing an area map that has been initialized by a call to ARINAM and to which edges have been added by calls to AREDAM. If you did not preprocess the area map by calling ARPRAM, ARGTAI calls it before doing anything else. 

 Note: As part of initializing the area map, ARINAM stores the dimension of MAP in <a HREF="/docs/linux/man/1-map/">MAP</a>(1); therefore, the dimension does not have to be given as an argument in calls to ARGTAI.)
<dt>XCD
<dd>(an input expression of type REAL) - The X coordinate, in the current user coordinate system, of a point about which you want to obtain information.
<dt>YCD
<dd>(an input expression of type REAL) - The Y coordinate, in the current user coordinate system, of a point about which you want to obtain information.
<dt>IAI
<dd>(an output array, dimensioned MAI, of type INTEGER) - The array in which area identifiers for the area containing the specified point will be returned.
<dt>IAG
<dd>(an output array, dimensioned MAI, of type INTEGER) - The array in which group identifiers for the area containing the specified point will be returned.
<dt>MAI
<dd>(an input expression of type INTEGER) - Dimension of each of the arrays IAI and IAG. MAI must be greater than or equal to NAI.
<dt>NAI
<dd>(an output expression of type INTEGER) - The number of values returned in IAI and IAG. NAI equals the number of groups of edges that you put in the area map.
<dt>ICF
<dd>(an input expression of type INTEGER) - Flag set nonzero by you to indicate that the definition of the user coordinate system has been changed since the last call to ARGTAI; in this case, calls to GETSET must be executed by ARGTAI. If you set the flag to zero, Areas assumes that the information retrieved previously is still correct and skips calls to GETSET. This option is valuable if you are planning to make thousands of calls to ARGTAI with the same area map: do the first one with ICF = 1 and the rest with ICF = 0.</dl><h2>C-Binding Description</h2>The C-binding argument descriptions are the same as the FORTRAN argument descriptions.
<h2>Examples</h2>Use the ncargex command to see the following relevant examples: carfill, carline, carmap, cbex01, tareas, fsppoint.
<h2>Access</h2>To use ARGTAI or c_argtai, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.
<h2>Messages</h2>See the areas man page for a description of all Areas error messages and/or informational messages.
<h2>See Also</h2>Online: areas, areas_params, ardbpa, ardrln, aredam, argeti, argetr, arinam, armvam, arpram, arscam, arseti, arsetr, ncarg_cbind 

 Hardcopy: NCAR Graphics Contouring and Mapping Tutorial
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
