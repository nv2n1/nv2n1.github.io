---
title: "ncl_gset_seg_tran(3)"
name: "ncl_gset_seg_tran"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_gset_seg_tran/"
description: "gset_seg_tran (Set segment transformation) – Associates a segment transformation with a named segment."
---

<p>gset_seg_tran (Set segment transformation) &#8211; Associates a segment transformation with a named segment.</p>
<h2>Synopsis</h2>
<p>#include &lt;ncarg/gks.h&gt; </p>
<p> void gset_seg_tran(Gint seg_name, const Gtran_matrix tran_matrix);</p>
<h2>Description</h2>
<dl COMPACT>
<dt>seg_name</p>
<dd>(Input) A segment name as used in a previous gcreate_seg call.</p>
<dt>tran_matrix</p>
<dd>(Gfloat, Input) &#8211; A 2&#215;3 array giving the GKS segment transformation to be associated with the segment specified in seg_name.</dl>
<h2>Usage</h2>
<p>When the segment named in seg_name is displayed, the coordinates of its primitives are transformed by the matrix specified in tran_matrix. </p>
<h2>Access</h2>
<p>To use the GKS C-binding routines, load the ncarg_gks and ncarg_c libraries.</p>
<h2>See Also</h2>
<p>Online: <code>gaccum_tran_matrix(3NCARG),</code> <code>geval_tran_matrix(3NCARG),</code> <code>gclose_seg(3NCARG),</code> <code>gcreate_seg(3NCARG),</code> <code>gcopy_seg_ws(3NCARG),</code> <code>gdel_seg(3NCARG),</code> <code>ginq_name_open_seg(3NCARG),</code> <code>ginq_set_seg_names(3NCARG),</code> <code>gks(3NCARG),</code> <code>ncarg_gks_cbind(3NCARG)</code> </p>
<p> Hardcopy: User&#8217;s Guide for NCAR GKS-0A Graphics; NCAR Graphics Fundamentals, UNIX Version</p>
<h2>Copyright</h2>
<p>Copyright (C) 1987-2009<br />
 University Corporation for Atmospheric Research<br />
 The use of this Software is governed by a License Agreement.</p>
