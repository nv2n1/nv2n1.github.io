---
title: "ncl_stseti(3)"
name: "ncl_stseti"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_stseti/"
---

STSETI - Sets the value of an internal parameter of type INTEGER.

<h2>Synopsis</h2>

CALL STSETI (CNM,IVL)

<h2>C-Binding Synopsis</h2>

#include &lt;ncarg/ncargC.h&gt; 

 void c_stseti(char *cnm, int ivl)

<h2>Description</h2>

<dl><dt>CNM
<dd>(CHARACTER, input) is the name of a parameter to be given an integer value. Only the first three characters of CNM are examined. The three characters must either be entirely upper or entirely lower case; mixed case is not recognized. It is recommended that the rest of the character string be used to improve the readability of the code. For example, instead of 'CKP', use 'CKP - Check Progress Iteration Count'.
<dt>IVL
<dd>(INTEGER, input) is an expression, the value of which is to be given to the parameter specified by CNM.</dl>

<h2>C-Binding Description</h2>

The C-binding argument descriptions are the same as the FORTRAN argument descriptions.

<h2>Usage</h2>

This routine allows you to set the current value of Streamlines parameters of type INTEGER. For a complete list of parameters available in this utility, see the streamlines_params man page.

<h2>Examples</h2>

Use the ncargex command to see the following relevant examples: ffex00, ffex03, ffex04, stex01, stex02, stex03.

<h2>Access</h2>

To use STSETI or c_stseti, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.

<h2>Messages</h2>

See the streamlines man page for a description of all Streamlines error messages and/or informational messages.

<h2>See Also</h2>

Online: stgetc, stgeti, stgetr, stinit, stream, streamlines, streamlines_params, strset, stsetc, stsetr, stuixy, stumsl, stumta, stumxy, ncarg_cbind. 

 Hardcopy: NCAR Graphics Fundamentals, UNIX Version

<h2>Copyright</h2>

Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
