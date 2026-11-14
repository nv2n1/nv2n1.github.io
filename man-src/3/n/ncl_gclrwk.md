---
title: "ncl_gclrwk(3)"
name: "ncl_gclrwk"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_gclrwk/"
---

GCLRWK (Clear workstation) - clears a workstation.
<h2>Synopsis</h2>CALL GCLRWK (WKID, COFL)
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/gks.h&gt; 

 void gclear_ws(Gint ws_id, Gctrl_flag ctrl_flag);
<h2>Description</h2><dl COMPACT><dt>WKID
<dd>(Integer, Input) - A number identifying the workstation to be cleared. WKID must be the same as that used in some previous GOPWK call.
<dt>COFL
<dd>(Integer, Input) - Clear the workstation display surface. Options are:
<dl COMPACT><dd><dl COMPACT><dt>0
<dd>Check to see if the display surface is empty. If so, do not issue a clear surface command.
<dt>1
<dd>Issue a clear surface command whether the surface has been written to or not.</dl></dl>
</dl><h2>Usage</h2>For workstations of type &quot;1&quot; (CGM), GCLRWK is interpreted as a picture termination in CGM generation. If COFL = 0 and no output primitives have been written in the current picture, then a call to GCLRWK is a &quot;do nothing&quot;; otherwise, it generates an END PICTURE element (as well as other picture initializing elements). If COFL = 1, then a call to GCLRWK generates an END PICTURE. 

 For workstations of types &quot;7&quot; or &quot;8&quot; (see the man page for GOPWK for a description of workstation types) clear workstations erases all primitives that appear on the screen. 

 For all other workstation types, clear workstation simply updates the workstation.
<h2>Access</h2>To use GKS routines, load the NCAR GKS-0A library ncarg_gks.
<h2>See Also</h2>Online: gopwk, gacwk, gdawk, gclwk, gclear_ws 

 Hardcopy: User's Guide for NCAR GKS-0A Graphics; NCAR Graphics Fundamentals, UNIX Version
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
