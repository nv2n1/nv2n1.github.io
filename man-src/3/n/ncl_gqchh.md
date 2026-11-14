---
title: "ncl_gqchh(3)"
name: "ncl_gqchh"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_gqchh/"
---

GQCHH (Inquire character height) - retrieves the current character height.
<h2>Synopsis</h2>CALL GQCHH (ERRIND, CHH)
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/gks.h&gt; 

 void ginq_char_ht(Gint *err_ind, Gdouble *char_ht);
<h2>Description</h2><dl COMPACT><dt>ERRIND
<dd>(Integer, Output) - If the inquired value cannot be returned correctly, a non-zero error indicator is returned in ERRIND, otherwise a zero is returned. Consult &quot;User's Guide for NCAR GKS-0A Graphics&quot; for a description of the meaning of the error indicators.
<dt>CHH
<dd>(Real, Output) - Contains the current character height as set by default or by GSCHH.</dl><h2>Access</h2>To use GKS routines, load the NCAR GKS-0A library ncarg_gks.
<h2>See Also</h2>Online: gtx, gstxp, gstxal, gstxfp, gschh, gschsp, gschup, gschxp, gscr, gstxci, gqtxp, gqtxal, gqtxfp, gqchsp, gqchup, gqchxp, plotchar, ginq_char_ht 

 Hardcopy: User's Guide for NCAR GKS-0A Graphics; NCAR Graphics Fundamentals, UNIX Version
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
