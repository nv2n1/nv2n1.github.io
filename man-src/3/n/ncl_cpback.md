---
title: "ncl_cpback(3)"
name: "ncl_cpback"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_cpback/"
---

CPBACK - Draws a background for a contour plot. 

<h2>Synopsis</h2>CALL CPBACK (ZDAT, RWRK, IWRK)
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/ncargC.h&gt; 

 void c_cpback (float *zdat, float *rwrk, int *iwrk)
<h2>Description</h2>All three arguments are arrays used in the last call to CPRECT, CPSPS1, or CPSPS2, the contents of which must not have been changed since that call.
<dl COMPACT><dt>ZDAT
<dd>(REAL array, dimensioned as specified in the last call to CPRECT, CPSPS1, or CPSPS2, input) is the data array.
<dt>RWRK
<dd>(REAL array, dimensioned as specified in the last call to CPRECT, CPSPS1, or CPSPS2, input/output) is the real workspace array.
<dt>IWRK
<dd>(INTEGER array, dimensioned as specified in the last call to CPRECT, CPSPS1, or CPSPS2, input/output) is the integer workspace array.</dl><h2>C-Binding Description</h2>The C-binding argument descriptions are the same as the FORTRAN argument descriptions.
<h2>Usage</h2>You can call CPBACK at any time after the initialization call to CPRECT, CPSPS1, or CPSPS2. What CPBACK does depends on the value of the internal parameter 'MAP':
<dl COMPACT><dt>&bull;
<dd>If 'MAP' is set to zero, CPBACK draws the perimeter of the current viewport by calling PERIM, in the utility Gridall, requesting 'ZDM'-1 major ticks on the horizontal sides of the perimeter and 'ZDN'-1 major ticks on the vertical sides. No minor ticks are drawn.
<dt>&bull;
<dd>If 'MAP' is set non-zero, CPBACK does nothing.</dl><h2>Examples</h2>Use the ncargex command to see the following relevant examples: ccpback, ccpcff, ccpcfx, ccpcis, ccpcit, ccpclc, ccpcld, ccpcldm, ccpcll, ccpclu, ccpdflt, ccpfil, ccphand, ccphcf, ccphl, ccphlt, ccpila, ccpils, ccpilt, ccpklb, ccplbam, ccplbdr, ccpline, ccpllb, ccpllc, ccplll, ccpllo, ccpllp, ccpllt, ccpllw, ccpncls, ccpnet, ccpnof, ccpnsd, ccppc, ccppc1, ccppc2, ccppc3, ccppc4, ccppkcl, ccprc, ccprect, ccprwc, ccprwu, ccpscam, ccpset, ccpsps1, ccpsps2, ccpspv, ccptitle, ccpvp, cidsfft, cpex01, fsfsgfa.
<h2>Access</h2>To use CPBACK or c_cpback, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.
<h2>Messages</h2>See the conpack man page for a description of all Conpack error messages and/or informational messages.
<h2>See Also</h2>Online: conpack, cpchcf, cpchcl, cpchhl, cpchil, cpchll, cpcica, cpclam, cpcldm, cpcldr, cpcltr, cpcnrc, cpdrpl, cpezct, cpgetc, cpgeti, cpgetr, cplbam, cplbdr, cpmpxy, cpmviw, cpmvrw, cppkcl, cppklb, cprect, cprset, cpscae, cpsetc, cpseti, cpsetr, cpsps1, cpsps2, ncarg_cbind 

 Hardcopy: NCAR Graphics Contouring and Mapping Tutorial
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 

 The use of this Software is governed by a License Agreement.
