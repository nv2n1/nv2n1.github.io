---
title: "ncl_set3(3)"
name: "ncl_set3"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_set3/"
---

SET3 - Defines the transformation from three dimensions to two dimensions.

<h2>Synopsis</h2>

CALL SET3 (XMIN,XMAX,YMIN,YMAX,UMIN,UMAX,VMIN,VMAX,WMIN,WMAX,PEYE)

<h2>C-Binding Synopsis</h2>

#include &lt;ncarg/ncargC.h&gt; 

 void c_set3 (float xmin, float xmax, float ymin, float ymax, 
 float umin, float umax, float vmin, float vmax, float wmin, 
 float wmax, float peye[3])

<h2>Description</h2>

<dl><dt>XMIN,XMAX,YMIN,YMAX
<dd>(input expressions of type REAL) are the fractional coordinates (in NDCs) defining the portion of the plotter frame (the &quot;viewport&quot;) into which 3-D objects are to be projected. Each has a value between 0. and 1., inclusive. Examples: To use the whole plotter frame, set XMIN=0., XMAX=1., YMIN=0., and YMAX=1.; to use the upper left quarter of the plotter frame, set XMIN=0., XMAX=.5, YMIN=.5, and YMAX=1.
<dt>UMIN,UMAX,VMIN,VMAX,WMIN,WMAX
<dd>(input expressions of type REAL) are the limiting coordinates, in a 3-D coordinate space of the user's choosing, of the rectangular box that is to be projected. This box normally contains all of the objects whose projections are to be drawn.
<dt>PEYE
<dd>(an input array, dimensioned 3, of type REAL) is an array specifying the coordinates, in the user's 3-D coordinate system, of the eye position. The point
<dl><dd><dl><dd>(<a HREF="/docs/linux/man/1-peye/">PEYE</a>(1),<a HREF="/docs/linux/man/2-peye/">PEYE</a>(2),<a HREF="/docs/linux/man/3-peye/">PEYE</a>(3))</dl></dl><dd>must be outside the box defined by UMIN, UMAX, VMIN, VMAX, WMIN, and WMAX. Objects will be drawn as they appear from this point.</dl>
 

 The call to SET3 says what portion of the 3-D coordinate system is to be projected, from what point it is to be projected, and where the resulting picture is to be placed on the plotter frame. 

 The array PEYE specifies the position of the eye, which may be referred to as the &quot;viewpoint&quot; or &quot;center&quot; of the projection. 

 The &quot;line of sight&quot; runs from the point
<dl><dd>(<a HREF="/docs/linux/man/1-peye/">PEYE</a>(1),<a HREF="/docs/linux/man/2-peye/">PEYE</a>(2),<a HREF="/docs/linux/man/3-peye/">PEYE</a>(3))</dl>
 

 (the eye position) to the point
<dl><dd>(.5*(UMIN+UMAX),.5*(VMIN+VMAX),.5*(WMIN+WMAX))</dl>
 

 (the point at the center of the projected box). 

 The &quot;image plane&quot; is perpendicular to the line of sight and may be thought of as passing through the center of the box. The projection of an arbitrary point P in 3-space is the point where the straight line from the eye position to P passes through the image plane. The projection of a more complicated object is just the union of the projections of its constituent points. 

 The projection in the image plane of the box specified by the arguments UMIN, UMAX, VMIN, VMAX, WMIN, and WMAX will be scaled to fit in the viewport specified by the arguments XMIN, XMAX, YMIN, and YMAX. The projected box will retain its natural aspect ratio; typically, it will just touch the left and right edges of the viewport, or the top and bottom of the viewport, but not both. 

 The image of the box will be rotated so that the projection of a unit vector based at the center of the box and pointing in the direction of the positive W axis will be made to point upward in the viewport. However, if the line of sight is very nearly parallel to the W axis, so that the projection of this unit vector shrinks almost to a point, then a unit vector based at the center of the box and pointing in the direction of the positive V axis will be made to point upward in the viewport instead. One implication of this is that, if you are making a movie by letting the eye &quot;fly around&quot; the objects being projected and it gets too close to being directly above or below the center of the box, there may be a sudden disconcerting rotation of the projected image.

<h2>C-Binding Description</h2>

The C-binding argument descriptions are the same as the FORTRAN argument descriptions.

<h2>Usage</h2>

SET3 should be called before calling other THREED routines.

<h2>Examples</h2>

Use the ncargex command to see the following relevant examples: tpwrzt, tthree.

<h2>Access</h2>

To use SET3 or c_set3, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.

<h2>See Also</h2>

Online: threed, curve3, fence3, frst3, line3, perim3, point3, psym3, pwrz, pwrzt, threed, tick3, tick43, vect3, ncarg_cbind. 

 Hardcopy: NCAR Graphics Fundamentals, UNIX Version

<h2>Copyright</h2>

Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
