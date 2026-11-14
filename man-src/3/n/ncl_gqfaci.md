---
title: "ncl_gqfaci(3)"
name: "ncl_gqfaci"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_gqfaci/"
---

GQFACI (Inquire fill area color index) - retrieves the current fill area color index.
<h2>Synopsis</h2>CALL GQFACI (ERRIND, COLI)
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/gks.h&gt; 

 void ginq_fill_colr_ind(Gint *err_ind, Gint *fill_colr_ind);
<h2>Description</h2><dl COMPACT><dt>ERRIND
<dd>(Integer, Output) - If the inquired value cannot be returned correctly, a non-zero error indicator is returned in ERRIND, otherwise a zero is returned. Consult &quot;User's Guide for NCAR GKS-0A Graphics&quot; for a description of the meaning of the error indicators.
<dt>COLI
<dd>(Integer, Output) - Returns the current fill area color index as set by default or by a call to GSFACI.</dl><h2>Access</h2>To use GKS routines, load the NCAR GKS-0A library ncarg_gks.
<h2>See Also</h2>Online: gfa, gsfais, gsfasi, gscr, gsfaci, gqfais, gqfasi, areas, ginq_fill_colr_ind 

 Hardcopy: &quot;User's Guide for NCAR GKS-0A Graphics&quot;
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
