---
title: "ncl_ppdipo(3)"
name: "ncl_ppdipo"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_ppdipo/"
---

PPDIPO - generates and returns the boundary of the &quot;difference&quot; polygon, which consists of all points that are inside the subject polygon but not inside the clip polygon.

<h2>Synopsis</h2>

CALL PPDIPO (XCCP,YCCP,NCCP,XCSP,YCSP,NCSP,RWRK,IWRK,NWRK,URPP,IERR)

<h2>C-Binding Synopsis</h2>

#include &lt;ncarg/ncargC.h&gt; 

 <pre>void c_ppdipo(
 float *xccp,
 float *yccp,
 int nccp,
 float *xcsp,
 float *ycsp,
 int ncsp,
 float *rwrk,
 int *iwrk,
 int nwrk,
 int (*urpp_)( float *xcra, float *ycra, int *ncra),
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
<dd>(an input expression of type INTEGER) is the length of the workspace array(s). It is a bit difficult to describe how much space might be required. At the moment, I would recommend using NWRK equal to about ten times the total of the number of points in the input polygons and the number of intersection points. This situation will change with time; at the very least, I would like to put in an internal parameter that will tell one how much space was actually used on a given call, but I have not yet done so.
<dt>URPP
<dd>is the name of a user-provided routine to process the polygon-boundary pieces. This name must appear in an EXTERNAL statement in the routine that calls PPDIPO and the routine itself must have the following form: 

 <pre> SUBROUTINE URPP (XCRA,YCRA,NCRA)
 DIMENSION XCRA(NCRA),YCRA(NCRA)
 ...(code to process a polygon boundary piece)...
 RETURN
 END</pre>Each of the arguments XCRA and YCRA is a real array, dimensioned NCRA; the former holds the X coordinates, and the latter the Y coordinates, of a piece of the polygon boundary. It will be the case that XCRA(NCRA)=<a HREF="/docs/linux/man/1-xcra/">XCRA</a>(1) and YCRA(NCRA)=<a HREF="/docs/linux/man/1-ycra/">YCRA</a>(1).
<dt>IERR
<dd>(an output variable of type INTEGER) is returned with the value zero if no errors occurred in the execution of PPDIPO or with a small positive value if an error did occur. The value 1 indicates that a degenerate clip polygon was detected, the value 2 that a degenerate subject polygon was detected, and the value 3 that the workspace provided was too small; values greater than 3 should be reported to the author, as they indicate some problem with the algorithm. Currently, if IERR is returned non-zero, one can be sure that no calls to URPP were executed; in the future, this could change, but, in that case, there will be an internal parameter allowing one to request the current behavior.</dl>

<h2>C-Binding Description</h2>

The C-binding argument descriptions are the same as the FORTRAN argument descriptions.

<h2>Usage</h2>

The FORTRAN statement 

 <pre>CALL PPDIPO (XCCP,YCCP,NCCP,XCSP,YCSP,NCSP,RWRK,IWRK,NWRK,URPP,IERR)</pre>causes the formation of a difference polygon (the subject polygon minus the clip polygon) and the delivery of that polygon's boundary, piece by piece, to the user-specified polygon-processing routine URPP.

<h2>Examples</h2>

Use the ncargex command to see the following relevant examples: ppex01, tppack, c_ppex01.

<h2>Access</h2>

To use PPDIPO or c_ppdipo, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.

<h2>See Also</h2>

Online: polypack, ppditr, ppinpo, ppintr, ppplcl, ppppap, ppunpo, ppuntr, ncarg_cbind. 

 Hardcopy: None.

<h2>Copyright</h2>

Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
