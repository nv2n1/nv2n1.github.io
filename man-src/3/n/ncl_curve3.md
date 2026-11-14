---
title: "ncl_curve3(3)"
name: "ncl_curve3"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_curve3/"
---

CURVE3 - Draws the projection of a curve defined by a sequence of points in 3-space. 

<h2>Synopsis</h2>CALL CURVE3 (U,V,W,N)
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/ncargC.h&gt; 

 void c_curve3 (float *u, float *v, float *w, int n)
<h2>Description</h2><dl COMPACT><dt>U,V,W
<dd>(input arrays, dimensioned at least N, of type REAL) contain the U, V, and W coordinates, respectively, of the points defining the curve whose projection is to be drawn.
<dt>N
<dd>(an input expression of type INTEGER) is the number of points defining the curve.</dl>
 

 Curves drawn by CURVE3 are drawn in the current polyline color, as determined by the last call to the GKS routine GSPLCI; by default, color index 1 is used. Line width is determined by the last call to the GKS routine GSLWSC; by default, the line width scale factor is 1.
<h2>C-Binding Description</h2>The C-binding argument descriptions are the same as the FORTRAN argument descriptions.
<h2>Examples</h2>Use the ncargex command to see the following relevant examples: tthree, fthex03.
<h2>Access</h2>To use CURVE3 or c_curve3, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.
<h2>See Also</h2>Online: threed, fence3, frst3, line3, perim3, point3, psym3, pwrz, pwrzt, set3, threed, tick3, tick43, vect3, ncarg_cbind. 

 Hardcopy: NCAR Graphics Fundamentals, UNIX Version
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
