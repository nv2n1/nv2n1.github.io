---
title: "ncl_wmbarb(3)"
name: "ncl_wmbarb"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_wmbarb/"
---

WMBARB - plots wind barbs.

<h2>Synopsis</h2>

CALL WMBARB (X,Y,U,V)

<h2>C-Binding Synopsis</h2>

#include &lt;ncarg/gks.h&gt; 

 void c_wmbarb(float x, float y, float u, float v)

<h2>Description</h2>

<dl><dt>X
<dd>(Real, Input) - An X coordinate (specified in world coordinates) of a point that specifies the position of the base of a wind barb.
<dt>Y
<dd>(Real, Input) - A Y coordinate (specified in world coordinates) of a point that specifies the position of the base of a wind barb.
<dt>U
<dd>(Real, Input) - The X component of a wind vector.
<dt>V
<dd>(Real, Input) - The Y component of a wind vector.</dl>

<h2>Usage</h2>

The angle at which the wind barb is drawn is determined by the vector (U,V) and the magnitude of that vector denotes the wind speed in knots. Set the values for the appropriate internal parameters before calling WMBARB to produce the wind barb. The internal parameters that control the appearance of wind barbs are: COL, WBA, WBD, WBF, WBS, WBT.

<h2>Access</h2>

To use WMBARB or c_wmbarb, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.

<h2>See Also</h2>

Online: wmap, wmdflt, wmgetc, wmgeti, wmgetr, wmlabs, wmsetc, wmseti, wmsetr, wmstnm, wmap_params 

 Hardcopy: WMAP - A Package for Producing Daily Weather Maps and Plotting Station Model Data

<h2>Copyright</h2>

Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
