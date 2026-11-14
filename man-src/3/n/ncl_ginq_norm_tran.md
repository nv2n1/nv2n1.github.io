---
title: "ncl_ginq_norm_tran(3)"
name: "ncl_ginq_norm_tran"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_ginq_norm_tran/"
description: "ginq_norm_tran (Inquire normalization transformation) – retrieves the window and viewport associated with a given normalization transformation. Users of NCAR Graphics are encouraged to use the SPPS..."
---

<p>ginq_norm_tran (Inquire normalization transformation) &#8211; retrieves the window and viewport associated with a given normalization transformation. Users of NCAR Graphics are encouraged to use the SPPS routines c_set and c_getset to handle normalization transformations instead of the GKS entries gset_win, gset_vp, gsel_norm_tran, and ginq_norm_tran.</p>
<h2>Synopsis</h2>
<p>#include &lt;ncarg/gks.h&gt; </p>
<p> void ginq_norm_tran(Gint num, Gint *err_ind, Gtran *norm_tran);</p>
<h2>Description</h2>
<dl COMPACT>
<dt>num</p>
<dd>(Input) &#8211; Gives the number of the normalization transformation.</p>
<dt>err_ind</p>
<dd>(Output) &#8211; If the inquired value cannot be returned correctly, a non-zero error indicator is returned in err_ind, otherwise a zero is returned. Consult &quot;User&#8217;s Guide for NCAR GKS-0A Graphics&quot; for a description of the meaning of the error indicators.</p>
<dt>norm_tran.win</p>
<dd>(Glimit, Output) &#8211; The world coordinate window limits.</p>
<dt>norm_tran.vp</p>
<dd>(Glimit, Output) &#8211; The normalized device coordinate viewport limits.</dl>
<h2>Access</h2>
<p>To use the GKS C-binding routines, load the ncarg_gks and ncarg_c libraries.</p>
<h2>See Also</h2>
<p>Online: <code>gset_win(3NCARG),</code> <code>gset_vp(3NCARG),</code> <code>gsel_norm_tran(3NCARG),</code> <code>ginq_cur_norm_tran_num(3NCARG),</code> <code>ginq_max_norm_tran_num(3NCARG),</code> <code>getset(3NCARG),</code> <code>gset_clip_ind(3NCARG),</code> <code>ginq_clip(3NCARG),</code> <code>gks(3NCARG),</code> <code>ncarg_gks_cbind(3NCARG)</code> </p>
<p> Hardcopy: User&#8217;s Guide for NCAR GKS-0A Graphics; NCAR Graphics Fundamentals, UNIX Version</p>
<h2>Copyright</h2>
<p>Copyright (C) 1987-2009<br />
 University Corporation for Atmospheric Research<br />
 The use of this Software is governed by a License Agreement.</p>
