---
title: "ncl_gdsg(3)"
name: "ncl_gdsg"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_gdsg/"
---

GDSG (Delete segment) - deletes a GKS segment.
<h2>Synopsis</h2>CALL GDSG(SGNA)
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/gks.h&gt; 

 void gdel_seg(Gint seg_name);
<h2>Description</h2><dl COMPACT><dt>SGNA
<dd>(Integer, Input) - Specifies the segment identifier for a segment that will be deleted by a call to this function.</dl><h2>Usage</h2>The segment name is removed from the set of names of segments that are currently in use.
<h2>Access</h2>To use GKS routines, load the NCAR GKS-0A library ncarg_gks.
<h2>See Also</h2>Online: gevtm, gactm, gclsg, gcrsg, gcsgwk, gqopsg, gqsgus, gssgt., gdel_seg 

 Hardcopy: &quot;User's Guide for NCAR GKS-0A Graphics&quot;
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
