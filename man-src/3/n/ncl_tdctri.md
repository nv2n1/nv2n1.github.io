---
title: "ncl_tdctri(3)"
name: "ncl_tdctri"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_tdctri/"
---

TDCTRI - Cut triangles defined by a triangle list.

<h2>Synopsis</h2>

CALL TDCTRI (RTRI, MTRI, NTRI, IAXS, RCUT)

<h2>C-Binding Synopsis</h2>

#include &lt;ncarg/ncargC.h&gt; 

 void c_tdctri(float *rtri, int mtri, int *ntri, int iaxs, float rcut)

<h2>Description</h2>

This routine, given a list of NTRI triangles in the array RTRI, an axis identifier IAXS (1 =&gt; U axis, 2 =&gt; V axis, 3 =&gt; W axis), and a value RCUT along that axis, cuts all the triangles that intersect the plane perpendicular to the identified axis at the specified value into two pieces, one on either side of the plane. This is useful when one is rendering the triangles in colors that depend on their position in U, V, or W. (See the example &quot;tdex04&quot;.) 

 The arguments of TDCTRI are as follows:
<dl><dt>RTRI
<dd>(an input/output array, of type REAL, dimensioned 10 x MTRI) - a list of triangles, probably created by means of calls to TDSTRI, TDITRI, and/or TDMTRI. The number of triangles in the list may increase as a result of calling TDCTRI.
<dt>MTRI
<dd>(an input expression of type INTEGER) - the second dimension of RTRI and thus the maximum number of triangles the triangle list will hold.
<dt>NTRI
<dd>(an input/output variable of type INTEGER) - specifies the number of triangles currently in the list. It is the user's responsibility to zero this initially; its value is increased by each call to a triangle-generating routine like TDSTRI or TDITRI and may be increased by a call to TDCTRI.
<dt>IAXS
<dd>(an input variable of type INTEGER) - specifies the axis to which the cut plane is perpendicular (1 =&gt; U axis, 2 =&gt; V axis, 3 =&gt; W axis).
<dt>RCUT
<dd>(an input variable of type REAL) - specifies that value of U, V, or W at which the cut plane intersects the axis.</dl>

<h2>C-Binding Description</h2>

The C-binding argument descriptions are the same as the FORTRAN argument descriptions.

<h2>Access</h2>

To use TDCTRI or c_tdctri, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.

<h2>See Also</h2>

Online: tdclrs, tddtri, tdgeti, tdgetr, tdgrds, tdgrid, tdgtrs, tdinit, tditri, tdlbla, tdlbls, tdline, tdlnpa, tdmtri, tdpack, tdpack_params, tdpara, tdplch, tdprpa, tdprpi, tdprpt, tdseti, tdsetr, tdsort, tdstri, tdstrs

<h2>Copyright</h2>

Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 

 The use of this Software is governed by a License Agreement.
