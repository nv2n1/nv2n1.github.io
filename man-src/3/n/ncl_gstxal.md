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
</dt><dd>(Integer, Input) - Determines the horizontal alignment of the text to be drawn. Options are:
</dd><dl COMPACT><dd></dd><dl COMPACT><dt>0
</dt><dd>Normal (default)
</dd><dt>1
</dt><dd>Left
</dd><dt>2
</dt><dd>Center
</dd><dt>3
</dt><dd>Right</dd></dl></dl><dt>TXALV
</dt><dd>(Integer, Input) - Determines the vertical alignment of the text to be drawn. Options are:
</dd><dl COMPACT><dd></dd><dl COMPACT><dt>0
</dt><dd>Normal (default)
</dd><dt>1
</dt><dd>Top
</dd><dt>2
</dt><dd>Cap
</dd><dt>3
</dt><dd>Half
</dd><dt>4
</dt><dd>Base
</dd><dt>5
</dt><dd>Bottom</dd></dl></dl>
</dl><h2>Usage</h2>Text alignment is used to position the text extent rectangle. The text extent rectangle rotates about the point determined by the horizontal and vertical text alignment settings (TXALH, TXALV).
<h2>Access</h2>To use GKS routines, load the NCAR GKS-0A library ncarg_gks.
<h2>See Also</h2>Online: gtx, gstxp, gstxfp, gschh, gschsp, gschup, gschxp, gscr, gstxci, gqtxp, gqtxal, gqtxfp, gqchh, gqchsp, gqchup, gqchxp, plotchar, gset_text_align 

 Hardcopy: User's Guide for NCAR GKS-0A Graphics; NCAR Graphics Fundamentals, UNIX Version
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
