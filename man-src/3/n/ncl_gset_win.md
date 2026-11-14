---
title: "ncl_gset_win(3)"
name: "ncl_gset_win"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_gset_win/"
description: "gset_win (Set window) – establishes a window, or rectangular subspace, of world coordinates to be plotted. Calls to gset_win are discouraged with NCAR Graphics. Instead, use the c_set routine becau..."
---

<p>gset_win (Set window) &#8211; establishes a window, or rectangular subspace, of world coordinates to be plotted. Calls to gset_win are discouraged with NCAR Graphics. Instead, use the c_set routine because c_set also supports mirror imaging and log scaling of axes.</p>
<h2>Synopsis</h2>
<p>#include &lt;ncarg/gks.h&gt; </p>
<p> void gset_win(Gint tran_num, const Glimit *win_limits);</p>
<h2>Description</h2>
<dl COMPACT>
<dt>tran_num</p>
<dd>(Input) A normalization transformation number. The number of available transformations is implementation specific. In the case of NCAR GKS-0A, two normalization transformations are provided:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>0</p>
<dd>Selects the identity transformation in which both the window and viewport have the range of 0. to 1. in both coordinate directions. This is the default normalization transformation for GKS. It is also fixed within GKS; that is, it is illegal to call gset_win with tran_num = 0.</p>
<dt>1</p>
<dd>A normalization transformation in which the window is defined by win_limits.x_min to win_limits.x_max and win_limits.y_min to win_limits.y_max.</dl>
</dl>
<dt>win_limits.x_min</p>
<dd>(Gfloat, Input) &#8211; The left horizontal coordinate of the window. x_min &lt; x_max</p>
<dt>win_limits.x_max</p>
<dd>(Gfloat, Input) &#8211; The right horizontal coordinate of the window.</p>
<dt>win_limits.y_min</p>
<dd>(Gfloat, Input) &#8211; The bottom vertical coordinate of the window. y_min &lt; y_max</p>
<dt>win_limits.y_max</p>
<dd>(Gfloat, Input) &#8211; The top vertical coordinate of the window.</dl>
<h2>Access</h2>
<p>To use the GKS C-binding routines, load the ncarg_gks and ncarg_c libraries.</p>
<h2>See Also</h2>
<p>Online: <code>set(3NCARG),</code> <code>gset_vp(3NCARG),</code> <code>gsel_norm_tran(3NCARG),</code> <code>ginq_clip(3NCARG),</code> <code>gks(3NCARG)</code> <code>ncarg_gks_cbind(3NCARG)</code> </p>
<p> Hardcopy: User&#8217;s Guide for NCAR GKS-0A Graphics; NCAR Graphics Fundamentals, UNIX Version</p>
<h2>Copyright</h2>
<p>Copyright (C) 1987-2009<br />
 University Corporation for Atmospheric Research </p>
<p> The use of this Software is governed by a License Agreement.</p>
