---
title: "ncl_gacolr(3)"
name: "ncl_gacolr"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_gacolr/"
---

GACOLR - Sets the values of internal parameters determining the color of various parts of the background. 

<h2>Synopsis</h2>CALL GACOLR (KAXS,KLBL,KMJT,KMNT)
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/ncargC.h&gt; 

 void c_gacolr (int kaxs, int klbl, int kmjt, int kmnt)
<h2>Description</h2><dl COMPACT><dt>KAXS, KLBL, KMJT, and KMNT
<dd>(input expressions of type INTEGER) are new values for the internal parameters 'CAX', 'CLB', 'CMJ', and 'CMN', specifying the color indices to be used for the axes, the labels, the major ticks/grid lines, and the minor ticks/grid lines, respectively. Values less than zero imply that no call is to be done to set the color before drawing items of the associated type. The default value of each of the four internal parameters is -1.</dl><h2>C-Binding Description</h2>The C-binding argument descriptions are the same as the FORTRAN argument descriptions.
<h2>Usage</h2>This routine allows you to set the current value of Gridall parameters. For a complete list of parameters available in this utility, see the gridall_params man page.
<h2>Access</h2>To use GACOLR or c_gacolr, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.
<h2>See Also</h2>Online: gridall, gridall_params, gagetc, gageti, gagetr, gasetc, gaseti, gasetr, grid, gridal, gridl, halfax, labmod, perim, periml, tick4, ticks, ncarg_cbind. 

 Hardcopy: NCAR Graphics Fundamentals, UNIX Version
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
