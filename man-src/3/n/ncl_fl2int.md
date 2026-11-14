---
title: "ncl_fl2int(3)"
name: "ncl_fl2int"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_fl2int/"
---

FL2INT - converts X and Y coordinates from the User Coordinate System to the Metacode Coordinate System. 

<h2>Status</h2>Metacode units are no longer used in NCAR Graphics; thus, FL2INT is considered an obsolete routine. 

 The current recognized coordinate systems are GKS world coordinates, GKS normalized device coordinates, NCAR Graphics fractional coordinates, and NCAR Graphics user coordinates. See the NCAR Graphics document &quot;NCAR Graphics Fundamentals, UNIX Version&quot; for a description of these coordinate systems. 

 FL2INT continues to be provided for compatibility of early NCAR Graphics codes. If you are writing new code, we suggest that you use user coordinates and fractional coordinates. The routines CUFX and CUFY will convert from user coordinates to fractional coordinates. CFUX and CFUY will convert fractional coordinates to user coordinates. 

 The following definition of the Metacode Coordinate System is included for the purpose of interpreting and converting codes: 

 The metacode coordinates of a point are integers IMX and IMY between 0 and 32767 inclusive. The area addressed is a square in a &quot;metacode space&quot; that is usually mapped into a square subset of the addressable area of the plotting device. Metacode coordinates were used in calls to the routine PLOTIT and are returned in calls to FL2INT.
<h2>Synopsis</h2>CALL FL2INT (PX,PY,IX,IY)
<h2>Description</h2><dl COMPACT><dt>PX
<dd>(an input expression of type REAL) is the X coordinate of a point in user coordinates.
<dt>PY
<dd>(an input expression of type REAL) is the Y coordinate of a point in user coordinates.
<dt>IX
<dd>(an output variable of type INTEGER) is the X coordinate of the point in metacode coordinates.
<dt>IY
<dd>(an output variable of type INTEGER) is the Y coordinate of the point in metacode coordinates.</dl><h2>Access</h2>To use FL2INT, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.
<h2>See Also</h2>Online: spps, plotit, cmfx, cmfy, cmux, cmuy, kfmx, kfmy, kmpx, kmpy, kpmx, kpmy, kumx, kumy 

 Hardcopy: NCAR Graphics Fundamentals, UNIX Version; User's Guide for NCAR GKS-0A Graphics
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
