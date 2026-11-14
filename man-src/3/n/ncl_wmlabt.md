---
title: "ncl_wmlabt(3)"
name: "ncl_wmlabt"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_wmlabt/"
---

WMLABT - plots weather map regional temperatures labels (like 90s, 80s, etc.)

<h2>Synopsis</h2>

CALL WMLABT (X, Y, LABEL, IPOS)

<h2>C-Binding Synopsis</h2>

#include &lt;ncarg/gks.h&gt; 

 void c_wmlabt(float x, float y, char *label, int ipos)

<h2>Description</h2>

<dl><dt>X
<dd>(Real, Input) - An X coordinate (specified in world coordinates) of a point that specifies a position for the label in LABEL.
<dt>Y
<dd>(Real, Input) - A Y coordinate (specified in world coordinates) of a point that specifies a position for the label in LABEL.
<dt>LABEL
<dd>(Character, Input) - A character variable that contains the desired label.
<dt>IPOS
<dd>(Integer, Input) - A flag for controlling whether an optional arrow is drawn. If IPOS is 0, then no arrow is drawn and the label is centered at (X,Y). If IPOS is between 1 and 12 (inclusive), then an arrow is drawn in one of twelve positions and (X,Y) specifies the location of the tip of the arrow.</dl>

<h2>Usage</h2>

Set the values for the appropriate internal parameters before calling WMLABT to produce the desired label. The internal parameters that control the appearance of the labels are: RBS, RFC, RLS, ROS, and THT. The appearance of the optional arrows is controlled by the internal parameters controlling arrows (see the documentation for WMLABS).

<h2>Access</h2>

To use WMLABT or c_wmlabt, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.

<h2>See Also</h2>

Online: wmap, wmdflt, wmgetc, wmgeti, wmgetr, wmlabs, wmsetc, wmseti, wmsetr, wmap_params 

 Hardcopy: WMAP - A Package for Producing Daily Weather Maps and Plotting Station Model Data

<h2>Copyright</h2>

Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
