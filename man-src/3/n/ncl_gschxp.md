---
title: "ncl_gschxp(3)"
name: "ncl_gschxp"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_gschxp/"
---

GSCHXP (Set character expansion factor) - sets the width to height ratio of text.
<h2>Synopsis</h2>CALL GSCHXP (CHXP)
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/gks.h&gt; 

 void gset_char_expan(Gdouble char_expan);
<h2>Description</h2><dl COMPACT><dt>CHXP
<dd>(Real, Input) - Specifies a deviation of the width to height ratio for characters drawn using the GTX output primitive. CHXP of 10.0 would specify a character that is 10 times as wide as normal. CHXP of 0.1 would request characters that are 1/10th as wide as normal. The character height remains unchanged. CHXP &gt; 0. By default CHXP = 1.0</dl><h2>Access</h2>To use GKS routines, load the NCAR GKS-0A library ncarg_gks.
<h2>See Also</h2>Online: gtx, gstxp, gstxal, gstxfp, gschh, gschsp, gschup, gscr, gstxci, gqtxp, gqtxal, gqtxfp, gqchh, gqchsp, gqchup, gqchxp, plotchar, gset_char_expan 

 Hardcopy: User's Guide for NCAR GKS-0A Graphics; NCAR Graphics Fundamentals, UNIX Version
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
