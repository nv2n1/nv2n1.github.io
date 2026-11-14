---
title: "ncl_dpfrst(3)"
name: "ncl_dpfrst"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_dpfrst/"
---

DPFRST - Specifies the first point in a sequence of points, in the user coordinate system, defining a curve to be drawn. 

<h2>Synopsis</h2>CALL DPFRST (XCPU,YCPU)
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/ncargC.h&gt; 

 void c_dpfrst (float xcpu, float ycpu);
<h2>Description</h2><dl COMPACT><dt>XCPU
<dd>(an input expression of type REAL) specifies the X coordinate of a point, in the user coordinate system.
<dt>YCPU
<dd>(an input expression of type REAL) specifies the Y coordinate of a point, in the user coordinate system.</dl><h2>C-Binding Description</h2>The C-binding argument descriptions are the same as the FORTRAN argument descriptions.
<h2>Usage</h2>Call DPFRST to do a &quot;pen-up&quot; move to the first of a sequence of points defining a curve. Call DPVECT to do &quot;pen-down&quot; moves to each of the other points in the sequence and then call DPLAST to finish drawing the curve and flush the buffers. 

 DPFRST maps the input coordinates to the fractional coordinate system and then does a &quot;pen-up&quot; call to either DPDRAW (if smoothing is turned off) or to DPSMTH (if smoothing is turned on) with those coordinates.
<h2>Examples</h2>Use the ncargex command to see the following relevant examples: tdshpk.
<h2>Access</h2>To use DPFRST or c_dpfrst, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.
<h2>See Also</h2>Online: dashpack, dashpack_params, dpcurv, dpdraw, dpgetc, dpgeti, dpgetr, dplast, dpline, dpsetc, dpseti, dpsetr, dpsmth, dpvect, ncarg_cbind. 

 Hardcopy: None.
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
