---
title: "ncl_ezvec(3)"
name: "ncl_ezvec"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_ezvec/"
---

EZVEC - A front-end to VELVCT with a simpler interface. Like VELVCT, it plots a a vector field in a single call. 

<h2>Synopsis</h2>CALL EZVEC (U,V,M,N)
<h2>Status</h2>EZVEC is obsolete, and is supported only to provide compatibility with old NCAR Graphics codes. However, the compatibility mode parameter, CPM, offers a number of options to help ease the the transition to the new version of the utility. When writing new code you are encouraged not to use this entry point, since it provides less capability than the standard Vectors interface, and may eventually be phased out.
<h2>C-Binding Synopsis#</h2>#include &lt;ncarg/ncargC.h&gt; 

 void c_ezvec (float *u, float *v, int m, int n)
<h2>Description</h2><dl COMPACT><dt>U
<dd>(REAL 2-dimensional array, dimensioned M x n: n &gt;= N, input) By default, assumed to contain the first dimensional Cartesian components of the vector field. However, if PLR is non-zero, it is treated as containing the vector magnitudes.
<dt>V
<dd>(REAL 2-dimensional array, dimensioned M x n: n &gt;= N, input) By default, assumed to contain the second dimensional Cartesian components of the vector field. However, if PLR is non-zero, it is treated as containing the vector angles.
<dt>M
<dd>(INTEGER, input) Actual size of the first dimension of arrays U and V
<dt>N
<dd>(INTEGER, input) Assumed size of the second dimension of arrays U and V.</dl><h2>C-Binding Description</h2>The C-binding argument descriptions are the same as the FORTRAN argument descriptions with the following exceptions:
<dl COMPACT><dt>m
<dd>The actual size of the second dimension of arrays u and v.
<dt>n
<dd>The assumed size of first dimension of arrays u and v.</dl><h2>Usage</h2>U and V are 2-dimensional vector component arrays, whose actual first dimensions must be equal to the value of M, and whose second dimensions must equal or exceed the value of N. 

 Assuming the default value of the compatibility mode parameter, CPM, Vectors always performs a SET call and draws a perimeter around the plot when accessed through the EZVEC interface. Before the return from EZVEC, another call to SET restores the previous coordinate system mapping. 

 By modifying the value of CPM, you may take more control over the utility than originally possible using this entry point. For instance, you can override the default value of the SET parameter, or use the Version 3.2 coordinate system mapping routines instead of the old FX, FY, MXF, and MYF functions. Nevertheless, when creating new code, use the VVINIT/VVECTR interface, since its capabilities are greater and more likely to improve with time.
<h2>Examples</h2>Use the ncargex command to see the following relevant example: tvelvc.
<h2>Access</h2>To use EZVEC, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.
<h2>See Also</h2>Online: vectors, vectors_params, fx, velvct, vvectr, vvgetc, vvgeti, vvgetr, vvinit, vvrset, vvsetc, vvseti, vvsetr, vvudmv, vvumxy, ncarg_cbind.
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 

 The use of this Software is governed by a License Agreement.
