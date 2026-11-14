---
title: "ncl_cpclam(3)"
name: "ncl_cpclam"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_cpclam/"
---

CPCLAM - Adds contour lines to an area map. This is part of the process of drawing a solid-fill contour plot. 

<h2>Synopsis</h2>CALL CPCLAM (ZDAT, RWRK, IWRK, IAMA)
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/ncargC.h&gt; 

 void c_cpclam (float *zdat, float *rwrk, int *iwrk, 
 int *iama)
<h2>Description</h2>The first three arguments are arrays used in the last call to CPRECT, CPSPS1, or CPSPS2, the contents of which must not have been changed since that call.
<dl COMPACT><dt>ZDAT
<dd>(REAL array, dimensioned as specified in the last call to CPRECT, CPSPS1, or CPSPS2, input) is the data array.
<dt>RWRK
<dd>(REAL array, dimensioned as specified in the last call to CPRECT, CPSPS1, or CPSPS2, input/output) is the real workspace array.
<dt>IWRK
<dd>(INTEGER array, dimensioned as specified in the last call to CPRECT, CPSPS1, or CPSPS2, input/output) is the integer workspace array.
<dt>IAMA
<dd>(INTEGER array, dimensioned as specified in a call to ARINAM, in the package Areas) is the array containing the area map to which contour lines are to be added.</dl><h2>C-Binding Description</h2>The C-binding argument descriptions are the same as the FORTRAN argument descriptions.
<h2>Usage</h2>The routine CPCLAM, which adds contour lines generated from the data in the array ZDAT to the area map in the array IAMA, may be called at any time after the initialization call to CPRECT, CPSPS1, or CPSPS2. The area map must previously have been initialized by a call to the routine ARINAM in the utility Areas. 

 The contour lines added to the area map are as specified by the first 'NCL' elements of the parameter arrays 'CLV', 'AIA', and 'AIB'. If 'NCL' is zero, CPPKCL is called to generate these values. 

 The contour levels defined by the first 'NCL' elements of the parameter array 'CLV' are examined. If a given contour level is associated with a non-zero value of 'AIA' and/or a non-zero value of 'AIB', then contour lines at that contour level are added to the area map. If there is an associated non-zero value of 'AIA', it is used as the area identifier for the area &quot;above&quot; the line (where field values are greater than they are along the line); otherwise, a zero is used. If there is an associated non-zero value of 'AIB', it is used as the area identifier for the area &quot;below&quot; the line (where field values are less than they are along the line); otherwise, a zero is used. Note that a given contour level may occur more than once in the internal parameter array 'CLV', but there must be at most one non-zero value of 'AIA' and at most one non-zero value of 'AIB' associated with it; otherwise, an error exit occurs. 

 If the parameter 'T2D' has a non-zero value, the contour lines are smoothed, using cubic splines under tension. 

 Four other types of lines are added to the area map by CPCLAM: (1) the edge of the current viewport and possibly a set of vertical lines within the viewport, (2) the edge of the grid, (3) the edges of special-value areas, if any, and (4) the edges of out-of-range areas, if any. The area identifier for the outside of the viewport is always -1. You can use elements of the parameter array 'AIA' for 'PAI' = -1, -2, and -3 to specify the area identifiers to be used for the outside of the grid, the inside of a special-value area, and the inside of an out-of-range area, respectively; the default values of all three are -1's. Area identifiers for all other sides of these edges are determined from the area-identifier information given for the contour levels. 

 Lines are added to the area map in the following order:
<dl COMPACT><dt>&bull;
<dd>the edge of the viewport and the vertical lines within it,
<dt>&bull;
<dd>the edges of the out-of-range areas, if any,
<dt>&bull;
<dd>the edge of the grid,
<dt>&bull;
<dd>the edges of the special-value areas, if any, and,
<dt>&bull;
<dd>the contour lines, in order of increasing contour level.</dl>
 

 The edge of the viewport may actually be added to the area map twice:
<dl COMPACT><dt>&bull;
<dd>as part of the edge group with group identifier 'GIC', and
<dt>&bull;
<dd>as part of the edge group with group identifier 'GIS'.</dl>
 

 Vertical lines, if any, are added with group identifier 'GIS'. 

 The object of the edge group with group identifier 'GIS' is to break up the areas represented by the area map into smaller pieces. Whether this is done or not is under your control, by means of the internal parameters 'NVS' and 'GIS'. For more information, see the descriptions of those internal parameters in the conpack_params man page. 

 If, during the last call to CPRECT, CPSPS1 or CPSPS2, the data being contoured were found to be essentially constant, then no contour lines are added to the area map; the other lines are added, however.
<h2>Examples</h2>Use the ncargex command to see the following relevant examples: ccpcldm, ccpfil, ccplbam, ccpllb, ccpllc, ccplll, ccpllo, ccpllp, ccpllt, ccpllw, ccppc, ccppc1, ccppc2, ccppc3, ccppc4, ccppole, ccprc, ccpscam, ccpt2d, ccpvs, colcon, cpex01, cpex02, cpex03, cpex04, cpex05, cpex07, cpex08, vvex01, tconpa, fsfsgfa.
<h2>Access</h2>To use CPCLAM or c_cpclam, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.
<h2>Messages</h2>See the conpack man page for a description of all Conpack error messages and/or informational messages.
<h2>See Also</h2>Online: conpack, cpback, cpchcf, cpchcl, cpchhl, cpchil, cpchll, cpcica, cpcldm, cpcldr, cpcltr, cpcnrc, cpdrpl, cpezct, cpgetc, cpgeti, cpgetr, cplbam, cplbdr, cpmpxy, cpmviw, cpmvrw, cppkcl, cppklb, cprect, cprset, cpscae, cpsetc, cpseti, cpsetr, cpsps1, cpsps2, ncarg_cbind 

 Hardcopy: NCAR Graphics Contouring and Mapping Tutorial
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 

 The use of this Software is governed by a License Agreement.
