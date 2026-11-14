---
title: "ncl_gqsgus(3)"
name: "ncl_gqsgus"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_gqsgus/"
---

GQSGUS (Inquire set of segment names in use) - Retrieves what segment names are currently in use.
<h2>Synopsis</h2>CALL GQSGUS(N,ERRIND,OL,SGNA)
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/gks.h&gt; 

 void ginq_set_seg_names(Gint num_elems_appl_list, Gint start_pos, Gint *err_ind, Gint_list *seg_names, Gint *length_list);
<h2>Description</h2><dl COMPACT><dt>N
<dd>(Integer, Input) - The set member requested.
<dt>ERRIND
<dd>(Integer, Output) - If the GKS state is WSOP (workstation open), WSAC (workstation active), or SGOP (segment open), then ERRIND is returned as &quot;0&quot;; otherwise ERRIND is returned as &quot;7&quot;.
<dt>OL
<dd>(Integer, Output) - The number of segment names that are currently in use.
<dt>SGNA
<dd>(Integer, Output) - If the GKS state is WSOP (workstation open), WSAC (workstation active), or SGOP (segment open), and if OL is larger than zero, then SGNA is returned as the name in the Nth element of the list of segment names that are currently in use; otherwise SGNA is undefined.</dl><h2>Usage</h2>For NCAR GKS, segment names are integers between 0 and 99 inclusive (see the man page for GCRSG). 

 If one wants to obtain a list of all segment names that are currently in use, then the procedure usually is first to determines the number of segment names currently in use by making an initial call to GQSGUS with first argument of &quot;1&quot;. If ERRIND is returned as &quot;0&quot;, then OL will tell you how many segments are currently in use. Then, to get the list of all segment names currently in use, call GQSGUS in a loop on N from 1 to OL and retrieve the N values of SGNA returned from such calls.
<h2>Access</h2>To use GKS routines, load the NCAR GKS-0A library ncarg_gks.
<h2>See Also</h2>Online: gevtm, gactm, gclsg, gcrsg, gcsgwk, gqopsg, gdsg, gssgt., ginq_set_seg_names 

 Hardcopy: &quot;User's Guide for NCAR GKS-0A Graphics&quot;
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
