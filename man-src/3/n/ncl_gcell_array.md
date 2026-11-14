---
title: "ncl_gcell_array(3)"
name: "ncl_gcell_array"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_gcell_array/"
description: "gcell_array (Cell array) – draws a cell array starting with a rectangle specified by two corner points; this initial rectangle is subdivided into subrectangles by specifying an arbitrary number of ..."
---

<p>gcell_array (Cell array) &#8211; draws a cell array starting with a rectangle specified by two corner points; this initial rectangle is subdivided into subrectangles by specifying an arbitrary number of divisions in the X and Y directions; each subrectangle (or cell) is assigned a color and drawn with that color.</p>
<h2>Synopsis</h2>
<p>#include &lt;ncarg/gks.h&gt; </p>
<p> void gcell_array(const Grect *rect, const Gpat_rep *colr_array);</p>
<h2>Description</h2>
<dl COMPACT>
<dt>rect.p.x</p>
<dd>(Gfloat Input) &#8211; X world coordinate of point 1.</p>
<dt>rect.p.y</p>
<dd>(Gfloat Input) &#8211; Y world coordinate of point 1.</p>
<dt>rect.q.x</p>
<dd>(Gfloat Input) &#8211; X world coordinate of point 2.</p>
<dt>rect.q.y</p>
<dd>(Gfloat Input) &#8211; Y world coordinate of point 2.</p>
<dt>colr_array.dims.size_x</p>
<dd>(Gint, Input) &#8211; X dimension of the color index array colr_array.colr_array.</p>
<dt>colr_array.dims.size_y</p>
<dd>(Gint, Input) &#8211; Y dimension of the color index array colr_array.colr_array.</p>
<dt>colr_array.colr_array</p>
<dd>(Gint *, Input) &#8211; An array of color indices dimensioned colr_array.dims.size_x by colr_array.dims.size_y which is used to determine the color of each cell drawn.</dl>
<h2>Usage</h2>
<p>Points 1 and 2 must be diagonally opposite corner points of a rectangle to be divided into colr_array.dims.size_x cells in the X dimension and colr_array.dims.size_y cells in the Y dimension.</p>
<h2>Access</h2>
<p>To use the GKS C-binding routines, load the ncarg_gks and ncarg_c libraries.</p>
<h2>See Also</h2>
<p>Online: <code>gset_colr_rep(3NCARG),</code> <code>gks(3NCARG),</code> <code>ncarg_gks_cbind(3NCARG)</code> </p>
<p> Hardcopy: User&#8217;s Guide for NCAR GKS-0A Graphics; NCAR Graphics Fundamentals, UNIX Version</p>
<h2>Copyright</h2>
<p>Copyright (C) 1987-2009<br />
 University Corporation for Atmospheric Research<br />
 The use of this Software is governed by a License Agreement.</p>
