---
title: "ncl_ppintr(3)"
name: "ncl_ppintr"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_ppintr/"
---

PPINTR - generates and returns a set of trapezoids representing the interior of the &quot;intersection&quot; polygon, which consists of all points that are inside both the clip polygon and the subject polygon.

<h2>Synopsis</h2>

CALL PPINTR (XCCP,YCCP,NCCP,XCSP,YCSP,NCSP,RWRK,IWRK,NWRK,URPT,IERR)

<h2>C-Binding Synopsis</h2>

#include &lt;ncarg/ncargC.h&gt; 

 <pre>void c_ppintr(
 float *xccp,
 float *yccp,
 int nccp,
 float *xcsp,
 float *ycsp,
 int ncsp,
 float *rwrk,
 int *iwrk,
 int nwrk,
 int (*urpt_)(float *xcbl,
 float *xcbr,
 float *ycob,
 float *dxle,
 float *dxre,
 float *ycot),
 int *ierr)</pre>

<h2>Description</h2>

<dl><dt>XCCP
<dd>(an input array of type REAL) is the X coordinate array for the clip polygon.
<dt>YCCP
<dd>(an input array of type REAL) is the Y coordinate array for the clip polygon.
<dt>NCCP
<dd>(an input expression of type INTEGER) is the number of points defining the clip polygon.
<dt>XCSP
<dd>(an input array of type REAL) is the X coordinate array for the subject polygon.
<dt>YCSP
<dd>(an input array of type REAL) is the Y coordinate array for the subject polygon.
<dt>NCSP
<dd>(an input expression of type INTEGER) is the number of points defining the subject polygon.
<dt>RWRK
<dd>(a scratch array, dimensioned NWRK, of type REAL) is a real workspace array. Because of the way in which they are used, RWRK and IWRK may be EQUIVALENCEd (and, to save space, they should be).
<dt>IWRK
<dd>(a scratch array, dimensioned NWRK, of type INTEGER) is an integer workspace array. Because of the way in which they are used, RWRK and IWRK may be EQUIVALENCEd (and, to save space, they should be).
<dt>NWRK
<dd>(an input expression of type INTEGER) is the length of the workspace array(s). The routines that produce trapezoids use a lot less workspace than the ones that produce polygons. The amount of space used at a particular time during the execution of one of these routines is roughly ten or eleven times the number of intersections of a horizontal &quot;scan line&quot; with the edge segments making up the input polygons, plus about three times the number of points above the current scan line that are &quot;local minima&quot;. (A &quot;local minimum&quot; is a point on one of the polygons that is connected to two other points on the polygon having larger Y coordinates than its own). I have not yet developed a rule of thumb for setting the value of NWRK. Ultimately, I would like to at least put in an internal parameter that will tell one how much space was actually used on a given call, but I have not yet done so.
<dt>URPT
<dd>is the name of a user-provided routine to process the trapezoids. This name must appear in an EXTERNAL statement in the routine that calls PPINTR and the routine itself must have the following form: 

 <pre> SUBROUTINE URPP (XCBL,XCBR,YCOB,DXLE,DXRE,YCOT)
 ...(code to process a trapezoid)...
 RETURN
 END</pre>The bottom and top of the trapezoid are horizontal (parallel to the X axis); the arguments XCBL and XCBR define the X coordinates of its bottom left and bottom right corners, YCOB is the Y coordinate of its bottom edge, DXLE and DXRE are the inverses (dx/dy) of the slopes of its left and right edges, and YCOT is the Y coordinate of its top edge. The corners of the trapezoid are therefore as follows: (XCBL,YCOB), (XCBR,YCOB), (XCBL+DXLE*(YCOT-YCOB),YCOT), and (XCBR+DXRE*(YCOT-YCOB),YCOT).
<dt>IERR
<dd>(an output variable of type INTEGER) is returned with the value zero if no errors occurred in the execution of PPINTR or with a small positive value if an error did occur. The value 1 indicates that a degenerate clip polygon was detected, the value 2 that a degenerate subject polygon was detected, and the value 3 that the workspace provided was too small; values greater than 3 should be reported to the author, as they probably indicate some problem with the algorithm. If IERR is returned non-zero, one can be sure that there have been no calls to URPT only if IERR = 1 or 2; otherwise, some trapezoids probably have been generated and delivered to URPT.</dl>

<h2>C-Binding Description</h2>

The C-binding argument descriptions are the same as the FORTRAN argument descriptions.

<h2>Usage</h2>

The FORTRAN statement 

 <pre>CALL PPINTR (XCCP,YCCP,NCCP,XCSP,YCSP,NCSP,RWRK,IWRK,NWRK,URPT,IERR)</pre>causes the formation of an intersection polygon (of the subject and clip clip polygons) and the delivery of trapezoids representing the interior of that polygon, one at a time, to the user-specified trapezoid-processing routine URPT.

<h2>Examples</h2>

Use the ncargex command to see the following relevant examples: ppex01, tppack, c_ppex01.

<h2>Access</h2>

To use PPINTR or c_ppintr, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.

<h2>See Also</h2>

Online: polypack, ppdipo, ppditr, ppinpo, ppplcl, ppppap, ppunpo, ppuntr, ncarg_cbind. 

 Hardcopy: None.

<h2>Copyright</h2>

Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
