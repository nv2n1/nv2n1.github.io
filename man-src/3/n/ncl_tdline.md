---
title: "ncl_tdline(3)"
name: "ncl_tdline"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_tdline/"
---

TDLINE - Given the coordinates of two points in 3-space, draw the projection of the line joining them.

<h2>Synopsis</h2>

CALL TDLINE (UCP1, VCP1, WCP1, UCP2, VCP2, WCP2)

<h2>C-Binding Synopsis</h2>

#include &lt;ncarg/ncargC.h&gt; 

 void c_tdline(float ucp1, float vcp1, float wcp1, float ucp2, float vcp2, float wcp2)

<h2>Description</h2>

The arguments of TDLINE are as follows:
<dl><dt>UCP1, VCP1, and WCP1
<dd>(input expressions of type REAL) - the coordinates of a point in 3-space.
<dt>UCP2, VCP2, and WCP2
<dd>(input expressions of type REAL) - the coordinates of another point in 3-space.</dl>

<h2>C-Binding Description</h2>

The C-binding argument descriptions are the same as the FORTRAN argument descriptions.

<h2>Access</h2>

To use TDLINE or c_tdline, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.

<h2>See Also</h2>

Online: tdclrs, tdctri, tddtri, tdgeti, tdgetr, tdgrds, tdgrid, tdgtrs, tdinit, tditri, tdlbla, tdlbls, tdlnpa, tdmtri, tdotri, tdpack, tdpack_params, tdpara, tdplch, tdprpa, tdprpi, tdprpt, tdseti, tdsetr, tdsort, tdstri, tdstrs

<h2>Copyright</h2>

Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
