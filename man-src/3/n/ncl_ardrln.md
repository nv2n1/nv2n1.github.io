---
title: "ncl_ardrln(3)"
name: "ncl_ardrln"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_ardrln/"
---

ARDRLN - Draws a polyline that is masked by a given area map. 

<h2>Synopsis</h2>CALL ARDRLN (MAP,XCD,YCD,NCD,XCS,YCS,MCS,IAI,IAG,MAI,LPR)
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/ncargC.h&gt; 

 void c_ardrln (int *map, float *xcd, float *ycd, int ncd, float *xcs, float *ycs, int mcs, int *iai, int *iag, int mai, int (*lpr)(float *xcs, float *ycs, int *ncs, int *iai, int *iag, int *nai))
<h2>Description</h2><dl COMPACT><dt>MAP
</dt><dd>(an input/output array of type INTEGER) - An array containing an area map that has been initialized by a call to ARINAM and to which edges have been added by calls to AREDAM. If you did not preprocess the area map by calling ARPRAM, ARDRLN calls it before doing anything else. 
 Note: As part of initializing the area map, ARINAM stores the dimension of MAP in <a HREF="/docs/linux/man/1-map/">MAP</a>(1); therefore, the dimension does not have to be given as an argument in calls to ARDRLN.)
</dd><dt>XCD
</dt><dd>(an input array, dimensioned NCD, of type REAL) - The X coordinates, in the user coordinate system, of the points defining the polyline.
</dd><dt>YCD
</dt><dd>(an input array, dimensioned NCD, of type REAL) - The Y coordinates, in the user coordinate system, of the points defining the polyline.
</dd><dt>NCD
</dt><dd>(an input expression of type INTEGER) - The number of points defining the polyline.
</dd><dt>XCS
</dt><dd>(a workspace array, dimensioned MCS, of type REAL) - Used by ARDRLN in calls to LPR, the user-supplied line-processing routine, to hold the X coordinates of the polyline segment contained in a given area.
</dd><dt>YCS
</dt><dd>(a workspace array, dimensioned MCS, of type REAL) - Used by ARDRLN in calls to LPR, the user-supplied line-processing routine, to hold the Y coordinates of the polyline segment contained in a given area.
</dd><dt>MCS
</dt><dd>(an input expression of type INTEGER) - Dimension of each of the arrays XCS and YCS.
</dd><dt>IAI
</dt><dd>(a workspace array, dimensioned MAI, of type INTEGER) - The area identifier array, used in calls to LPR, the user-supplied line-processing routine.
</dd><dt>IAG
</dt><dd>(a workspace array, dimensioned MAI, of type INTEGER) - The group identifier array, used in calls to LPR, the user-supplied line-processing routine.
</dd><dt>MAI
</dt><dd>(an input expression of type INTEGER) - Dimension of each of the arrays IAI and IAG. MAI must be greater than or equal to n, where n is the number of groups in the area map.
</dd><dt>LPR
</dt><dd>(a subroutine) - A line-processing routine that you supply for ARDRLN to call. LPR must be declared EXTERNAL in the routine that calls ARDRLN. LPR must have the following structure: 
 SUBROUTINE LPR (XCS,YCS,NCS,IAI,IAG,NAI) 
 DIMENSION XCS(*),YCS(*),IAI(*),IAG(*) 
 (code to process polyline defined by XCS, YCS, IAI, and IAG) 
 RETURN 
 END
</dd><dl COMPACT><dd></dd><dl COMPACT><dt>XCS,YCS
</dt><dd>(input arrays, dimensioned NCS, of type REAL) - Hold the X and Y coordinates, in NDCs, of NCS points defining a piece of the original polyline that is completely contained in one of the areas defined by the area map.
</dd><dt>NCS
</dt><dd>(an input expression of type INTEGER) - Number of X and Y coordinates in the arrays XCS and YCS.
</dd><dt>IAI,IAG
</dt><dd>(input arrays, dimensioned NAI, of type INTEGER) - Hold NAI pairs of area identifiers and group identifiers, respectively, for the area in which the piece of the polyline lies. For each value of I from 1 to NAI, IAI(I) is the area identifier for the area with respect to the group of edges specified by the group identifier IAG(I).
</dd><dt>NAI
</dt><dd>(an input expression of type INTEGER) - Number of values given in IAI and IAG. NAI equals the number of groups of edges that you put in the area map.</dd></dl></dl>
 

 Before executing the first call to LPR, ARDRLN calls GETSET to retrieve the current user-system mapping parameters and then executes the following statement: 

 CALL SET (VPL,VPR,VPB,VPT,VPL,VPR,VPB,VPT,1) 

 where VPL, VPR, VPB, and VPT are the viewport left, right, bottom, and top coordinates in NDCs. 

 This ensures correct results if the NDCs in XCS and YCS are used by the line-processing routine LPR in calls to such routines as GPL and CURVE, and it allows for clipping at the edges of the viewport. LPR may make its own SET call to achieve some other effect. Before returning control to the calling routine, ARDRLN calls SET again to restore the original mapping parameters.</dl><h2>C-Binding Description</h2>The C-binding argument descriptions are the same as the FORTRAN argument descriptions.
<h2>Examples</h2>Use the ncargex command to see the following relevant examples: carline, tareas, fsppoint.
<h2>Access</h2>To use ARDRLN or c_ardrln, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.
<h2>Messages</h2>See the areas man page for a description of all Areas error messages and/or informational messages.
<h2>See Also</h2>Online: areas, areas_params, ardbpa, aredam, argeti, argetr, argtai, arinam, armvam, arpram, arscam, arseti, arsetr, ncarg_cbind 

 Hardcopy: NCAR Graphics Contouring and Mapping Tutorial
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
