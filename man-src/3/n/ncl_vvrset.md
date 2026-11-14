---
title: "ncl_vvrset(3)"
name: "ncl_vvrset"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_vvrset/"
---

VVRSET - Resets all parameters to their initial default values.

<h2>Synopsis</h2>

CALL VVRSET

<h2>C-Binding Synopsis</h2>

#include &lt;ncarg/ncargC.h&gt; 

 void c_vvrset( void )

<h2>Description</h2>

None.

<h2>Usage</h2>

This routine resets all Vectors parameters to their default values. For a complete list of the parameters affected and their default values, see the vectors_params man page.

<h2>Access</h2>

To use VVRSET or c_vvrset, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.

<h2>See Also</h2>

Online: vectors, vectors_params, vvectr, vvgetc, vvgeti, vvgetr, vvinit, vvsetc, vvseti, vvsetr, vvudmv, vvumxy, ncarg_cbind. 

 Hardcopy: NCAR Graphics Fundamentals, UNIX Version

<h2>Copyright</h2>

Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
