---
title: "ncl_halftone(3)"
name: "ncl_halftone"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_halftone/"
---

Halftone - is a utility for drawing half-tone pictures in which the gray scale level is proportional to the value in a two dimensional array. 

<h2>Status</h2>Halftone is obsolete. It has been replaced by the CPCICA entry of the Conpack contouring package. 

 Halftone continues to be provided for compatibility of early NCAR Graphics codes. If you are writing new code, we suggest that you use CPCICA.
<h2>Synopsis</h2>EZHFTN(Z,M,N) - draws a half-tone picture based upon a set of default options. 
 HAFTON (Z,L,M,N,FLO,HI,NLEV,NOPT,NPRM,ISPV,SPVAL) - Draws a half-tone picture from data stored in a rectangular array with the intensity in the picture proportional to the data value.
<h2>Access</h2>To use EZHFTN or HAFTON, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.
<h2>See Also</h2>Online: hafton, ezhftn, halftone_params, conpack, conpack_params, cpcica 

 Hardcopy: NCAR Graphics Contouring and Mapping Tutorial; NCAR Graphics Fundamentals, UNIX Version; User's Guide for NCAR GKS-0A Graphics
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
