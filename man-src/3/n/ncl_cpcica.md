---
title: "ncl_cpcica(3)"
name: "ncl_cpcica"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_cpcica/"
---

CPCICA - Incorporates into a user's cell array color indices determined by examining where the user's contours lie relative to the cell array. 

<h2>Synopsis</h2>&nbsp;<wbr>CALL CPCICA&nbsp;<wbr>(ZDAT, RWRK, IWRK, ICRA, ICA1, ICAM, ICAN,&nbsp;<wbr> 
 + XCPF, YCPF, XCQF, YCQF)
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/ncargC.h&gt; 

 void c_cpcica (float *zdat, float *rwrk, int *iwrk, 
 int *icra, int ica1, int icam, int ican, float xcpf, 
 float ycpf, float xcqf, float ycqf)
<h2>Description</h2>The first three arguments are arrays used in the last call to CPRECT, CPSPS1, or CPSPS2, the contents of which must not have been changed since that call.
<dl COMPACT><dt>ZDAT
<dd>(REAL array, dimensioned as specified in the last call to CPRECT, CPSPS1, or CPSPS2, input) is the data array.
<dt>RWRK
<dd>(REAL array, dimensioned as specified in the last call to CPRECT, CPSPS1, or CPSPS2, input/output) is the real workspace array.
<dt>IWRK
<dd>(INTEGER array, dimensioned as specified in the last call to CPRECT, CPSPS1, or CPSPS2, input/output) is the integer workspace array.
<dt>ICRA
<dd>(INTEGER array, dimensioned ICA1 by &quot;n&quot;, where &quot;n&quot; is greater than or equal to the value of the argument ICAN, input/output) is the user's cell array.
<dt>ICA1
<dd>(INTEGER, input) is the first dimension of the FORTRAN array ICRA, which contains the user's cell array.
<dt>ICAM
<dd>(INTEGER, input) is the first dimension of the user's cell array.
<dt>ICAN
<dd>(INTEGER, input) is the second dimension of the user's cell array.
<dt>XCPF and YCPF
<dd>(REAL, input) are the coordinates, in the fractional coordinate system, of a point P. P is the point at that corner of the rectangular area into which the cell array maps that corresponds to the cell (1,1).
<dt>XCQF and YCQF
<dd>(REAL, input) are the coordinates, in the fractional coordinate system, of a point Q. Q is the point at that corner of the rectangular area into which the cell array maps that corresponds to the cell (ICAM,ICAN).</dl><h2>C-Binding Description</h2>The C-binding argument descriptions are the same as the FORTRAN argument descriptions, with the following exceptions:
<dl COMPACT><dt>icra
<dd>icra is dimensioned n by ica1 where n is greater than or equal to the value of the argument ican
<dt>ica1
<dd>The second dimension of the array icra.</dl><h2>Examples</h2>Use the ncargex command to see the following relevant examples: ccpcica, ccpmovi.
<h2>Access</h2>To use CPCICA or c_cpcica, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.
<h2>Messages</h2>See the conpack man page for a description of all Conpack error messages and/or informational messages.
<h2>See Also</h2>Online: conpack, cpback, cpchcf, cpchcl, cpchhl, cpchil, cpchll, cpclam, cpcldm, cpcldr, cpcltr, cpcnrc, cpdrpl, cpezct, cpgetc, cpgeti, cpgetr, cplbam, cplbdr, cpmpxy, cpmviw, cpmvrw, cppkcl, cppklb, cprect, cprset, cpscae, cpsetc, cpseti, cpsetr, cpsps1, cpsps2, ncarg_cbind 

 Hardcopy: NCAR Graphics Contouring and Mapping Tutorial
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
