---
title: "ncl_gqfais(3)"
name: "ncl_gqfais"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_gqfais/"
---

GQFAIS (Inquire fill area interior style) - retrieves the current value for fill area interior style.
<h2>Synopsis</h2>CALL GQFAIS (ERRIND, INTS)
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/gks.h&gt; 

 void ginq_fill_int_style(Gint *err_ind, Gfill_int_style *fill_int_style);
<h2>Description</h2><dl COMPACT><dt>ERRIND
<dd>(Integer, Output) - If the inquired value cannot be returned correctly, a non-zero error indicator is returned in ERRIND, otherwise a zero is returned. Consult &quot;User's Guide for NCAR GKS-0A Graphics&quot; for a description of the meaning of the error indicators.
<dt>INTS
<dd>(Integer, Output) - Returns the current value for fill style as set by default or by a call to GSFAIS.</dl><h2>Access</h2>To use GKS routines, load the NCAR GKS-0A library ncarg_gks.
<h2>See Also</h2>Online: gfa, gsfais, gsfasi, gscr, gsfaci, gqfasi, areas, ginq_fill_int_style 

 Hardcopy: &quot;User's Guide for NCAR GKS-0A Graphics&quot;;
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
