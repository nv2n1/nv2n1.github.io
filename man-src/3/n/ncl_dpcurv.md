---
title: "ncl_dpcurv(3)"
name: "ncl_dpcurv"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_dpcurv/"
---

DPCURV - Used to draw a complete curve defined by a sequence of points in the user coordinate system. 

<h2>Synopsis</h2>CALL DPCURV (XCPU,YCPU,NPTS)
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/ncargC.h&gt; 

 void c_dpcurv (float *xcpu, float *ycpu, int npts);
<h2>Description</h2><dl COMPACT><dt>XCPU
<dd>(an input array of type REAL) specifies the X coordinates of points in the user coordinate system defining a curve to be drawn.
<dt>YCPU
<dd>(an input array of type REAL) specifies the Y coordinates of points in the user coordinate system defining a curve to be drawn.
<dt>NPTS
<dd>(an input expression of type INTEGER) specifies the number of points defining the curve.</dl><h2>C-Binding Description</h2>The C-binding argument descriptions are the same as the FORTRAN argument descriptions.
<h2>Usage</h2>The FORTRAN statement &quot;CALL DPCURV(XCPU,YCPU,NPTS)&quot; draws a complete curve by connecting the point (<a HREF="/docs/linux/man/1-xcpu/">XCPU</a>(1),<a HREF="/docs/linux/man/1-ycpu/">YCPU</a>(1)) to the point (<a HREF="/docs/linux/man/2-xcpu/">XCPU</a>(2),<a HREF="/docs/linux/man/2-ycpu/">YCPU</a>(2)), connecting that point to the point (<a HREF="/docs/linux/man/3-xcpu/">XCPU</a>(3),<a HREF="/docs/linux/man/3-ycpu/">YCPU</a>(3)), and so on, through the last point, (XCPU(NPTS),YCPU(NPTS)), in a manner described by the current values of the internal parameters of DASHPACK. 

 DPCURV maps the input coordinates to the fractional system and then passes them on to lower-level routines. If smoothing is turned off, DPCURV calls DPDRAW; if smoothing is turned on, it calls DPSMTH.
<h2>Examples</h2>Use the ncargex command to see the following relevant examples: tdshpk.
<h2>Access</h2>To use DPCURV or c_dpcurv, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.
<h2>See Also</h2>Online: dashpack, dashpack_params, dpdraw, dpfrst, dpgetc, dpgeti, dpgetr, dplast, dpline, dpsetc, dpseti, dpsetr, dpsmth, dpvect, ncarg_cbind. 

 Hardcopy: None.
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
