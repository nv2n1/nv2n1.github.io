---
title: "ncl_velvec(3)"
name: "ncl_velvec"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_velvec/"
---

VELVEC - A older version of the Vectors utility, now a front-end to VELVCT. It is identical to the VELVCT call except that there is no LENGTH parameter to allow adjustment of the realized length of the maximum vector magnitude.

<h2>Synopsis</h2>

VELVEC (U,LU,V,LV,M,N,FLO,HI,NSET,ISPV,SPV)

<h2>Status</h2>

VELVEC is obsolete, and is supported only to provide compatibility with old NCAR Graphics codes. However, the compatibility mode parameter, CPM, offers a number of options to help ease the the transition to the new version of the utility. When writing new code you are encouraged not to use this entry point, since it provides less capability than the standard Vectors interface, and may eventually be phased out.

<h2>C-Binding Synopsis</h2>

#include &lt;ncarg/ncargC.h&gt; 

 void c_velvec(float *u, int lu, float *v, int lv, int m, 
 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>int n, float flo, float hi, int nset, 
 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>int ispv, float&nbsp;<wbr>*spv)

<h2>Description</h2>

<dl><dt>U
<dd>(REAL 2-dimensional array, dimensioned LU x n: n &gt;= N, input): By default, assumed to contain the first dimensional Cartesian components of the vector field. However, if PLR is non-zero, it is treated as containing the vector magnitudes.
<dt>LU
<dd>(INTEGER, input): Actual value of the first dimension of array U.
<dt>V
<dd>(REAL 2-dimensional array, dimensioned LV x n: n &gt;= N, input): By default, assumed to contain the second dimensional Cartesian components of the vector field. However, if PLR is non-zero, it is treated as containing the vector angles.
<dt>LV
<dd>LV (INTEGER, input): Actual value of the first dimension of array V.
<dt>M
<dd>(INTEGER, input): Number of contiguous elements along the first dimensional axis containing data to be processed in each of the arrays, U and V.
<dt>N
<dd>(INTEGER, input): Number of contiguous elements along the second dimensional axis containing data to be processed in each of the arrays, U and V.
<dt>FLO
<dd>(REAL, input): Minimum vector magnitude allowed to be displayed in the plot.
<dt>HI
<dd>(REAL, input): Maximum vector magnitude allowed to be displayed in the plot. If set to 0.0 there is no upper limit imposed.
<dt>NSET
<dd>(INTEGER, input): Flag that controls how and when the SET call is invoked. If NSET is 0, VELVEC makes a SET call to establish a standard viewport and window boundaries coincident with the array coordinate boundaries. PERIM is called to draw a border. If NSET is greater than zero, VELVEC does not call SET or PERIM. If NSET is less than zero, VELVEC calls SET to establish window boundaries coincident with the array grid coordinate boundaries but does not modify the viewport or call PERIM. Unlike the VVINIT/VVECTR interface, when VELVEC does a SET call, it always restores the original coordinate system state before returning.
<dt>ISPV
<dd>(INTEGER, input): Flag to control the special value feature. 0 means that the feature is not in use. 1 means that if the value of U(I,J)=<a HREF="/docs/linux/man/1-spv/">SPV</a>(1) the vector will not be plotted. 2 means that if the value of V(I,J)=<a HREF="/docs/linux/man/2-spv/">SPV</a>(2) the vector will not be plotted. 3 means that if either U(I,J)=<a HREF="/docs/linux/man/1-spv/">SPV</a>(1) or V(I,J)=<a HREF="/docs/linux/man/2-spv/">SPV</a>(2) then the vector will not be plotted. 4 means that if U(I,J)=<a HREF="/docs/linux/man/1-spv/">SPV</a>(1) and V(I,J)=<a HREF="/docs/linux/man/2-spv/">SPV</a>(2), the vector will not be plotted.
<dt>SPV
<dd>(REAL array, dimensioned 2, input): An array of length 2 which gives the value in the U array and the value in the V array which denote special values. This argument is ignored if ISPV=0. The default values are 1.0E12.</dl>

<h2>C-Binding Description</h2>

The C-binding argument descriptions are the same as the FORTRAN argument descriptions with the following exceptions: 

<dl><dt>lu
<dd>The second dimension of u in the calling program.
<dt>lv
<dd>The second dimension of v in the calling program.
<dt>m
<dd>Number of contiguous elements along the second dimensional axis containing data to be processed in each of the arrays, u and v.
<dt>n
<dd>Number of contiguous elements along the first dimensional axis containing data to be processed in each of the arrays, u and v.</dl>

<h2>Usage</h2>

VELVEC is used identically to VELVCT except that there is no provision for adjusting the realized length of the maximum vector magnitude. See the velvct man page for more information.

<h2>Access</h2>

To use VELVEC or c_velvec, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.

<h2>See Also</h2>

Online: vectors, vectors_params, fx, vvectr, vvgetc, vvgeti, vvgetr, vvinit, vvrset, vvsetc, vvseti, vvsetr, vvudmv, vvumxy, ncarg_cbind.

<h2>Copyright</h2>

Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 

 The use of this Software is governed by a License Agreement.
