---
title: "ncl_frstpt(3)"
name: "ncl_frstpt"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_frstpt/"
---

FRSTPT - generates a &quot;pen-up&quot; move to a specified point in the user coordinate system. FRSTPT is used in conjunction with the routine VECTOR to draw lines. 

<h2>Synopsis</h2>CALL FRSTPT (PX,PY)
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/ncargC.h&gt; 

 void c_frstpt (float px, float py)
<h2>Description</h2><dl COMPACT><dt>PX
<dd>(an input expression of type REAL) defines the X user coordinate.
<dt>PY
<dd>(an input expression of type REAL) defines the Y user coordinate.</dl><h2>C-Binding Description ,,</h2>The C-binding argument descriptions are the same as the FORTRAN argument descriptions.
<h2>Usage</h2>Polyline type, line width, and color can be set by calling the GKS routines GSLN, GSLWSC, GSCR, and GSPLCI before calling FRSTPT. 

 Note that, for the sake of efficiency, the routines FRSTPT and VECTOR buffer the polylines resulting from pen moves. One must be sure to flush the SPPS polyline buffer before changing polyline attributes. A &quot;CALL PLOTIF (0.,0.,2)&quot; will flush the buffer.
<h2>Examples</h2>Use the ncargex command to see the following relevant examples: tgflas.
<h2>Access</h2>To use FRSTPT or c_frstpt, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.
<h2>See Also</h2>Online: gpl, gsln, gslwsc, gscr, gsplci, spps, spps_params, vector, line, curve, ncarg_cbind 

 Hardcopy: NCAR Graphics Fundamentals, UNIX Version; User's Guide for NCAR GKS-0A Graphics
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
