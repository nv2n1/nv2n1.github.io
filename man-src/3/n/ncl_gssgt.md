---
title: "ncl_gssgt(3)"
name: "ncl_gssgt"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_gssgt/"
---

GSSGT (Set segment transformation) - Associates a segment transformation with a named segment.
<h2>Synopsis</h2>CALL GSSGT(SGNA,M)
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/gks.h&gt; 

 void gset_seg_tran(Gint seg_name, const Gtran_matrix tran_matrix);
<h2>Description</h2><dl COMPACT><dt>SGNA
<dd>(Integer, Input) - A segment name as used in a previous GCRSG call.
<dt>M
<dd>(Real, Input) - A 2x3 array giving the GKS segment transformation to be associated with the segment specified in SGNA.</dl><h2>Usage</h2>When the segment named in SGNA is displayed, the coordinates of its primitives are transformed by the matrix specified in M. 

<h2>Access</h2>To use GKS routines, load the NCAR GKS-0A library ncarg_gks.
<h2>See Also</h2>Online: gactm, gevtm, gclsg, gcrsg, gcsgwk, gdsg, gqopsg, gqsgus., gset_seg_tran 

 Hardcopy: &quot;User's Guide for NCAR GKS-0A Graphics&quot;
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
