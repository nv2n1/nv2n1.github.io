---
title: "ncl_gqcr(3)"
name: "ncl_gqcr"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_gqcr/"
---

GQCR (Inquire color representation) - retrieves the color value associated with a color index on a particular workstation.
<h2>Synopsis</h2>CALL GQCR (WKID, CI, TYPE, ERRIND, CR, CG, CB)
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/gks.h&gt; 

 void ginq_colr_rep(Gint ws_id, Gint colr_ind, Ginq_type type, Gint *err_ind, Gcolr_rep *colr_rep);
<h2>Description</h2><dl COMPACT><dt>WKID
<dd>(Integer, Input) - Gives a workstation identifier as was set in a previous call to GOPWK.
<dt>CI
<dd>(Integer, Input) - A color index.
<dt>TYPE
<dd>(Integer, Input) - Specifies whether the returned color values are the ones that were specified by a call to GSCR or whether they are the color values that are actually being used on the specified workstation (frequently a workstation will not be able to represent a requested color value precisely).
<dl COMPACT><dd><dl COMPACT><dt>0
<dd>Returns the color value set for index CI either by default or by a call to GSCR.
<dt>1
<dd>Returns the color value actually used by the workstation to represent the requested color.</dl></dl><dt>ERRIND
<dd>(Integer, Output) - If the inquired values cannot be returned correctly, a non-zero error indicator is returned in ERRIND, otherwise a zero is returned. Consult &quot;User's Guide for NCAR GKS-0A Graphics&quot; for a description of the meaning of the error indicators.
<dt>CR
<dd>(Real, Output) - Returns an intensity value for red in the range 0. to 1. inclusive.
<dt>CG
<dd>(Real, Output) - Returns an intensity value for green in the range 0. to 1. inclusive.
<dt>CB
<dd>(Real, Output) - Returns an intensity value for blue in the range 0. to 1. inclusive.</dl><h2>Usage</h2>For details on setting and using color indices see the man page for GSCR.
<h2>Access</h2>To use GKS routines, load the NCAR GKS-0A library ncarg_gks.
<h2>See Also</h2>Online: gscr, gsplci, gsmkci, gstxci, gsfaci, ginq_colr_rep 

 Hardcopy: User's Guide for NCAR GKS-0A Graphics; NCAR Graphics Fundamentals, UNIX Version
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
