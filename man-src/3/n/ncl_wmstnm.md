---
title: "ncl_wmstnm(3)"
name: "ncl_wmstnm"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_wmstnm/"
---

WMSTNM - plots station model data as per WMO guidelines.

<h2>Synopsis</h2>

CALL WMSTNM (X, Y, IMDAT)

<h2>C-Binding Synopsis</h2>

#include &lt;ncarg/gks.h&gt; 

 void c_wmstnm(float x, float y, char *imdat)

<h2>Description</h2>

<dl><dt>X
<dd>(Real, Input) - An X coordinate (specified in world coordinates) of a point that specifies the position of the base of the wind barb shaft in the station model display.
<dt>Y
<dd>(Real, Input) - A Y coordinate (specified in world coordinates) of a point that specifies the position of the base of the wind barb shaft in the station model display.
<dt>IMDAT
<dd>(Character, Input) - A CHARACTER*5 array of dimension 10 encoded as per the WMO/NOAA guidelines.</dl>

<h2>Usage</h2>

Set the values for the appropriate internal parameters before calling WMSTNM to produce station model data plots. The internal parameters that control the appearance of the station model data plots are: WBC and WBL. The appearance of the wind barb part of the station model data is controlled by the internal parameters applying to wind barbs. See the documentation for WMBARB for a description of wind barbs.

<h2>Access</h2>

To use WMSTNM or c_wmstnm, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.

<h2>See Also</h2>

Online: wmap, wmdflt, wmgetc, wmgeti, wmgetr, wmlabs, wmsetc, wmseti, wmsetr, wmap_params 

 Hardcopy: WMAP - A Package for Producing Daily Weather Maps and Plotting Station Model Data

<h2>Copyright</h2>

Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
