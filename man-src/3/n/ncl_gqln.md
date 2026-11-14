---
title: "ncl_gqln(3)"
name: "ncl_gqln"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_gqln/"
---

GQLN (Inquire line type) - retrieves the current setting for linetype.
<h2>Synopsis</h2>CALL GQLN (ERRIND, LTYPE)
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/gks.h&gt; 

 void ginq_linetype(Gint *err_ind, Gint *linetype);
<h2>Description</h2><dl COMPACT><dt>ERRIND
<dd>(Integer, Output) - If the inquired value cannot be returned correctly, a non-zero error indicator is returned in ERRIND, otherwise a zero is returned. Consult &quot;User's Guide for NCAR GKS-0A Graphics&quot; for a description of the meaning of the error indicators.
<dt>LTYPE
<dd>(Integer, Output) - Returns the current value for the line type as set by default or by a call to GSLN.
<dl COMPACT><dd><dl COMPACT><dt>1
<dd>Solid
<dt>2
<dd>Dashed
<dt>3
<dd>Dotted
<dt>4
<dd>Dot-dash</dl></dl>
</dl><h2>Access</h2>To use GKS routines, load the NCAR GKS-0A library ncarg_gks.
<h2>See Also</h2>Online: gpl, gsln, gslwsc, gscr, gsplci, gqlwsc, gqplci, dashline, ginq_linetype 

 Hardcopy: User's Guide for NCAR GKS-0A Graphics; NCAR Graphics Fundamentals, UNIX Version
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
