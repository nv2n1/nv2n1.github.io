---
title: "ncl_strset(3)"
name: "ncl_strset"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_strset/"
---

STRSET - Resets all parameters to their initial default values.

<h2>Synopsis</h2>

CALL STRSET

<h2>C-Binding Synopsis</h2>

#include &lt;ncarg/ncargC.h&gt; 

 void c_strset(void)

<h2>Description</h2>

None.

<h2>C-Binding Description</h2>

None.

<h2>Usage</h2>

This routine resets all Streamlines parameters to their default values. For a complete list of the parameters affected and their default values, see the vectors_params man page.

<h2>Access</h2>

To use STRSET or c_strset, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.

<h2>See Also</h2>

Online: stgetc, stgeti, stgetr, stinit, stream, streamlines, streamlines_params, stsetc, stseti, stsetr, stuixy, stumsl, stumta, stumxy, ncarg_cbind. 

 Hardcopy: NCAR Graphics Fundamentals, UNIX Version

<h2>Copyright</h2>

Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
