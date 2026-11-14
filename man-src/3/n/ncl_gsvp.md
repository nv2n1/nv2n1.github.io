---
title: "ncl_gsvp(3)"
name: "ncl_gsvp"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_gsvp/"
---

GSVP (Set viewport) - establishes a rectangular subspace of normalized device coordinates space. Calls to GSVP are discouraged with NCAR Graphics. Instead, use the SET subroutine because SET also supports mirror imaging and log scaling of axes.
<h2>Synopsis</h2>CALL GSVP (TRNUM, XMIN, XMAX, YMIN, YMAX)
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/gks.h&gt; 

 void gset_vp(Gint tran_num, const Glimit *vp_limits);
<h2>Description</h2><dl COMPACT><dt>TRNUM
<dd>(Integer, Input) - A normalization transformation number. The number of available transformations is implementation specific. In the case of NCAR GKS-0A, two normalization transformations are provided:
<dl COMPACT><dd><dl COMPACT><dt>0
<dd>Selects the identity transformation in which both the window and viewport have the range of 0. to 1. in both coordinate directions. This is the default normalization transformation for GKS. It is also fixed within GKS; that is, it is illegal to call GSVP with TRNUM = 0.
<dt>1
<dd>A normalization transformation in which the viewport is defined by XMIN to XMAX and YMIN to YMAX.</dl></dl><dt>XMIN
<dd>(Real, Input) - The left horizontal coordinate of the viewport.
<dt>XMAX
<dd>(Real, Input) - The right horizontal coordinate of the viewport. 0. &le; XMIN &lt; XMAX &le; 1.
<dt>YMIN
<dd>(Real, Input) - The bottom vertical coordinate of the viewport.
<dt>YMAX
<dd>(Real, Input) - The top vertical coordinate of the viewport. 0. &le; YMIN &lt; YMAX &le; 1.
<dt>Defaults:
<dd>TRNUM = 0, XMIN = 0.0, XMAX = 1.0, YMIN = 0.0, YMAX = 1.0</dl><h2>Access</h2>To use GKS routines, load the NCAR GKS-0A library ncarg_gks.
<h2>See Also</h2>Online: set, gswn, gselnt, gqclip, gset_vp 

 Hardcopy: NCAR Graphics Fundamentals, UNIX Version; User's Guide for NCAR GKS-0A Graphics
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
