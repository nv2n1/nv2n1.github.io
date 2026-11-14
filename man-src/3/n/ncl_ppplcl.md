---
title: "ncl_ppplcl(3)"
name: "ncl_ppplcl"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_ppplcl/"
---

PPPLCL - clips a polyline against a clipping rectangle. It is intended that, eventually, there should be a better routine that will clip a polyline against an arbitrary polygon, but that routine has not yet been written.

<h2>Synopsis</h2>

CALL PPPLCL (XMIN,XMAX,YMIN,YMAX,XCPL,YCPL,NCPL,RWRK,LRWK,URPF,IERR)

<h2>C-Binding Synopsis</h2>

#include &lt;ncarg/ncargC.h&gt; 

 <pre>void c_ppplcl(float xmin,
 float xmax,
 float ymin,
 float ymax,
 float *xcpl,
 float *ycpl,
 int ncpl,
 float *rwrk,
 int lwrk,
 int (*urpf_)(float *xcra,
 float *ycra,
 int *ncra),
 int *ierr)</pre>

<h2>Description</h2>

<dl><dt>XMIN
<dd>(an input expression of type REAL) is the X coordinate value defining the position of the left edge of the clipping rectangle.
<dt>XMAX
<dd>(an input expression of type REAL) is the X coordinate value defining the position of the right edge of the clipping rectangle.
<dt>YMIN
<dd>(an input expression of type REAL) is the Y coordinate value defining the position of the bottom of the clipping rectangle.
<dt>YMAX
<dd>(an input expression of type REAL) is the Y coordinate value defining the position of the top of the clipping rectangle.
<dt>XCPL
<dd>(an input array of type REAL) is the X coordinate array for the polyline that is to be clipped.
<dt>YCPL
<dd>(an input array of type REAL) is the Y coordinate array for the polyline that is to be clipped.
<dt>NCPL
<dd>(an input expression of type INTEGER) is the number of points defining the input polyline (the number of meaningful elements in each of the arrays XCPL and YCPL).
<dt>RWRK
<dd>(a scratch array of type REAL) is a workspace array for PPPLCL to use. It is divided into halves; one half is used for X coordinates and the other half for Y coordinates. This array doesn't have to be too big unless it is important not to break the polyline except at the edges of the clipping rectangle.
<dt>LRWK
<dd>(an input expression of type INTEGER) is the length of the array RWRK.
<dt>URPF
<dd>is the name of a user-provided routine to process the fragments of the polyline resulting from the clipping process. This name must appear in an EXTERNAL statement in the routine that calls PPPLCL and the routine itself must have the following form: 

 <pre> SUBROUTINE URPF (XCRA,YCRA,NCRA)
 DIMENSION XCRA(NCRA),YCRA(NCRA)
 ...(code to process a polyline)...
 RETURN
 END</pre>Each of the arguments XCRA and YCRA is a real array, dimensioned NCRA; the former holds the X coordinates, and the latter the Y coordinates, of a polyline fragment.
<dt>IERR
<dd>(an output variable of type INTEGER) is returned with the value zero if no errors occurred in the execution of PPPLCL or with a small positive value if an error did occur. The value 1 indicates that NCPL is less than or equal to zero and the value 2 indicates that LRWK is less than 4.</dl>

<h2>C-Binding Description</h2>

The C-binding argument descriptions are the same as the FORTRAN argument descriptions.

<h2>Usage</h2>

The FORTRAN statement 

 <pre>CALL PPPLCL (XMIN,XMAX,YMIN,YMAX,XCPL,YCPL,NCPL,RWRK,LRWK,URPF,IERR) </pre>clips a polyline against a rectangle and delivers the portions of the polyline that fall within the rectangle, one by one, to the user-specified polyline-fragment-processing routine URPF.

<h2>Examples</h2>

Use the ncargex command to see the following relevant examples: ppex01, tppack, c_ppex01.

<h2>Access</h2>

To use PPPLCL or c_ppplcl, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.

<h2>See Also</h2>

Online: polypack, ppdipo, ppditr, ppinpo, ppintr, ppppap, ppunpo, ppuntr, ncarg_cbind. 

 Hardcopy: None.

<h2>Copyright</h2>

Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
