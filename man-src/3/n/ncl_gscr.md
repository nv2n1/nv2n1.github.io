---
title: "ncl_gscr(3)"
name: "ncl_gscr"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_gscr/"
---

GSCR (Set color representation) - associates a color value with a color index.
<h2>Synopsis</h2>CALL GSCR (WKID, CI, CR, CG, CB)
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/gks.h&gt; 

 void gset_colr_rep(Gint ws_id, Gint colr_ind, const Gcolr_rep *colr_rep);
<h2>Description</h2><dl COMPACT><dt>WKID
<dd>(Integer, Input) - A workstation identifier. WKID must be the same as that used in some previous GOPWK call.
<dt>CI
<dd>(Integer, Input) - A color index.
<dt>CR
<dd>(Real, Input) - An intensity value for red between 0. and 1. inclusive.
<dt>CG
<dd>(Real, Input) - An intensity value for green between 0. and 1. inclusive.
<dt>CB
<dd>(Real, Input) - An intensity value for blue between 0. and 1. inclusive.</dl><h2>Usage</h2>Color in GKS is &quot;indexed&quot;, i.e. color attributes are assigned to primitives by using a color index. The GKS function GSCR is used to associate a color value with color indices. 

 It is recommended that all color indices used in a given job be defined prior to calling any output primitive. Since the result of a dynamic color change can be ambiguous, it is also recommended that GSCR not be called to change a color value after the original definitions. 

 GSCR may be called after opening the workstation for which the color indices are to be defined, and not before that workstation is opened. Different color tables can be maintained for different workstations. For example, color index 2 for a CGM file may be associated with &quot;red&quot; while at the same time it may be associated with &quot;green&quot; for some X workstation. 

 It is important to stress that color index 0 defines the background color. If any color indices are defined, then you should define the background color index 0. Otherwise you run the risk of having a user-defined color match the default background color. 

 For all GKS output primitives, color is assigned by an indexing scheme. The indices run from 0 to 255, where 0 is the background color index and 1 is the foreground color index.
<h2>Access</h2>To use GKS routines, load the NCAR GKS-0A library ncarg_gks.
<h2>See Also</h2>Online: gqcr, gsplci, gspmci, gsfaci, gstxci, gqplci, gqpmci, gqfaci, gqtxci, gset_colr_rep 

 Hardcopy: User's Guide for NCAR GKS-0A Graphics; NCAR Graphics Fundamentals, UNIX Version
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
