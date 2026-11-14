---
title: "ncl_gslwsc(3)"
name: "ncl_gslwsc"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_gslwsc/"
---

GSLWSC (Set linewidth scale factor) - sets the linewidth scale factor, or relative thickness of a polyline.
<h2>Synopsis</h2>CALL GSLWSC (LWIDTH)
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/gks.h&gt; 

 void gset_linewidth(Gdouble linewidth);
<h2>Description</h2><dl COMPACT><dt>LWIDTH
<dd>(Real, Input) - A scale factor to control the linewidth of the polyline to be drawn. It must be greater than or equal to 0. LWIDTH is applied to the nominal linewidth on a given device and the linewidths are mapped to the nearest available linewidth representable on that device. 

 By default LWIDTH = 1.0, so setting LWIDTH = 2.0 will double line width on most devices.</dl><h2>Access</h2>To use GKS routines, load the NCAR GKS-0A library ncarg_gks.
<h2>See Also</h2>Online: gpl, gsln, gscr, gsplci, gqln, gqlwsc, gqplci, dashline, gset_linewidth 

 Hardcopy: User's Guide for NCAR GKS-0A Graphics; NCAR Graphics Fundamentals, UNIX Version
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
