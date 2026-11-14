---
title: "ncl_tdstri(3)"
name: "ncl_tdstri"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_tdstri/"
---

TDSTRI - Add triangles defining a simple surface to the triangles in a triangle list.

<h2>Synopsis</h2>

CALL TDSTRI (U, NU, V, NV, W, LW1D, RTRI, MTRI, NTRI, IRST)

<h2>C-Binding Synopsis</h2>

#include &lt;ncarg/ncargC.h&gt; 

 void c_tdstri(float *u, int nu, float *v, int nv, float *w, int lw1d, float *rtri, int mtri, int *ntri, int irst)

<h2>Description</h2>

The arguments of TDSTRI are as follows:
<dl><dt>U
<dd>(an input array, of type REAL, dimensioned NU) - values of an independent variable &quot;u&quot;. It must be the case that <a HREF="/docs/linux/man/1-u/">U</a>(1) &lt; <a HREF="/docs/linux/man/2-u/">U</a>(2) &lt; ... U(NU-1) &lt; U(NU).
<dt>NU
<dd>(an input expression of type INTEGER) - the dimension of U.
<dt>V
<dd>(an input array, of type REAL, dimensioned NV) - values of an independent variable &quot;v&quot;. It must be the case that <a HREF="/docs/linux/man/1-v/">V</a>(1) &lt; <a HREF="/docs/linux/man/2-v/">V</a>(2) &lt; ... V(NV-1) &lt; V(NV).
<dt>NV
<dd>(an input expression of type INTEGER) - the dimension of V.
<dt>W
<dd>(an input array, of type REAL, dimensioned NU x NV and having FORTRAN first dimension LW1D) - values of a dependent variable &quot;w(u,v)&quot;. The points (((U(I),V(J),W(I,J)),I=1,NU),J=1,NV) define a surface that one wishes to draw.
<dt>LW1D
<dd>(an input expression of type INTEGER) - the FORTRAN first dimension of the array W. It must be the case that LW1D is greater than or equal to NU.
<dt>RTRI
<dd>(an input array, of type REAL, dimensioned 10 x MTRI) - a list of triangles, probably created by means of calls to TDSTRI, TDITRI, and/or TDMTRI, and sorted, probably by means of a call to TDOTRI.
<dt>MTRI
<dd>(an input expression of type INTEGER) - the second dimension of RTRI and thus the maximum number of triangles the triangle list will hold.
<dt>NTRI
<dd>(an input/output variable of type INTEGER) - keeps track of the number of triangles currently in the list. It is the user's responsibility to zero this initially and its value is increased by each call to a triangle-generating routine like TDSTRI. If NTRI becomes equal to MTRI, TDSTRI does not take an error exit; instead, it just stops generating triangles. Therefore, it's a good idea, after calling TDSTRI, to check the value of NTRI against the dimension MTRI; if they're equal, it probably means that the triangle list filled up and that the rendered surface will be incomplete.
<dt>IRST
<dd>(an input expression of type INTEGER) - specifies the index of the rendering style to to be used for the triangles added to the triangle list by this call.</dl>

<h2>C-Binding Description</h2>

The C-binding argument descriptions are the same as the FORTRAN argument descriptions.

<h2>Access</h2>

To use TDSTRI or c_tdstri, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.

<h2>See Also</h2>

Online: tdclrs, tdctri, tddtri, tdgeti, tdgetr, tdgrds, tdgrid, tdgtrs, tdinit, tditri, tdlbla, tdlbls, tdline, tdlnpa, tdmtri, tdotri, tdpack, tdpack_params, tdpara, tdplch, tdprpa, tdprpi, tdprpt, tdseti, tdsetr, tdsort, tdstrs

<h2>Copyright</h2>

Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 

 The use of this Software is governed by a License Agreement.
