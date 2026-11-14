---
title: "ncl_clsgks(3)"
name: "ncl_clsgks"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_clsgks/"
---

CLSGKS - Deactivates workstation 1, closes workstation 1, and closes GKS. 

<h2>Status</h2>CLSGKS is somewhat dated. It was primarily used with NCAR GKS-0A when this package only allowed for a single metacode workstation. Now that the NCAR GKS package provides for multiple workstations to be open, it is recommended that standard GKS calls to GDAWK, GCLWK, and GCLKS be used instead.
<h2>Synopsis</h2>CALL CLSGKS
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/ncargC.h&gt; 

 void c_clsgks()
<h2>Examples</h2>Use the ncargex command to see the following relevant examples: agex01.
<h2>Access</h2>To use CLSGKS or c_clsgks, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.
<h2>See Also</h2>Online: spps, gdawk, gclwk, gclks, opngks, setusv, getusv, ncarg_cbind 

 Hardcopy: NCAR Graphics Fundamentals, UNIX Version; User's Guide for NCAR GKS-0A Graphics
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
