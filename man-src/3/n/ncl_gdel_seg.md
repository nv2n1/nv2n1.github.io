---
title: "ncl_gdel_seg(3)"
name: "ncl_gdel_seg"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_gdel_seg/"
description: "gdel_seg (Delete segment) – deletes a GKS segment."
---

<p>gdel_seg (Delete segment) &#8211; deletes a GKS segment.</p>
<h2>Synopsis</h2>
<p>#include &lt;ncarg/gks.h&gt; </p>
<p> void gdel_seg(Gint seg_name);</p>
<h2>Description</h2>
<dl COMPACT>
<dt>seg_name</p>
<dd>(Input) &#8211; Specifies the segment identifier for a segment that will be deleted by a call to this function.</dl>
<h2>Usage</h2>
<p>The segment name is removed from the set of names of segments that are currently in use.</p>
<h2>Access</h2>
<p>To use the GKS C-binding routines, load the ncarg_gks and ncarg_c libraries.</p>
<h2>See Also</h2>
<p>Online: <code>geval_tran_matrix(3NCARG),</code> <code>gaccum_tran_matrix(3NCARG),</code> <code>gclose_seg(3NCARG),</code> <code>gcreate_seg(3NCARG),</code> <code>gcopy_seg_ws(3NCARG),</code> <code>ginq_name_open_seg(3NCARG),</code> <code>ginq_set_seg_names(3NCARG),</code> <code>gset_seg_tran(3NCARG),</code> <code>gks(3NCARG),</code> <code>ncarg_gks_cbind(3NCARG)</code> </p>
<p> Hardcopy: User&#8217;s Guide for NCAR GKS-0A Graphics; NCAR Graphics Fundamentals, UNIX Version</p>
<h2>Copyright</h2>
<p>Copyright (C) 1987-2009<br />
 University Corporation for Atmospheric Research<br />
 The use of this Software is governed by a License Agreement.</p>
