---
title: "ncl_gupd_ws(3)"
name: "ncl_gupd_ws"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_gupd_ws/"
description: "gupd_ws (Update workstation) – Insures that the workstation is current and reflects all requests that have been made."
---

<p>gupd_ws (Update workstation) &#8211; Insures that the workstation is current and reflects all requests that have been made.</p>
<h2>Synopsis</h2>
<p>#include &lt;ncarg/gks.h&gt; </p>
<p> void gupd_ws(Gint ws_id, Gupd_regen_flag upd_regen_flag);</p>
<h2>Description</h2>
<dl COMPACT>
<dt>ws_id</p>
<dd>(Input) A number identifying the workstation to be updated. ws_id must be the same as that used in some previous gopen_ws call.</p>
<dt>upd_regen_flag</p>
<dd>(Input) A flag to specify if the current picture should be regenerated. The possible values include:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>GUPD_NOT_PEND</p>
<dd>Postpone</p>
<dt>GUPD_PEND</p>
<dd>Perform</dl>
</dl>
<p> For the workstation types supported in NCAR GKS, this flag should always be set to GUPD_PEND.</dl>
<h2>Usage</h2>
<p>A call to gupd_ws flushes all buffers to bring the workstation up to date.</p>
<h2>Access</h2>
<p>To use the GKS C-binding routines, load the ncarg_gks, and ncarg_c libraries.</p>
<h2>See Also</h2>
<p>Online: <code>sflush(3NCARG),</code> <code>plotif(3NCARG),</code> <code>gks(3NCARG),</code> <code>ncarg_gks_cbind(3NCARG)</code> </p>
<p> Hardcopy: User&#8217;s Guide for NCAR GKS-0A Graphics; NCAR Graphics Fundamentals, UNIX Version</p>
<h2>Copyright</h2>
<p>Copyright (C) 1987-2009<br />
 University Corporation for Atmospheric Research<br />
 The use of this Software is governed by a License Agreement.</p>
