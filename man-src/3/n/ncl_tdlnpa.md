---
title: "ncl_tdlnpa(3)"
name: "ncl_tdlnpa"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_tdlnpa/"
---

TDLNPA - Given the coordinates of two points in the reference parallelogram, draw the projection of the line joining them.

<h2>Synopsis</h2>

CALL TDLNPA (XCP1, YCP1, XCP2, YCP2)

<h2>C-Binding Synopsis</h2>

#include &lt;ncarg/ncargC.h&gt; 

 void c_tdlnpa(float xcp1, float ycp1, float xcp2, float ycp2)

<h2>Description</h2>

The arguments of TDLNPA are as follows:
<dl><dt>XCP1 and YCP1
<dd>(input expressions of type REAL) - the parallelogram coordinates of a point in the reference parallelogram (as defined by the last call to TDPARA).
<dt>XCP2 and YCP2
<dd>(input expressions of type REAL) - the parallelogram coordinates of another point in the reference parallelogram.</dl>

<h2>C-Binding Description</h2>

The C-binding argument descriptions are the same as the FORTRAN argument descriptions.

<h2>Access</h2>

To use TDLNPA or c_tdlnpa, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.

<h2>See Also</h2>

Online: tdclrs, tdctri, tddtri, tdgeti, tdgetr, tdgrds, tdgrid, tdgtrs, tdinit, tditri, tdlbla, tdlbls, tdline, tdmtri, tdotri, tdpack, tdpack_params, tdpara, tdplch, tdprpa, tdprpi, tdprpt, tdseti, tdsetr, tdsort, tdstri, tdstrs

<h2>Copyright</h2>

Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
