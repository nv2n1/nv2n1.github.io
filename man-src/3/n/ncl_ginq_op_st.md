---
title: "ncl_ginq_op_st(3)"
name: "ncl_ginq_op_st"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_ginq_op_st/"
description: "ginq_op_st (Inquire operating state value) – returns the operating state of GKS."
---

<p>ginq_op_st (Inquire operating state value) &#8211; returns the operating state of GKS.</p>
<h2>Synopsis</h2>
<p>#include &lt;ncarg/gks.h&gt; </p>
<p> void ginq_op_st(Gop_st *op_st);</p>
<h2>Description</h2>
<dl COMPACT>
<dt>op_st</p>
<dd>(Output) &#8211; Returns the GKS operating state:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>GST_GKCL</p>
<dd>GKS is closed</p>
<dt>GST_GKOP</p>
<dd>GKS is open</p>
<dt>GST_WSOP</p>
<dd>Additionally, a workstation is open</p>
<dt>GST_WSAC</p>
<dd>Additionally, a workstation is active</p>
<dt>GST_SGOP</p>
<dd>Additionally, a segment is open</dl>
</dl>
</dl>
<h2>Access</h2>
<p>To use the GKS C-binding routines, load the ncarg_gks and ncarg_c libraries.</p>
<h2>See Also</h2>
<p>Online: <code>gopen_gks(3NCARG),</code> <code>gopen_ws(3NCARG),</code> <code>gactivate_ws(3NCARG),</code> <code>gdeactivate_ws(3NCARG),</code> <code>gclose_ws(3NCARG),</code> <code>gclose_gks(3NCARG),</code> <code>opngks(3NCARG),</code> <code>clsgks(3NCARG),</code> <code>gks(3NCARG),</code> <code>ncarg_gks_cbind(3NCARG)</code> </p>
<p> Hardcopy: User&#8217;s Guide for NCAR GKS-0A Graphics; NCAR Graphics Fundamentals, UNIX Version</p>
<h2>Copyright</h2>
<p>Copyright (C) 1987-2009<br />
 University Corporation for Atmospheric Research<br />
 The use of this Software is governed by a License Agreement.</p>
