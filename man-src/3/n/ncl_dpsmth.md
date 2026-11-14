---
title: "ncl_dpsmth(3)"
name: "ncl_dpsmth"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_dpsmth/"
---

DPSMTH - Used to draw a curve when fractional coordinates are available and smoothing is to be done. 

<h2>Synopsis</h2>CALL DPSMTH (XCPF,YCPF,IFVL)
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/ncargC.h&gt; 

 void c_dpsmth (float xcpf, float ycpf, int ifvl);
<h2>Description</h2><dl COMPACT><dt>XCPF
<dd>(an input expression of type REAL) specifies the X coordinate of a point in the fractional coordinate system. Ignored when IFVL = 2.
<dt>YCPF
<dd>(an input expression of type REAL) specifies the Y coordinate of a point in the fractional coordinate system. Ignored when IFVL = 2.
<dt>IFVL
<dd>(an input expression of type INTEGER) indicates what type of call is being done: &quot;0&quot; implies a &quot;first-point&quot; call, &quot;1&quot; implies a &quot;vector&quot; call, and &quot;2&quot; implies a &quot;last-point&quot; or &quot;buffer-flush&quot; call.</dl><h2>C-Binding Description</h2>The C-binding argument descriptions are the same as the FORTRAN argument descriptions.
<h2>Usage</h2>Use &quot;CALL DPSMTH(XCPF,YCPF,0)&quot; to do a &quot;pen-up&quot; move to the first point in a sequence of points defining a curve. 

 Use &quot;CALL DPSMTH(XCPF,YCPF,1)&quot; to do &quot;pen-down&quot; moves to the second and following points in a sequence of points defining a curve. 

 Use &quot;CALL DPSMTH(0.,0.,2) to terminate a sequence of calls, finish drawing the curve, and flush internal buffers. 

 DPSMTH accumulates points until it has an internal buffer-load or until the last one has been received. It then creates a smooth curve passing through all the points, interpolates points along that smooth curve, and passes those points along to the routine DPDRAW. If the internal parameter 'TCS' has a value less than or equal to zero, the smoothing is done using simple cubic splines; if 'TCS' has a value greater than zero, the smoothing is done using cubic splines under tension and 'TCS' specifies the desired tension.
<h2>Examples</h2>Use the ncargex command to see the following relevant examples: tdshpk.
<h2>Access</h2>To use DPSMTH or c_dpsmth, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.
<h2>See Also</h2>Online: dashpack, dashpack_params, dpcurv, dpdraw, dpfrst, dpgetc, dpgeti, dpgetr, dplast, dpline, dpsetc, dpseti, dpsetr, dpvect, ncarg_cbind. 

 Hardcopy: None.
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
