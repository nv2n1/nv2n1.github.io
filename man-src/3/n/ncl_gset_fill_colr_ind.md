---
title: "ncl_gset_fill_colr_ind(3)"
name: "ncl_gset_fill_colr_ind"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_gset_fill_colr_ind/"
description: "gset_fill_colr_ind (Set fill area color index) – sets the fill area color index."
---

<p>gset_fill_colr_ind (Set fill area color index) &#8211; sets the fill area color index.</p>
<h2>Synopsis</h2>
<p>#include &lt;ncarg/gks.h&gt; </p>
<p> void gset_fill_colr_ind(Gint fill_colr_ind);</p>
<h2>Description</h2>
<dl COMPACT>
<dt>fill_colr_ind</p>
<dd>(Input) &#8211; A color index.</dl>
<h2>Usage</h2>
<p>All filled areas drawn with calls to the gfill_area output primitive will be drawn with the color associated with index fill_colr_ind until gset_fill_colr_ind is called again and a new index is assigned. </p>
<p> For all GKS output primitives, color is assigned using a color index. The color indices run from 0 to 255, where 0 is the background color index and 1 is the foreground color index. Color values are associated with indices by calls to the GKS routine gset_colr_rep. If a color index is used that has no user-assigned color value set in a gset_colr_rep call, then a device-dependent color value will be assigned to that index.</p>
<h2>Access</h2>
<p>To use the GKS C-binding routines, load the ncarg_gks and ncarg_c libraries.</p>
<h2>See Also</h2>
<p>Online: <code>gfill_area(3NCARG),</code> <code>gset_fill_int_style(3NCARG),</code> <code>gset_fill_style_ind(3NCARG),</code> <code>gset_colr_rep(3NCARG),</code> <code>ginq_fill_int_style(3NCARG),</code> <code>ginq_fill_style_ind(3NCARG),</code> <code>areas(3NCARG),</code> <code>gks(3NCARG),</code> <code>ncarg_gks_cbind(3NCARG)</code> </p>
<p> Hardcopy: User&#8217;s Guide for NCAR GKS-0A Graphics; NCAR Graphics Fundamentals, UNIX Version</p>
<h2>Copyright</h2>
<p>Copyright (C) 1987-2009<br />
 University Corporation for Atmospheric Research<br />
 The use of this Software is governed by a License Agreement.</p>
