---
title: "ncl_gstxal(3)"
name: "ncl_gstxal"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_gstxal/"
---

GSTXAL (Set text alignment) - sets the text alignment.
<h2>Synopsis</h2>CALL GSTXAL (TXALH, TXALV)
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/gks.h&gt; 

 void gset_text_align(const Gtext_align *text_align);
<h2>Description</h2><dl COMPACT><dt>TXALH
<dd>(Integer, Input) - Determines the horizontal alignment of the text to be drawn. Options are:
<dl COMPACT><dd><dl COMPACT><dt>0
<dd>Normal (default)
<dt>1
<dd>Left
<dt>2
<dd>Center
<dt>3
<dd>Right</dl></dl><dt>TXALV
<dd>(Integer, Input) - Determines the vertical alignment of the text to be drawn. Options are:
<dl COMPACT><dd><dl COMPACT><dt>0
<dd>Normal (default)
<dt>1
<dd>Top
<dt>2
<dd>Cap
<dt>3
<dd>Half
<dt>4
<dd>Base
<dt>5
<dd>Bottom</dl></dl>
</dl><h2>Usage</h2>Text alignment is used to position the text extent rectangle. The text extent rectangle rotates about the point determined by the horizontal and vertical text alignment settings (TXALH, TXALV).
<h2>Access</h2>To use GKS routines, load the NCAR GKS-0A library ncarg_gks.
<h2>See Also</h2>Online: gtx, gstxp, gstxfp, gschh, gschsp, gschup, gschxp, gscr, gstxci, gqtxp, gqtxal, gqtxfp, gqchh, gqchsp, gqchup, gqchxp, plotchar, gset_text_align 

 Hardcopy: User's Guide for NCAR GKS-0A Graphics; NCAR Graphics Fundamentals, UNIX Version
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
