---
title: "ncl_gqopsg(3)"
name: "ncl_gqopsg"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_gqopsg/"
---

GQOPSG (Inquire name of open segment) - returns the name of the currently open segment.
<h2>Synopsis</h2>CALL GQOPSG(ERRIND,SGNA)
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/gks.h&gt; 

 void ginq_name_open_seg(Gint *err_ind, Gint *name_open_seg);
<h2>Description</h2><dl COMPACT><dt>ERRIND
<dd>(Integer, Output) - If the GKS state is SGOP (segment open), then ERRIND is returned as &quot;0&quot;; otherwise ERRIND is returned as &quot;4&quot;.
<dt>SGNA
<dd>(Integer, Output) - If the GKS state is SGOP (segment open), then SGNA is returned as the number of the currently open segment; otherwise SGNA is undefined.</dl><h2>Access</h2>To use GKS routines, load the NCAR GKS-0A library ncarg_gks.
<h2>See Also</h2>Online: gevtm, gactm, gclsg, gcrsg, gcsgwk, gdsg, gqsgus, gssgt., ginq_name_open_seg 

 Hardcopy: &quot;User's Guide for NCAR GKS-0A Graphics&quot;
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
