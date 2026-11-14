---
title: "ncl_set(3)"
name: "ncl_set"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_set/"
---

SET - defines the mapping between fractional and user coordinates: sets the values of the SPPS internal parameters 'LS' (axis linear/log scaling) and 'MI' (axis mirror imaging); defines GKS normalization transformation 1.

<h2>Synopsis</h2>

CALL SET(VL,VR,VB,VT,WL,WR,WB,WT,LF)

<h2>C-Binding Synopsis</h2>

#include &lt;ncarg/ncargC.h&gt; 

 void c_set(float vl, float vr, float vb, float vt, float wl, float wr, float wb, float wt, int lf)

<h2>Description</h2>

<dl><dt>VL
<dd>(an input expression of type REAL) defines the left margin of the viewport in fractional coordinates.
<dt>VR
<dd>(an input expression of type REAL) defines the right margin of the viewport in fractional coordinates.
<dt>VB
<dd>(an input expression of type REAL) defines the bottom margin of the viewport in fractional coordinates.
<dt>VT
<dd>(an input expression of type REAL) defines the top margin of the viewport in fractional coordinates.
<dt>WL
<dd>(an input expression of type REAL) defines the left margin of the window in user coordinates.
<dt>WR
<dd>(an input expression of type REAL) defines the right margin of the window in user coordinates.
<dt>WB
<dd>(an input expression of type REAL) defines the bottom margin of the window in user coordinates.
<dt>WT
<dd>(an input expression of type REAL) defines the top margin of the window in user coordinates.
<dt>LF
<dd>(an input expression of type INTEGER) defines the linear/log nature of the mapping, as follows:
<dl><dd><dl><dt>1
<dd>linear X, linear Y
<dt>2
<dd>linear X, log Y
<dt>3
<dd>log X, linear Y
<dt>4
<dd>log X, log Y</dl></dl>
</dl>

<h2>C-Binding Description</h2>

The C-binding argument descriptions are the same as the FORTRAN argument descriptions.

<h2>Usage</h2>

Note that in setting the limits of the viewport and the window, the left margin can have a user coordinate value that is larger than the user coordinate value at the right margin. This means the X axis scale will run from a maximum value at the left to a minimum value at the right. Likewise the bottom value can exceed the top value meaning that the Y axis can run from a maximum at the bottom to a minimum at the top. This reversal of the axes is referred to as &quot;mirror imaging&quot;. It represents a substantial functional enhancement over what is provided in GKS. That is why NCAR Graphics SET calls using fractional and user coordinates are in general preferred over GKS calls to GSVP and GSWN using normalized device coordinates and world coordinates.

<h2>Examples</h2>

Use the ncargex command to see the following relevant examples: fcoord1, fcoord2, splogy, sprevx. 

 sprevx shows the use of routine SET for an X axis scaling reversal, splogy shows the use of routine SET for logarithmic scaling of the Y axis, fcoord1 shows the mapping from GKS world coordinates to GKS normalized device coordinates, and fcoord2 shows the mapping from NCAR Graphics user coordinates to GKS normalized device coordinates.

<h2>Access</h2>

To use SET or c_set, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.

<h2>See Also</h2>

Online: gsvp, gswn, getset, getusv, setusv, spps, spps_params, ncarg_cbind 

 Hardcopy: NCAR Graphics Contouring and Mapping Tutorial; NCAR Graphics Fundamentals, UNIX Version; User's Guide for NCAR GKS-0A Graphics;

<h2>Copyright</h2>

Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
