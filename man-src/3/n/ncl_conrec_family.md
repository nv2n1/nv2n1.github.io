---
title: "ncl_conrec_family(3)"
name: "ncl_conrec_family"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_conrec_family/"
---

Conrec_family - is a set of two dimensional contour mapping routines. There are options for generating standard contours, smoothing contour lines, labeling the contours, and removing crowded lines. 

<h2>Status</h2>Conrec_family is obsolete. It has been replaced by the contouring package, Conpack. See the Conpack entry CPCNRC for a simple CONREC replacement. For more complex examples refer to the conpack and conpack_params man pages as well as the NCAR Graphics Contouring and Mapping Tutorial. 

 Conrec_family continues to be provided for compatibility of early NCAR Graphics codes. If you are writing new code, we suggest that you use the more general and rigorous Conpack contouring package. All Conrec_family options are available via Conpack parameters.
<h2>Synopsis</h2>EZCNTR(Z,M,N) - draws a contour map based upon a set of default options. 
 CONREC(Z,L,M,N,FLO,HI,FINC,NSET,NHI,NDOT) - draws a contour map using options specified as input arguments.
<h2>Access</h2>The Conrec family contains only two user callable entries, EZCNTR, and CONREC. However, these two entries can be invoked in four different ways to create contour plots which vary considerably in appearance. The four variations include quick, normal, smooth, and super contour lines. This progression represents a tradeoff between speed of computation and the appearance of the contour plots. These variations are specified through selected command line options of the ncargf77 command. 

 To use EZCNTR or CONREC, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order. Other optional libraries to create the quick, smooth, and super contours will automatically be linked by the ncargf77 command. To run a code called mycode.f which has one or more calls to entry EZCNTR or CONREC, issue one of the commands: 

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

 STLINE - WARNING FROM ROUTINE STLINE IN CONREC--WORK ARRAY OVERFLOW 
 This warning message is printed to standard output if the number of contour lines for a contour level would exceed the dimension size of work array IR in routine STLINE. 

 Should this happen the following messages are also sent to the output plot file: 

 **WARNING--PICTURE INCOMPLETE** 
 WORK ARRAY OVERFLOW IN STLINE 

 Processing stops before the actual array overflow occurs and control is returned to the calling program.
<h2>See Also</h2>Online: conrec, ezcntr, conrec_family_params, conpack, conpack_params, cpcnrc, dashline_family, ncargf77 

 Hardcopy: NCAR Graphics Contouring and Mapping Tutorial; NCAR Graphics Fundamentals, UNIX Version; User's Guide for NCAR GKS-0A Graphics
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
