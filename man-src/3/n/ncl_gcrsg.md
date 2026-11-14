---
title: "ncl_gcrsg(3)"
name: "ncl_gcrsg"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_gcrsg/"
---

GCRSG (Create segment) - creates a GKS segment.
<h2>Synopsis</h2>CALL GCRSG(SGNA)
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/gks.h&gt; 

 void gcreate_seg(Gint seg_name);
<h2>Description</h2><dl COMPACT><dt>SGNA
<dd>(Integer, Input) - Specifies the segment identifier that will be used in calls to subsequent segment functions applying to this segment. There can be a maximum of 100 segments in a given job step. Legal values for SGNA are integers between 0 and 99 inclusive.</dl><h2>Access</h2>To use GKS routines, load the NCAR GKS-0A library ncarg_gks.
<h2>See Also</h2>Online: gevtm, gactm, gclsg, gcsgwk, gdsg, gqopsg, gqsgus, gssgt., gcreate_seg 

 Hardcopy: &quot;User's Guide for NCAR GKS-0A Graphics&quot;
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
