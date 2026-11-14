---
title: "ncl_spps_params(3)"
name: "ncl_spps_params"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_spps_params/"
---

SPPS_params - This document briefly describes all of the internal parameters of SPPS.

<h2>Description</h2>

In calls to GETUSV and SETUSV, which are used to access the internal parameters of SPPS, the arguments VN and IV are as follows: 

<dl><dt>VN
<dd>(an input constant or variable of type CHARACTER) is the name of a parameter; only the first two characters are meaningful. Remember that, in FORTRAN, a constant of type CHARACTER is a string of characters enclosed in apostrophes. 

<dt>IV
<dd>(an input or output value of type INTEGER), is either the returned current value of the parameter specified by VN or the desired new value of that parameter, as described in the following table: <pre>Parameter Description Possible Values of IV
Name (VN)
--------- ----------- ---------------------
 'LS' Axis scaling 1 = linear X, linear Y
 (&quot;Log Scaling&quot; flag) 2 = linear X, log Y
 3 = log X, linear Y
 4 = log X, log Y
 'MI' Axis direction reversal 1 = neither X nor Y
 (&quot;MIrroring&quot; flag - axis 2 = X, but not Y
 from maximum to minimum 3 = Y, but not X
 rather than min to max) 4 = both X and Y
 'MU' Metacode output Unit 2
 'PB' Pen-move Buffer size 2 to 50</pre>Both 'LS' and 'MI' are normally set by calling the routine SET, but can be set independently by calling SETUSV. 

 The parameter 'MU' is set, prior to calling OPNGKS, to change the FORTRAN logical unit number to be used by GKS for metacode output. 

 The parameter 'PB' sets the size of the SPPS polyline buffer. The value &quot;2&quot; effectively turns buffering off. <pre>Obsolete Description
parameters
---------- -----------
 'XF' X axis exponent for plotter coordinates
 (The PAU range would be 1 to 2**XF - 1 in X)
 'YF' Y axis exponent for plotter coordinates
 (The PAU range would be 1 to 2**YF - 1 in Y)
 'IR' Red color intensity (relative to green and blue)
 'IG' Green color intensity (relative to red and blue)
 'IB' Blue color intensity (relative to red and green)
 'IM' Maximum color index to be used
 'IN' Overall color intensity
 'II' Restore color index
 'LW' Line width scale factor in thousandths
 (2000 means double the default line width)
 'MS' Marker size in thousandths
 (2000 means double the default marker size)</pre>The values of the parameters 'XF' and 'YF' are the same as the values of the arguments IX and IY in calls to the routines SETI and GETSI. 

 The parameters 'IR', 'IG', 'IB', 'IM', 'IN', and 'II' were all part of a color-setting scheme meant to allow overall intensity to be set independently of color. This scheme is now obsolete; it has been replaced by normal GKS color setting through the routines GSCR, GSPLCI, GSFACI, GSPMCI, and GSTXCI. The corresponding GKS inquiry routines to determine current color settings are GQCR, GQPLCI, GQFACI, GQPMCI, and GQTXCI. See Section 6 of &quot;User's Guide for NCAR GKS-0A Graphics.&quot; 

 The parameter 'LW' is replaced by the GKS line width scale factor routine, GSLWSC, which has the corresponding query function GQLWSC. 

 The parameter 'MS' is replaced by the GKS marker size scale factor routine, GSMKSC, which has the corresponding query function GQMKSC.</dl>

<h2>Usage</h2>

Values of SPPS parameters are set by calling the routine SETUSV and retrieved by calling the routine GETUSV.

<h2>See Also</h2>

Online: gscr,gsplci, gsfaci, gspmci, gstxci, gsmksc, gslwsc, spps, getset, getsi, getusv, plotif, set, setsi, setusv 

 Hardcopy: NCAR Graphics Fundamentals, UNIX Version; User's Guide for NCAR GKS-0A Graphics

<h2>Copyright</h2>

Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
