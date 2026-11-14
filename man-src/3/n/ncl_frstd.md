---
title: "ncl_frstd(3)"
name: "ncl_frstd"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_frstd/"
---

FRSTD - Defines the first of a sequence of points through which a curve is to be drawn. 

<h2>Synopsis</h2>CALL FRSTD (X,Y)
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/ncargC.h&gt; 

 void c_frstd (float x, float y)
<h2>Description</h2><dl COMPACT><dt>X
<dd>(an input expression of type REAL) defines the X user coordinate of the starting point of the curve.
<dt>Y
<dd>(an input expression of type REAL) defines the Y user coordinate of the starting point of the curve.</dl><h2>C-Binding Description</h2>The C-binding argument descriptions are the same as the FORTRAN argument descriptions.
<h2>Usage</h2>One way to draw a curve with Dashline is to call FRSTD once to define the first point of the curve and then to call VECTD repeatedly to define the second and all following points of the curve. 

 If three or more distinct points are given, and if one of the smoothing versions of Dashline is being used, and if the internal parameter that suppresses smoothing is not set, then splines under tension are used to generate a smooth curve; the number of points actually used to draw the curve will depend on its length. In all other cases, the &quot;curve&quot; will be approximated by just connecting the user-given points in the specified order. 

 After the call to VECTD defining the last point of the curve, you may call LASTD, which flushes any portions of smoothed curves that are defined by coordinates saved in internal buffers of FRSTD and VECTD and that have not yet been drawn. Calls to LASTD are not always required - for example, when a non-smoothing version of Dashline is used (no buffering) or when the next call to an NCAR Graphics routine will be to FRSTD (which flushes the buffers) - but unnecessary calls do no harm. If you judge that one of the smoothing versions of Dashline may be used, it is best to put in the calls to LASTD.
<h2>Examples</h2>Use the ncargex command to see the following relevant examples: tdashc, tdashl, tdashp, tdashs, fdldashc, fdldashd.
<h2>Access</h2>To use FRSTD or c_frstd load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.
<h2>See Also</h2>Online: dashline, dashline_params, curved, dashdb, dashdc, lastd, lined, reset, vectd, ncarg_cbind 

 Hardcopy: NCAR Graphics Contouring and Mapping Tutorial; NCAR Graphics Fundamentals, UNIX Version; User's Guide for NCAR GKS-0A Graphics
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 

 The use of this Software is governed by a License Agreement.
