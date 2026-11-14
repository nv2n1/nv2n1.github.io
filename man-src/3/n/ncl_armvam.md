---
title: "ncl_armvam(3)"
name: "ncl_armvam"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_armvam/"
---

ARMVAM - Moves an area map from one integer array to another. 

<h2>Synopsis</h2>CALL ARMVAM (IAM,IAN,LAN)
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/ncargC.h&gt; 

 void c_armvam (int *iam, int *ian, int lan)
<h2>Description</h2><dl COMPACT><dt>IAM
<dd>(an input array of type INTEGER) - An array containing an area map that has at least been initialized by a call to ARINAM. 

 Note: As part of initializing the area map, ARINAM stores the dimension of MAP in <a HREF="/docs/linux/man/1-map/">MAP</a>(1); therefore, the dimension does not have to be given as an argument in calls to ARMVAM.)
<dt>IAN
<dd>(an input array, dimensioned LAN, of type INTEGER) - An array to which the area map in the array IAM is to be moved.
<dt>LAN
<dd>(an input expression of type INTEGER) - The length of the array IAN. This may be less than or greater than the length of the array IAM.</dl><h2>C-Binding Description</h2>The C-binding argument descriptions are the same as the FORTRAN argument descriptions.
<h2>Usage</h2>This routine may be used for two purposes: 1) to pack an area map down into the smallest possible space in the area map array; 2) during recovery from an area map array overflow condition, to move the area map from a smaller array to a larger array. 

 The area-map array IAM must at least have been initialized by a call to ARINAM, and it may have appeared in calls to one or more of AREDAM, ARPRAM, ARGTAI, ARDRLN, and ARSCAM. If the arrays IAM and IAN overlap in memory, they must start at the same location in memory.
<h2>Examples</h2>Use the ncargex command to see the following relevant examples: arex02.
<h2>Access</h2>To use ARMVAM or c_armvam, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.
<h2>Messages</h2>See the areas man page for a description of all Areas error messages and/or informational messages.
<h2>See Also</h2>Online: areas, areas_params, ardbpa, ardrln, argeti, argetr, argtai, arinam, arpram, arscam, arseti, arsetr, ncarg_cbind 

 Hardcopy: NCAR Graphics Contouring and Mapping Tutorial
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
