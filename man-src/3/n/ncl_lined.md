---
title: "ncl_lined(3)"
name: "ncl_lined"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_lined/"
---

LINED - Draws a line segment between two points whose user coordinates are given. 

<h2>Synopsis</h2>CALL LINED (XA,XB,YA,YB)
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/ncargC.h&gt; 

 void c_lined (float xa, float xb, float ya, float yb)
<h2>Description</h2><dl COMPACT><dt>XA
<dd>(an input expression of type REAL) defines the X user coordinate of the starting point of a line segment.
<dt>YA
<dd>(an input expression of type REAL) defines the Y user coordinate of the starting point of a line segment.
<dt>XB
<dd>(an input expression of type REAL) defines the X user coordinate of the ending point of a line segment.
<dt>YB
<dd>(an input expression of type REAL) defines the Y user coordinate of the ending point of a line segment.</dl><h2>C-Binding Description</h2>The C-binding argument descriptions are the same as the FORTRAN argument descriptions.
<h2>Examples</h2>Use the ncargex command to see the following relevant examples: tdashc, tdashl, tdashp, tdashs, fcoord1, fcoord2, fdldashc, fdldashd, fgklnclr, fgklnwth dashdb, dashdc, frstd, lined, reset, vectd, ncarg_cbind
<h2>Access</h2>To use LINED or c_lined, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.
<h2>See Also</h2>Online: dashline, dashline_params, curved, dashdb, dashdc, frstd, lastd, reset, vectd, ncarg_cbind 

 Hardcopy: NCAR Graphics Contouring and Mapping Tutorial; NCAR Graphics Fundamentals, UNIX Version; User's Guide for NCAR GKS-0A Graphics
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
