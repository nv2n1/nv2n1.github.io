---
title: "ncl_cpsetr(3)"
name: "ncl_cpsetr"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_cpsetr/"
---

CPSETR - Sets the value of an internal parameter of type REAL or INTEGER. 

<h2>Synopsis</h2>CALL CPSETR (PNAM, RVAL)
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/ncargC.h&gt; 

 void c_cpsetr (char *pnam, float rval)
<h2>Description</h2><dl COMPACT><dt>PNAM
<dd>(CHARACTER, input) is the name of a parameter to be given a real value. Only the first three characters of PNAM are examined. It is recommended that the rest of the character string be used to improve the readability of the code. For example, instead of 'CIS', use 'CIS - CONTOUR INTERVAL SPECIFIER'.
<dt>RVAL
<dd>(REAL, input) is an expression, the value of which is to be given to the parameter specified by PNAM. If the internal parameter is of type REAL, the value given to it is RVAL. If the internal parameter is of type INTEGER, the value given to it is INT(RVAL).</dl><h2>C-Binding Description</h2>The C-binding argument descriptions are the same as the FORTRAN argument descriptions.
<h2>Usage</h2>This routine allows you to set the current value of Conpack parameters. For a complete list of parameters available in this utility, see the conpack_params man page.
<h2>Examples</h2>Use the ncargex command to see the following relevant examples: caredg, ccpcfx, ccpcica, ccpcir, ccpcis, ccpcit, ccpcll, ccpclu, ccpga, ccphand, ccphcf, ccphl, ccphlt, ccpila, ccpils, ccpilt, ccplbam, ccpline, ccpllc, ccplll, ccpllp, ccpllt, ccpllw, ccpmap, ccpmovi, ccpmpxy, ccpnsd, ccppc1, ccppc2, ccppc3, ccppc4, ccppkcl, ccppole, ccprc, ccpscam, ccpset, ccpsps2, ccpspv, ccpt2d, ccpvp, colcon, cpex01, cpex02, cpex03, cpex04, cpex05, cpex06, cpex07, cpex08, cpex09, cbex01, vvex01, tconpa, fcover, ffex03, ffex05, fsfsgfa.
<h2>Access</h2>To use CPSETR or c_cpsetr, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.
<h2>Messages</h2>See the conpack man page for a description of all Conpack error messages and/or informational messages.
<h2>See Also</h2>Online: conpack, conpack_params, cpback, cpchcf, cpchcl, cpchhl, cpchil, cpchll, cpcica, cpclam, cpcldm, cpcldr, cpcltr, cpcnrc, cpdrpl, cpezct, cpgetc, cpgeti, cpgetr, cplbam, cplbdr, cpmpxy, cpmviw, cpmvrw, cppkcl, cppklb, cprect, cprset, cpscae, cpsetc, cpseti, cpsprs, cpsps2, ncarg_cbind 

 Hardcopy: NCAR Graphics Contouring and Mapping Tutorial
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 

 The use of this Software is governed by a License Agreement.
