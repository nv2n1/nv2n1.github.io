---
title: "ncl_gpm(3)"
name: "ncl_gpm"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_gpm/"
---

GPM (Polymarker) - the polymarker output primitive draws selected symmetric symbols to mark user-specified coordinate positions.
<h2>Synopsis</h2>CALL GPM (N, X, Y)
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/gks.h&gt; 

 void gpolymarker(const Gpoint_list *point_list);
<h2>Description</h2><dl COMPACT><dt>N
<dd>(Integer, Input) - The number of markers to be drawn. N must be greater than zero.
<dt>X (N)
<dd>(Real Array, Input) - The X coordinates of the N markers to be drawn, in world coordinates.
<dt>Y (N)
<dd>(Real Array, Input) - The Y coordinates of the N markers to be drawn, in world coordinates.</dl><h2>Usage</h2>By default, the polymarker type is an asterisk. To select other polymarker types and attributes, see the man page for gsmk. 

 Note that the coordinate pairs must be in world coordinates and not user coordinates. Among other things, this means that the log scaling and mirror-imaging features available via the SET call and the SPPS functions for drawing dots and markers are not applicable here.
<h2>Access</h2>To use GKS routines, load the NCAR GKS-0A library ncarg_gks.
<h2>See Also</h2>Online: gsmk, gsmksc, gscr, gspmci, gqmk, gqmksc, gqpmci, point, points, ngdots, gpolymarker 

 Hardcopy: User's Guide for NCAR GKS-0A Graphics; NCAR Graphics Fundamentals, UNIX Version
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
