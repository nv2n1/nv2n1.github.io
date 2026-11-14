---
title: "ncl_ginq_name_open_seg(3)"
name: "ncl_ginq_name_open_seg"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_ginq_name_open_seg/"
description: "ginq_name_open_seg (Inquire name of open segment) – returns the name of the currently open segment."
---

<p>ginq_name_open_seg (Inquire name of open segment) &#8211; returns the name of the currently open segment.</p>
<h2>Synopsis</h2>
<p>#include &lt;ncarg/gks.h&gt; </p>
<p> void ginq_name_open_seg(Gint *err_ind, Gint *name_open_seg);</p>
<h2>Description</h2>
<dl COMPACT>
<dt>err_ind</p>
<dd>(Output) &#8211; If the GKS state is SGOP (segment open), then err_ind is returned as &quot;0&quot;; otherwise err_ind is returned as &quot;4&quot;.</p>
<dt>name_open_seg</p>
<dd>(Output) &#8211; If the GKS state is SGOP (segment open), then name_open_seg is returned as the number of the currently open segment; otherwise name_open_seg is undefined.</dl>
<h2>Access</h2>
<p>To use the GKS C-binding routines, load the ncarg_gks and ncarg_c libraries.</p>
<h2>See Also</h2>
<p>Online: <code>geval_tran_matrix(3NCARG),</code> <code>gaccum_tran_matrix(3NCARG),</code> <code>gclose_seg(3NCARG),</code> <code>gcreate_seg(3NCARG),</code> <code>gcopy_seg_ws(3NCARG),</code> <code>gdel_seg(3NCARG),</code> <code>ginq_set_seg_names(3NCARG),</code> <code>gset_seg_tran(3NCARG),</code> <code>gks(3NCARG),</code> <code>ncarg_gks_cbind(3NCARG)</code> </p>
<p> Hardcopy: User&#8217;s Guide for NCAR GKS-0A Graphics; NCAR Graphics Fundamentals, UNIX Version</p>
<h2>Copyright</h2>
<p>Copyright (C) 1987-2009<br />
 University Corporation for Atmospheric Research<br />
 The use of this Software is governed by a License Agreement.</p>
