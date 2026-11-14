---
title: "ncl_stgetc(3)"
name: "ncl_stgetc"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_stgetc/"
---

STGETC - Gets the current value of a Streamlines parameter of type CHARACTER.

<h2>Synopsis</h2>

CALL STGETC (CNM,CVL)

<h2>C-Binding Synopsis</h2>

#include &lt;ncarg/ncargC.h&gt; 

 void c_stgetc(char *cnm, char *cvl, int len)

<h2>Description</h2>

<dl><dt>CNM
<dd>(CHARACTER, input) is the name of a parameter whose character value is to be retrieved. Only the first three characters of CNM are examined. The three characters may either be entirely upper or entirely lower case; mixed case is not recognized. It is recommended that the rest of the character string be used to improve the readability of the code. For example, instead of just 'ZFT', use 'ZFT - Zero Field Text String'.
<dt>CVL
<dd>(CHARACTER, output) is a variable in which the value of the parameter specified by CNM is to be returned.</dl>

<h2>C-Binding Description</h2>

The C-binding argument descriptions are the same as the FORTRAN argument descriptions with the following exception: 

<dl><dt>len
<dd>The size of cvl as dimensioned in the calling program.</dl>

<h2>Usage</h2>

This routine allows you to retrieve the current value of Streamlines parameters of type CHARACTER. For a complete list of parameters available in this utility, see the streamlines_params man page.

<h2>Access</h2>

To use STGETC or c_stgetc, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.

<h2>Messages</h2>

See the streamlines man page for a description of all Streamlines error messages and/or informational messages.

<h2>See Also</h2>

Online: stgeti, stgetr, stinit, stream, streamlines, streamlines_params, strset, stsetc, stseti, stsetr, stuixy, stumsl, stumta, stumxy, ncarg_cbind. 

 Hardcopy: NCAR Graphics Fundamentals, UNIX Version

<h2>Copyright</h2>

Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
