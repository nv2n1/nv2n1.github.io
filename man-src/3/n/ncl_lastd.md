---
title: "ncl_lastd(3)"
name: "ncl_lastd"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_lastd/"
---

LASTD - Terminates a sequence of calls to draw a curve (a call to FRSTD followed by one or more calls to VECTD). 

<h2>Synopsis</h2>CALL LASTD
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/ncargC.h&gt; 

 void c_lastd()
<h2>Usage</h2>A sequence of calls to draw a curve (a call to FRSTD followed by one or more calls to VECTD) may be followed by a call to LASTD. It flushes any portions of smoothed curves that are defined by coordinates saved in internal buffers of FRSTD and VECTD and that have not yet been drawn. Calls to LASTD are not always required - for example, when a non-smoothing version of Dashline is used (no buffering) or when the next call to an NCAR Graphics routine will be to FRSTD (which flushes the buffers) - but unnecessary calls do no harm. If you judge that one of the smoothing versions of Dashline may be used, it is best to put in the calls to LASTD.
<h2>Examples</h2>Use the ncargex command to see the following relevant examples: tdashp, tdashs.
<h2>Access</h2>To use LASTD or c_lastd, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.
<h2>See Also</h2>Online: dashline, dashline_params, curved, dashdb, dashdc, frstd, lastd, lined, reset, ncarg_cbind 

 Hardcopy: NCAR Graphics Contouring and Mapping Tutorial; NCAR Graphics Fundamentals, UNIX Version; User's Guide for NCAR GKS-0A Graphics
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
