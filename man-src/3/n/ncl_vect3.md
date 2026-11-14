---
title: "ncl_vect3(3)"
name: "ncl_vect3"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_vect3/"
---

VECT3 - Defines the second and all subsequent points in a sequence of points connected by straight-line segments, the projections of which are to be drawn. (FRST3 is called for the first point in the sequence and VECT3 is called for the rest.)

<h2>Synopsis</h2>

CALL VECT3 (U,V,W)

<h2>C-Binding Synopsis</h2>

#include &lt;ncarg/ncargC.h&gt; 

 void c_vect3 (float u, float v, float w)

<h2>Description</h2>

<dl><dt>U,V,W
<dd>(input expressions of type REAL) are the coordinates of a point in 3-space to the projection of which a line is to be drawn.</dl>
 

 Each call to FRST3 moves a conceptual &quot;pen&quot; to the new starting point for a sequence of line draws. Each call to VECT3 draws a line from the current pen position to a new pen position and then makes that the current pen position. 

 Line segments are drawn in the current polyline color, as determined by the last call to the GKS routine GSPLCI; by default, color index 1 is used. Line width is determined by the last call to the GKS routine GSLWSC; by default, the value of the line width scale factor is 1. 

 Note that the routines FRST3 and VECT3 do not flush the SPPS pen-move buffer. In fact, to have them do so would entirely defeat the purpose of that buffer. Therefore, if your last call was to the routine VECT3 and you are about to call GKS routines to change color or line width, you must first call the SPPS routine PLOTIF to flush the buffer; otherwise, the color and line width changes will affect line draws flushed from the buffer later.

<h2>C-Binding Description</h2>

The C-binding argument descriptions are the same as the FORTRAN argument descriptions.

<h2>Examples</h2>

Use the ncargex command to see the following relevant examples: fthex01, fthex02, fthex03.

<h2>Access</h2>

To use VECT3 or c_vect3, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.

<h2>See Also</h2>

Online: threed, curve3, fence3, frst3, line3, perim3, point3, psym3, pwrz, pwrzt, set3, threed, tick3, tick43, ncarg_cbind. 

 Hardcopy: NCAR Graphics Fundamentals, UNIX Version

<h2>Copyright</h2>

Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
