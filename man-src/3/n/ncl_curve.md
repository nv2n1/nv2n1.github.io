---
title: "ncl_curve(3)"
name: "ncl_curve"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_curve/"
---

CURVE - draws the curve defined by a specified series of points in the user coordinate system. The &quot;pen&quot; (for subsequent calls to FRSTPT, VECTOR, PLOTIF, and PLOTIT) is left at the location of the last point in the curve. 

<h2>Synopsis</h2>CALL CURVE (PX,PY,NP)
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/ncargC.h&gt; 

 void c_curve (float *px, float *py, int np)
<h2>Description</h2><dl COMPACT><dt>PX
<dd>(an input array of type REAL) defines the X user coordinates of the curve. Array PX is of length NP.
<dt>PY
<dd>(an input array of type REAL) defines the Y user coordinates of the curve. Array PY is of length NP.
<dt>NP
<dd>(an input expression of type INTEGER) specifies the number of points in the curve.</dl><h2>C-Binding Description</h2>The C-binding argument descriptions are the same as the FORTRAN argument descriptions.
<h2>Usage</h2>If the routine SET was not called, or if it was called with a linear mapping in both the X and Y coordinates, then the GKS routine GPL is called to output a polyline of length NP points. If the mapping in either axis is logarithmic, the input coordinates are transformed and drawn ten points at a time. (The last segment may be less than ten points.) 

 Polyline type, line width, and color can also be set by calling the GKS routines GSLN, GSLWSC, GSCR, and GSPLCI, before calling CURVE.
<h2>Examples</h2>Use the ncargex command to see the following relevant examples: sfex01, sfex02, and tsoftf.
<h2>Access</h2>To use CURVE or c_curve, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.
<h2>See Also</h2>Online: gpl, gsln, gslwsc, gscr, gsplci, frstpt, vector, plotif, line, spps, spps_params, ncarg_cbind 

 Hardcopy: NCAR Graphics Fundamentals, UNIX Version User's Guide for NCAR GKS-0A Graphics; &quot;The Use of X/Y Coordinates in NCAR Graphics&quot; SCD User Document
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
