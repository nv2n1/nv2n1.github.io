---
title: "ncl_frame(3)"
name: "ncl_frame"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_frame/"
---

FRAME - advances to the next picture (in the case of CGM output), or pauses in the window of most recent creation (for X11 output). A mouse or key click in the window on pause will cause all active workstations to be cleared. 

<h2>Synopsis</h2>CALL FRAME
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/ncargC.h&gt; 

 void c_frame()
<h2>Usage</h2>If a CGM workstation is open, a call to routine FRAME causes an END_PICTURE CGM element to be generated. If there are open X windows, it updates all workstations and pauses in the window of most recent creation. After a mouse click or a key click in the window on pause, all workstations are cleared. 

 FRAME is most applicable to an environment with a single active workstation. When multiple workstations are used, the more versatile NGPICT routine should be considered. NGPICT includes the option of issuing a &quot;&lt;READY&gt;&quot; prompt when a window is on pause. 

 To use NGPICT to replace routine FRAME for a single CGM workstation use: CALL NGPICT(WKID,1), where WKID is the workstation ID for the metafile and the second argument flags a CLEAR WORKSTATION.
<h2>Examples</h2>Use the ncargex command to see the following relevant examples: agex06
<h2>Access</h2>To use FRAME or c_frame, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.
<h2>See Also</h2>Online: sflush, ngpict, spps, spps_params, ncarg_cbind 

 Hardcopy: NCAR Graphics Fundamentals, UNIX Version; User's Guide for NCAR GKS-0A Graphics
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
