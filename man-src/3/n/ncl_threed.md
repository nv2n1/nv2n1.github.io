---
title: "ncl_threed(3)"
name: "ncl_threed"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_threed/"
---

THREED - 3-d line drawing package.

<h2>Synopsis</h2>

CURVE3 - Draws the projection of a curve defined by a sequence of points in 3-space. 

 FENCE3 - Draws the projection of a curve, just as CURVE3 does, but with a &quot;fence&quot; of straight line segments that are parallel to one of the three axes and that extend to a specified plane perpendicular to that axis. 

 FRST3 - Specifies the first in a sequence of points connected by straight-line segments, the projections of which are to be drawn. (FRST3 is called for the first point in the sequence and VECT3 is called for the rest.) 

 LINE3 - Draws the projection of a straight-line segment. 

 PERIM3 - Draws the projection of a rectangular perimeter in a plane parallel to one of the three coordinate planes, with inward-pointing tick marks at specified intervals. 

 POINT3 - Draws the projection of a point. 

 PWRZT - Draws the projection of character strings that are positioned in a plane parallel to one of the three coordinate planes. 

 SET3 - Defines the transformation from three dimensions to two dimensions. 

 TICK43 - Gives user control of tick mark length in PERIM3. 

 VECT3 - Defines the second and all subsequent points in a sequence of points connected by straight-line segments, the projections of which are to be drawn. (FRST3 is called for the first point in the sequence and VECT3 is called for the rest.)

<h2>C-Binding Synopsis</h2>

#include &lt;ncarg/ncargC.h&gt; 

 c_curve3 
 c_fence3 
 c_frst3 
 c_line3 
 c_perim3 
 c_point3 
 c_pwrzt 
 c_set3 
 c_threed 
 c_tick43 
 c_vect3

<h2>Access</h2>

To use THREED routines, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.

<h2>See Also</h2>

Online: threed, curve3, fence3, frst3, line3, perim3, point3, psym3, pwrz, pwrzt, set3, tick3, tick43, vect3, ncarg_cbind. 

 Hardcopy: NCAR Graphics Fundamentals, UNIX Version

<h2>Copyright</h2>

Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
