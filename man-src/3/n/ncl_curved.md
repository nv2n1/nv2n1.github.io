---
title: "ncl_curved(3)"
name: "ncl_curved"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_curved/"
---

CURVED - Draws a curve through a sequence of points. 

<h2>Synopsis</h2>CALL CURVED (X,Y,N)
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/ncargC.h&gt; 

 void c_curved (float *x, float *y, int n)
<h2>Description</h2><dl COMPACT><dt>X
<dd>(an input array of type REAL) defines the X user coordinates of the curve. Array X is of length N.
<dt>Y
<dd>(an input array of type REAL) defines the Y user coordinates of the curve. Array Y is of length N.
<dt>N
<dd>(an input expression of type INTEGER) specifies the number of points in the curve.</dl><h2>C-Binding Description</h2>The C-binding argument descriptions are the same as the FORTRAN argument description.
<h2>Usage</h2>The statement
<dl COMPACT><dd>CALL CURVED (X,Y,N)</dl>
 

 is equivalent to the statements
<dl COMPACT><dd>CALL FRSTD (<a HREF="/docs/linux/man/1-x/">X</a>(1),<a HREF="/docs/linux/man/1-y/">Y</a>(1)) 
 CALL VECTD (<a HREF="/docs/linux/man/2-x/">X</a>(2),<a HREF="/docs/linux/man/2-y/">Y</a>(2)) 
 CALL VECTD (<a HREF="/docs/linux/man/3-x/">X</a>(3),<a HREF="/docs/linux/man/3-y/">Y</a>(3)) 
 ...(et cetera)... 
 CALL VECTD (X(N),Y(N)) 
 CALL LASTD</dl>
 

 The basic difference is that CURVED requires you to have all of the coordinates defining the curve available at once; sometimes this is convenient and sometimes it is not. 

 If three or more distinct points are given, and if one of the smoothing versions of Dashline is being used, and if the internal parameter that suppresses smoothing is not set, then splines under tension are used to generate a smooth curve; the number of points actually used to draw the curve will depend on its length. In all other cases, the &quot;curve&quot; will be approximated by just connecting the given points in the specified order.
<h2>Examples</h2>Use the ncargex command to see the following relevant examples: carline, colcon, cmpfil, cmpgrp, cmpitm, cmplab, cmpmsk, cmptit, cpex01, cpex02, cpex03, cpex04, cpex06, vvex01, tdashc, tdashl, tdashp, tdashs, carline, fcover, ffex03, ffex05, fdlcurvd, fdldashd, fdlsmth, fpcloqu.
<h2>Access</h2>To use CURVED or c_curved, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order. 

 See the man page for dashline to see how to access the quick, normal, smooth, and super line draw options.
<h2>See Also</h2>Online: dashline, dashline_params, dashdb, dashdc, frstd, lastd, lined, reset, vectd, ncarg_cbind 

 Hardcopy: NCAR Graphics Contouring and Mapping Tutorial; NCAR Graphics Fundamentals, UNIX Version; User's Guide for NCAR GKS-0A Graphics
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
