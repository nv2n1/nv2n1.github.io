---
title: "ncl_line(3)"
name: "ncl_line"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_line/"
---

LINE - draws a line from the point (X1,Y1) to the point (X2,Y2). The &quot;pen&quot; (for subsequent calls to FRSTPT, VECTOR, PLOTIF, and PLOTIT) is left at (X2,Y2). 

<h2>Synopsis</h2>CALL LINE (X1,Y1,X2,Y2)
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/ncargC.h&gt; 

 void c_line (float x1, float y1, float x2, float y2)
<h2>Description</h2><dl COMPACT><dt>X1
<dd>(an input expression of type REAL) defines the X user coordinate of the starting point of a line segment.
<dt>Y1
<dd>(an input expression of type REAL) defines the Y user coordinate of the starting point of a line segment.
<dt>X2
<dd>(an input expression of type REAL) defines the X user coordinate of the ending point of a line segment.
<dt>Y2
<dd>(an input expression of type REAL) defines the Y user coordinate of the ending point of a line segment.</dl><h2>C-Binding Description</h2>The C-binding argument descriptions are the same as the FORTRAN argument descriptions.
<h2>Usage</h2>Polyline type, line width, and color can be set by calling the GKS routines GSLN, GSLWSC, GSCR, and GSPLCI before calling LINE. 

 This routine flushes the SPPS polyline buffer at each line draw. Thus, polyline attributes can be safely changed between successive calls.
<h2>Examples</h2>Use the ncargex command to see the following relevant examples: mpex07, mpex09, cbex01, coex01, coex03, epltch, srex01, and tgflas.
<h2>Access</h2>To use LINE or c_line, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.
<h2>See Also</h2>Online: gpl, gsln, gslwsc, gscr, gsplci, spps, spps_params, frstpt, vector, plotif, curve, ncarg_cbind 

 Hardcopy: NCAR Graphics Fundamentals, UNIX Version; User's Guide for NCAR GKS-0A Graphics
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
