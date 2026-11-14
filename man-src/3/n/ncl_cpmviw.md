---
title: "ncl_cpmviw(3)"
name: "ncl_cpmviw"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_cpmviw/"
---

CPMVIW - Moves the contents of an old integer workspace to a new one. 

<h2>Synopsis</h2>CALL CPMVIW (IWKO, IWKN, LWKN)
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/ncargC.h&gt; 

 void c_cpback (int *iwko, int *iwkn, int *lwkn)
<h2>Description</h2>The arguments define the old and new integer workspaces.
<dl COMPACT><dt>IWKO
<dd>(an input array of type INTEGER, dimensioned as specified in the last call to CPRECT, CPSPS1, CPSPS2, or CPMVIW) is the old integer workspace array.
<dt>IWKN
<dd>(an output array of type INTEGER, dimensioned LWKN) is the new integer workspace array.
<dt>LWKN
<dd>(an input expression of type INTEGER) specifies the length of IWKN.</dl><h2>C-Binding Description</h2>The C-binding argument descriptions are the same as the FORTRAN argument descriptions.
<h2>Usage</h2>When, in the execution of a CONPACK routine, the amount of space left in the integer workspace array is found to be insufficient, if the internal parameter 'WSO' has the value 3, the error-handling routine SETER is called with an appropriate error message. If, in addition, the user has turned recovery mode on, execution continues and, eventually, control is returned to the user. At that point, the user should detect the fact that an error has occurred. If he/she chooses to try to recover from the error, CPMVIW may be of use: it may be called to move everything from the current integer workspace to a new (and presumably bigger) one, after which it may be possible to resume execution.
<h2>Examples</h2>None, at present.
<h2>Access</h2>To use CPMVIW or c_cpmviw, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.
<h2>Messages</h2>See the conpack man page for a description of all Conpack error messages and/or informational messages.
<h2>See Also</h2>Online: conpack, cpback, cpchcf, cpchcl, cpchhl, cpchil, cpchll, cpcica, cpclam, cpcldm, cpcldr, cpcltr, cpcnrc, cpdrpl, cpezct, cpgetc, cpgeti, cpgetr, cplbam, cplbdr, cpmpxy, cpmvrw, cppkcl, cppklb, cprect, cprset, cpscae, cpsetc, cpseti, cpsetr, cpsps1, cpsps2, ncarg_cbind 

 Hardcopy: NCAR Graphics Contouring and Mapping Tutorial
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 

 The use of this Software is governed by a License Agreement.
