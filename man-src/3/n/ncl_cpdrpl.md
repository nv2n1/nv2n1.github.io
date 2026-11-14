---
title: "ncl_cpdrpl(3)"
name: "ncl_cpdrpl"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_cpdrpl/"
---

CPDRPL - Provides a useful polyline-drawer for the routine CPCLDM. 

<h2>Synopsis</h2>CALL CPDRPL (XCS, YCS, NCS, IAI, IAG, NAI)
<h2>Description</h2><dl COMPACT><dt>XCS
<dd>(a REAL array of dimension at least NCS, input) is an array containing the X coordinates of NCS points defining a polyline.
<dt>YCS
<dd>(a REAL array of dimension at least NCS, input) is an array containing the Y coordinates of NCS points defining a polyline.
<dt>NCS
<dd>(INTEGER, input) is the number of points defining the polyline.
<dt>IAI
<dd>(an INTEGER array of dimension at least NAI, input) is an array of area identifiers for the area in which the polyline lies. For each I from 1 to NAI, IAI(I) is the area identifier of the area with respect to the edge group IAG(I).
<dt>IAG
<dd>(an INTEGER array of dimension at least NAI, input) is an array of group identifiers. See the description of IAI, above.
<dt>NAI
<dd>(INTEGER, input) is the number of area identifiers in the array IAI and the number of group identifiers in the array IAG.</dl><h2>Usage</h2>If CPCLDM is called, and the only object of using it, instead of CPCLDR, to draw contour lines is to avoid drawing the lines through labels, then, in the routine which calls CPCLDM, put the declaration 

<dl COMPACT><dd>EXTERNAL CPDRPL</dl>
 

 and, in the call to CPCLDM, use CPDRPL for the argument RTPL. Each time CPDRPL is called, it draws the polyline defined by its first three arguments if, and only if, none of the area identifiers defined by the other three arguments is negative.
<h2>Access</h2>To use CPDRPL, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.
<h2>See Also</h2>Online: conpack, cpback, cpchcf, cpchcl, cpchhl, cpchil, cpchll, cpcica, cpclam, cpcldm, cpcldr, cpcltr, cpcnrc, cpezct, cpgetc, cpgeti, cpgetr, cplbam, cplbdr, cpmpxy, cpmviw, cpmvrw, cppkcl, cppklb, cprect, cprset, cpscae, cpsetc, cpseti, cpsetr, cpsps1, cpsps2, ncarg_cbind 

 Hardcopy: NCAR Graphics Contouring and Mapping Tutorial
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 

 The use of this Software is governed by a License Agreement.
