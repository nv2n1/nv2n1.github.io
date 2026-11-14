---
title: "ncl_dashdb(3)"
name: "ncl_dashdb"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_dashdb/"
---

DASHDB - Defines a dash pattern without labels. 

<h2>Synopsis</h2>CALL DASHDB (IPAT)
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/ncargC.h&gt; 

 void c_dashdb (int *ipat)
<h2>Description</h2><dl COMPACT><dt>IPAT
<dd>(an input expression of type INTEGER) is a 16-bit dash pattern (1=solid, 0=blank); e.g., the binary number 1111000011110000, which is a decimal 61680, will give dashes of medium length.</dl><h2>C-Binding Description</h2>The C-binding argument description is the same as the FORTRAN argument description.
<h2>Examples</h2>Use the ncargex command to see the following relevant examples: carline, colcon, cmpfil, cmpitm, cmplab, cmpmsk, cmptit, cmpusr, mpex08, tdashc, tdashl, tdashp, tdashs, fdldashd.
<h2>Usage</h2>DASHDB may be called to define a dash pattern for any of the four versions of Dashline. 

 A dash pattern defined by a call to DASHDB will supersede one defined by an earlier call to DASHDB or DASHDC.
<h2>Access</h2>To use DASHDB or c_dashdb, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.
<h2>See Also</h2>Online: dashline, dashline_params, curved, dashdc, frstd, lastd, lined, reset, vectd, ncarg_cbind 

 Hardcopy: NCAR Graphics Contouring and Mapping Tutorial; NCAR Graphics Fundamentals, UNIX Version; User's Guide for NCAR GKS-0A Graphics
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
