---
title: "ncl_gset_linewidth(3)"
name: "ncl_gset_linewidth"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_gset_linewidth/"
description: "gset_linewidth (Set linewidth scale factor) – sets the linewidth scale factor, or relative thickness of a polyline."
---

<p>gset_linewidth (Set linewidth scale factor) &#8211; sets the linewidth scale factor, or relative thickness of a polyline.</p>
<h2>Synopsis</h2>
<p>#include &lt;ncarg/gks.h&gt; </p>
<p> void gset_linewidth(Gdouble linewidth);</p>
<h2>Description</h2>
<dl COMPACT>
<dt>linewidth</p>
<dd>(Input) &#8211; A scale factor to control the linewidth of the polyline to be drawn. It must be greater than or equal to 0. linewidth is applied to the nominal linewidth on a given device and the linewidths are mapped to the nearest available linewidth representable on that device. </p>
<p> By default linewidth = 1.0, so setting linewidth = 2.0 will double line width on most devices.</dl>
<h2>Access</h2>
<p>To use the GKS C-binding routines, load the ncarg_gks and ncarg_c libraries.</p>
<h2>See Also</h2>
<p>Online: <code>gpolyline(3NCARG),</code> <code>gset_linetype(3NCARG),</code> <code>gset_colr_rep(3NCARG),</code> <code>gset_line_colr_ind(3NCARG),</code> <code>ginq_linetype(3NCARG),</code> <code>ginq_linewidth(3NCARG),</code> <code>ginq_line_colr_ind(3NCARG),</code> <code>dashline(3NCARG),</code> <code>gks(3NCARG),</code> <code>ncarg_gks_cbind(3NCARG)</code> </p>
<p> Hardcopy: User&#8217;s Guide for NCAR GKS-0A Graphics; NCAR Graphics Fundamentals, UNIX Version</p>
<h2>Copyright</h2>
<p>Copyright (C) 1987-2009<br />
 University Corporation for Atmospheric Research<br />
 The use of this Software is governed by a License Agreement.</p>
