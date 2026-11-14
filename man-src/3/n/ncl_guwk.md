---
title: "ncl_guwk(3)"
name: "ncl_guwk"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_guwk/"
---

GUWK (Update workstation) - Insures that the workstation is current and reflects all requests that have been made.
<h2>Synopsis</h2>CALL GUWK(WKID,REGFL)
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/gks.h&gt; 

 void gupd_ws(Gint ws_id, Gupd_regen_flag upd_regen_flag);
<h2>Description</h2><dl COMPACT><dt>WKID
<dd>(Integer, Input) - A number identifying the workstation to be updated. WKID must be the same as that used in some previous GOPWK call.
<dt>REGFL
<dd>(Integer, Input) - A flag to specify if the current picture should be regenerated. The possible values for this are &quot;0&quot; for postpone, and &quot;1&quot; for perform. For the workstation types supported in NCAR GKS, this flag should always be set to &quot;0&quot;.</dl><h2>Usage</h2>A call to GUWK flushes all GKS buffers to bring the workstation up to date. GUWK does not flush any NCAR Graphics buffers that sit above GKS such as the pen-move buffer in SPPS (see the man page for plotif).
<h2>Access</h2>To use GKS routines, load the NCAR GKS-0A library ncarg_gks.
<h2>See Also</h2>Online: sflush, plotif, gupd_ws 

 Hardcopy: User's Guide for NCAR GKS-0A Graphics; NCAR Graphics Fundamentals, UNIX Version
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
