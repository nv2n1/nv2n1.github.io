---
title: "ncl_gpolyline(3)"
name: "ncl_gpolyline"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_gpolyline/"
description: "gpolyline (Polyline) – This output primitive draws line segments connecting a sequence of user-specified coordinate pairs."
---

<p>gpolyline (Polyline) &#8211; This output primitive draws line segments connecting a sequence of user-specified coordinate pairs.</p>
<h2>Synopsis</h2>
<p>#include &lt;ncarg/gks.h&gt; </p>
<p> void gpolyline(const Gpoint_list *point_list);</p>
<h2>Description</h2>
<dl COMPACT>
<dt>point_list.num_points</p>
<dd>(Gint, Input) &#8211; The number of points in the line to be drawn. Must be larger than one.</p>
<dt>point_list.points</p>
<dd>(Gint *, Input) &#8211; The X and Y coordinates (specified in world coordinates) of the point_list.num_points points to be connected by line segments.</dl>
<h2>Usage</h2>
<p>Note that the coordinate pairs must be in world coordinates and not user coordinates. Among other things, this means that the log scaling and mirror-imaging features available via the c_set call and the SPPS functions for drawing lines are not applicable here.</p>
<h2>Access</h2>
<p>To use the GKS C-binding routines, load the ncarg_gks and ncarg_c libraries.</p>
<h2>See Also</h2>
<p>Online: <code>gset_linetype(3NCARG),</code> <code>gset_linewidth(3NCARG),</code> <code>gset_colr_rep(3NCARG),</code> <code>gset_line_colr_ind(3NCARG),</code> <code>ginq_linetype(3NCARG),</code> <code>ginq_linewidth(3NCARG),</code> <code>ginq_line_colr_ind(3NCARG),</code> <code>dashline(3NCARG),</code> <code>set(3NCARG),</code> <code>gks(3NCARG),</code> <code>ncarg_gks_cbind(3NCARG)</code> </p>
<p> Hardcopy: User&#8217;s Guide for NCAR GKS-0A Graphics; NCAR Graphics Fundamentals, UNIX Version &quot;The Use of X/Y Coordinates in NCAR Graphics&quot; SCD User Document&quot;</p>
<h2>Copyright</h2>
<p>Copyright (C) 1987-2009<br />
 University Corporation for Atmospheric Research<br />
 The use of this Software is governed by a License Agreement.</p>
