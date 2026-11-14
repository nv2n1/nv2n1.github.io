---
title: "ncl_gclose_seg(3)"
name: "ncl_gclose_seg"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_gclose_seg/"
description: "gclose_seg (Close segment) – closes a GKS segment."
---

<p>gclose_seg (Close segment) &#8211; closes a GKS segment.</p>
<h2>Synopsis</h2>
<p>#include &lt;ncarg/gks.h&gt; </p>
<p> void gclose_seg( void );</p>
<h2>Usage</h2>
<p>A call to gclose_seg closes the currently open segment (graphics output primitives will no longer be stored in that segment). gclose_seg can be called only if a segment is open.</p>
<h2>Access</h2>
<p>To use the GKS C-binding routines, load the ncarg_gks and ncarg_c libraries.</p>
<h2>See Also</h2>
<p>Online: <code>geval_tran_matrix(3NCARG),</code> <code>gaccum_tran_matrix(3NCARG),</code> <code>gcreate_seg(3NCARG),</code> <code>gcopy_seg_ws(3NCARG),</code> <code>gdel_seg(3NCARG),</code> <code>ginq_name_open_seg(3NCARG),</code> <code>ginq_set_seg_names(3NCARG),</code> <code>gset_seg_tran(3NCARG),</code> <code>gks(3NCARG),</code> <code>ncarg_gks_cbind(3NCARG)</code> </p>
<p> Hardcopy: User&#8217;s Guide for NCAR GKS-0A Graphics; NCAR Graphics Fundamentals, UNIX Version</p>
<h2>Copyright</h2>
<p>Copyright (C) 1987-2009<br />
 University Corporation for Atmospheric Research<br />
 The use of this Software is governed by a License Agreement.</p>
