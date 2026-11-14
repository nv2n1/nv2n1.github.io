---
title: "ncl_gfa(3)"
name: "ncl_gfa"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_gfa/"
---

GFA (Fill area) - output primitive for filling polygonal areas.
<h2>Synopsis</h2>CALL GFA (N, X, Y)
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/gks.h&gt; 

 void gfill_area(const Gpoint_list *point_list);
<h2>Description</h2><dl COMPACT><dt>N
<dd>(Integer, Input) - The number of points in the polygon to be filled. N must be greater than two.
<dt>X (N)
<dd>(Real Array, Integer) - The X world coordinates of the polygon.
<dt>Y (N)
<dd>(Real Array, Integer) - The Y world coordinates of the polygon.</dl><h2>Usage</h2>The area to be filled is delimited by the sequence of straight line segments connecting the successive points (<a HREF="/docs/linux/man/1-x/">X</a>(1), <a HREF="/docs/linux/man/1-y/">Y</a>(1)), (<a HREF="/docs/linux/man/2-x/">X</a>(2), <a HREF="/docs/linux/man/2-y/">Y</a>(2)), ..., (X(N), Y(N)). The last point in the polygon is connected to the first point with a straight line segment in the case that (X(N), Y(N)) does not equal (<a HREF="/docs/linux/man/l-x/">X</a>(l), <a HREF="/docs/linux/man/l-y/">Y</a>(l)). 

 Given a polygon whose edges cross each other, it becomes ambiguous as to what constitutes the &quot;inside&quot; of the polygon. The algorithm used in GKS is as follows: for a given point, draw a ray starting at that point and going to infinity in any direction; if the number of intersections between the ray and the polygon is odd, the point is within the polygon, otherwise it is outside. If the straight line passes through a polygon vertex tangentially, the intersection count is not affected. If a point is within the polygon, it is included in the area to be filled. 

 Several interior styles (hollow, solid, and various hatch patterns) can be selected. See the man pages for gsfais and gsfasi for these. 

 Note well: By default in GKS, the interior fill style is hollow, or no fill. If you call GFA and do not get a filled interior as you expected, you will probably need to call GSFAIS to set the fill style to something other than &quot;hollow&quot;.
<h2>Access</h2>To use GKS routines, load the NCAR GKS-0A library ncarg_gks.
<h2>See Also</h2>Online: gsfais, gsfasi, gscr, gsfaci, gqfais, gqfasi, gfill_area 

 Hardcopy: User's Guide for NCAR GKS-0A Graphics; NCAR Graphics Fundamentals, UNIX Version
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
