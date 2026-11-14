---
title: "ncl_gqchxp(3)"
name: "ncl_gqchxp"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_gqchxp/"
---

GQCHXP (Inquire character expansion factor) - retrieves the current value of the character expansion factor.
<h2>Synopsis</h2>CALL GQCHXP (ERRIND, CHXP)
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/gks.h&gt; 

 void ginq_char_expan(Gint *err_ind, Gdouble *char_expan);
<h2>Description</h2><dl COMPACT><dt>ERRIND
<dd>(Integer, Output) - If the inquired value cannot be returned correctly, a non-zero error indicator is returned in ERRIND, otherwise a zero is returned. Consult &quot;User's Guide for NCAR GKS-0A Graphics&quot; for a description of the meaning of the error indicators.
<dt>CHXP
<dd>(Real, Output) - Contains the current value of the character expansion factor as set by default or by a call to GSCHXP.</dl><h2>Access</h2>To use GKS routines, load the NCAR GKS-0A library ncarg_gks.
<h2>See Also</h2>Online: gtx, gstxp, gstxal, gstxfp, gschh, gschsp, gschup, gschxp, gscr, gstxci, gqtxp, gqtxal, gqtxfp, gqchh, gqchsp, gqchup, plotchar, ginq_char_expan 

 Hardcopy: User's Guide for NCAR GKS-0A Graphics; NCAR Graphics Fundamentals, UNIX Version
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
