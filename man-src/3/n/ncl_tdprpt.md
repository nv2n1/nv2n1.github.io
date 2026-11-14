---
title: "ncl_tdprpt(3)"
name: "ncl_tdprpt"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_tdprpt/"
---

TDPRPT - Given the coordinates of a point in 3-space, get the coordinates of its projection in the projection plane.

<h2>Synopsis</h2>

CALL TDPRPT (UI3D, VI3D, WI3D, XI2D, YI2D)

<h2>C-Binding Synopsis</h2>

#include &lt;ncarg/ncargC.h&gt; 

 void c_tdprpt(float ui3d, float vi3d, float wi3d, float *xi2d, float *yi2d)

<h2>Description</h2>

The arguments of TDPRPT are as follows:
<dl><dt>UI3D, VI3D, and WI3D
<dd>(input expressions of type REAL) - the coordinates of a point in 3-space.
<dt>XI2D and YI2D
<dd>(output variables of type REAL) - the coordinates of the projection of the point in the projection plane.</dl>

<h2>C-Binding Description</h2>

The C-binding argument descriptions are the same as the FORTRAN argument descriptions.

<h2>Access</h2>

To use TDPRPT or c_tdprpt, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.

<h2>See Also</h2>

Online: tdclrs, tdctri, tddtri, tdgeti, tdgetr, tdgrds, tdgrid, tdgtrs, tdinit, tditri, tdlbla, tdlbls, tdline, tdlnpa, tdmtri, tdotri, tdpack, tdpack_params, tdpara, tdplch, tdprpa, tdprpi, tdseti, tdsetr, tdsort, tdstri, tdstrs

<h2>Copyright</h2>

Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
