---
title: "ncl_ginq_set_seg_names(3)"
name: "ncl_ginq_set_seg_names"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_ginq_set_seg_names/"
description: "ginq_set_seg_names (Inquire set of segment names in use) – Retrieves what segment names are currently in use."
---

<p>ginq_set_seg_names (Inquire set of segment names in use) &#8211; Retrieves what segment names are currently in use.</p>
<h2>Synopsis</h2>
<p>#include &lt;ncarg/gks.h&gt; </p>
<p> void ginq_set_seg_names(Gint num_elems_appl_list, Gint start_pos, Gint *err_ind, Gint_list *seg_names, Gint *length_list);</p>
<h2>Description</h2>
<dl COMPACT>
<dt>num_elems_appl_list</p>
<dd>(Input) &#8211; The number of elements in the application list you wish to request.</p>
<dt>start_pos</p>
<dd>(Input) &#8211; The first set member requested.</p>
<dt>err_ind</p>
<dd>(Output) &#8211; If the GKS state is WSOP (workstation open), WSAC (workstation active), or SGOP (segment open), then err_ind is returned as &quot;0&quot;; otherwise err_ind is returned as &quot;7&quot;.</p>
<dt>length_list</p>
<dd>(Output) &#8211; The number of segment names that are currently in use.</p>
<dt>seg_names.num_ints</p>
<dd>(Gint, Output) &#8211; The number of segment names returned.</p>
<dt>seg_names.ints</p>
<dd>(Gint *, Output) &#8211; If the GKS state is WSOP (workstation open), WSAC (workstation active), or SGOP (segment open), and if start_pos is non-negative, then seg_names.ints is returned as the list of segment names starting with element &quot;start_pos&quot; and ending with element &quot;start_pos + num_elems_appl_list &#8211; 1&quot; or &quot;start_pos + length_list &#8211; 1&quot;, whichever is less; otherwise seg_names.num_ints is undefined.</dl>
<h2>Usage</h2>
<p>For NCAR GKS, segment names are integers between 0 and 99 inclusive (see the man page for gcreate_seg(3NCARG)). </p>
<h2>Access</h2>
<p>To use the GKS C-binding routines, load the ncarg_gks and ncarg_c libraries.</p>
<h2>See Also</h2>
<p>Online: <code>geval_tran_matrix(3NCARG),</code> <code>gaccum_tran_matrix(3NCARG),</code> <code>gclose_seg(3NCARG),</code> <code>gcreate_seg(3NCARG),</code> <code>gcopy_seg_ws(3NCARG),</code> <code>ginq_name_open_seg(3NCARG),</code> <code>gdel_seg(3NCARG),</code> <code>gset_seg_tran(3NCARG),</code> <code>gks(3NCARG),</code> <code>ncarg_gks_cbind(3NCARG)</code> </p>
<p> Hardcopy: User&#8217;s Guide for NCAR GKS-0A Graphics; NCAR Graphics Fundamentals, UNIX Version</p>
<h2>Copyright</h2>
<p>Copyright (C) 1987-2009<br />
 University Corporation for Atmospheric Research<br />
 The use of this Software is governed by a License Agreement.</p>
