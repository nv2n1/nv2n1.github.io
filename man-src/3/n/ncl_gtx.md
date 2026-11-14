---
title: "ncl_gtx(3)"
name: "ncl_gtx"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_gtx/"
---

GTX (Text) - The basic output primitive for drawing text. A number of attribute setting routines are available for selecting the size, font, precision, orientation, color, character spacing, etc.
<h2>Synopsis</h2>CALL GTX (X, Y, STRING)
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/gks.h&gt; 

 void gtext(const Gpoint *text_pos, const char *char_string);
<h2>Description</h2><dl COMPACT><dt>X
<dd>(Real, Input) - The X world coordinate of the text alignment of the first character in STRING.
<dt>Y
<dd>(Real, Input) - The Y world coordinate of the text alignment of the first character in STRING.
<dt>STRING
<dd>(Character variable, Input) - The characters to be drawn.</dl><h2>Access</h2>To use GKS routines, load the NCAR GKS-0A library ncarg_gks.
<h2>See Also</h2>Online: gstxp, gstxal, gstxfp, gschh, gschsp, gschup, gschxp, gscr, gstxci, gqtxp, gqtxal, gqtxfp, gqchh, gqchsp, gqchup, gqchxp, plotchar, gtext 

 Hardcopy: User's Guide for NCAR GKS-0A Graphics; NCAR Graphics Fundamentals, UNIX Version
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
