---
title: "ncl_gselnt(3)"
name: "ncl_gselnt"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_gselnt/"
---

GSELNT (Select normalization transformation) - selects a predefined or user-defined transformation that maps world coordinates to normalized device coordinates.
<h2>Synopsis</h2>CALL GSELNT (TRNUM)
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/gks.h&gt; 

 void gsel_norm_tran(Gint tran_num);
<h2>Description</h2><dl COMPACT><dt>TRNUM
<dd>(Integer, Input) - A normalization transformation number. The number of available transformations is implementation specific. In the case of NCAR GKS-0A, two normalization transformations are provided: 

<dl COMPACT><dd><dl COMPACT><dt>0
<dd>Selects the identity transformation in which both the window and viewport have the range of 0. to 1. in both coordinate directions. This is the default. 

<dt>1
<dd>Selects a normalization transformation in which the window and viewport have been defined by calls to GSWN and GSVP.</dl></dl>
</dl><h2>Usage</h2>When a normalization transformation is selected, all world coordinate arguments to GKS functions are transformed by it.
<h2>Access</h2>To use GKS routines, load the NCAR GKS-0A library ncarg_gks.
<h2>See Also</h2>Online: set, gsup, gswn, gqclip, gsel_norm_tran 

 Hardcopy: NCAR Graphics Fundamentals, UNIX Version; User's Guide for NCAR GKS-0A Graphics
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
