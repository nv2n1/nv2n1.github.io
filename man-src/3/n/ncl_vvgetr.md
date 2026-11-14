---
title: "ncl_vvgetr(3)"
name: "ncl_vvgetr"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_vvgetr/"
---

VVGETR - Gets the current value of a Vectors parameter of type REAL.

<h2>Synopsis</h2>

CALL VVGETR (CNM,RVL)

<h2>C-Binding Synopsis</h2>

#include &lt;ncarg/ncargC.h&gt; 

 void c_vvgetr(char *cnm, float *rvl)

<h2>Description</h2>

<dl><dt>CNM
<dd>(CHARACTER, input) is the name of a parameter whose real value is to be retrieved. Only the first three characters of CNM are examined. The three characters may either be entirely upper or entirely lower case; mixed case is not recognized. It is recommended that the rest of the character string be used to improve the readability of the code. For example, instead of just 'DMX', use 'DMX - Device Maximum Vector Size'.
<dt>RVL
<dd>(REAL, output) is a variable in which the value of the parameter specified by CNM is to be returned.</dl>

<h2>C-Binding Description</h2>

The C-binding argument descriptions are the same as the FORTRAN argument descriptions.

<h2>Usage</h2>

This routine allows you to retrieve the current value of Vectors parameters of type REAL. For a complete list of parameters available in this utility, see the vectors_params man page.

<h2>Examples</h2>

Use the ncargex command to see the following relevant examples: ffex02, ffex05, vvex01, vvex02.

<h2>Access</h2>

To use VVGETR or c_vvgetr, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.

<h2>Messages</h2>

See the vectors man page for a description of all Vectors error messages and/or informational messages.

<h2>See Also</h2>

Online: vectors, vectors_params, vvectr, vvgetc, vvgeti, vvinit, vvrset, vvsetc, vvseti, vvsetr, vvudmv, vvumxy, ncarg_cbind. 

 Hardcopy: NCAR Graphics Fundamentals, UNIX Version

<h2>Copyright</h2>

Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
