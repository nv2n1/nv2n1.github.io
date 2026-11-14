---
title: "ncl_gfill_area(3)"
name: "ncl_gfill_area"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_gfill_area/"
description: "gfill_area (Fill area) – output primitive for filling polygonal areas."
---

<p>gfill_area (Fill area) &#8211; output primitive for filling polygonal areas.</p>
<h2>Synopsis</h2>
<p>#include &lt;ncarg/gks.h&gt; </p>
<p> void gfill_area(const Gpoint_list *point_list);</p>
<h2>Description</h2>
<dl COMPACT>
<dt>point_list.num_points</p>
<dd>(Gint, Input) &#8211; The number of points in the polygon to be filled. Must be greater than two.</p>
<dt>point_list.points</p>
<dd>(Gpoint *, Input) &#8211; The X and Y world coordinates of the polygon.</dl>
<h2>Usage</h2>
<p>The area to be filled is delimited by the sequence of straight line segments connecting the successive points ((point_list.points[0].x, point_list.points[0].y), &#8230;(point_list.points[point_list.num_points-1].x, point_list.points[point_list.num_points-1].y)) The last point in the polygon is connected to the first point with a straight line segment in the case that it is not the same as the first point. </p>
<p> Given a polygon whose edges cross each other, it becomes ambiguous as to what constitutes the &quot;inside&quot; of the polygon. The algorithm used in GKS is as follows: for a given point, draw a ray starting at that point and going to infinity in any direction; if the number of intersections between the ray and the polygon is odd, the point is within the polygon, otherwise it is outside. If the straight line passes through a polygon vertex tangentially, the intersection count is not affected. If a point is within the polygon, it is included in the area to be filled. </p>
<p> Several interior styles (hollow, solid, and various hatch patterns) can be selected. See the man pages for gset_fill_int_style and gset_fill_style_ind for these. </p>
<p> Note well: By default in GKS, the interior fill style is hollow, or no fill. If you call gfill_area and do not get a filled interior as you expected, you will probably need to call gset_fill_int_style to set the fill style to something other than &quot;hollow&quot;.</p>
<h2>Access</h2>
<p>To use the GKS C-binding routines, load the ncarg_gks and ncarg_c libraries.</p>
<h2>See Also</h2>
<p>Online: <code>gset_fill_int_style(3NCARG),</code> <code>gset_fill_style_ind(3NCARG),</code> <code>gset_colr_rep(3NCARG),</code> <code>gset_fill_colr_ind(3NCARG),</code> <code>ginq_fill_int_style(3NCARG),</code> <code>ginq_fill_style_ind(3NCARG),</code> <code>gks(3NCARG),</code> <code>ncarg_gks_cbind(3NCARG)</code> </p>
<p> Hardcopy: User&#8217;s Guide for NCAR GKS-0A Graphics; NCAR Graphics Fundamentals, UNIX Version</p>
<h2>Copyright</h2>
<p>Copyright (C) 1987-2009<br />
 University Corporation for Atmospheric Research<br />
 The use of this Software is governed by a License Agreement.</p>
