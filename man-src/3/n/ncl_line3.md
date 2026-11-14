---
title: "ncl_line3(3)"
name: "ncl_line3"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_line3/"
---

LINE3 - Draws the straight-line segment joining the projections of two points in 3-space. 

<h2>Synopsis</h2>CALL LINE3 (UA,VA,WA,UB,VB,WB)
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/ncargC.h&gt; 

 void c_line3 (float ua, float va, float wa, float ub, 
 float vb, float wb)
<h2>Description</h2><dl COMPACT><dt>UA,VA,WA
<dd>(input expressions of type REAL) are the coordinates of the first point in 3-space.
<dt>UB,VB,WB
<dd>(input expressions of type REAL) are the coordinates of the second point in 3-space.</dl>
 

 The statement &quot;CALL LINE3 (UA,VA,WA,UB,VB,WB)&quot; is equivalent to the three statements &quot;CALL FRST3 (UA,VA,WA)&quot;, &quot;CALL VECT3 (UB,VB,,WB)&quot;, and &quot;CALL PLOTIF (0.,0.,2), but is slightly more efficient. To approximate a curve defined by three or more points, though, it is not efficient to use LINE3, because the first point of each line segment after the first will be a repeat of the second point of the previous line segment and will therefore be repeated in the metafile. Thus, to approximate a curve, you should use FRST3 and VECT3 or CURVE3. 

 Straight-line segments drawn by LINE3 are drawn in the current polyline color, as determined by the last call to the GKS routine GSPLCI; by default, color index 1 is used. Line width is determined by the last call to the GKS routine GSLWSC; by default, the line width scale factor is 1.
<h2>C-Binding Description</h2>The C-binding argument descriptions are the same as the FORTRAN argument descriptions.
<h2>Examples</h2>Use the ncargex command to see the following relevant example: tpwrzt, fthex02.
<h2>Access</h2>To use LINE3 or c_line3, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.
<h2>See Also</h2>Online: threed, curve3, fence3, frst3, perim3, point3, psym3, pwrz, pwrzt, set3, threed, tick3, tick43, vect3, ncarg_cbind. 

 Hardcopy: NCAR Graphics Fundamentals, UNIX Version
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
