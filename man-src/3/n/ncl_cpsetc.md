---
title: "ncl_cpsetc(3)"
name: "ncl_cpsetc"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_cpsetc/"
---

CPSETC - Sets the value of an internal parameter of type CHARACTER. 

<h2>Synopsis</h2>CALL CPSETC (PNAM, CVAL)
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/ncargC.h&gt; 

 void c_cpsetc (char *pnam, char *cval)
<h2>Description</h2><dl COMPACT><dt>PNAM
<dd>(CHARACTER, input) is the name of a parameter to be given a character value. Only the first three characters of PNAM are examined. It is recommended that the rest of the character string be used to improve the readability of the code. For example, instead of 'ILT', use 'ILT - INFORMATIONAL LABEL TEXT'.
<dt>CVAL
<dd>(CHARACTER, input) is a character constant or variable, the value of which is to be given to the parameter specified by PNAM.</dl><h2>C-Binding Description</h2>The C-binding argument descriptions are the same as the FORTRAN argument descriptions.
<h2>Usage</h2>This routine allows you to set the current value of Conpack parameters. For a complete list of parameters available in this utility, see the conpack_params man page.
<h2>Examples</h2>Use the ncargex command to see the following relevant examples: ccpcica, ccphlt, ccpilt, ccpklb, ccplbdr, ccpllc, ccpllp, ccpllt, ccpmovi, cpex02, cpex04, cpex05, cpex06, cbex01, fcover, ffex03, ffex05.
<h2>Access</h2>To use CPSETC or c_cpsetc, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.
<h2>Messages</h2>See the conpack man page for a description of all Conpack error messages and/or informational messages.
<h2>See Also</h2>Online: conpack, conpack_params, cpback, cpchcf, cpchcl, cpchhl, cpchil, cpchll, cpcica, cpclam, cpcldm, cpcldr, cpcltr, cpcnrc, cpdrpl, cpezct, cpgetc, cpgeti, cpgetr, cplbam, cplbdr, cpmpxy, cpmviw, cpmvrw, cppkcl, cppklb, cprect, cprset, cpscae, cpseti, cpsetr, cpsps1, cpsps2, ncarg_cbind 

 Hardcopy: NCAR Graphics Contouring and Mapping Tutorial
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 

 The use of this Software is governed by a License Agreement.
