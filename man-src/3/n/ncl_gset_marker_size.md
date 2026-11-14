---
title: "ncl_gset_marker_size(3)"
name: "ncl_gset_marker_size"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_gset_marker_size/"
description: "gset_marker_size (Set marker size scale factor) – sets the polymarker size scale factor — the relative size of the marker."
---

<p>gset_marker_size (Set marker size scale factor) &#8211; sets the polymarker size scale factor &#8212; the relative size of the marker.</p>
<h2>Synopsis</h2>
<p>#include &lt;ncarg/gks.h&gt; </p>
<p> void gset_marker_size(Gdouble marker_size);</p>
<h2>Description</h2>
<dl COMPACT>
<dt>marker_size</p>
<dd>(Input) A scale factor to control the size of the marker. It must be greater than or equal to 0. Since marker_size = 1.0 by default, setting marker_size = 2.0 doubles polymarker size.</dl>
<h2>Access</h2>
<p>To use the GKS C-binding routines, load the ncarg_gks and ncarg_c libraries.</p>
<h2>See Also</h2>
<p>Online: <code>gpolymarker(3NCARG),</code> <code>gset_marker_type(3NCARG),</code> <code>gset_colr_rep(3NCARG),</code> <code>gset_marker_colr_ind(3NCARG),</code> <code>ginq_marker_type(3NCARG),</code> <code>ginq_marker_size(3NCARG),</code> <code>ginq_marker_colr_ind(3NCARG),</code> <code>point(3NCARG),</code> <code>points(3NCARG),</code> <code>gks(3NCARG),</code> <code>ncarg_gks_cbind(3NCARG)</code> </p>
<p> Hardcopy: User&#8217;s Guide for NCAR GKS-0A Graphics; NCAR Graphics Fundamentals, UNIX Version</p>
<h2>Copyright</h2>
<p>Copyright (C) 1987-2009<br />
 University Corporation for Atmospheric Research<br />
 The use of this Software is governed by a License Agreement.</p>
