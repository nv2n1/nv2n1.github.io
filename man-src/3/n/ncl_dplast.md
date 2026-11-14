---
title: "ncl_dplast(3)"
name: "ncl_dplast"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_dplast/"
---

DPLAST - Says that the preceding call to DPVECT defined the final point in a sequence of points, in the user coordinate system, defining a curve to be drawn. 

<h2>Synopsis</h2>CALL DPLAST
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/ncargC.h&gt; 

 void c_dplast ();
<h2>Description</h2>There are no arguments.
<h2>C-Binding Description</h2>The C-binding argument descriptions are the same as the FORTRAN argument descriptions.
<h2>Usage</h2>Call DPFRST to do a &quot;pen-up&quot; move to the first of a sequence of points defining a curve. Call DPVECT to do &quot;pen-down&quot; moves to each of the other points in the sequence and then call DPLAST to finish drawing the curve and flush the buffers.
<h2>Examples</h2>Use the ncargex command to see the following relevant examples: tdshpk.
<h2>Access</h2>To use DPLAST or c_dplast, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.
<h2>See Also</h2>Online: dashpack, dashpack_params, dpcurv, dpdraw, dpfrst, dpgetc, dpgeti, dpgetr, dpline, dpsetc, dpseti, dpsetr, dpsmth, dpvect, ncarg_cbind. 

 Hardcopy: None.
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
