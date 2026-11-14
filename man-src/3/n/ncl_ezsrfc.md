---
title: "ncl_ezsrfc(3)"
name: "ncl_ezsrfc"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_ezsrfc/"
---

EZSRFC - Draws a perspective picture of a function of two variables with hidden lines removed. The function is approximated by a two-dimensional array of heights. Use EZSRFC only if the entire array is to be drawn, the data points are equally spaced in the X-Y plane, there are no stereo pairs, and scaling is chosen internally. 

<h2>Synopsis</h2>CALL EZSRFC (Z,M,N,ANGH,ANGV,WORK)
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/ncargC.h&gt; 

 void c_ezsrfc (float *z, int m, int n, float angh, float angv, 
 float *work)
<h2>Description</h2><dl COMPACT><dt>Z
<dd>The M by N array to be drawn.
<dt>M
<dd>The first dimension of Z.
<dt>N
<dd>The second dimension of Z.
<dt>ANGH
<dd>Angle in degrees in the X-Y plane to the line of sight (counterclockwise from the plus-X axis).
<dt>ANGV
<dd>Angle in degrees from the X-Y plane to the line of sight (positive angles are above the middle Z, negative below).
<dt>WORK
<dd>A scratch storage dimensioned at least 2*M*N+M+N.</dl><h2>C-Binding Description</h2>The C-binding argument descriptions are the same as the FORTRAN argument descriptions, with the following exceptions:
<dl COMPACT><dt>z
<dd>The n by m array to be drawn.
<dt>m
<dd>The second dimension of z.
<dt>n
<dd>The first dimension of z.</dl><h2>Examples</h2>Use the ncargex command to see the following relevant examples: fsrezsrf, tsrfac.
<h2>Access</h2>To use EZSRFC or c_ezsrfc, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.
<h2>See Also</h2>Online: surface, surface_params, pwrzs, setr, srface. ncarg_cbind. 

 Hardcopy: NCAR Graphics Fundamentals, UNIX Version
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
