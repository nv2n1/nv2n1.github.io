---
title: "ncl_gqmntn(3)"
name: "ncl_gqmntn"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_gqmntn/"
---

GQMNTN (Inquire maximum normalization transformation number) - retrieves the maximum number of supported normalization transformations.
<h2>Synopsis</h2>CALL GQMNTN (ERRIND, MAXTRN)
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/gks.h&gt; 

 void ginq_max_norm_tran_num(Gint *err_ind, Gint *max_norm_tran_num);
<h2>Description</h2><dl COMPACT><dt>ERRIND
<dd>(Integer, Output) - If the inquired value cannot be returned correctly, a non-zero error indicator is returned in ERRIND, otherwise a zero is returned. Consult &quot;User's Guide for NCAR GKS-0A Graphics&quot; for a description of the meaning of the error indicators.
<dt>MAXTRN
<dd>(Integer, Output) - Gives the maximum number of normalization transformations available in the GKS package. In NCAR GKS-0A, MAXTRN = 2.</dl><h2>Access</h2>To use GKS routines, load the NCAR GKS-0A library ncarg_gks.
<h2>See Also</h2>Online: gselnt, gqcntn, gqnt, getset, ginq_max_norm_tran_num 

 Hardcopy: &quot;User's Guide for NCAR GKS-0A Graphics&quot;
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
