---
title: "ncl_plotit(3)"
name: "ncl_plotit"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_plotit/"
---

PLOTIT - A line-drawing routine, described in terms of &quot;pen moves&quot;. Most calls to PLOTIT specify whether the &quot;pen&quot; should be up (not drawing) or down (drawing) and then move it to a designated position in the metacode coordinate system. The polylines resulting from the pen moves are buffered; some calls to PLOTIT just cause the SPPS polyline buffer to be flushed.

<h2>Status</h2>

Metacode units are no longer used in NCAR Graphics; thus, PLOTIT is considered an obsolete routine. 

 The current recognized coordinate systems are GKS world coordinates, GKS normalized device coordinates, NCAR Graphics fractional coordinates, and NCAR Graphics user coordinates. See the NCAR Graphics User Document &quot;NCAR Graphics Fundamentals, UNIX Version&quot; for a description of these coordinate systems. 

 PLOTIT continues to be provided for compatibility of early NCAR Graphics codes. If you are writing new code, we suggest that you use the routine PLOTIF which uses fractional coordinates. 

 The following definition of the Metacode Coordinate System is included for the purpose of interpreting and converting codes: 

 The metacode coordinates of a point are integers IMX and IMY between 0 and 32767 inclusive. The area addressed is a square in a &quot;metacode space&quot; that is usually mapped into a square subset of the addressable area of the plotting device. Metacode coordinates were used in calls to the routine PLOTIT and are returned in calls to FL2INT.

<h2>Synopsis</h2>

CALL PLOTIT (IX,IY,IP)

<h2>C-Binding Synopsis</h2>

#include &lt;ncarg/ncargC.h&gt; 

 void c_plotit(int ix, int iy, int ip);

<h2>Description</h2>

<dl><dt>IX
<dd>(an input expression of type INTEGER) is the X metacode coordinate of the point to which the plotter pen is to be moved.
<dt>IY
<dd>(an input expression of type INTEGER) is the Y metacode coordinate of the point to which the plotter pen is to be moved.
<dt>IP
<dd>(an input expression of type INTEGER) determines whether the movement of the plotter pen to the point (IX,IY) will occur with the pen up (IP = 0), or with the pen down (IP = 1). If IP = 2, no pen move occurs, but the SPPS polyline buffer is flushed. For historical reasons, a &quot;CALL PLOTIT (0,0,0)&quot; will also flush the buffer. 

 The size of the SPPS polyline buffer can be changed by calling the parameter-setting routine SETUSV to set the parameter 'PB'. The legal range of 'PB' is between 2 and 50. For example, to set 'PB' to 2, use &quot;CALL SETUSV ('PB',2)&quot;. 

 The SPPS polyline buffer is provided to increase drawing efficiency.</dl>

<h2>C-Binding Description</h2>

The C-binding argument descriptions are the same as the FORTRAN argument descriptions.

<h2>Access</h2>

To use PLOTIT or c_plotit, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.

<h2>See Also</h2>

Online: gpl, fl2int, plotif, setusv, getusv, sflush, frstpt, vector, line, curve, spps, spps_converters 

 Hardcopy: NCAR Graphics Fundamentals, UNIX Version; User's Guide for NCAR GKS-0A Graphics

<h2>Copyright</h2>

Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
