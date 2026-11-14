---
title: "ncl_gdeactivate_ws(3)"
name: "ncl_gdeactivate_ws"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_gdeactivate_ws/"
description: "gdeactivate_ws (Deactivate workstation) – deactivates a workstation."
---

<p>gdeactivate_ws (Deactivate workstation) &#8211; deactivates a workstation.</p>
<h2>Synopsis</h2>
<p>#include &lt;ncarg/gks.h&gt; </p>
<p> void gdeactivate_ws(Gint ws_id);</p>
<h2>Description</h2>
<dl COMPACT>
<dt>ws_id</p>
<dd>(Input) &#8211; A number identifying the workstation to be deactivated. ws_id must be the same as that used in some previous gactivate_ws call.</dl>
<h2>Usage</h2>
<p>The specified workstation is removed from the set of active workstations. GKS output primitives are not sent to workstations that are not active.</p>
<h2>Access</h2>
<p>To use the GKS C-binding routines, load the ncarg_gks and ncarg_c libraries.</p>
<h2>See Also</h2>
<p>Online: <code>gopen_gks(3NCARG),</code> <code>gopen_ws(3NCARG),</code> <code>gactivate_ws(3NCARG),</code> <code>gclose_ws(3NCARG),</code> <code>gclose_gks(3NCARG),</code> <code>opngks(3NCARG),</code> <code>clsgks(3NCARG),</code> <code>gks(3NCARG),</code> <code>ncarg_gks_cbind(3NCARG)</code> </p>
<p> Hardcopy: User&#8217;s Guide for NCAR GKS-0A Graphics; NCAR Graphics Fundamentals, UNIX Version</p>
<h2>Copyright</h2>
<p>Copyright (C) 1987-2009<br />
 University Corporation for Atmospheric Research<br />
 The use of this Software is governed by a License Agreement.</p>
