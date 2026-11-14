---
title: "ncl_gpolymarker(3)"
name: "ncl_gpolymarker"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_gpolymarker/"
description: "gpolymarker (Polymarker) – the polymarker output primitive draws selected symmetric symbols to mark user-specified coordinate positions."
---

<p>gpolymarker (Polymarker) &#8211; the polymarker output primitive draws selected symmetric symbols to mark user-specified coordinate positions.</p>
<h2>Synopsis</h2>
<p>#include &lt;ncarg/gks.h&gt; </p>
<p> void gpolymarker(const Gpoint_list *point_list);</p>
<h2>Description</h2>
<dl COMPACT>
<dt>point_list.num_points</p>
<dd>(Gint, Input) &#8211; The number of markers to be drawn. Must be greater than zero.</p>
<dt>point_list.points</p>
<dd>(Gpoint *, Input) &#8211; The X and Y coordinates of the point_list.num_points markers to be drawn, in world coordinates.</dl>
<h2>Usage</h2>
<p>By default, the polymarker type is an asterisk. To select other polymarker types and attributes, see the man page for gset_marker_type(3NCARG). </p>
<p> Note that the coordinate pairs must be in world coordinates and not user coordinates. Among other things, this means that the log scaling and mirror-imaging features available via the c_set call and the SPPS functions for drawing dots and markers are not applicable here.</p>
<h2>Access</h2>
<p>To use the GKS C-binding routines, load the ncarg_gks and ncarg_c libraries.</p>
<h2>See Also</h2>
<p>Online: <code>gset_marker_type(3NCARG),</code> <code>gset_marker_size(3NCARG),</code> <code>gset_colr_rep(3NCARG),</code> <code>gset_marker_colr_ind(3NCARG),</code> <code>ginq_marker_type(3NCARG),</code> <code>ginq_marker_size(3NCARG),</code> <code>ginq_marker_colr_ind(3NCARG),</code> <code>point(3NCARG),</code> <code>points(3NCARG),</code> <code>ngdots(3NCARG),</code> <code>gks(3NCARG),</code> <code>ncarg_gks_cbind(3NCARG)</code> </p>
<p> Hardcopy: User&#8217;s Guide for NCAR GKS-0A Graphics; NCAR Graphics Fundamentals, UNIX Version</p>
<h2>Copyright</h2>
<p>Copyright (C) 1987-2009<br />
 University Corporation for Atmospheric Research<br />
 The use of this Software is governed by a License Agreement.</p>
