---
title: "ncl_gclwk(3)"
name: "ncl_gclwk"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_gclwk/"
---

GCLWK (Close workstation) - closes a workstation.
<h2>Synopsis</h2>CALL GCLWK (WKID)
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/gks.h&gt; 

 void gclose_ws(Gint ws_id);
<h2>Description</h2><dl COMPACT><dt>WKID
<dd>(Input, Integer) - A number identifying the workstation to be closed. WKID must be the same as that used in some previous GOPWK call.</dl><h2>Usage</h2>Close workstation updates the workstation and removes its identifier from the set of open workstations. The connection to the workstation is released and the associated connection ID is available for re-use.
<h2>Access</h2>To use GKS routines, load the NCAR GKS-0A library ncarg_gks.
<h2>See Also</h2>Online: gopks, gopwk, gacwk, gdawk, gclks, opngks, clsgks, gclear_ws 

 Hardcopy: User's Guide for NCAR GKS-0A Graphics; NCAR Graphics Fundamentals, UNIX Version
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
