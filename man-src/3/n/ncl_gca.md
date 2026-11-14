---
title: "ncl_gca(3)"
name: "ncl_gca"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_gca/"
---

GCA (Cell array) - draws a cell array starting with a rectangle specified by two corner points; this initial rectangle is subdivided into subrectangles by specifying an arbitrary number of divisions in the X and Y directions; each subrectangle (or cell) is assigned a color and drawn with that color.
<h2>Synopsis</h2>CALL GCA (XP1, YP1, XP2, YP2, NXCLR, NYCLR, IXCLR, IYCLR, NXDO, NYDO, CLRIA)
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/gks.h&gt; 

 void gcell_array(const Grect *rect, const Gpat_rep *colr_array);
<h2>Description</h2><dl COMPACT><dt>XP1
<dd>(Real, Input) - X world coordinate of point 1.
<dt>YP1
<dd>(Real, Input) - Y world coordinate of point 1.
<dt>XP2
<dd>(Real, Input) - X world coordinate of point 2.
<dt>YP2
<dd>(Real, Input) - Y world coordinate of point 2.
<dt>NXCLR
<dd>(Integer, Input) - X dimension of the color index array CLRIA.
<dt>NYCLR
<dd>(Integer, Input) - Y dimension of the color index array CLRIA.
<dt>IXCLR
<dd>(Integer, Input) - The index of the starting column in index array CLRIA.
<dt>IYCLR
<dd>(Integer, Input) - The index of the starting row in index array CLRIA.
<dt>NXDO
<dd>(Integer, Input) - Number of cell elements to draw in the X dimension.
<dt>NYDO
<dd>(Integer, Input) - Number of cell elements to draw in the Y dimension.
<dt>CLRIA
<dd>(Integer array, Input) - An array of color indices dimensioned NXCLR x NYCLR which is used to determine the color of each cell drawn.</dl><h2>Usage</h2>Points 1 and 2 must be diagonally opposite corner points of a rectangle to be divided into NXDO cells in the X dimension and NYDO cells in the Y dimension.
<h2>Access</h2>To use GKS routines, load the NCAR GKS-0A library ncarg_gks.
<h2>See Also</h2>Online: gscr, gcell_array 

 Hardcopy: User's Guide for NCAR GKS-0A Graphics; NCAR Graphics Fundamentals, UNIX Version
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
