---
title: "ncl_ezhftn(3)"
name: "ncl_ezhftn"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_ezhftn/"
---

EZHFTN - draws a half-tone picture from data stored in a rectangular array with the intensity in the picture proportional to the data value. 

<h2>Utility</h2>This routine is part of the Halftone utility in NCAR Graphics. To see the overview man page for this utility, type &quot;man halftone&quot;.
<h2>Status</h2>EZHFTN is obsolete. It has been replaced by the CPCICA entry of the Conpack contouring package. 

 EZHFTN continues to be provided for compatibility of early NCAR Graphics codes. If you are writing new code, we suggest that you use CPCICA.
<h2>Synopsis</h2>CALL EZHFTN (Z,M,N)
<h2>Description</h2><dl COMPACT><dt>Z
<dd>(an input array of type REAL) defining a two-dimensional field to be half-tone plotted.
<dt>M
<dd>(an input parameter of type INTEGER) which is the first dimension of the Z array.
<dt>N
<dd>(an input parameter of type INTEGER) which is the second dimension of the Z array.</dl><h2>Usage</h2>EZHFTN has a shortened argument list from entry HAFTON which is based upon the following assumptions. <pre>1. The entire Z array is to be plotted.
2. The lowest value in Z will be at the lowest intensity of the output device.
3. The highest value in Z will be at the highest intensity of the output device.
4. Other values in Z will appear linearly spaced.
5. The maximum number of intensities will be used.
6. The picture will have a perimeter drawn.
7. The frame will be advanced after the picture is drawn.
8. The Z array contains no missing values.</pre>If these conditions are not met, use the HAFTON entry.
<h2>Access</h2>To use EZHFTN, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.
<h2>See Also</h2>Online: halftone, hafton, halftone_params, conpack, conpack_params, cpcica 

 Hardcopy: NCAR Graphics Contouring and Mapping Tutorial; NCAR Graphics Fundamentals, UNIX Version; User's Guide for NCAR GKS-0A Graphics
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
