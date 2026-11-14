---
title: "ncl_gschh(3)"
name: "ncl_gschh"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_gschh/"
---

GSCHH (Set character height) - sets the character height for text.
<h2>Synopsis</h2>CALL GSCHH (CHH)
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/gks.h&gt; 

 void gset_char_ht(Gdouble char_ht);
<h2>Description</h2><dl COMPACT><dt>CHH
<dd>(Real, Input) - Gives the height in world coordinates at which a character is drawn using the GTX output primitive. CHH &gt; 0. By default CHH = 0.01.</dl><h2>Access</h2>To use GKS routines, load the NCAR GKS-0A library ncarg_gks.
<h2>See Also</h2>Online: gtx, gstxp, gstxal, gstxfp, gschsp, gschup, gschxp, gscr, gstxci, gqtxp, gqtxal, gqtxfp, gqchh, gqchsp, gqchup, gqchxp, plotchar, gset_char_ht 

 Hardcopy: User's Guide for NCAR GKS-0A Graphics; NCAR Graphics Fundamentals, UNIX Version
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
