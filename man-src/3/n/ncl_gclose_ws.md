---
title: "ncl_gclose_ws(3)"
name: "ncl_gclose_ws"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_gclose_ws/"
description: "gclose_ws (Close workstation) – closes a workstation."
---

<p>gclose_ws (Close workstation) &#8211; closes a workstation.</p>
<h2>Synopsis</h2>
<p>#include &lt;ncarg/gks.h&gt; </p>
<p> void gclose_ws(Gint ws_id);</p>
<h2>Description</h2>
<dl COMPACT>
<dt>ws_id</p>
<dd>(Input) &#8211; A number identifying the workstation to be closed. ws_id must be the same as that used in some previous gopen_ws call.</dl>
<h2>Usage</h2>
<p>Close workstation updates the workstation and removes its identifier from the set of open workstations. The connection to the workstation is released and the associated connection ID is available for re-use.</p>
<h2>Access</h2>
<p>To use the GKS C-binding routines, load the ncarg_gks and ncarg_c libraries.</p>
<h2>See Also</h2>
<p>Online: <code>gopen_gks(3NCARG),</code> <code>gopen_ws(3NCARG),</code> <code>gactivate_ws(3NCARG),</code> <code>gdeactivate_ws(3NCARG),</code> <code>gclose_gks(3NCARG),</code> <code>opngks(3NCARG),</code> <code>clsgks(3NCARG),</code> <code>gks(3NCARG),</code> <code>ncarg_gks_cbind(3NCARG)</code> </p>
<p> Hardcopy: User&#8217;s Guide for NCAR GKS-0A Graphics; NCAR Graphics Fundamentals, UNIX Version</p>
<h2>Copyright</h2>
<p>Copyright (C) 1987-2009<br />
 University Corporation for Atmospheric Research<br />
 The use of this Software is governed by a License Agreement.</p>
