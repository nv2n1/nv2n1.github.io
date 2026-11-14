---
title: "ncl_isosurface(3)"
name: "ncl_isosurface"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_isosurface/"
---

Isosurface - Allows the user to draw a perspective view of the surface defined by the equation f(u,v,w)=fiso, where the function f is approximated by a 3-dimensional array of data and fiso is a user-specified &quot;isovalue&quot;. Contours created by taking slices in any of three directions through the surface are drawn with hidden portions of the contour lines removed. 

<h2>Synopsis</h2>EZISOS - May be called to draw an isosurface. 

 ISOSRF - May be called to draw an isosurface. 

 ISGETI - Retrieves the current values of various internal parameters affecting the behavior of ISOSRF. 

 ISGETR - Retrieves the current values of various internal parameters affecting the behavior of ISOSRF. 

 ISSETI - Gives new values to internal parameters. 

 ISSETR - Gives new values to internal parameters. 

 PWRZI - Plots characters in three-space when using ISOSRF.
<h2>C-Binding Synopsis</h2>c_ezisos, 
 c_isosrf, 
 c_isgeti, 
 c_isgetr, 
 c_isseti, 
 c_issetr, 
 c_pwrzi
<h2>User-Modifiable Internal Routines</h2>None.
<h2>Access</h2>To use Isosurface, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.
<h2>Messages</h2>The error messages described below can be written to the output unit by routines in the package Isosurface. All of these errors are fatal and cause the user's program to terminate execution (on the other hand, all of the errors are easily avoided).
<dl COMPACT><dt>ISGETI OR ISGETR - PARAMETER NAME TOO SHORT - x
<dd>The argument &quot;PNAM&quot;, in a call to ISGETI or ISGETR, is only one character long.
<dt>ISGETI OR ISGETR - PARAMETER NAME NOT KNOWN - xx
<dd>The argument &quot;PNAM&quot;, in a call to ISGETI or ISGETR, begins with two characters that do not constitute one of the legal internal parameter names described in the man page isosurface_params.
<dt>ISSETI OR ISSETR - PARAMETER NAME TOO SHORT - x
<dd>The argument &quot;PNAM&quot;, in a call to ISSETI or ISSETR, is only one character long.
<dt>ISSETI OR ISSETR - PARAMETER NAME NOT KNOWN - xx
<dd>The argument &quot;PNAM&quot;, in a call to ISSETI or ISSETR, begins with two characters that do not constitute one of the legal internal parameter names described in the man page isosurface_params.
<dt>ISINIT - INSTALLATION OF ISOSRF IMPROPERLY DONE
<dd>This error message means that the screen models used to do hidden-line removal have been found to be improperly dimensioned for the system on which the code is being run. About the only way this can happen is if the distributed code is run on a a machine with sixteen-bit words or if the distributed code has been modified incorrectly.</dl><h2>See Also</h2>Online: isosurface_params, ezisos, isgeti, isgetr, isosrf, isseti, issetr, pwrzi, ncarg_cbind 

 Hardcopy: NCAR Graphics Fundamentals, UNIX Version
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
