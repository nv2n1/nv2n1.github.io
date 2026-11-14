---
title: "ncl_gacwk(3)"
name: "ncl_gacwk"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_gacwk/"
---

GACWK (Activate workstation) - activates a GKS workstation.
<h2>Synopsis</h2>CALL GACWK (WKID)
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/gks.h&gt; 

 void gactivate_ws(Gint ws_id);
<h2>Description</h2><dl COMPACT><dt>WKID
<dd>(Integer, Input) - A number identifying the workstation to be activated. WKID must be the same as that used in some previous GOPWK call.</dl><h2>Usage</h2>Active workstations receive all GKS output primitives.
<h2>Access</h2>To use GKS routines, load the NCAR GKS-0A library ncarg_gks.
<h2>See Also</h2>Online: gopks, gopwk, gdawk, gclwk, gclks, opngks, clsgks, gactivate_ws 

 Hardcopy: User's Guide for NCAR GKS-0A Graphics; NCAR Graphics Fundamentals, UNIX Version
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
