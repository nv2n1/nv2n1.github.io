---
title: "ncl_pwrite_family(3)"
name: "ncl_pwrite_family"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_pwrite_family/"
---

Pwrite_family - A utility for drawing text and other characters using polylines.

<h2>Status</h2>

Pwrite_family is obsolete. It has been replaced by the Plotchar utility. 

 Entries PWRITX and PWRITY continue to be provided for compatibility of early NCAR Graphics codes. If you are writing new code, we suggest that you use Plotchar.

<h2>Synopsis</h2>

PWRITX (X,Y,IDPC,NCHAR,JSIZE,JOR,JCTR) - draws characters as stroked polylines. It is the higher quality routine of the Pwrite_family. 
 PWRITY (X,Y,IDPC,NCHAR,JSIZE,JOR,JCTR) - also draws characters as stroked polylines, but is quicker, of lower quality, and with less options than PWRITX.

<h2>Access</h2>

To use PWRITX or PWRITY, load the NCAR Graphics libraries ncarg, ncarg_gks, ncarg_c, and ncarg_c, preferably in that order.

<h2>See Also</h2>

Online: pwritx, pwrity, plotchar, plchhq, plchmq, plchlq 

 Hardcopy: NCAR Graphics Fundamentals, UNIX Version; User's Guide for NCAR GKS-0A Graphics

<h2>Copyright</h2>

Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
