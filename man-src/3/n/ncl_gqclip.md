---
title: "ncl_gqclip(3)"
name: "ncl_gqclip"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_gqclip/"
---

GQCLIP (Inquire clipping indicator) - retrieves the current value of the clipping indicator as well as the current clipping rectangle.
<h2>Synopsis</h2>CALL GQCLIP (ERRIND, ICLIP, CLRECT)
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/gks.h&gt; 

 void ginq_clip(Gint *err_ind, Gclip *clip_ind_rect);
<h2>Description</h2><dl COMPACT><dt>ERRIND
<dd>(Integer, Output) - If the inquired values cannot be returned correctly, a non-zero error indicator is returned in ERRIND, otherwise a zero is returned. Consult &quot;User's Guide for NCAR GKS-0A Graphics&quot; for a description of the meaning of the error indicators.
<dt>ICLIP
<dd>(Integer, Output) - Returns the current value of the clipping indicator as set by default or by a call to GSCLIP.
<dl COMPACT><dd><dl COMPACT><dt>0
<dd>Clipping is off, or deactivated.
<dt>1
<dd>Clipping is on. Data outside of the world coordinate window will not be plotted.</dl></dl><dt>CLRECT
<dd>(Real, <a HREF="/docs/linux/man/4-array/">Array</a>(4)) - Four normalized device coordinates providing the corner points of the current clipping rectangle in the order XMIN, XMAX, YMIN, YMAX.</dl><h2>Access</h2>To use GKS routines, load the NCAR GKS-0A library ncarg_gks.
<h2>See Also</h2>Online: set, gsclip, gswn, gselnt, ginq_clip 

 Hardcopy: &quot;User's Guide for NCAR GKS-0A Graphics&quot;
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
