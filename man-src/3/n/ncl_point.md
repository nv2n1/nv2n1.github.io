---
title: "ncl_point(3)"
name: "ncl_point"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_point/"
---

POINT - draws a point at a specified position in the user coordinate system.

<h2>Synopsis</h2>

CALL POINT (PX,PY)

<h2>C-Binding Synopsis</h2>

#include &lt;ncarg/ncargC.h&gt; 

 void c_point (float px, float py)

<h2>Description</h2>

<dl><dt>PX
<dd>(an input expression of type REAL) defines the X user coordinate where the dot is to be drawn.
<dt>PY
<dd>(an input expression of type REAL) defines the Y user coordinate where the dot is to be drawn.</dl>

<h2>C-Binding Description</h2>

The C-binding argument descriptions are the same as the FORTRAN argument descriptions.

<h2>Usage</h2>

If one desires a filled dot of arbitrary size see the routine NGDOTS. 

 The GKS routine GPM can also be used to draw a dot in world coordinates; however, NCAR Graphics user coordinates allow for mirror imaging of axes and logarithmic axes which GKS does not. See the SCD User Doc &quot;NCAR Graphics Fundamentals, UNIX Version&quot; for a description of these coordinate systems.

<h2>Examples</h2>

Use the ncargex command to see the following relevant examples: tareas.

<h2>Access</h2>

To use POINT or c_point, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.

<h2>See Also</h2>

Online: gpm, gsmk, gsmksc, gscr, gspmci, spps, spps_params, plotif, ngdots, points, ncarg_cbind 

 Hardcopy: NCAR Graphics Fundamentals, UNIX Version; User's Guide for NCAR GKS-0A Graphics

<h2>Copyright</h2>

Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
