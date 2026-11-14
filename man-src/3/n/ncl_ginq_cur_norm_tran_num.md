---
title: "ncl_ginq_cur_norm_tran_num(3)"
name: "ncl_ginq_cur_norm_tran_num"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_ginq_cur_norm_tran_num/"
description: "ginq_cur_norm_tran_num (Inquire current normalization transformation number) – retrieves the number of the current normalization transformation."
---

<p>ginq_cur_norm_tran_num (Inquire current normalization transformation number) &#8211; retrieves the number of the current normalization transformation.</p>
<h2>Synopsis</h2>
<p>#include &lt;ncarg/gks.h&gt; </p>
<p> void ginq_cur_norm_tran_num(Gint *err_ind, Gint *norm_tran_num);</p>
<h2>Description</h2>
<dl COMPACT>
<dt>err_ind</p>
<dd>(Output) &#8211; If the inquired value cannot be returned correctly, a non-zero error indicator is returned in err_ind, otherwise a zero is returned. Consult &quot;User&#8217;s Guide for NCAR GKS-0A Graphics&quot; for a description of the meaning of the error indicators.</p>
<dt>norm_tran_num</p>
<dd>(Output) &#8211; Returns the current normalization transformation number as set by default or by a call to gsel_norm_tran.</dl>
<h2>Access</h2>
<p>To use the GKS C-binding routines, load the ncarg_gks and ncarg_c libraries.</p>
<h2>See Also</h2>
<p>Online: <code>gsel_norm_tran(3NCARG),</code> <code>ginq_max_norm_tran_num(3NCARG),</code> <code>ginq_norm_tran(3NCARG),</code> <code>getset(3NCARG),</code> <code>gks(3NCARG),</code> <code>ncarg_gks_cbind(3NCARG)</code> </p>
<p> Hardcopy: User&#8217;s Guide for NCAR GKS-0A Graphics; NCAR Graphics Fundamentals, UNIX Version</p>
<h2>Copyright</h2>
<p>Copyright (C) 1987-2009<br />
 University Corporation for Atmospheric Research<br />
 The use of this Software is governed by a License Agreement.</p>
