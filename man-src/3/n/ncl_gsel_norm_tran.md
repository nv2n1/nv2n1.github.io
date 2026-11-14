---
title: "ncl_gsel_norm_tran(3)"
name: "ncl_gsel_norm_tran"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_gsel_norm_tran/"
description: "gsel_norm_tran (Select normalization transformation) – selects a predefined or user-defined transformation that maps world coordinates to normalized device coordinates."
---

<p>gsel_norm_tran (Select normalization transformation) &#8211; selects a predefined or user-defined transformation that maps world coordinates to normalized device coordinates.</p>
<h2>Synopsis</h2>
<p>#include &lt;ncarg/gks.h&gt; </p>
<p> void gsel_norm_tran(Gint tran_num);</p>
<h2>Description</h2>
<dl COMPACT>
<dt>tran_num</p>
<dd>(Input) &#8211; A normalization transformation number. The number of available transformations is implementation specific. In the case of NCAR GKS-0A, two normalization transformations are provided: </p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>0</p>
<dd>Selects the identity transformation in which both the window and viewport have the range of 0. to 1. in both coordinate directions. This is the default. </p>
<dt>1</p>
<dd>Selects a normalization transformation in which the window and viewport have been defined by calls to gset_win and gset_vp.</dl>
</dl>
</dl>
<h2>Usage</h2>
<p>When a normalization transformation is selected, all world coordinate arguments to GKS functions are transformed by it.</p>
<h2>Access</h2>
<p>To use the GKS C-binding routines, load the ncarg_gks and ncarg_c libraries.</p>
<h2>See Also</h2>
<p>Online: <code>set(3NCARG),</code> <code>gset_win(3NCARG),</code> <code>gset_vp(3NCARG),</code> <code>ginq_clip(3NCARG),</code> <code>gks(3NCARG),</code> <code>ncarg_gks_cbind(3NCARG)</code> </p>
<p> Hardcopy: User&#8217;s Guide for NCAR GKS-0A Graphics; NCAR Graphics Fundamentals, UNIX Version</p>
<h2>Copyright</h2>
<p>Copyright (C) 1987-2009<br />
 University Corporation for Atmospheric Research<br />
 The use of this Software is governed by a License Agreement.</p>
