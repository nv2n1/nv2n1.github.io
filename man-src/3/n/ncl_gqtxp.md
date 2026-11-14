---
title: "ncl_gqtxp(3)"
name: "ncl_gqtxp"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_gqtxp/"
---

GQTXP (Inquire text path) - retrieves the current text path.
<h2>Synopsis</h2>CALL GQTXP (ERRIND, TXP)
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/gks.h&gt; 

 void ginq_text_path(Gint *err_ind, Gtext_path *text_path);
<h2>Description</h2><dl COMPACT><dt>ERRIND
<dd>(Integer, Output) - If the inquired value cannot be returned correctly, a non-zero error indicator is returned in ERRIND, otherwise a zero is returned. Consult &quot;User's Guide for NCAR GKS-0A Graphics&quot; for a description of the meaning of the error indicators.
<dt>TXP
<dd>(Integer, Output) - Returns the current text path as set by default or by a call to GSTXP. Legal values are:
<dl COMPACT><dd><dl COMPACT><dt>0
<dd>Draw successive characters in the string such that character n+l appears to the right of character n. This is text path &quot;right&quot; and is the default.
<dt>1
<dd>Draw character n+1 to the left of character n. This is text path &quot;left&quot;.
<dt>2
<dd>Draw character n+1 above character n. This is text path &quot;up&quot;.
<dt>3
<dd>Draw character n+1 below character n. This is text path &quot;down&quot;.</dl></dl>
</dl><h2>Access</h2>To use GKS routines, load the NCAR GKS-0A library ncarg_gks.
<h2>See Also</h2>Online: gtx, gstxp, gstxal, gstxfp, gschh, gschsp, gschup, gschxp, gscr, gstxci, gqtxp, gqtxal, gqtxfp, gqchh, gqchsp, gqchup, gqchxp, plotchar, ginq_text_path 

 Hardcopy: User's Guide for NCAR GKS-0A Graphics; NCAR Graphics Fundamentals, UNIX Version
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
