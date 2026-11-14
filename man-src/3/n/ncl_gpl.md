---
title: "ncl_gpl(3)"
name: "ncl_gpl"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_gpl/"
---

GPL (Polyline) - This output primitive draws line segments connecting a sequence of user-specified coordinate pairs.
<h2>Synopsis</h2>CALL GPL (N, X, Y)
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/gks.h&gt; 

 void gpolyline(const Gpoint_list *point_list);
<h2>Description</h2><dl COMPACT><dt>N
<dd>(Integer, Input) - The number of points in the line to be drawn. N must be larger than one.
<dt>X (N)
<dd>(Real Array, Input) - The X coordinates (specified in world coordinates) of the N points to be connected by line segments.
<dt>Y (N)
<dd>(Real Array, Input) - The Y coordinates (specified in world coordinates) of the N points to be connected by line segments.</dl><h2>Usage</h2>Note that the coordinate pairs must be in world coordinates and not user coordinates. Among other things, this means that the log scaling and mirror-imaging features available via the SET call and the SPPS functions for drawing lines are not applicable here.
<h2>Access</h2>To use GKS routines, load the NCAR GKS-0A library ncarg_gks.
<h2>See Also</h2>Online: gsln, gslwsc, gscr, gsplci, gqln, gqlwsc, gqplci, dashline, set, gpolyline 

 Hardcopy: User's Guide for NCAR GKS-0A Graphics; NCAR Graphics Fundamentals, UNIX Version &quot;The Use of X/Y Coordinates in NCAR Graphics&quot; SCD User Document&quot;
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
