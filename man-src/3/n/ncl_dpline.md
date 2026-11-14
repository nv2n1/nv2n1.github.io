---
title: "ncl_dpline(3)"
name: "ncl_dpline"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_dpline/"
---

DPLINE - Draws a straight-line segment between two points in the user coordinate system. 

<h2>Synopsis</h2>CALL DPLINE (XCP1,YCP1,XCP2,YCP2)
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/ncargC.h&gt; 

 void c_dpline (float xcp1, float ycp1, float xcp2, float ycp2);
<h2>Description</h2><dl COMPACT><dt>XCP1
<dd>(an input expression of type REAL) specifies the X coordinate of a point at the beginning of the straight-line segment.
<dt>YCP1
<dd>(an input expression of type REAL) specifies the Y coordinate of a point at the beginning of the straight-line segment.
<dt>XCP2
<dd>(an input expression of type REAL) specifies the X coordinate of a point at the end of the straight-line segment.
<dt>YCP2
<dd>(an input expression of type REAL) specifies the Y coordinate of a point at the end of the straight-line segment.</dl><h2>C-Binding Description</h2>The C-binding argument descriptions are the same as the FORTRAN argument descriptions.
<h2>Usage</h2>DPLINE maps the input coordinates to the fractional system and then passes them on to DPDRAW. Even is smoothing is turned on, no smoothing is done by a call to DPLINE.
<h2>Examples</h2>Use the ncargex command to see the following relevant examples: tdshpk.
<h2>Access</h2>To use DPLINE or c_dpline, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.
<h2>See Also</h2>Online: dashpack, dashpack_params, dpcurv, dpdraw, dpfrst, dpgetc, dpgeti, dpgetr, dplast, dpsetc, dpseti, dpsetr, dpsmth, dpvect, ncarg_cbind. 

 Hardcopy: None.
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
