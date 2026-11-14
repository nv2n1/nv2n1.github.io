---
title: "ncl_vvinit(3)"
name: "ncl_vvinit"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_vvinit/"
---

VVINIT - Performs initialization tasks required before VVECTR may be called to plot a vector field, including copying array size information into internal common block variables, establishing coordinate system mappings and boundaries, determining the maximum and minimum vector magnitudes and scalar array values, and, if required, setting up the color threshold value array.

<h2>Synopsis</h2>

CALL VVINIT (U,LU,V,LV,P,LP,M,N,WRK,LW)

<h2>C-Binding Synopsis</h2>

#include &lt;ncarg/ncargC.h&gt; 

 void c_vvinit(float *u, int lu, float *v, int lv, 
 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>float&nbsp;<wbr>*p, int lp, int m, int n, 
 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>float&nbsp;<wbr>*wrk, int lw)

<h2>Description</h2>

<dl><dt>U
<dd>(REAL 2-dimensional array, dimensioned LU x n: n &gt;= N, input): By default, assumed to contain the first dimensional Cartesian components of the vector field. However, if PLR is non-zero, it is treated as containing the vector magnitudes.
<dt>LU
<dd>(INTEGER, input): Actual value of the first dimension of array U.
<dt>V
<dd>(REAL 2-dimensional array, dimensioned LV x n: n &gt;= N, input): By default, assumed to contain the second dimensional Cartesian components of the vector field. However, if PLR is non-zero, it is treated as containing the vector angles.
<dt>LV
<dd>(INTEGER, input): Actual value of the first dimension of array V
<dt>P
<dd>(REAL 2-dimensional array, dimensioned LP x n: n &gt;= N, input): Array of scalar data that may be used to color the vectors. The grid points are assumed to coincide with the grid points of the U and V arrays. Required only if CTV has an absolute value of 2; otherwise this argument is ignored and may be assigned a dummy value.
<dt>LP
<dd>(INTEGER, input): Actual value of the first dimension of array P
<dt>M
<dd>(INTEGER, input): Number of contiguous elements along the first dimensional axis containing data to be processed in each of the arrays, U, V, and P (if used).
<dt>N
<dd>(INTEGER, input): Number of contiguous elements along the second dimensional axis containing data to be processed in each of the arrays, U, V, and P (if used).
<dt>WRK
<dd>(REAL, array dimensioned n: n &gt;= LW, input/output): Work array required only if the parameter VMD is set to a value greater than 0.0. If required must be dimensioned greater or equal to 2 * M * N. Otherwise may be set to a dummy value.
<dt>LW
<dd>(INTEGER, input): Assumed size of the array WRK. If the parameter VMD is set to a value greater than 0.0, must be set to a value less than or equal to the dimension of the WRK array, but greater or equal to 2 * M * N. Otherwise, this argument should be assigned the integer value 0.</dl>

<h2>C-Binding Description</h2>

The C-binding argument descriptions are the same as the FORTRAN argument descriptions with the following exceptions: 

<dl><dt>lu
<dd>The second dimension of u in the calling program.
<dt>lv
<dd>The second dimension of v in the calling program.
<dt>lp
<dd>The second dimension of p in the calling program.
<dt>m
<dd>Number of contiguous elements along the second dimensional axis containing data to be processed in each of the arrays, u, v, and p (if used).
<dt>n
<dd>Number of contiguous elements along the first dimensional axis containing data to be processed in each of the arrays, u, v, and p (if used).</dl>

<h2>Usage</h2>

Call VVINIT before the first invocation of VVECTR and again anytime you modify the contents of the input data arrays. You may precede a VVINIT call with any number of calls to the Vectors parameter setting routines (VVSETC, VVSETI, or VVSETR). After the VVINIT call, you may still change certain parameters before calling VVECTR. (Consult the vectors_params man page for further information on this point.) 

 Set up the two vector component arrays prior to calling VVINIT. To permit multiple purpose use of the array space, the VVINIT argument list includes both the actual size and an assumed size for the first dimension of each input array. Due to FORTRAN array ordering conventions, only the assumed size needs to be specified for the second dimension. (Note: when using the C bindings, mentally exchange all references to first and second dimensions in this discussion.) The arguments LU, LV, and LP contain the actual size of the first dimensions of arrays U, V, and P respectively. Since the grid locations for each of the data arrays are assumed to coincide, a single argument, M, represents the assumed size of the first dimension for all the arrays. Similarly, the argument, N, is the assumed size of the second dimension. The only requirement for the actual second dimension size is that it be greater than or equal to N for each array. 

 The array specified by the WRK argument and its associated size specifier, LW, are used only when the parameter VMD (Vector Minimum Distance) is given a value greater than 0.0. In this case, Vectors uses the array to keep track of the location of each vector in NDC space so that the distances between vectors can be compared. Based on these comparisons, Vectors eliminates some vectors such that the remaining vectors are separated by at least the specified distance. If VMD is less than or equal to 0.0, you may assign an arbitrary dummy value to WRK, but you should set LW to the integer value 0.

<h2>C-Binding Usage</h2>

C-Binding usage is the same as FORTRAN usage discussed above if the references to &quot;first dimension&quot; and &quot;second dimension&quot; are exchanged.

<h2>Examples</h2>

Use the ncargex command to see the following relevant examples: bnchmk, fcover, ffex00, ffex01, ffex02, ffex05, stex02, stex03, vvex01, vvex02.

<h2>Access</h2>

To use VVINIT or c_vvinit, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.

<h2>Messages</h2>

See the vectors man page for a description of all Vectors error messages and/or informational messages.

<h2>See Also</h2>

Online: vectors, vectors_params, vvectr, vvgetc, vvgeti, vvgetr, vvrset, vvsetc, vvseti, vvsetr, vvudmv, vvumxy, ncarg_cbind. 

 Hardcopy: NCAR Graphics Fundamentals, UNIX Version

<h2>Copyright</h2>

Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
