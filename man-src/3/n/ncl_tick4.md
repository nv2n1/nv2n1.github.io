---
title: "ncl_tick4(3)"
name: "ncl_tick4"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_tick4/"
---

TICK4 - Allows for program control of tick mark length and direction.

<h2>Synopsis</h2>

CALL TICK4 (LMJX, LMNX, LMJY, LMNY)

<h2>C-Binding Synopsis</h2>

#include &lt;ncarg/ncargC.h&gt; 

 void c_tick4 (int lmjx, int lmnx, int lmjy, int lmny)

<h2>Description</h2>

All arguments are in plotter address units (PAUs). By default, one PAU is 1/1023rd of the width of the plotter frame. 

 Note: A call to the SPPS routine SETI will change the definition of a PAU. Such calls are no longer recommended, but the possibility still exists.
<dl><dt>LMJX and LMNX
<dd>(input expressions of type INTEGER) are the lengths, in plotter address units, of major and minor ticks on the X axis. The default values are 12 and 8.
<dt>LMJY and LMNY
<dd>(input expressions of type INTEGER) are the lengths, in plotter address units, of major and minor ticks on the Y axis. The default values are 12 and 8.
<dd>By default, tick marks point inward. Negative values of LMJX, LMNX, LMJY, and LMNY may be used to create outward-pointing tick marks.</dl>

<h2>C-Binding Description</h2>

The C-binding argument descriptions are the same as the FORTRAN argument descriptions.

<h2>Usage</h2>

This routine allows you to set the current value of Gridall parameters. For a complete list of parameters available in this utility, see the gridall_params man page.

<h2>Examples</h2>

Use the ncargex command to see the following relevant example: tgrida.

<h2>Access</h2>

To use TICK4 or c_tick4, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.

<h2>See Also</h2>

Online: gridall, gridall_params, gacolr, gagetc, gageti, gagetr, gasetc, gaseti, gasetr, grid, gridal, gridl, halfax, labmod, perim, periml, ticks, ncarg_cbind. 

 Hardcopy: NCAR Graphics Fundamentals, UNIX Version

<h2>Copyright</h2>

Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
