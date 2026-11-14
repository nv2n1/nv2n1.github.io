---
title: "ncl_dpdraw(3)"
name: "ncl_dpdraw"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_dpdraw/"
---

DPDRAW - Used to draw a curve when fractional coordinates are available and no smoothing is to be done. 

<h2>Synopsis</h2>CALL DPDRAW (XCPF,YCPF,IFVL)
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/ncargC.h&gt; 

 void c_dpdraw (float xcpf, float ycpf, int ifvl);
<h2>Description</h2><dl COMPACT><dt>XCPF
<dd>(an input expression of type REAL) specifies the X coordinate of a point in the fractional coordinate system. Ignored when IFVL = 2.
<dt>YCPF
<dd>(an input expression of type REAL) specifies the Y coordinate of a point in the fractional coordinate system. Ignored when IFVL = 2.
<dt>IFVL
<dd>(an input expression of type INTEGER) indicates what type of call is being done: &quot;0&quot; implies a &quot;first-point&quot; call, &quot;1&quot; implies a &quot;vector&quot; call, and &quot;2&quot; implies a &quot;last-point&quot; or &quot;buffer-flush&quot; call.</dl><h2>C-Binding Description</h2>The C-binding argument descriptions are the same as the FORTRAN argument descriptions.
<h2>Usage</h2>Use &quot;CALL DPDRAW(XCPF,YCPF,0)&quot; to do a &quot;pen-up&quot; move to the first point in a sequence of points defining a curve. 

 Use &quot;CALL DPDRAW(XCPF,YCPF,1)&quot; to do &quot;pen-down&quot; moves to the second and following points in a sequence of points defining a curve. 

 Use &quot;CALL DPDRAW(0.,0.,2) to terminate a sequence of calls, finish drawing the curve, and flush internal buffers.
<h2>Examples</h2>Use the ncargex command to see the following relevant examples: tdshpk.
<h2>Access</h2>To use DPDRAW or c_dpdraw, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.
<h2>See Also</h2>Online: dashpack, dashpack_params, dpcurv, dpfrst, dpgetc, dpgeti, dpgetr, dplast, dpline, dpsetc, dpseti, dpsetr, dpsmth, dpvect, ncarg_cbind. 

 Hardcopy: None.
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
