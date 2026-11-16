---
title: "ncl_getset(3)"
name: "ncl_getset"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_getset/"
---

GETSET - returns a set of values which, if used as arguments in a call to SET, will cause normalization transformation 1, axis linear/log scaling (internal parameter 'LS'), and axis mirror imaging (internal parameter 'MI') to be defined in such a way as to duplicate the combined effects of the current normalization transformation, axis scaling, and axis mirror imaging. 

<h2>Synopsis</h2>CALL GETSET (VL,VR,VB,VT,WL,WR,WB,WT,LS)
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/ncargC.h&gt; 

 void c_getset(float *vl, float *vr, float *vb, float *vt, float *wl, float *wr, float *wb, float *wt, int *lf)
<h2>Description</h2><dl COMPACT><dt>VL
</dt><dd>(an output variable of type REAL) defines the left margin of the viewport in fractional coordinates.
</dd><dt>VR
</dt><dd>(an output variable of type REAL) defines the right margin of the viewport in fractional coordinates.
</dd><dt>VB
</dt><dd>(an output variable of type REAL) defines the bottom margin of the viewport in fractional coordinates.
</dd><dt>VT
</dt><dd>(an output variable of type REAL) defines the top margin of the viewport in fractional coordinates.
</dd><dt>WL
</dt><dd>(an output variable of type REAL) defines the left margin of the window in user coordinates.
</dd><dt>WR
</dt><dd>(an output variable of type REAL) defines the right margin of the window in user coordinates.
</dd><dt>WB
</dt><dd>(an output variable of type REAL) defines the bottom margin of the window in user coordinates.
</dd><dt>WT
</dt><dd>(an output variable of type REAL) defines the top margin of the window in user coordinates.
</dd><dt>LS
</dt><dd>(an output variable of type INTEGER) defines the linear/log nature of the mapping, as follows:
</dd><dl COMPACT><dd></dd><dl COMPACT><dt>1
</dt><dd>linear X, linear Y
</dd><dt>2
</dt><dd>linear X, log Y
</dd><dt>3
</dt><dd>log X, linear Y
</dd><dt>4
</dt><dd>log X, log Y</dd></dl></dl>
</dl><h2>C-Binding Description</h2>The C-binding argument descriptions are the same as the FORTRAN argument descriptions.
<h2>Usage</h2>Note that in setting the limits of the viewport and the window, the left margin can have a user coordinate value that is larger than the user coordinate value at the right margin. This means the X axis scale will run from a maximum value at the left to a minimum value at the right. Likewise the bottom value can exceed the top value meaning that the Y axis can run from a maximum at the bottom to a minimum at the top. This reversal of the axes is referred to as &quot;mirror imaging&quot;. It represents a substantial functional enhancement over what is provided in GKS. That is why NCAR Graphics SET calls using fractional and user coordinates are in general preferred over GKS calls to GSVP and GSWN using normalized device coordinates and world coordinates.
<h2>Examples</h2>Use the ncargex command to see the following relevant examples: arex01, mpex07, mpex09, cpexcc.
<h2>Access</h2>To use GETSET or c_getset, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.
<h2>See Also</h2>Online: gqnt, set, getusv, setusv, spps, spps_params, ncarg_cbind 

 Hardcopy: NCAR Graphics Fundamentals, UNIX Version; User's Guide for NCAR GKS-0A Graphics
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
