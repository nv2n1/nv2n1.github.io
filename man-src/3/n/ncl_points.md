---
title: "ncl_points(3)"
name: "ncl_points"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_points/"
---

POINTS - draws a marker at each of a series of specified positions in the user coordinate system. The markers can also be connected by drawing lines between them.

<h2>Synopsis</h2>

CALL POINTS (PX,PY,NP,IC,IL)

<h2>C-Binding Synopsis</h2>

#include &lt;ncarg/ncargC.h&gt; 

 void c_points (float *px, float *py, int np, int ic, int il)

<h2>Description</h2>

<dl><dt>PX
<dd>(an input array of type REAL) defines the X user coordinates where a series of NP markers are to be drawn.
<dt>PY
<dd>(an input array of type REAL) defines the Y user coordinates where a series of NP markers are to be drawn.
<dt>NP
<dd>(an input expression of type INTEGER) specifies the number of markers to be drawn.
<dt>IC
<dd>(an input expression of type INTEGER) describes the type of marker to be drawn, as follows:
<dd>IC &lt; 0 - draw a GKS polymarker of type -IC, as follows:
<dl><dd><dl><dt> -1
<dd>requests a dot (.),
<dt> -2
<dd>requests a plus (+),
<dt> -3
<dd>requests an asterisk (*),
<dt> -4
<dd>requests a circle (o), and
<dt> -5
<dd>requests a cross (x).</dl></dl><dd>The polymarker size and color can be set by calling the GKS routines GSMKSC, GSCR, and GSPMCI before calling POINTS.
<dd>IC = 0 - draw a dot (.). Effect is the same as IC = -1.
<dd>IC &gt; 0 - draw the FORTRAN77 character CHAR(IC).
<dd>In this case, the GKS routine GTX is used to draw the specified character CHAR(IC) at each of the NP points. Each character is drawn with the horizontal and vertical text alignment centered at the specified point with a call to the GKS routine GSTXAL. The horizontal and vertical text alignment parameters are then restored to their previous values. Other text attributes such as character orientation, character height, and color, can be set by calling GKS text attribute setting routines before the call to the routine POINTS.
<dt>IL
<dd>(a input expression of type INTEGER) determines if the markers are to be connected with line segments.
<dd>IL = 0 - do not connect the markers with line segments.
<dd>IL .NE. 0 - connect the markers with line segments.</dl>

<h2>C-Binding Description</h2>

The C-binding argument descriptions are the same as the FORTRAN argument descriptions.

<h2>Usage</h2>

If the routine SET has not been called, or if the last call to SET specified linear mappings in X and Y, and the value of IC specifies a GKS polymarker, then the GKS routine GPM is called to draw the polymarkers. If, in addition, IL is non-zero, the GKS routine GPL is called to draw the line segments. In all other cases, NCAR Graphics routines are used to draw the more complicated set of graphical objects. 

 Since a call to POINTS can result in subsequent calls to the GKS routines GPM or GPL, various polymarker and polyline attributes may need to be set before the routine POINTS is called. Polymarker attributes which can be set are listed above in the DESCRIPTION Section. Polyline attributes which can be set include polyline type (call GSLN), polyline line width (call GSLWSC), and color (call GSCR and GSPLCI). 

 A call to the routine POINTS causes the SPPS polyline buffer to be flushed. Refer to the man page for the routine PLOTIF.

<h2>Examples</h2>

Use the ncargex command to see the following relevant examples: agex11, cmptra.

<h2>Access</h2>

To use POINTS or c_points, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.

<h2>See Also</h2>

Online: gpl, gsln, gslwsc, gpm, gsmk, gsmksc, gtx, gstxal, gstxp, gstxfp, gschh, gschsp, gschup, gschxp, gscr, gstxci, gsplci, gspmci, spps, spps_params, plotif, ngdots, point, ncarg_cbind 

 Hardcopy: NCAR Graphics Fundamentals, UNIX Version; User's Guide for NCAR GKS-0A Graphics

<h2>Copyright</h2>

Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
