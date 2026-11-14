---
title: "ncl_tdprpi(3)"
name: "ncl_tdprpi"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_tdprpi/"
---

TDPRPI - Given a point in the projection plane, retrieve the parallelogram coordinates of that point in the reference parallelogram (as defined by the last call to TDPARA) that projects into it. This routine is essentially the inverse of the routine TDPRPA.

<h2>Synopsis</h2>

CALL TDPRPI (XI2D, YI2D, XIPA, YIPA)

<h2>C-Binding Synopsis</h2>

#include &lt;ncarg/ncargC.h&gt; 

 void c_tdprpi(float xi2d, float yi2d, float *xipa, float *yipa)

<h2>Description</h2>

The arguments of TDPRPI are as follows:
<dl><dt>XI2D and YI2D
<dd>(input expressions of type REAL) - the coordinates of a point in the projection plane.
<dt>XIPA and YIPA
<dd>(output variables of type REAL) - the parallelogram coordinates of that point in the reference parallelogram that projects into (XI2D,YI2D). (The parallelogram is as defined by a prior call to TDPARA.)</dl>

<h2>C-Binding Description</h2>

The C-binding argument descriptions are the same as the FORTRAN argument descriptions.

<h2>Access</h2>

To use TDPRPI or c_tdprpi, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.

<h2>See Also</h2>

Online: tdclrs, tdctri, tddtri, tdgeti, tdgetr, tdgrds, tdgrid, tdgtrs, tdinit, tditri, tdlbla, tdlbls, tdline, tdlnpa, tdmtri, tdotri, tdpack, tdpack_params, tdpara, tdplch, tdprpa, tdprpt, tdseti, tdsetr, tdsort, tdstri, tdstrs

<h2>Copyright</h2>

Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
