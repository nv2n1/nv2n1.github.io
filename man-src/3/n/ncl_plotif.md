---
title: "ncl_plotif(3)"
name: "ncl_plotif"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_plotif/"
---

PLOTIF - A line-drawing routine, described in terms of &quot;pen moves&quot;. Most calls to PLOTIF specify whether the &quot;pen&quot; should be up (not drawing) or down (drawing) and then move it to a designated position in the fractional coordinate system. The polylines resulting from the pen moves are buffered; some calls to PLOTIF just cause the SPPS polyline buffer to be flushed.

<h2>Synopsis</h2>

CALL PLOTIF (FX,FY,IP)

<h2>C-Binding Synopsis</h2>

#include &lt;ncarg/ncargC.h&gt; 

 void c_plotif (float fx, float fy, int ip)

<h2>Description</h2>

<dl><dt>FX
<dd>(an input expression of type REAL) is the X fractional coordinate of the point to which the plotter pen is to be moved. If IP = 2, this argument is ignored.
<dt>FY
<dd>(an input expression of type REAL) is the Y fractional coordinate of the point to which the plotter pen is to be moved. If IP = 2, this argument is ignored.
<dt>IP
<dd>(an input expression of type INTEGER) determines whether the movement of the plotter pen to the point (FX,FY) will occur with the pen up (IP = 0), or with the pen down (IP = 1). If IP = 2, no pen move occurs, but the SPPS polyline buffer is flushed.</dl>

<h2>C-Binding Description</h2>

The C-binding argument descriptions are the same as the FORTRAN argument descriptions.

<h2>Usage</h2>

&quot;CALL PLOTIF (FX,FY,0)&quot; moves the pen to a new starting position. 

 &quot;CALL PLOTIF (FX,FY,1)&quot; moves the pen to a new position, drawing a straight line segment from the previous position to the new one. 

 &quot;CALL PLOTIF (0.,0.,2)&quot; flushes the SPPS polyline buffer. 

 The size of the SPPS polyline buffer can be changed by calling the parameter-setting routine SETUSV to set the parameter 'PB'. The legal range of 'PB' is between 2 and 50. For example, to set 'PB' to 2, use &quot;CALL SETUSV ('PB',2)&quot;. 

 NOTE! 

 The SPPS polyline buffer is provided to increase drawing efficiency. However, there are side effects that can occur because the polyline segments get buffered. For example, if one wanted to change the color of a line at a certain point, one would have to remember to flush the buffer before calling GSPLCI to change the polyline color index. This applies to the changing of any polyline attribute.

<h2>Examples</h2>

Use the ncargex command to see the following relevant examples: arex01, cbex01, cmppos, coex03, cpexcc, epltch.

<h2>Access</h2>

To use PLOTIF or c_plotif, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.

<h2>See Also</h2>

Online: gpl, plotit, setusv, getusv, sflush, frstpt, vector, line, curve, spps, spps_params, ncarg_cbind 

 Hardcopy: NCAR Graphics Fundamentals, UNIX Version; User's Guide for NCAR GKS-0A Graphics

<h2>Copyright</h2>

Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
