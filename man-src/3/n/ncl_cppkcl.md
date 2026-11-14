---
title: "ncl_cppkcl(3)"
name: "ncl_cppkcl"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_cppkcl/"
---

CPPKCL - Picks a set of contour levels. 

<h2>Synopsis</h2>CALL CPPKCL (ZDAT, RWRK, IWRK)
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/ncargC.h&gt; 

 void c_cppkcl (float *zdat, float *rwrk, int *iwrk)
<h2>Description</h2>All three arguments are arrays used in the last call to CPRECT, CPSPS1, or CPSPS2, the contents of which must not have been changed since that call.
<dl COMPACT><dt>ZDAT
<dd>(REAL array, dimensioned as specified in the last call to CPRECT, CPSPS1, or CPSPS2, input) is the data array.
<dt>RWRK
<dd>(REAL array, dimensioned as specified in the last call to CPRECT, CPSPS1, or CPSPS2, input/output) is the real workspace array.
<dt>IWRK
<dd>(INTEGER array, dimensioned as specified in the last call to CPRECT, CPSPS1, or CPSPS2, input/output) is the integer workspace array.</dl><h2>C-Binding Description</h2>The C-binding argument descriptions are the same as the FORTRAN argument descriptions.
<h2>Usage</h2>Normally, CPPKCL is called by CONPACK when the contour levels are needed; it may be called directly by the user when it is desired to modify the resulting parameter arrays specifying contour levels and associated quantities in some way. CPPKCL must be called after initialization has been done (by a call to one of the initialization routines CPRECT, CPSPS1, or CPSPS2); this is because CPPKCL depends on values set during initialization. 

 If the contour-level-selection parameter 'CLS' is zero (indicating that the user intends to pick contour levels), or if the constant-field-flag 'CFF' is non-zero (indicating that, during initialization, the data were found to be essentially constant), CPPKCL does nothing. Otherwise, CPPKCL picks a set of contour levels. The way in which it picks these levels is determined by the value of the internal parameter 'CLS'; see the description of this parameter in the conpack_params man page. 

 When CPPKCL picks contour levels, it sets the value of the internal parameter 'NCL' equal to the number of contour levels picked. It then sets the values of elements 1 through 'NCL' of the parameter array 'CLV' (contour level values) to the levels chosen. The Ith elements of the associated parameter arrays are set as follows: <table> <tr VALIGN=top><td>CLU = 1 or 3</td><td>Contour level use flag 
</td></tr><tr VALIGN=top><td>AIA = I+1</td><td>Area identifier above the level
</td></tr><tr VALIGN=top><td>AIB = I</td><td>Area identifier below the level
</td></tr><tr VALIGN=top><td>LLT = ' ' (single blank)</td><td>Contour line label text
</td></tr><tr VALIGN=top><td>CLD = '$$$$$$$$$$$$$'</td><td>Contour line dash pattern
</td></tr><tr VALIGN=top><td>CLC = -1</td><td>Contour line color
</td></tr><tr VALIGN=top><td>LLC = -1</td><td>Contour line label color
</td></tr><tr VALIGN=top><td>CLL = 0.</td><td>Contour line line width
</td></tr> </table> 

 Thus, after CPPKCL is called, the situation for each contour level is as follows:
<dl COMPACT><dt>&bull;
<dd>Contour lines at the level are to be drawn by calls to CPCLDM or CPCLDR.
<dt>&bull;
<dd>The lines will be labeled if 'CLU'=3, but not if 'CLU'=1.
<dt>&bull;
<dd>If CPCLAM is called, lines at the level will be added to the area map; the area identifiers for areas &quot;above&quot; the level and for areas &quot;below&quot; the level are as specified by 'AIA' and 'AIB'.
<dt>&bull;
<dd>The dash pattern for the level is solid, and neither the color of the line, the color of the labels on it, nor its width are to be set.
<dt>&bull;
<dd>The text of the label associated with the level is, as yet, unspecified.</dl>
 

 By resetting elements in these parameter arrays, the user can change the situation in various ways.
<h2>Examples</h2>Use the ncargex command to see the following relevant examples: ccpclc, ccpcld, ccpcldm, ccpcll, ccpklb, ccplbam, ccplbdr, ccpllb, ccpllc, ccplll, ccpllo, ccpllp, ccpllt, ccpllw, ccppc, ccppc1, ccppc2, ccppc3, ccppc4, ccppkcl, ccprc, ccprwc, ccpscam, cpex01, cpex02, cpex03, cpex06, vvex01, fcover, ffex03, ffex05.
<h2>Access</h2>To use CPPKCL or c_cppkcl, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.
<h2>Messages</h2>See the conpack man page for a description of all Conpack error messages and/or informational messages.
<h2>See Also</h2>Online: conpack, cpback, cpchcf, cpchcl, cpchhl, cpchil, cpchll, cpcica, cpclam, cpcldm, cpcldr, cpcltr, cpcnrc, cpdrpl, cpezct, cpgetc, cpgeti, cpgetr, cplbam, cplbdr, cpmpxy, cpmviw, cpmvrw, cppklb, cprect, cprset, cpscae, cpsetc, cpseti, cpsetr, cpsps1, cpsps2, ncarg_cbind 

 Hardcopy: NCAR Graphics Contouring and Mapping Tutorial
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 

 The use of this Software is governed by a License Agreement.
