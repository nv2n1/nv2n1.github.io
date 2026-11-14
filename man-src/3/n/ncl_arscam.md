---
title: "ncl_arscam(3)"
name: "ncl_arscam"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_arscam/"
---

ARSCAM - Scans an area map from left to right, extracting the definitions of all the areas defined by the area map and delivering them to a user-defined subroutine for processing. 

<h2>Synopsis</h2>CALL ARSCAM (MAP,XCS,YCS,MCS,IAI,IAG,MAI,APR)
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/ncargC.h&gt; 

 void c_arscam (int *map, float *xcs, float *ycs, int mcs, int *iai, int *iag, int mai, int (*apr)(float *xcs, float *ycs, int *ncs, int *iai, int *iag, int *nai))
<h2>Description</h2><dl COMPACT><dt>MAP
<dd>(an input/output array of type INTEGER) - An array containing an area map that has been initialized by a call to ARINAM and to which edges have been added by calls to AREDAM. If you did not preprocess the area map by calling ARPRAM, ARSCAM calls it before doing anything else. 

 Note: As part of initializing the area map, ARINAM stores the dimension of MAP in <a HREF="/docs/linux/man/1-map/">MAP</a>(1); therefore, the dimension does not have to be given as an argument in calls to ARSCAM.)
<dt>XCS,YCS
<dd>(workspace arrays, dimensioned MCS, of type REAL) - Hold the X and Y coordinates defining the edge of a given area, for use by ARSCAM in calls to the area-processing routine APR.
<dt>MCS
<dd>(an input expression of type INTEGER) - Dimension of each of the arrays XCS and YCS.
<dt>IAI,IAG
<dd>(workspace arrays, dimensioned MAI, of type INTEGER) - Hold MAI pairs of area identifiers and group identifiers, respectively. Used by ARSCAM in calls to the area-processing routine APR.
<dt>MAI
<dd>(an input expression of type INTEGER) - Dimension of each of the arrays IAI and IAG. MAI must be greater than or equal to n, where n is the number of groups in the area map.
<dt>APR
<dd>(a subroutine) - An area-processing routine that is called by ARSCAM, and must be declared EXTERNAL in the routine that calls ARSCAM. You must supply the routine APR, and it must have the following form: 

 SUBROUTINE APR (XCS,YCS,NCS,IAI,IAG,NAI) 
 DIMENSION XCS(*),YCS(*),IAI(*),IAG(*) 

 (code to process the area defined by XCS, YCS, IAI, and IAG) 

 RETURN 
 END 

<dl COMPACT><dd><dl COMPACT><dt>XCS,YCS
<dd>(input arrays, dimensioned NCS, of type REAL) - The X and Y coordinates, in NDCs, of NCS points defining a polygonal area. The last of these points is a duplicate of the first. Holes in an area are traced in a way that maximizes the probability of hardware fill working properly.
<dt>NCS
<dd>(an input expression of type INTEGER) - Number of X and Y coordinates in the arrays XCS and YCS.
<dt>IAI,IAG
<dd>(input arrays, dimensioned NAI, of type INTEGER) - Hold NAI pairs of identifiers for the area defined by XCS and YCS. For each value of I from 1 to NAI, IAI(I) is the area identifier for the area with respect to the group of edges specified by the group identifier IAG(I).
<dt>NAI
<dd>(an input expression of type INTEGER) - Number of values returned in IAI and IAG. NAI equals the number of groups of edges that you put in the area map.</dl></dl>
 

 Before executing the first call to APR, ARSCAM calls GETSET to retrieve the current user coordinates and then executes the statement: 

 CALL SET (VPL,VPR,VPB,VPT,VPL,VPR,VPB,VPT,1) 

 where VPL, VPR, VPB, and VPT are the viewport left, right, bottom, and top coordinates in NDCs. 

 This ensures correct results if the NDCs in XCS and YCS are used in calls to such routines as GFA and GPL, and it allows clipping at the edges of the viewport. APR may make its own SET call to achieve some other effect. Before returning control to the calling routine, ARSCAM calls SET again to restore the original mapping parameters.</dl><h2>C-Binding Description</h2>The C-binding argument descriptions are the same as the FORTRAN argument descriptions.
<h2>Examples</h2>Use the ncargex command to see the following relevant examples: cardb1, carfill, ccpcldm, ccpfil, ccplbam, ccpllb, ccplll, ccpllw, ccpscam, ccpvs, colcon, cmpfil, cmpgrp, cmpita, cmptit, cpex01, cpex02, cpex03, cpex04, cpex05, cpex07, cpex08, eezmpa, arex01, vvex01, tareas, tconpa, tezmpa, fcover, ffex00, fcirc, fsfsgfa, fsppoint.
<h2>Access</h2>To use ARSCAM or c_arscam, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.
<h2>Messages</h2>See the areas man page for a description of all Areas error messages and/or informational messages.
<h2>See Also</h2>Online: areas, areas_params, ardbpa, ardrln, aredam, argeti, argetr, argtai, arinam, armvam, arpram, arseti, arsetr, ncarg_cbind 

 Hardcopy: NCAR Graphics Contouring and Mapping Tutorial
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
