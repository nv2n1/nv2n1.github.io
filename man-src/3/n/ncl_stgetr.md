---
title: "ncl_stgetr(3)"
name: "ncl_stgetr"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_stgetr/"
---

STGETR - Gets the current value of an internal parameter of type REAL.

<h2>Synopsis</h2>

CALL STGETR (CNM,RVL)

<h2>C-Binding Synopsis</h2>

#include &lt;ncarg/ncargC.h&gt; 

 void c_stgetr(char *cnm, float *rvl)

<h2>Description</h2>

<dl><dt>CNM
<dd>(CHARACTER, input) is the name of a parameter whose real value is to be retrieved. Only the first three characters of CNM are examined. The three characters must either be entirely upper or entirely lower case; mixed case is not recognized. It is recommended that the rest of the character string be used to improve the readability of the code. For example, instead of just 'ARL', use 'ARL - Arrowhead Length'.
<dt>RVL
<dd>(REAL, output) is a variable in which the value of the parameter specified by CNM is to be returned.</dl>

<h2>C-Binding Description</h2>

The C-binding argument descriptions are the same as the FORTRAN argument descriptions.

<h2>Usage</h2>

This routine allows you to retrieve the current value of Streamlines parameters of type REAL. For a complete list of parameters available in this utility, see the streamlines_params man page.

<h2>Access</h2>

To use STGETR or c_stgetr, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.

<h2>Messages</h2>

See the streamlines man page for a description of all Streamlines error messages and/or informational messages.

<h2>See Also</h2>

Online: stgetc, stgeti, stinit, stream, streamlines, streamlines_params, strset, stsetc, stseti, stsetr, stuixy, stumsl, stumta, stumxy, ncarg_cbind. 

 Hardcopy: NCAR Graphics Fundamentals, UNIX Version

<h2>Copyright</h2>

Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
