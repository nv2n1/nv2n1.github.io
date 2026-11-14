---
title: "ncl_gcreate_seg(3)"
name: "ncl_gcreate_seg"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_gcreate_seg/"
description: "gcreate_seg (Create segment) – creates a GKS segment."
---

<p>gcreate_seg (Create segment) &#8211; creates a GKS segment.</p>
<h2>Synopsis</h2>
<p>#include &lt;ncarg/gks.h&gt; </p>
<p> void gcreate_seg(Gint seg_name);</p>
<h2>Description</h2>
<dl COMPACT>
<dt>seg_name</p>
<dd>(Input) &#8211; Specifies the segment identifier that will be used in calls to subsequent segment functions applying to this segment. There can be a maximum of 100 segments in a given job step. Legal values for seg_name are integers between 0 and 99 inclusive.</dl>
<h2>Access</h2>
<p>To use the GKS C-binding routines, load the ncarg_gks and ncarg_c libraries.</p>
<h2>See Also</h2>
<p>Online: <code>geval_tran_matrix(3NCARG),</code> <code>gaccum_tran_matrix(3NCARG),</code> <code>gclose_seg(3NCARG),</code> <code>gcopy_seg_ws(3NCARG),</code> <code>gdel_seg(3NCARG),</code> <code>ginq_name_open_seg(3NCARG),</code> <code>ginq_set_seg_names(3NCARG),</code> <code>gset_seg_tran(3NCARG),</code> <code>gks(3NCARG),</code> <code>ncarg_gks_cbind(3NCARG)</code> </p>
<p> Hardcopy: User&#8217;s Guide for NCAR GKS-0A Graphics; NCAR Graphics Fundamentals, UNIX Version</p>
<h2>Copyright</h2>
<p>Copyright (C) 1987-2009<br />
 University Corporation for Atmospheric Research<br />
 The use of this Software is governed by a License Agreement.</p>
