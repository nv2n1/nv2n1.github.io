---
title: "ncl_cplbam(3)"
name: "ncl_cplbam"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_cplbam/"
---

CPLBAM - Adds label boxes (for the informational label, high and low labels, and contour-line labels) to an area map. The ultimate object of this will usually be to prevent contour lines drawn by CPCLDM from passing through labels or to prevent fill of the label boxes as contour bands are filled. 

<h2>Synopsis</h2>CALL CPLBAM (ZDAT, RWRK, IWRK, IAMA)
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/ncargC.h&gt; 

 void c_cplbam (float *zdat, float *rwrk, int *iwrk, 
 int *iama)
<h2>Description</h2>The first three arguments are arrays used in the last call to CPRECT, CPSPS1, or CPSPS2, the contents of which must not have been changed since that call.
<dl COMPACT><dt>ZDAT
<dd>(REAL array, dimensioned as specified in the last call to CPRECT, CPSPS1, or CPSPS2, input) is the data array.
<dt>RWRK
<dd>(REAL array, dimensioned as specified in the last call to CPRECT, CPSPS1, or CPSPS2, input/output) is the real workspace array.
<dt>IWRK
<dd>(INTEGER array, dimensioned as specified in the last call to CPRECT, CPSPS1, or CPSPS2, input/output) is the integer workspace array.
<dt>IAMA
<dd>(INTEGER array, dimensioned as specified in a call to ARINAM) is the array holding the area map to which the label boxes are to be added.</dl><h2>C-Binding Description</h2>The C-binding argument descriptions are the same as the FORTRAN argument descriptions.
<h2>Usage</h2>The routine CPLBAM, which adds label boxes to an area map, may be called at any time after the initialization call to CPRECT, CPSPS1, or CPSPS2. If, during the last call to CPRECT, CPSPS1, or CPSPS2, the data being contoured were found to be essentially constant, then the box for the constant field label is added to the area map. Otherwise, boxes for the informational label, the high and low labels, and/or the contour line labels are added, as follows:
<dl COMPACT><dt>&bull;
<dd>A box for the informational label is added only if the parameter 'ILT', which specifies the text of that label, is non-blank.
<dt>&bull;
<dd>Boxes for the high labels are added only if the parameter 'HIT', which specifies the text of those labels, is non-blank.
<dt>&bull;
<dd>Boxes for the low labels are added only if the parameter 'LOT', which specifies the text of those labels, is non-blank.
<dt>&bull;
<dd>Boxes for the contour line labels are added only if the parameter 'LLP', which specifies how those labels are to be positioned, has an absolute value of 2 or 3, and if, for some I between 1 and 'NCL', inclusive, the Ith element of the parameter array 'CLU' has a value implying that contour lines at the contour level specified by the Ith element of 'CLV' are to be labeled.</dl><h2>Examples</h2>Use the ncargex command to see the following relevant examples: ccpcldm, ccplbam, ccpllb, ccpllc, ccplll, ccpllo, ccpllp, ccpllt, ccpllw, ccppc, ccppc1, ccppc2, ccppc3, ccppc4, ccprc, ccpscam, colcon, cpex01, cpex02, cpex03, cpex04, cpex06, cbex01, vvex01, fcover, ffex03, ffex05.
<h2>Access</h2>To use CPLBAM or c_cplbam, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.
<h2>Messages</h2>See the conpack man page for a description of all Conpack error messages and/or informational messages.
<h2>See Also</h2>Online: conpack, cpback, cpchcf, cpchcl, cpchhl, cpchil, cpchll, cpcica, cpclam, cpcldm, cpcldr, cpcltr, cpcnrc, cpdrpl, cpezct, cpgetc, cpgeti, cpgetr, cplbdr, cpmpxy, cpmviw, cpmvrw, cppkcl, cppklb, cprect, cprset, cpscae, cpsetc, cpseti, cpsetr, cpsps1, cpsps2, ncarg_cbind 

 Hardcopy: NCAR Graphics Contouring and Mapping Tutorial
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 

 The use of this Software is governed by a License Agreement.
