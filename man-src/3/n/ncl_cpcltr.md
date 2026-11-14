---
title: "ncl_cpcltr(3)"
name: "ncl_cpcltr"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_cpcltr/"
---

CPCLTR - Traces the contour lines at a given level and retrieves them for some sort of user-defined processing. 

<h2>Synopsis</h2>CALL CPCLTR (ZDAT,RWRK,IWRK,CLVL,IJMP,IRW1,IRW2,NRWK)
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/ncargC.h&gt; 

 void c_cpcltr (float *zdat, float *rwrk, int *iwrk, 
 float clvl, int *ijmp, int *irw1, int *irw2, int *nrwk)
<h2>Description</h2>The first three arguments are arrays used in the last call to CPRECT, CPSPS1, or CPSPS2, the contents of which must not have been changed since that call.
<dl COMPACT><dt>ZDAT
<dd>(REAL array, dimensioned as specified in the last call to CPRECT, CPSPS1, or CPSPS2, input) is the data array.
<dt>RWRK
<dd>(REAL array, dimensioned as specified in the last call to CPRECT, CPSPS1, or CPSPS2, input/output) is the real workspace array.
<dt>IWRK
<dd>(INTEGER array, dimensioned as specified in the last call to CPRECT, CPSPS1, or CPSPS2, input/output) is the integer workspace array.
<dt>CLEV
<dd>(REAL, input) is the desired contour level.
<dt>IJMP
<dd>(INTEGER, input/output) is initially set to zero by the user. Upon return from CPCLTR, it will be non-zero if coordinates of a contour line segment have been placed in RWRK; it will be zero if all contour line segments at the given level have been generated.
<dt>IRW1
<dd>(INTEGER, output) is a pointer to the place in RWRK where X coordinates have been stored. They will be in RWRK(IRW1+I) for I = 1, 2, ..., NRWK.
<dt>IRW2
<dd>(INTEGER, output) is a pointer to the place in RWRK where Y coordinates have been stored. They will be in RWRK(IRW2+I) for I = 1, 2, ..., NRWK.
<dt>NRWK
<dd>(INTEGER, output) is the number of points on the contour line segment. The points comprising the segment will be (RWRK(IRW1+I),RWRK(IRW2+I)) for I = 1, 2, ... NRWK.</dl><h2>C-Binding Description</h2>The C-binding argument descriptions are the same as the FORTRAN argument descriptions.
<h2>Usage</h2>The routine CPCLTR may be called at any time after the initialization call to CPRECT, CPSPS1, or CPSPS2. It is called using code like the following: 

 <pre> IJMP=0
<br>
 101 CALL CPCLTR (ZDAT,RWRK,IWRK,CLEV,IJMP,IRW1,IRW2,NRWK)
<br>
 IF (IJMP.NE.0) THEN
<br>
 (PROCESS SEGMENT OF CONTOUR LINE FROM RWRK)
<br>
 GO TO 101
<br>
 END IF</pre>CPCLTR is called repeatedly. Initially, IJMP is zeroed. Upon each return from CPCLTR, if the value of IJMP is non-zero, X and Y coordinates have been placed in the real workspace array RWRK and the values of IRW1, IRW2, and NRWK have been set to indicate where the coordinates were put. After the coordinates have been processed, CPCLTR is called again. If, upon return from CPCLTR, the value of IJMP is zero, all contour lines at the specified level have been processed. 

 If the parameter 'T2D' has a non-zero value, the contour lines are smoothed, using cubic splines under tension.
<h2>Access</h2>To use CPCLTR or c_cpcltr, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.
<h2>Messages</h2>See the conpack man page for a description of all Conpack error messages and/or informational messages.
<h2>See Also</h2>Online: conpack, cpback, cpchcf, cpchcl, cpchhl, cpchil, cpchll, cpcica, cpclam, cpcldm, cpcldr, cpcnrc, cpdrpl, cpezct, cpgetc, cpgeti, cpgetr, cplbam, cplbdr, cpmpxy, cpmviw, cpmvrw, cppkcl, cppklb, cprect, cprset, cpscae, cpsetc, cpseti, cpsetr, cpsps1, cpsps2, ncarg_cbind
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 

 The use of this Software is governed by a License Agreement.
