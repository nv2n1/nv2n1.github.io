---
title: "ncl_gsmksc(3)"
name: "ncl_gsmksc"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_gsmksc/"
---

GSMKSC (Set marker size scale factor) - sets the polymarker size scale factor -- the relative size of the marker.
<h2>Synopsis</h2>CALL GSMKSC (MSZSF)
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/gks.h&gt; 

 void gset_marker_size(Gdouble marker_size);
<h2>Description</h2><dl COMPACT><dt>MSZSF
<dd>(Real, Input) - A scale factor to control the size of the marker. It must be greater than or equal to 0. Since MSZSF = 1.0 by default, setting MSZSF = 2.0 doubles polymarker size.</dl><h2>Access</h2>To use GKS routines, load the NCAR GKS-0A library ncarg_gks.
<h2>See Also</h2>Online: gpm, gsmk, gscr, gspmci, gqmk, gqmksc, gqpmci, point, points, gset_marker_size 

 Hardcopy: User's Guide for NCAR GKS-0A Graphics; NCAR Graphics Fundamentals, UNIX Version
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
