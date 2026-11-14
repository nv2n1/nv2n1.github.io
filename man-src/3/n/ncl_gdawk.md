---
title: "ncl_gdawk(3)"
name: "ncl_gdawk"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_gdawk/"
---

GDAWK (Deactivate workstation) - deactivates a workstation.
<h2>Synopsis</h2>CALL GDAWK (WKID)
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/gks.h&gt; 

 void gdeactivate_ws(Gint ws_id);
<h2>Description</h2><dl COMPACT><dt>WKID
<dd>(Integer, Input) - A number identifying the workstation to be deactivated. WKID must be the same as that used in some previous GACWK call.</dl><h2>Usage</h2>The specified workstation is removed from the set of active workstations. GKS output primitives are not sent to workstations that are not active.
<h2>Access</h2>To use GKS routines, load the NCAR GKS-0A library ncarg_gks.
<h2>See Also</h2>Online: gopks, gopwk, gacwk, gclwk, gclks, opngks, clsgks, gdeactivate_ws 

 Hardcopy: User's Guide for NCAR GKS-0A Graphics; NCAR Graphics Fundamentals, UNIX Version
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
