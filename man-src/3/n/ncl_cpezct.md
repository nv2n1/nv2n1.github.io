---
title: "ncl_cpezct(3)"
name: "ncl_cpezct"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_cpezct/"
---

CPEZCT - Draws black and white contours with a single call. Simulates the behavior of the old subroutine EZCNTR in Conrec_family; it has the same arguments and will produce similar output. 

<h2>Synopsis</h2>CALL CPEZCT (ZDAT,MZDT,NZDT)
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/ncargC.h&gt; 

 void c_cpezct (float *zdat, int mzdt, int nzdt)
<h2>Description</h2><dl COMPACT><dt>ZDAT
<dd>(REAL array, dimensioned MZDT x NZDT, input) is the array containing the data to be contoured.
<dt>MZDT
<dd>(INTEGER, input) is the first dimension of the FORTRAN array ZDAT and of the array of data stored in it.
<dt>NZDT
<dd>(INTEGER, input) is the second dimension of the FORTRAN array ZDAT and of the array of data stored in it.</dl><h2>C-Binding Description</h2>The C-binding argument descriptions are the same as the FORTRAN argument descriptions with the following exceptions:
<dl COMPACT><dt>z(nzdt,mzdt)
<dd>An n by m data array holding values to be contoured.
<dt>mzdt
<dd>The second dimension of z.
<dt>nzdt
<dd>The first dimension of z.</dl><h2>Usage</h2>The effect of calling CPEZCT will be exactly the same as if you had executed the statements: 

 CALL CPCNRC (ZDAT,MZDT,MZDT,NZDT,0.,0.,0.,0,0,-682) 
 CALL FRAME 

 See the man page for CPCNRC.
<h2>Examples</h2>Use the ncargex command to see the following relevant examples: ccpezct, cpex09, tconpa.
<h2>Access</h2>To use CPEZCT or c_cpezct, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.
<h2>See Also</h2>Online: conpack, cpback, cpchcf, cpchcl, cpchhl, cpchil, cpchll, cpcica, cpclam, cpcldm, cpcldr, cpcltr, cpcnrc, cpdrpl, cpgetc, cpgeti, cpgetr, cplbam, cplbdr, cpmpxy, cpmviw, cpmvrw, cppkcl, cppklb, cprect, cprset, cpscae, cpsetc, cpseti, cpsetr, cpsps1, cpsps2, ncarg_cbind 

 Hardcopy: NCAR Graphics Contouring and Mapping Tutorial
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 

 The use of this Software is governed by a License Agreement.
