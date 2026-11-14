---
title: "ncl_cpcldr(3)"
name: "ncl_cpcldr"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_cpcldr/"
---

CPCLDR - Draws contour lines. 

<h2>Synopsis</h2>CALL CPCLDR (ZDAT, RWRK, IWRK)
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/ncargC.h&gt; 

 void c_cpcldr (float *zdat, float *rwrk, int *iwrk)
<h2>Description</h2>All three arguments are arrays used in the last call to CPRECT, CPSPS1, or CPSPS2, the contents of which must not have been changed since that call.
<dl COMPACT><dt>ZDAT
<dd>(REAL array, dimensioned as specified in the last call to CPRECT, CPSPS1, or CPSPS2, input) is the data array.
<dt>RWRK
<dd>(REAL array, dimensioned as specified in the last call to CPRECT, CPSPS1, or CPSPS2, input/output) is the real workspace array.
<dt>IWRK
<dd>(INTEGER array, dimensioned as specified in the last call to CPRECT, CPSPS1, or CPSPS2, input/output) is the integer workspace array.</dl><h2>C-Binding Description</h2>The C-binding argument descriptions are the same as the FORTRAN argument descriptions.
<h2>Usage</h2>The routine CPCLDR, which draws contour lines, may be called at any time after the initialization call to CPRECT, CPSPS1, or CPSPS2. The contour lines drawn are those specified by the first 'NCL' elements of the parameter arrays 'CLV' and 'CLU'. If 'NCL' is zero, CPPKCL is called to generate these values. Each element of 'CLV' specifies a contour level, and the corresponding element of 'CLU' specifies whether or not contour lines are to be drawn at that level and whether or not the lines are to be labeled. If the parameter 'T2D' has a non-zero value, the contour lines are smoothed, using cubic splines under tension. 

 If the element of the parameter array 'CLU' corresponding to 'PAI' = -1 is non-zero, the edge of the grid is also drawn. If the element of 'CLU' corresponding to 'PAI' = -2 is non-zero, the edges of special-value areas, if any, are drawn. If the element of 'CLU' corresponding to 'PAI' = -3 is non-zero, the edges of out-of-range areas, if any, are drawn. The default values are such that none of these edges are drawn. 

 Groups of lines are drawn in the following order:
<dl COMPACT><dt>&bull;
<dd>contour lines for each of the specified levels, in ascending numeric order,
<dt>&bull;
<dd>the edges of special-value areas, if any,
<dt>&bull;
<dd>the edges of out-of-range areas, if any, and
<dt>&bull;
<dd>the edge of the grid.</dl>
 

 The color, dash pattern, and line width to be used for the lines drawn may be specified by elements of the parameter arrays 'CLC', 'CLD', and 'CLL', respectively. Each of these contains elements corresponding to values of 'PAI' from 1 to 'NCL' and three special elements, corresponding to 'PAI' = -1, -2, and -3. Before and after each group of lines is drawn, the routine CPCHCL is called. You can supply your own version of CPCHCL to override the settings of color, dash pattern, and line width. 

 The dash-pattern-usage parameter ('DPU') affects the pattern used to draw the lines. Set the value of 'DPU' as follows:
<dl COMPACT><dt>Value
<dd>Description
<dt>&lt; 0 or = 0
<dd>Lines are drawn by calling the SPPS routine CURVE. Lines are all solid and unlabeled; specified dash patterns are not used.
<dt>&gt; 0
<dd>Lines are drawn by calling the Dashline routine CURVED. Lines are solid or dashed, depending on the dash pattern specified by the appropriate element of 'CLD'. 

 If ABS('LLP') = 1, then the dash pattern for those lines that are to be labeled is constructed by replicating, 'DPU' times, the dash pattern specified by the appropriate element of 'CLD', and then appending to it the characters specified by the appropriate element of 'LLT'. 

 If ABS('LLP') is greater than 1, then the lines drawn will pass through any labels drawn by CPLBDR. If this is undesirable, you can call CPLBAM to put the label boxes into an area map and then call CPCLDM instead of CPCLDR to draw only those portions of the contour lines which do not lie inside the label boxes.</dl>
 

 If, during the last call to CPRECT or CPSPRS, the data being contoured were found to be essentially constant, then no contour lines are drawn; instead, the constant-field label is written. Other lines are still drawn.
<h2>Examples</h2>Use the ncargex command to see the following relevant examples: caredg, ccpcff, ccpcfx, ccpcica, ccpcir, ccpcis, ccpcit, ccpclc, ccpcld, ccpcldr, ccpcll, ccpclu, ccpdflt, ccpfil, ccpga, ccphand, ccphcf, ccphl, ccphlt, ccpila, ccpilt, ccpklb, ccplbdr, ccpline, ccpllp, ccpmap, ccpmovi, ccpmpxy, ccpncls, ccpnet, ccpnof, ccpnsd, ccppkcl, ccprect, ccprwc, ccprwu, ccpset, ccpsps1, ccpsps2, ccpspv, ccpt2d, ccptitle, ccpvp, ccpvs, cidsfft, cpex01, cpex05, cpex07, tconpa, fsfsgfa.
<h2>Access</h2>To use CPCLDR or c_cpcldr, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.
<h2>Messages</h2>See the conpack man page for a description of all Conpack error messages and/or informational messages.
<h2>See Also</h2>Online: conpack, cpback, cpchcf, cpchcl, cpchhl, cpchil, cpchll, cpcica, cpclam, cpcldm, cpcltr, cpcnrc, cpdrpl, cpezct, cpgetc, cpgeti, cpgetr, cplbam, cplbdr, cpmpxy, cpmviw, cpmvrw, cppkcl, cppklb, cprect, cprset, cpscae, cpsetc, cpseti, cpsetr, cpsps1, cpsps2, ncarg_cbind 

 Hardcopy: NCAR Graphics Contouring and Mapping Tutorial
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 

 The use of this Software is governed by a License Agreement.
