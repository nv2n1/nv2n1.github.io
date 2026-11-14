---
title: "ncl_ezcntr(3)"
name: "ncl_ezcntr"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_ezcntr/"
---

EZCNTR - draws a two dimensional contour map from data stored in a rectangular array. A number of contouring defaults are used. 

<h2>Status</h2>EZCNTR is obsolete. It has been superseded by the contouring package, Conpack. See the Conpack entry CPCNRC for a simple EZCNTR replacement. For more complex examples refer to the conpack and conpack_params man pages as well as the NCAR Graphics Contouring and Mapping Tutorial. 

 EZCNTR continues to be provided for compatibility of early NCAR Graphics codes. If you are writing new code, we suggest that you use the more general and rigorous Conpack contouring package. All EZCNTR options set by default can be duplicated by the proper selection of Conpack parameters.
<h2>Synopsis</h2>CALL EZCNTR(Z,M,N) - draws a contour map based upon a set of default options.
<h2>Description</h2><dl COMPACT><dt>Z
<dd>(an input array of type REAL) defining a two-dimensional field of extent M by N, which is to be contoured.
<dt>M
<dd>(an input parameter of type INTEGER) which is the first dimension of the Z array.
<dt>N
<dd>(an input parameter of type INTEGER) which is the second dimension of the Z array.</dl><h2>Examples</h2>Use the ncargex command to see the relevant examples tconre, tcnqck, tcnsmt, and tcnsup.
<h2>Access</h2>EZCNTR can be invoked in four different ways to create contour plots which vary considerably in appearance. The four variations include quick, normal, smooth, and super contour lines. This progression represents a tradeoff between speed of computation and the appearance of the contour plots. These variations are specified through selected command line options of the ncargf77 command. 

 To use EZCNTR, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order. Other optional libraries to create the quick, smooth, and super contours will automatically be linked by the ncargf77 command. To run a code called mycode.f which has one or more calls to entry EZCNTR, issue one of the commands: 

<dl COMPACT><dt>NORMAL
<dd>Command: &quot;ncargf77 mycode.f&quot; 

 The contours will be drawn as unsmoothed dashed or solid lines that can include characters along the lines. 

<dt>QUICK
<dd>Command: &quot;ncargf77 -quick mycode.f&quot; 

 The contours will be drawn as unsmoothed dashed or solid lines without characters along the lines. The QUICK drawing algorithm is faster and cruder than that used for NORMAL contour lines. QUICK uses a cell-by-cell analysis rather than following each contour line to completion in sequence as is done in the NORMAL algorithm. 

<dt>SMOOTH
<dd>Command: &quot;ncargf77 -smooth mycode.f&quot; 

 The contours will be drawn as smoothed dashed or solid lines using splines under tension. There may be characters along the lines. 

<dt>SUPER
<dd>Command: &quot;ncargf77 -super mycode.f&quot; 

 The contours will be drawn as smoothed dashed or solid lines using splines under tension. There may be characters along the lines. Crowded lines can be thinned.</dl><h2>Messages</h2>When error conditions are detected, the support routine SETER is called in such a way that it writes a message to the standard error file (as defined by <a HREF="/docs/linux/man/4-i1mach/">I1MACH</a>(4)) and then terminates execution. The possible error messages are as follows: 

 CONREC - DIMENSION ERROR - M*N .GT. (2**IARTH) 
 The array to be contoured is dimensioned M by N. This is larger than the address space on this computer (2**IARTH) where IARTH is the size of an address integer. Check your dimension sizes.
<h2>See Also</h2>Online: conrec, conrec_family_params, conrec_family, conpack, conpack_params, cpcnrc, ncargf77 

 Hardcopy: NCAR Graphics Contouring and Mapping Tutorial; NCAR Graphics Fundamentals, UNIX Version; User's Guide for NCAR GKS-0A Graphics
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
