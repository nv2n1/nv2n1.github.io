---
title: "ncl_gset_vp(3)"
name: "ncl_gset_vp"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_gset_vp/"
description: "gset_vp (Set viewport) – establishes a rectangular subspace of normalized device coordinates space. Calls to gset_vp are discouraged with NCAR Graphics. Instead, use the c_set routine because c_set..."
---

<p>gset_vp (Set viewport) &#8211; establishes a rectangular subspace of normalized device coordinates space. Calls to gset_vp are discouraged with NCAR Graphics. Instead, use the c_set routine because c_set also supports mirror imaging and log scaling of axes.</p>
<h2>Synopsis</h2>
<p>#include &lt;ncarg/gks.h&gt; </p>
<p> void gset_vp(Gint tran_num, const Glimit *vp_limits);</p>
<h2>Description</h2>
<dl COMPACT>
<dt>tran_num</dt>
<dd>(Input) A normalization transformation number. The number of available transformations is implementation specific. In the case of NCAR GKS-0A, two normalization transformations are provided:</dd>
<dl COMPACT>
<dd>
</dd><dl COMPACT>
<dt>0</dt>
<dd>Selects the identity transformation in which both the window and viewport have the range of 0. to 1. in both coordinate directions. This is the default normalization transformation for GKS. It is also fixed within GKS; that is, it is illegal to call gset_vp with tran_num = 0.</dd>
<dt>1</dt>
<dd>A normalization transformation in which the viewport is defined by vp_limits.x_min to vp_limits.x_max and vp_limits.y_min to vp_limits.y_max.</dd></dl>
</dl>
<dt>vp_limits.x_min</dt>
<dd>(Real, Input) &#8211; The left horizontal coordinate of the viewport.</dd>
<dt>vp_limits.x_max</dt>
<dd>(Real, Input) &#8211; The right horizontal coordinate of the viewport. 0. &le; vp_limits.x_min &lt; vp_limits.x_max &le; 1.</dd>
<dt>vp_limits.y_min</dt>
<dd>(Real, Input) &#8211; The bottom vertical coordinate of the viewport.</dd>
<dt>vp_limits.y_max</dt>
<dd>(Real, Input) &#8211; The top vertical coordinate of the viewport. 0. &le; vp_limits.y_min &lt; vp_limits.y_max &le; 1.</dd>
<dt>Defaults:</dt>
<dd>tran_num = 0, vp_limits.x_min = 0.0, vp_limits.x_max = 1.0, vp_limits.y_min = 0.0, vp_limits.y_max = 1.0</dd></dl>
<h2>Access</h2>
<p>To use the GKS C-binding routines, load the ncarg_gks and ncarg_c libraries.</p>
<h2>See Also</h2>
<p>Online: <code>set(3NCARG),</code> <code>gset_win(3NCARG),</code> <code>gsel_norm_tran(3NCARG),</code> <code>ginq_clip(3NCARG),</code> <code>gks(3NCARG),</code> <code>ncarg_gks_cbind(3NCARG)</code> </p>
<p> Hardcopy: User&#8217;s Guide for NCAR GKS-0A Graphics; NCAR Graphics Fundamentals, UNIX Version</p>
<h2>Copyright</h2>
<p>Copyright (C) 1987-2009<br/>
 University Corporation for Atmospheric Research<br/>
 The use of this Software is governed by a License Agreement.</p>
