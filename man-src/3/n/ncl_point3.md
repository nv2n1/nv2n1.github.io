---
title: "ncl_point3(3)"
name: "ncl_point3"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_point3/"
---

POINT3 - Draws the projection of a point in 3-space.

<h2>Synopsis</h2>

CALL POINT3 (U,V,W)

<h2>C-Binding Synopsis</h2>

#include &lt;ncarg/ncargC.h&gt; 

 void c_point3 (float u, float v, float w)

<h2>Description</h2>

<dl><dt>U,V,W
<dd>(input expressions of type REAL) are the coordinates of a point in 3-space.</dl>
 

 Each point is drawn by calling the GKS routine GPM to draw a polymarker of type 1. Points are therefore drawn in the current polymarker color, as determined by the last call to the GKS routine GSPMCI; by default, color index 1 is the one used. 

 Calling the GKS routine GSMKSC to change the polymarker size does not normally affect polymarkers of type 1, so there is no good way to make the points bigger; if you want to do this, you should use LINE3 (or perhaps FRST3 and VECT3) instead of POINT3 to draw an object of the desired size.

<h2>C-Binding Description</h2>

The C-binding argument descriptions are the same as the FORTRAN argument descriptions.

<h2>Examples</h2>

Use the ncargex command to see the following relevant examples: fthex01, fthex02, fthex03, fthex04, fthex05.

<h2>Access</h2>

To use POINT3 or c_point3, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.

<h2>See Also</h2>

Online: threed, curve3, fence3, frst3, line3, perim3, psym3, pwrz, pwrzt, set3, threed, tick3, tick43, vect3, ncarg_cbind. 

 Hardcopy: NCAR Graphics Fundamentals, UNIX Version

<h2>Copyright</h2>

Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
