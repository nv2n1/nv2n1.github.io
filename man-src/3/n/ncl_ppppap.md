---
title: "ncl_ppppap(3)"
name: "ncl_ppppap"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_ppppap/"
---

PPPPAP - can be called to preprocess a polygon in such a way as to remove certain peculiarities that can cause minor cosmetic errors in the output from the routines that return trapezoids.

<h2>Synopsis</h2>

CALL PPPPAP (XCIP,YCIP,NCIP,NBTS)

<h2>C-Binding Synopsis</h2>

#include &lt;ncarg/ncargC.h&gt; 

 void c_ppppap(float *xcip, float *ycip, int ncip, int nbts)

<h2>Description</h2>

<dl><dt>XCIP
<dd>(an input/output array of type REAL) is the X coordinate array for a polygon to be used as input to one of the routines PPDITR, PPINTR, or PPUNTR. PPPPAP will alter the contents of this array.
<dt>YCIP
<dd>(an input/output array of type REAL) is the Y coordinate arrays for a polygon to be used as input to one of the routines PPDITR, PPINTR, or PPUNTR. PPPPAP will alter the contents of this array.
<dt>NCIP
<dd>(an input/output variable of type INTEGER) is the number of points defining the input polygon. PPPPAP may reduce the value of NCIP.
<dt>NBTS
<dd>(an input expression of type INTEGER) is the number of significant bits to be left unzeroed in the fractional part of each coordinate. Generally, one would probably not want to use a value less than 10 or 12. On a 32-bit machine on which reals have 24-bit fractions, 18 may be a good choice; on a 64-bit machine with 48-bit fractions, larger values may be desirable.</dl>

<h2>C-Binding Description</h2>

The C-binding argument descriptions are the same as the FORTRAN argument descriptions.

<h2>Usage</h2>

The FORTRAN statement 

 <pre> CALL PPPPAP (XCIP,YCIP,NCIP,NBTS)</pre>causes preprocessing of the X and Y coordinates of the points defining a polygon which is to be used as input to one of the principal POLYPACK routines that produce trapezoids. The object is to cure an annoying (but basically cosmetic) problem that sometimes occurs. 

 The nature of the problem is as follows: Sometimes, when adjacent points have Y coordinates that differ only very slightly, there will be, among the output trapezoids, degenerates, of essentially zero height, that stick out to the left or right from the body of the polygon of which each trapezoid is a part. This happens because, in the calls to the user-defined trapezoid-processing routine URPT, the values of DXLE and DXRE become very large and the difference between the values of YCOT and YCOB becomes very small; in URPT, then, to get the X coordinates at the ends of the top of the trapezoid, the very large values and the very small values are multiplied together and the result is highly inaccurate. 

 What PPPPAP does is this: Each of the input coordinates is first modified by zeroing out all but the first NBTS bits of its fractional part; then, any point with the same coordinates as the preceding point is culled. This ensures that there are no adjacent points with X or Y coordinates that are so nearly identical as to cause the observed problem, but has little real effect on the values of the coordinates. 

 There are several reasons why this was not done automatically: 1) Because it's a little time-consuming (zeroing the low-order bits in a way that doesn't violate the FORTRAN-77 standard is a bit difficult), it shouldn't be done if it doesn't have to be done, and the user may have reason to know that the problem doesn't arise. 2) The problem may arise in one of the polygons, but not the other (most likely, in the subject polygon, but not in the clip polygon). 3) The user knows best what precision needs to be maintained in the data.

<h2>Examples</h2>

Use the ncargex command to see the following relevant examples: ppex01, tppack, c_ppex01.

<h2>Access</h2>

To use PPPPAP or c_ppppap, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.

<h2>See Also</h2>

Online: polypack, ppdipo, ppditr, ppinpo, ppintr, ppplcl, ppunpo, ppuntr, ncarg_cbind. 

 Hardcopy: None.

<h2>Copyright</h2>

Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
