---
title: "ncl_stinit(3)"
name: "ncl_stinit"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_stinit/"
---

STINIT - Performs initialization tasks required before STREAM may be called to create a streamline field flow plot. Information about the input data arrays is copied into internal common block variables and the coordinate system mappings and boundaries are established.

<h2>Synopsis</h2>

CALL STINIT (U,LU,V,LV,P,LP,M,N,WRK,LW)

<h2>C-Binding Synopsis</h2>

#include &lt;ncarg/ncargC.h&gt; 

 void c_stinit(float *u, int lu, float *v, int lv, 
 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>float&nbsp;<wbr>*p, int lp, int m, int n,&nbsp;<wbr> 
 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>float&nbsp;<wbr>*wrk, int lw)

<h2>Description</h2>

<dl><dt>U
<dd>(REAL 2-dimensional array, dimensioned LU x n: n &gt;= N, input): By default, assumed to contain the first dimensional Cartesian components of the vector field. However, if PLR is non-zero, it is treated as containing the vector magnitudes.
<dt>LU
<dd>(INTEGER, input): Actual value of the first dimension of array U.
<dt>V
<dd>(REAL 2-dimensional array, dimensioned LV x n: n &gt;= N, input): By default, assumed to contain the second dimensional Cartesian components of the vector field. However, if PLR is non-zero, it is treated as containing the vector angles.
<dt>LV
<dd>(INTEGER, input): Actual value of the first dimension of array V.
<dt>P
<dd>(REAL, input, DUMMY): This argument is currently ignored and may be assigned a dummy value.
<dt>LP
<dd>(INTEGER, input, DUMMY): The first dimension of array P. Not currently used, this argument should be assigned the integer value 0.
<dt>M
<dd>(INTEGER, input): Number of contiguous elements along the first dimensional axis containing data to be processed in each of the arrays, U and V.
<dt>N
<dd>(INTEGER, input): Number of contiguous elements along the second dimensional axis containing data to be processed in each of the arrays, U and V.
<dt>WRK
<dd>(REAL, array dimensioned n: n &gt;= LW, input/output): Work array used to store normalized values of the U and V vector components while the streamlines are calculated. It also holds bit flags indicating whether a grid location is eligible for starting a streamline or placing a directional arrowhead.
<dt>LW
<dd>(INTEGER, input): Assumed size of the array WRK. Currently it must greater or equal to 2*M*N.</dl>

<h2>C-Binding Description</h2>

The C-binding argument descriptions are the same as the FORTRAN argument descriptions, with the following exceptions: 

<dl><dt>lu
<dd>The second dimension of u in the calling program.
<dt>lv
<dd>The second dimension of v in the calling program.
<dt>lp
<dd>The second dimension of p in the calling program.
<dt>m
<dd>Number of contiguous elements along the second dimension containing data to be processed in each of the arrays, u and v.
<dt>n
<dd>Number of contiguous elements along the first dimension containing data to be processed in each of the arrays, u and v.</dl>

<h2>Usage</h2>

Call STINIT before the first invocation of STREAM, and again anytime you modify the contents of the input data arrays. You may precede an STINIT call with any number of calls to the parameter setting routines, STSETR and STSETI. Although it is possible to call STSETI or STSETR between calls to STINIT and STREAM, changing the setting of many of Streamline's parameters at this point will result in incorrect behavior. When in doubt, set parameters before the STINIT call; see the streamlines_params man page for more information. 

 Set up the two vector component arrays prior to calling STINIT. To permit multiple purpose use of the array space, the STINIT argument list includes both the actual size and an assumed size for the first dimension of each input array. Due to FORTRAN array ordering conventions, only the assumed size needs to be specified for the second dimension. (Note: when using the C bindings, mentally exchange all references to first and second dimensions in this discussion.) The arguments LU and LV contain the actual size of the first dimensions of U and V, respectively. Since the grid locations for each of the data arrays are assumed to coincide, a single argument, M, represents the assumed size of the first dimension for both arrays. Similarly, the argument, N, is the assumed size of the second dimension. The only requirement for the actual second dimension size is that it be greater than or equal to N for each array. 

 The P and LP arguments are intended for future enhancement of the Streamlines utility. They are not currently used or examined in any way. For maximum assurance of compatibility with future changes to the code, give the LP argument the INTEGER value 0. 

 WRK is an array used to store normalized values of the U and V vector components while the streamlines are calculated. It also holds bit flags indicating whether a grid location is eligible for starting a streamline or placing a directional arrowhead. Its assumed size is specified by the argument LW. LW must have a value greater or equal to 2*M*N.

<h2>Examples</h2>

Use the ncargex command to see the following relevant examples: ffex00, ffex01, ffex03, ffex04, fstream, stex01, stex02, stex03.

<h2>Access</h2>

To use STINIT or c_stinit, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.

<h2>Messages</h2>

See the streamlines man page for a description of all Streamlines error messages and/or informational messages.

<h2>See Also</h2>

Online: stgetc, stgeti, stgetr, stream, streamlines, streamlines_params, strset, stsetc, stseti, stsetr, stuixy, stumsl, stumta, stumxy, ncarg_cbind. 

 Hardcopy: NCAR Graphics Fundamentals, UNIX Version

<h2>Copyright</h2>

Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
