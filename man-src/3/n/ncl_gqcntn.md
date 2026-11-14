---
title: "ncl_gqcntn(3)"
name: "ncl_gqcntn"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_gqcntn/"
---

GQCNTN (Inquire current normalization transformation number) - retrieves the number of the current normalization transformation.
<h2>Synopsis</h2>CALL GQCNTN (ERRIND, CTNR)
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/gks.h&gt; 

 void ginq_cur_norm_tran_num(Gint *err_ind, Gint *norm_tran_num);
<h2>Description</h2><dl COMPACT><dt>ERRIND
<dd>(Integer, Output) - If the inquired value cannot be returned correctly, a non-zero error indicator is returned in ERRIND, otherwise a zero is returned. Consult &quot;User's Guide for NCAR GKS-0A Graphics&quot; for a description of the meaning of the error indicators.
<dt>CTNR
<dd>(Integer, Output) - Returns the current normalization transformation number as set by default or by a call to GSELNT.</dl><h2>Access</h2>To use GKS routines, load the NCAR GKS-0A library ncarg_gks.
<h2>See Also</h2>Online: gselnt, gqmntn, gqnt, getset, ginq_cur_norm_tran_num 

 Hardcopy: User's Guide for NCAR GKS-0A Graphics; NCAR Graphics Fundamentals, UNIX Version
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
