---
title: "ncl_fence3(3)"
name: "ncl_fence3"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_fence3/"
---

FENCE3 - Draws the projection of a curve, just as CURVE3 does, but with a &quot;fence&quot; of straight line segments that are parallel to one of the three axes and extend from the curve to a specified plane perpendicular to that axis. 

<h2>Synopsis</h2>CALL FENCE3 (U,V,W,N,IOREN,BOT)
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/ncargC.h&gt; 

 void c_fence3 (float *u, float *v, float *w, int n, 
 int ioren, float bot)
<h2>Description</h2><dl COMPACT><dt>U,V,W
<dd>(input arrays, dimensioned at least N, of type REAL) contain the U, V, and W coordinates, respectively, of the points defining the curve whose projection is to be drawn.
<dt>N
<dd>(an input expression of type INTEGER) is the number of points defining the curve.
<dt>IOREN
<dd>(an input expression of type INTEGER) is the direction in which fence lines are to be drawn, as follows:
<dl COMPACT><dd><dl COMPACT><dt>1
<dd>Parallel to the U axis.
<dt>2
<dd>Parallel to the V axis.
<dt>3
<dd>Parallel to the W axis.</dl></dl><dt>BOT
<dd>(an input expression of type REAL) specifies where the bottom of the fence is to be drawn. For example, if the fence lines are to be drawn parallel to the W-axis, and BOT=2., then the bottom of the fence would be the plane W=2. 

 The word &quot;bottom&quot; may be misleading here; the entire curve might be below the plane of the &quot;bottom&quot; and the fence might be horizontal, rather than vertical, in the three-dimensional space.</dl>
 

 The curve and the fence are drawn in the colors implied by the values of the variables ITHRMJ and ITHRMN, respectively, in the Threed COMMON block 

<dl COMPACT><dd><dl COMPACT><dd>COMMON /THRINT/ ITHRMJ,ITHRMN,ITHRTX</dl></dl>
 

 The default value of both ITHRMJ and ITHRMN is 1; user code may change these values.
<h2>C-Binding Description</h2>The C-binding argument descriptions are the same as the FORTRAN argument descriptions.
<h2>Examples</h2>Use the ncargex command to see the following relevant example: fthex04.
<h2>Access</h2>To use FENCE3 or c_fence3, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.
<h2>See Also</h2>Online: threed, curve3, frst3, line3, perim3, point3, psym3, pwrz, pwrzt, set3, threed, tick3, tick43, vect3, ncarg_cbind. 

 Hardcopy: NCAR Graphics Fundamentals, UNIX Version
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
