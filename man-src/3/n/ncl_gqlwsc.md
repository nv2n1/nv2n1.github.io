---
title: "ncl_gqlwsc(3)"
name: "ncl_gqlwsc"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_gqlwsc/"
---

GQLWSC (Inquire linewidth scale factor) - retrieves the current setting of the linewidth scale factor.
<h2>Synopsis</h2>CALL GQLWSC (ERRIND, LWIDTH)
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/gks.h&gt; 

 void ginq_linewidth(Gint *err_ind, Gdouble *linewidth);
<h2>Description</h2><dl COMPACT><dt>ERRIND
<dd>(Integer, Output) - If the inquired value cannot be returned correctly, a non-zero error indicator is returned in ERRIND, otherwise a zero is returned. Consult &quot;User's Guide for NCAR GKS-0A Graphics&quot; for a description of the meaning of the error indicators.
<dt>LWIDTH
<dd>(Real, Output) - Returns the current value of the linewidth scale factor as set by default or by a call to GSLWSC.</dl><h2>Access</h2>To use GKS routines, load the NCAR GKS-0A library ncarg_gks.
<h2>See Also</h2>Online: gpl, gsln, gslwsc, gscr, gsplci, gqln, gqplci, dashline, ginq_linewidth 

 Hardcopy: User's Guide for NCAR GKS-0A Graphics; NCAR Graphics Fundamentals, UNIX Version
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
