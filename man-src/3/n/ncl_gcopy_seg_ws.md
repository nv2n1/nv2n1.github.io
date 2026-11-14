---
title: "ncl_gcopy_seg_ws(3)"
name: "ncl_gcopy_seg_ws"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_gcopy_seg_ws/"
description: "gcopy_seg_ws (Copy segment to workstation) – copies a GKS segment to a GKS workstation."
---

<p>gcopy_seg_ws (Copy segment to workstation) &#8211; copies a GKS segment to a GKS workstation.</p>
<h2>Synopsis</h2>
<p>#include &lt;ncarg/gks.h&gt; </p>
<p> void gcopy_seg_ws(Gint ws_id, Gint seg_name);</p>
<h2>Description</h2>
<dl COMPACT>
<dt>ws_id</p>
<dd>(Input) &#8211; Specifies the workstation identifier (as defined in a gopen_ws call) that is to receive the segment copy.</p>
<dt>seg_name</p>
<dd>(Input) &#8211; Identifies the segment that is to be copied to the specified workstation. seg_name must have been used in a previous call to gcreate_seg.</dl>
<h2>Access</h2>
<p>To use the GKS C-binding routines, load the ncarg_gks and ncarg_c libraries.</p>
<h2>See Also</h2>
<p>Online: <code>geval_tran_matrix(3NCARG),</code> <code>gaccum_tran_matrix(3NCARG),</code> <code>gclose_seg(3NCARG),</code> <code>gcreate_seg(3NCARG),</code> <code>gdel_seg(3NCARG),</code> <code>ginq_name_open_seg(3NCARG),</code> <code>ginq_set_seg_names(3NCARG),</code> <code>gset_seg_tran(3NCARG),</code> <code>gks(3NCARG),</code> <code>ncarg_gks_cbind(3NCARG)</code> </p>
<p> Hardcopy: User&#8217;s Guide for NCAR GKS-0A Graphics; NCAR Graphics Fundamentals, UNIX Version</p>
<h2>Copyright</h2>
<p>Copyright (C) 1987-2009<br />
 University Corporation for Atmospheric Research<br />
 The use of this Software is governed by a License Agreement.</p>
