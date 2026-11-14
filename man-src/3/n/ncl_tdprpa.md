---
title: "ncl_tdprpa(3)"
name: "ncl_tdprpa"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_tdprpa/"
---

TDPRPA - Given the parallelogram coordinates of a point, get the coordinates of its projection in the projection plane. This routine is essentially the inverse of the routine TDPRPI.

<h2>Synopsis</h2>

CALL TDPRPA (XIPA, YIPA, XI2D, YI2D)

<h2>C-Binding Synopsis</h2>

#include &lt;ncarg/ncargC.h&gt; 

 void c_tdprpa(float xipa, float yipa, float *xi2d, float *yi2d)

<h2>Description</h2>

The arguments of TDPRPA are as follows:
<dl><dt>XIPA and YIPA
<dd>(input expressions of type REAL) - the parallelogram coordinates of a point. (The parallelogram is as defined by a prior call to TDPARA.)
<dt>XI2D and YI2D
<dd>(output variables of type REAL) - the coordinates of the projection of the point in the projection plane.</dl>

<h2>C-Binding Description</h2>

The C-binding argument descriptions are the same as the FORTRAN argument descriptions.

<h2>Access</h2>

To use TDPRPA or c_tdprpa, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.

<h2>See Also</h2>

Online: tdclrs, tdctri, tddtri, tdgeti, tdgetr, tdgrds, tdgrid, tdgtrs, tdinit, tditri, tdlbla, tdlbls, tdline, tdlnpa, tdmtri, tdotri, tdpack, tdpack_params, tdpara, tdplch, tdprpi, tdprpt, tdseti, tdsetr, tdsort, tdstri, tdstrs

<h2>Copyright</h2>

Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
