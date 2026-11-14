---
title: "ncl_gopen_gks(3)"
name: "ncl_gopen_gks"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_gopen_gks/"
description: "gopen_gks (Open GKS) – opens the GKS package"
---

<p>gopen_gks (Open GKS) &#8211; opens the GKS package</p>
<h2>Synopsis</h2>
<p>#include &lt;ncarg/gks.h&gt; </p>
<p> void gopen_gks(const char *err_file, size_t mem_unit);</p>
<h2>Description</h2>
<dl COMPACT>
<dt>err_file</p>
<dd>(Input) &#8211; The place to which error messages are to be written. Typically this should be &quot;stdout&quot;.</p>
<dt>mem_unit</p>
<dd>(Input) &#8211; The dimension of an internal buffer. Currently in NCAR GKS-0A, mem_unit is ignored.</dl>
<h2>Usage</h2>
<p>To get output to any workstation, gopen_gks, gopen_ws and gactivate_ws must be called in that order. For jobs producing only CGM output, the three calls to gopen_gks, gopen_ws, and gactivate_ws can be replaced with a call to the SPPS function c_opngks().</p>
<h2>Access</h2>
<p>To use the GKS C-binding routines, load the ncarg_gks and ncarg_c libraries.</p>
<h2>See Also</h2>
<p>Online: <code>gopen_ws(3NCARG),</code> <code>gactivate_ws(3NCARG),</code> <code>gdeactivate_ws(3NCARG),</code> <code>gclose_ws(3NCARG),</code> <code>gclose_gks(3NCARG),</code> <code>gupd_ws(3NCARG),</code> <code>opngks(3NCARG),</code> <code>clsgks(3NCARG),</code> <code>gks(3NCARG),</code> <code>ncarg_gks_cbind(3NCARG)</code> </p>
<p> Hardcopy: User&#8217;s Guide for NCAR GKS-0A Graphics; NCAR Graphics Fundamentals, UNIX Version</p>
<h2>Copyright</h2>
<p>Copyright (C) 1987-2009<br />
 University Corporation for Atmospheric Research<br />
 The use of this Software is governed by a License Agreement.</p>
