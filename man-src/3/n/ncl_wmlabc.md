---
title: "ncl_wmlabc(3)"
name: "ncl_wmlabc"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_wmlabc/"
---

WMLABC - plots weather map city names and daily hi/lows.

<h2>Synopsis</h2>

CALL WMLABC (X, Y, CITY, TEMPS)

<h2>C-Binding Synopsis</h2>

#include &lt;ncarg/gks.h&gt; 

 void c_wmlabc(float x, float y, char *city, char *temps)

<h2>Description</h2>

<dl><dt>X
<dd>(Real, Input) - An X coordinate (specified in world coordinates) of a point that specifies the center of the composite label that consists of the city name in the character variable CITY and the temperature ranges in the character variable TEMPS. The city name is plotted above the temperatures.
<dt>Y
<dd>(Real, Input) - A Y coordinate (specified in world coordinates) of a point that specifies the center of the composite label that consists of the city name in the character variable CITY and the temperature ranges in the character variable TEMPS. The city name is plotted above the temperatures.
<dt>CITY
<dd>(Character, Input) - A character variable that contains the name of the city being plotted.
<dt>TEMPS
<dd>(Character, Input) - A character variable that contains the daily hi/low label for the city named in the third argument.</dl>

<h2>Usage</h2>

Set the values for the appropriate internal parameters before calling WMLABC to produce the desired label. The internal parameters that control the appearance of the labels are: CBC, CHT, CMG, RFC. To mark the cities' position with a dot, see the documentation for WMLABS.

<h2>Access</h2>

To use WMLABC or c_wmlabc, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.

<h2>See Also</h2>

Online: wmap, wmdflt, wmgetc, wmgeti, wmgetr, wmlabs, wmsetc, wmseti, wmsetr, wmap_params 

 Hardcopy: WMAP - A Package for Producing Daily Weather Maps and Plotting Station Model Data

<h2>Copyright</h2>

Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
