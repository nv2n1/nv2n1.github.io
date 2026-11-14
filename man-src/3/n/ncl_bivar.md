---
title: "ncl_bivar(3)"
name: "ncl_bivar"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_bivar/"
---

Bivar - Provides bivariate interpolation and smooth surface fitting for values given at irregularly distributed points. The resulting interpolating function and its first-order partial derivatives are continuous. The method employed is local, i.e. a change in the data in one area of the plane does not affect the interpolating function except in that local area. Also, the method gives exact results when all points lie in a plane. 

<h2>Synopsis</h2><dl COMPACT><dt>IDBVIP
<dd>Produces interpolated values at points (XI(I), YI(I)), I=1,...,NIP. This is useful for filling in missing data points on a grid.
<dt>IDSFFT
<dd>Performs smooth surface fitting when the projections of the data points in the X-Y plane are irregularly distributed in the plane.
<dt>IDPLTR
<dd>Plots the triangulation of the data points.
<dt>IDGETI
<dd>Retrieves the integer value of a Bivar parameter.
<dt>IDGETR
<dd>Retrieves the real value of a Bivar parameter.
<dt>IDSETI
<dd>Provides a new integer value for a Bivar parameter.
<dt>IDSETR
<dd>Provides a new real value for a Bivar parameter.</dl><h2>C-Binding Synopsis</h2>c_idbvip, 
 c_idsfft 
 c_idpltr 
 c_idgeti 
 c_idgetr 
 c_idseti 
 c_idsetr
<h2>Examples</h2>See the example &quot;cbex01&quot;.
<h2>Access</h2>To use the Bivar Fortran or C routines, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order. 

<h2>Messages</h2>When error conditions are detected, the support routine SETER is called. By default, SETER writes a message to the standard error file (as defined by <a HREF="/docs/linux/man/4-i1mach/">I1MACH</a>(4)) and then terminates execution. It is possible to put SETER into recovery mode and regain control after a recoverable error (which includes all of the possible errors). 

 The possible error messages are listed below. All errors are recoverable in the sense that a user program which has called ENTSR to set recovery mode will get control back after one of these errors occurs. 

 IDBVIP (BIVAR) - UNCLEARED PRIOR ERROR 

 IDBVIP (BIVAR) - INPUT VARIABLE MD IS OUT OF RANGE 

 IDBVIP (BIVAR) - INPUT VARIABLE NDP IS OUT OF RANGE 

 IDBVIP (BIVAR) - INPUT VARIABLE NIP IS OUT OF RANGE 

 IDBVIP (BIVAR) - MD = 2 OR 3 BUT NDP WAS CHANGED SINCE LAST CALL 

 IDBVIP (BIVAR) - MD = 3 BUT ITY WAS CHANGED SINCE LAST CALL 

 IDBVIP (BIVAR) - MD = 3 BUT NIP WAS CHANGED SINCE LAST CALL 

 IDGETI (BIVAR) - UNCLEARED PRIOR ERROR 

 IDGETR (BIVAR) - UNCLEARED PRIOR ERROR 

 IDGETR (BIVAR) - INVALID KEYWORD: xxx 

 IDGRID (BIVAR) - INTERNAL ERROR - SEE CONSULTANT 

 IDPLTR (BIVAR) - UNCLEARED PRIOR ERROR 

 IDSETI (BIVAR) - UNCLEARED PRIOR ERROR 

 IDSETR (BIVAR) - UNCLEARED PRIOR ERROR 

 IDSETR (BIVAR) - INVALID KEYWORD: xxx 

 IDSFFT (BIVAR) - UNCLEARED PRIOR ERROR 

 IDSFFT (BIVAR) - INPUT VARIABLE MD IS OUT OF RANGE 

 IDSFFT (BIVAR) - INPUT VARIABLE NDP IS OUT OF RANGE 

 IDSFFT (BIVAR) - INPUT VARIABLE NXI OR NYI IS OUT OF RANGE 

 IDSFFT (BIVAR) - INPUT VARIABLE NZI IS LESS THAN NXI 

 IDSFFT (BIVAR) - MD = 2 OR 3 BUT NDP WAS CHANGED SINCE LAST CALL 

 IDSFFT (BIVAR) - MD = 3 BUT ITY WAS CHANGED SINCE LAST CALL 

 IDSFFT (BIVAR) - MD = 3 BUT NXI WAS CHANGED SINCE LAST CALL 

 IDSFFT (BIVAR) - MD = 3 BUT NYI WAS CHANGED SINCE LAST CALL 

 IDTANG (BIVAR) - INPUT PARAMETER NDP OUT OF RANGE 

 IDTANG (BIVAR) - TWO OF THE INPUT DATA POINTS ARE IDENTICAL 

 IDTANG (BIVAR) - ALL COLLINEAR DATA POINTS
<h2>See Also</h2>Online: bivar_params, idbvip, idsfft, idpltr, idgeti, idgetr, idseti, idsetr, ncarg_cbind 

 Hardcopy: NCAR Graphics Contouring and Mapping Tutorial; NCAR Graphics Fundamentals, UNIX Version
<h2>Acknowledgments</h2>Bivar was written by Hiroshi Akima in August 1975 and rewritten by him in late 1976. In 1989, a new version of Bivar, incorporating changes described in a Rocky Mountain Journal of Mathematics was obtained from Dr. Akima, and included in NCAR Graphics with his permission. In 1995, Dave Kennison incorporated the capability of doing linear interpolation and a different kind of triangulation, put in a parameter access interface, and wrote a routine to allow the triangulation to be plotted.
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
