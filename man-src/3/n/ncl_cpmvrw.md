---
title: "ncl_cpmvrw(3)"
name: "ncl_cpmvrw"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_cpmvrw/"
---

CPMVRW - Moves the contents of an old real workspace to a new one. 

<h2>Synopsis</h2>CALL CPMVRW (RWKO, RWKN, LWKN)
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/ncargC.h&gt; 

 void c_cpback (float *iwko, float *iwkn, int *lwkn)
<h2>Description</h2>The arguments define the old and new real workspaces.
<dl COMPACT><dt>IWKO
<dd>(an input array of type REAL, dimensioned as specified in the last call to CPRECT, CPSPS1, CPSPS2, or CPMVIW) is the old real workspace array.
<dt>IWKN
<dd>(an output array of type REAL, dimensioned LWKN) is the new real workspace array.
<dt>LWKN
<dd>(an input expression of type INTEGER) specifies the length of RWKN.</dl><h2>C-Binding Description</h2>The C-binding argument descriptions are the same as the FORTRAN argument descriptions.
<h2>Usage</h2>When, in the execution of a CONPACK routine, the amount of space left in the real workspace array is found to be insufficient, if the internal parameter 'WSO' has the value 3, the error-handling routine SETER is called with an appropriate error message. If, in addition, the user has turned recovery mode on, execution continues and, eventually, control is returned to the user. At that point, the user should detect the fact that an error has occurred. If he/she chooses to try to recover from the error, CPMVRW may be of use: it may be called to move everything from the current real workspace to a new (and presumably bigger) one, after which it may be possible to resume execution.
<h2>Examples</h2>None, at present.
<h2>Access</h2>To use CPMVRW or c_cpmvrw, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.
<h2>Messages</h2>See the conpack man page for a description of all Conpack error messages and/or informational messages.
<h2>See Also</h2>Online: conpack, cpback, cpchcf, cpchcl, cpchhl, cpchil, cpchll, cpcica, cpclam, cpcldm, cpcldr, cpcltr, cpcnrc, cpdrpl, cpezct, cpgetc, cpgeti, cpgetr, cplbam, cplbdr, cpmpxy, cpmviw, cppkcl, cppklb, cprect, cprset, cpscae, cpsetc, cpseti, cpsetr, cpsps1, cpsps2, ncarg_cbind 

 Hardcopy: NCAR Graphics Contouring and Mapping Tutorial
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 

 The use of this Software is governed by a License Agreement.
