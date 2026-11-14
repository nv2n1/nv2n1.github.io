---
title: "ncl_vvsetr(3)"
name: "ncl_vvsetr"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_vvsetr/"
---

VVSETR - Sets the value of a Vectors parameter of type REAL.

<h2>Synopsis</h2>

CALL VVSETR (CNM,RVL)

<h2>C-Binding Synopsis</h2>

#include &lt;ncarg/ncargC.h&gt; 

 void c_vvsetr(char *cnm, float rvl)

<h2>Description</h2>

<dl><dt>CNM
<dd>(CHARACTER, input) is the name of a parameter to be given a real value. Only the first three characters of CNM are examined. The three characters may either be entirely upper or entirely lower case; mixed case is not recognized. It is recommended that the rest of the character string be used to improve the readability of the code. For example, instead of 'VFR', use 'VFR - Minimum Vector Fractional Length'.
<dt>RVL
<dd>(REAL, input) is an expression, the value of which is to be given to the parameter specified by CNM.</dl>

<h2>C-Binding Description</h2>

The C-binding argument descriptions are the same as the FORTRAN argument descriptions.

<h2>Usage</h2>

This routine allows you to set the current value of Vectors parameters of type REAL. For a complete list of parameters available in this utility, see the vectors_params man page.

<h2>Examples</h2>

Use the ncargex command to see the following relevant examples: bnchmk, fcover, ffex00, ffex02, ffex05, stex02, stex03, vvex01, vvex02.

<h2>Access</h2>

To use VVSETR or c_vvsetr, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.

<h2>Messages</h2>

See the vectors man page for a description of all Vectors error messages and/or informational messages.

<h2>See Also</h2>

Online: vectors, vectors_params, vvectr, vvgetc, vvgeti, vvgetr, vvinit, vvrset, vvsetc, vvseti, vvudmv, vvumxy, ncarg_cbind. 

 Hardcopy: NCAR Graphics Fundamentals, UNIX Version

<h2>Copyright</h2>

Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
