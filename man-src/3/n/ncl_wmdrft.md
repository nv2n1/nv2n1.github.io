---
title: "ncl_wmdrft(3)"
name: "ncl_wmdrft"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_wmdrft/"
---

WMDRFT - plots weather map front lines.

<h2>Synopsis</h2>

CALL WMDRFT (N, X, Y)

<h2>C-Binding Synopsis</h2>

#include &lt;ncarg/gks.h&gt; 

 void c_wmdrft(int n, float *x, float *y)

<h2>Description</h2>

<dl><dt>N
<dd>(Integer, Input) - The number of points supplied in the second and third arguments.
<dt>X
<dd>(Real, Input) - The X coordinates (specified in world coordinates) of N points that specify the control points of a spline curve that will be fitted to represent the requested weather front.
<dt>Y
<dd>(Real, Input) - The Y coordinates (specified in world coordinates) of N points that specify the control points of a spline curve that will be fitted to represent the requested weather front.</dl>

<h2>Usage</h2>

Set the values for the appropriate internal parameters before calling WMDRFT to produce the desired weather front. The internal parameters that control the appearance of weather fronts are: ALO, ARC, BEG, BET, CFC, CS1, CS2, COL, DWD, END, FRO, LIN, NBZ, NMS, PAI, REV, SL1, SL2, SLF, STY, SWI, T1C, T2C, WFC, and WTY. The possible fronts are: warm, warm aloft, cold, cold aloft, stationary, stationary aloft, occluded, convergence line, instability line, intertropical. As mentioned above, the points specified in the X and Y arrays serve as control points for a spline curve that is fitted between the first and last point. The spline passes through the given points. If the desired front line is reasonably smooth, then only a few input points need be specified.

<h2>Access</h2>

To use WMDRFT or c_wmdrft, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.

<h2>See Also</h2>

Online: wmap, wmdflt, wmgetc, wmgeti, wmgetr, wmsetc, wmseti, wmsetr, wmap_params 

 Hardcopy: WMAP - A Package for Producing Daily Weather Maps and Plotting Station Model Data

<h2>Copyright</h2>

Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
