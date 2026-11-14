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
<dd>(Integer, Output) - If the inquired values cannot be returned correctly, a non-zero error indicator is returned in ERRIND, otherwise a zero is returned. Consult &quot;User's Guide for NCAR GKS-0A Graphics&quot; for a description of the meaning of the error indicators.
<dt>TXALH
<dd>(Real, Output) - Returns the current horizontal text alignment:
<dl COMPACT><dd><dl COMPACT><dt>0
<dd>Normal (default)
<dt>1
<dd>Left
<dt>2
<dd>Center
<dt>3
<dd>Right</dl></dl><dt>TXALV
<dd>(Real, Output) - Returns the current vertical text alignment:
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
</dl><h2>Access</h2>To use GKS routines, load the NCAR GKS-0A library ncarg_gks.
<h2>See Also</h2>Online: gtx, gstxp, gstxal, gstxfp, gschh, gschsp, gschup, gschxp, gscr, gstxci, gqtxp, gqtxal, gqtxfp, gqchh, gqchsp, gqchup, gqchxp, plotchar, ngdots, ginq_text_align 

 Hardcopy: User's Guide for NCAR GKS-0A Graphics; NCAR Graphics Fundamentals, UNIX Version
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
