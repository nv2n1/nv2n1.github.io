---
title: "ncl_gqtxal(3)"
name: "ncl_gqtxal"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_gqtxal/"
---

GQTXAL (Inquire text alignment) - retrieves the horizontal and vertical text alignments.
<h2>Synopsis</h2>CALL GQTXAL (ERRIND, TXALH, TXALV)
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/gks.h&gt; 

 void ginq_text_align(Gint *err_ind, Gtext_align *text_align);
<h2>Description</h2><dl COMPACT><dt>ERRIND
</dt><dd>(Integer, Output) - If the inquired values cannot be returned correctly, a non-zero error indicator is returned in ERRIND, otherwise a zero is returned. Consult &quot;User's Guide for NCAR GKS-0A Graphics&quot; for a description of the meaning of the error indicators.
</dd><dt>TXALH
</dt><dd>(Real, Output) - Returns the current horizontal text alignment:
</dd><dl COMPACT><dd></dd><dl COMPACT><dt>0
</dt><dd>Normal (default)
</dd><dt>1
</dt><dd>Left
</dd><dt>2
</dt><dd>Center
</dd><dt>3
</dt><dd>Right</dd></dl></dl><dt>TXALV
</dt><dd>(Real, Output) - Returns the current vertical text alignment:
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
</dl><h2>Access</h2>To use GKS routines, load the NCAR GKS-0A library ncarg_gks.
<h2>See Also</h2>Online: gtx, gstxp, gstxal, gstxfp, gschh, gschsp, gschup, gschxp, gscr, gstxci, gqtxp, gqtxal, gqtxfp, gqchh, gqchsp, gqchup, gqchxp, plotchar, ngdots, ginq_text_align 

 Hardcopy: User's Guide for NCAR GKS-0A Graphics; NCAR Graphics Fundamentals, UNIX Version
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
