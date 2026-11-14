---
title: "ncl_gqnt(3)"
name: "ncl_gqnt"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_gqnt/"
---

GQNT (Inquire normalization transformation) - retrieves the window and viewport associated with a given normalization transformation. Users of NCAR Graphics are encouraged to use the SPPS routines SET and GETSET to handle normalization transformations instead of the GKS entries GSWN, GSVP, GSELNT, and GQNT.
<h2>Synopsis</h2>CALL GQNT (NTNR, ERRIND, WINDOW, VIEWPT)
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/gks.h&gt; 

 void ginq_norm_tran(Gint num, Gint *err_ind, Gtran *norm_tran);
<h2>Description</h2><dl COMPACT><dt>NTNR
<dd>(Integer, Input) - Gives the number of the normalization transformation.
<dt>ERRIND
<dd>(Integer, Output) - If the inquired value cannot be returned correctly, a non-zero error indicator is returned in ERRIND, otherwise a zero is returned. Consult &quot;User's Guide for NCAR GKS-0A Graphics&quot; for a description of the meaning of the error indicators.
<dt><a HREF="/docs/linux/man/4-window/">WINDOW</a>(4)
<dd>(Real Array, Output) - The world coordinate window limits in the order WXMIN, WXMAX, WYMIN, WYMAX.
<dt><a HREF="/docs/linux/man/4-viewpt/">VIEWPT</a>(4)
<dd>(Real Array, Output) - The normalized device coordinate viewport limits in the order VXMIN, VXMAX, VYMIN, VYMAX.</dl><h2>Access</h2>To use GKS routines, load the NCAR GKS-0A library ncarg-gks.
<h2>See Also</h2>Online: gswn, gsvp, gselnt, gqcntn, gqmntn, getset, gsclip, gqclip, ginq_norm_tran 

 Hardcopy: &quot;User's Guide for NCAR GKS-0A Graphics&quot;
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 

 The use of this Software is governed by a License Agreement.
