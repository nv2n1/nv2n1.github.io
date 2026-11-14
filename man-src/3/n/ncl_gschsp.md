---
title: "ncl_gschsp(3)"
name: "ncl_gschsp"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_gschsp/"
---

GSCHSP (Set character spacing) - sets the character spacing for text.
<h2>Synopsis</h2>CALL GSCHSP (CHSP)
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/gks.h&gt; 

 void gset_char_space(Gdouble char_space);
<h2>Description</h2><dl COMPACT><dt>CHSP
<dd>(Real, Input) - Specifies how much additional white space should be inserted between characters drawn using the GTX output primitive. CHSP is specified as a fraction of the character height. 

 A character spacing of zero positions the character body of each successive character contiguously with enough white space between them to produce pleasing normal spacing. A positive value inserts extra space between successive characters. A negative value causes successive characters to overlap. By default CHSP = 0.0.</dl><h2>Access</h2>To use GKS routines, load the NCAR GKS-0A library ncarg_gks.
<h2>See Also</h2>Online: gtx, gstxp, gstxal, gstxfp, gschh, gschup, gschxp, gscr, gstxci, gqtxp, gqtxal, gqtxfp, gqchh, gqchsp, gqchup, gqchxp, plotchar, gset_char_space 

 Hardcopy: User's Guide for NCAR GKS-0A Graphics; NCAR Graphics Fundamentals, UNIX Version
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
