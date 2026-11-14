---
title: "ncl_sflush(3)"
name: "ncl_sflush"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_sflush/"
---

SFLUSH - Flushes polylines, accumulated through calls to the routines PLOTIF and PLOTIT, from the SPPS polyline buffer shared by those routines; updates all open workstations; and flushes all system-level I/O buffers.

<h2>Status</h2>

SFLUSH was called FLUSH in previous versions. The name was changed to avoid a naming conflict with a common system routine.

<h2>Synopsis</h2>

CALL SFLUSH

<h2>C-Binding Synopsis</h2>

#include &lt;ncarg/ncargC.h&gt; 

 void c_sflush()

<h2>Examples</h2>

Use the ncargex command to see the following relevant examples: (none)

<h2>Access</h2>

To use SFLUSH or c_sflush, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.

<h2>See Also</h2>

Online: ngpict, frame, plotif, spps, spps_params, ncarg_cbind 

 Hardcopy: NCAR Graphics Fundamentals, UNIX Version; User's Guide for NCAR GKS-0A Graphics

<h2>Copyright</h2>

Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
