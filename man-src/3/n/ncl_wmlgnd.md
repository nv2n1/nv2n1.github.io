---
title: "ncl_wmlgnd(3)"
name: "ncl_wmlgnd"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_wmlgnd/"
---

WMLGND - plots weather map legends.

<h2>Synopsis</h2>

CALL WMLGND (X,Y,NTYPE,IROWS,ICOLS)

<h2>C-Binding Synopsis</h2>

#include &lt;ncarg/gks.h&gt; 

 void c_wmlgnd(float x, float y, int ntype, int irows, int icols)

<h2>Description</h2>

<dl><dt>X
<dd>(Real, Input) - An X coordinate (specified in world coordinates) of a point that specifies a position for the legend to be plotted.
<dt>Y
<dd>(Real, Input) - A Y coordinate (specified in world coordinates) of a point that specifies a position for the legend to be plotted.
<dt>NTYPE
<dd>(Integer, Input) - A character variable that indicates the desired kind of legend.
<dl><dd><dl><dt>Legal values for NTYPE are:
<dd>1 - Plot the legend for the weather types. There are six weather types: showers; T-storms; rain; flurries; snow; ice. The coordinate (X,Y) for this type specifies the lower left corner of the legend. 

 2 - Plot the legend for front types. There are three front types labeled: cold; warm; stationary. The (X,Y) coordinate for this legend specifies the lower right corner of the legend. 

 3 - Plot the explanatory legend. The (X,Y) coordinate for this legend specifies the bottom center of the legend.</dl></dl><dt>IROWS
<dd>(Integer, Input) - An integer variable specifying how many rows there will be in displaying the weather types. IROWS and ICOLS are significant only when NTYPE=1. Choices for IROWS x ICOLS are: 1x6, 2x3, 3x2, and 6x1.
<dt>ICOLS
<dd>(Integer, Input) - An integer variable specifying how many columns there will be in displaying the weather types. IROWS and ICOLS are significant only when NTYPE=1. Choices for IROWS x ICOLS are: 1x6, 2x3, 3x2, and 6x1.</dl>

<h2>Usage</h2>

The only internal parameter that controls the appearance of a legend is COL, specifying its color.

<h2>Access</h2>

To use WMLGND or c_wmlgnd, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.

<h2>See Also</h2>

Online: wmap, wmdflt, wmgetc, wmgeti, wmgetr, wmsetc, wmseti, wmsetr, wmap_params 

 Hardcopy: WMAP - A Package for Producing Daily Weather Maps and Plotting Station Model Data

<h2>Copyright</h2>

Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
