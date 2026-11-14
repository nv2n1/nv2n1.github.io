---
title: "ncl_gclsg(3)"
name: "ncl_gclsg"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_gclsg/"
---

GCLSG (Close segment) - closes a GKS segment.
<h2>Synopsis</h2>CALL GCLSG
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/gks.h&gt; 

 void gclose_seg( void );
<h2>Usage</h2>A call to GCLSG closes the currently open segment (graphics output primitives will no longer be stored in that segment). GCLSG can be called only if a segment is open.
<h2>Access</h2>To use GKS routines, load the NCAR GKS-0A library ncarg_gks.
<h2>See Also</h2>Online: gevtm, gactm, gcrsg, gcsgwk, gdsg, gqopsg, gqsgus, gssgt, gclose_seg 

 Hardcopy: &quot;User's Guide for NCAR GKS-0A Graphics&quot;
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
