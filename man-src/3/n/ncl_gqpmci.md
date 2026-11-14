---
title: "ncl_gqpmci(3)"
name: "ncl_gqpmci"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_gqpmci/"
---

GQPMCI (Inquire polymarker color index) - retrieves the polymarker color index.
<h2>Synopsis</h2>CALL GQPMCI (ERRIND, COLI)
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/gks.h&gt; 

 void ginq_marker_colr_ind(Gint *err_ind, Gint *marker_colr_ind);
<h2>Description</h2><dl COMPACT><dt>ERRIND
<dd>(Integer, Output) - If the inquired value cannot be returned correctly, a non-zero error indicator is returned in ERRIND, otherwise a zero is returned. Consult &quot;User's Guide for NCAR GKS-0A Graphics&quot; for a description of the meaning of the error indicators.
<dt>COLI
<dd>(Integer, Output) - Returns the polymarker color index as set by default or by a call to GSPMCI.</dl><h2>Access</h2>To use GKS routines, load the NCAR GKS-0A library ncarg_gks.
<h2>See Also</h2>Online: gpm, gsmk, gsmksc, gscr, gspmci, gqmk, gqmksc, gqpmci, point, points, ginq_marker_colr_ind 

 Hardcopy: User's Guide for NCAR GKS-0A Graphics; NCAR Graphics Fundamentals, UNIX Version
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
