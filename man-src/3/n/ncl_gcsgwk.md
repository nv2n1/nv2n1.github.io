---
title: "ncl_gcsgwk(3)"
name: "ncl_gcsgwk"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_gcsgwk/"
---

GCSGWK (Copy segment to workstation) - copies a GKS segment to a GKS workstation.
<h2>Synopsis</h2>CALL GCSGWK(WKID,SGNA)
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/gks.h&gt; 

 void gcopy_seg_ws(Gint ws_id, Gint seg_name);
<h2>Description</h2><dl COMPACT><dt>WKID
<dd>(Integer, Input) - Specifies the workstation identifier (as defined in a GOPWK call) that is to receive the segment copy.
<dt>SGNA
<dd>(Integer, Input) - Identifies the segment that is to be copied to the specified workstation. SGNA must have been used in a previous call to GCRSG.</dl><h2>Access</h2>To use GKS routines, load the NCAR GKS-0A library ncarg_gks.
<h2>See Also</h2>Online: gevtm, gactm, gclsg, gcrsg, gdsg, gqopsg, gqsgus, gssgt., gcopy_seg_ws 

 Hardcopy: &quot;User's Guide for NCAR GKS-0A Graphics&quot;
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
