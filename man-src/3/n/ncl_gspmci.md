---
title: "ncl_gspmci(3)"
name: "ncl_gspmci"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_gspmci/"
---

GSPMCI - (Set polymarker color index) - sets the polymarker color index.
<h2>Synopsis</h2>CALL GSPMCI (COLI)
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/gks.h&gt; 

 void gset_marker_colr_ind(Gint marker_colr_ind);
<h2>Description</h2><dl COMPACT><dt>COLI
<dd>(Integer, Input) - A color index.</dl><h2>Usage</h2>All polymarkers drawn with calls to the GPM output primitive will be drawn with the color associated with index COLI until GSPMCI is called again and a new index is assigned. 

 For all GKS output primitives, color is assigned using a color index. The color indices run from 0 to 255, where 0 is the background color index and 1 is the foreground color index. Color values are associated with indices by calls to the GKS routine GSCR. If a color index is used that has no user-assigned color value set in a GSCR call, then a device-dependent color value will be assigned to that index.
<h2>Access</h2>To use GKS routines, load the NCAR GKS-0A library ncarg_gks.
<h2>See Also</h2>Online: gpm, gsmk, gsmksc, gscr, gqmk, gqmksc, gqpmci, point, points, gset_marker_colr_ind 

 Hardcopy: User's Guide for NCAR GKS-0A Graphics; NCAR Graphics Fundamentals, UNIX Version
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
