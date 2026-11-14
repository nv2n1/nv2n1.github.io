---
title: "ncl_wmlabw(3)"
name: "ncl_wmlabw"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_wmlabw/"
---

WMLABW - plots weather map regional weather labels (like &quot;HOT&quot;, &quot;BREEZY&quot;, &quot;COLD&quot;, etc.

<h2>Synopsis</h2>

CALL WMLABW (X, Y, LABEL)

<h2>C-Binding Synopsis</h2>

#include &lt;ncarg/gks.h&gt; 

 void c_wmlabw(float x, float y, char *label)

<h2>Description</h2>

<dl><dt>X
<dd>(Real, Input) - An X coordinate (specified in world coordinates) of a point that specifies the center of the label in LABEL.
<dt>Y
<dd>(Real, Input) - A Y coordinate (specified in world coordinates) of a point that specifies the center of the label in LABEL.
<dt>LABEL
<dd>(Character, Input) - A character variable that contains the desired label.</dl>

<h2>Usage</h2>

Set the values for the appropriate internal parameters before calling WMLABW to produce the desired label. The internal parameters that control the appearance of the labels are: RC1, RC2, RC3, RC4, RC5, and WHT.

<h2>Access</h2>

To use WMLABW or c_wmlabw, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.

<h2>See Also</h2>

Online: wmap, wmdflt, wmgetc, wmgeti, wmgetr, wmlabs, wmsetc, wmseti, wmsetr, wmap_params 

 Hardcopy: WMAP - A Package for Producing Daily Weather Maps and Plotting Station Model Data

<h2>Copyright</h2>

Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
