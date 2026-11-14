---
title: "ncl_wmlabs(3)"
name: "ncl_wmlabs"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_wmlabs/"
---

WMLABS - plots weather map special symbols and daily weather icons.

<h2>Synopsis</h2>

CALL WMLABS (X, Y, SYMTYP)

<h2>C-Binding Synopsis</h2>

#include &lt;ncarg/gks.h&gt; 

 void c_wmlabs(float x, float y, char *symtyp)

<h2>Description</h2>

<dl><dt>X
<dd>(Real, Input) - An X coordinate (specified in world coordinates) of a point that specifies a position for the symbol type in SYMTYP.
<dt>Y
<dd>(Real, Input) - A Y coordinate (specified in world coordinates) of a point that specifies a position for the symbol type in SYMTYP.
<dt>SYMTYP
<dd>(Character, Input) - A character variable that indicates the desired symbol.
<dl><dd><dl><dt>Legal values for SYMTYP are:
<dd>&nbsp;<wbr>'HI'&nbsp;<wbr>for high pressure symbols. 

 
&nbsp;<wbr>'LOW'&nbsp;<wbr>for low pressure symbols. 

 
&nbsp;<wbr>'ARROW'&nbsp;<wbr>for arrows. 

 
&nbsp;<wbr>'DOT'&nbsp;<wbr>for dots. 

 
&nbsp;<wbr>'CLOUD'&nbsp;<wbr>for a cloud daily weather icon. 

 
&nbsp;<wbr>'ICE'&nbsp;<wbr>for an ice daily weather icon. 

 
&nbsp;<wbr>'IS'&nbsp;<wbr>for the intermittent shower daily weather icon. 

 
&nbsp;<wbr>'IT'&nbsp;<wbr>for the sunny, chance of T-storms daily weather icon. 

 
&nbsp;<wbr>'MC'&nbsp;<wbr>for the mostly cloudy daily weather icon. 

 
&nbsp;<wbr>'RAIN'&nbsp;<wbr>for the daily weather icon indicating rain. 

 
&nbsp;<wbr>'RS'&nbsp;<wbr>for the daily weather icon indicating rain and snow. 

 
&nbsp;<wbr>'SNOWFLAKES'&nbsp;<wbr>for the daily weather icon indicating snow. 

 
&nbsp;<wbr>'SUN'&nbsp;<wbr>for the sunny daily weather icon. 

 
&nbsp;<wbr>'THUNDERSTROM'&nbsp;<wbr>for the daily weather icon indicating thunderstorms. 

 
&nbsp;<wbr>'WIND'&nbsp;<wbr>for the windy daily weather icon.</dl></dl>
</dl>

<h2>Usage</h2>

Set the values for the appropriate internal parameters before calling WMLABS to produce the desired symbol. The internal parameters that control the appearance of the symbols and icons are: SHT, HIB, HIF, HIS, HIC (for the high symbols); SHT, LOF, LOB, LOS (for the low symbols); ARS, AWC, ARD, ASC, AOC (for arrows); DBC, DTC, DTS (for dots); CC1, CC2, CC3 (for the cloud icon); LC1, LC2, LC3 (for lightening bolts); SC1, SC2, SC3, SC4 (for the sun icon); COL.

<h2>Access</h2>

To use WMLABS or c_wmlabs, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.

<h2>See Also</h2>

Online: wmap, wmdflt, wmgetc, wmgeti, wmgetr, wmsetc, wmseti, wmsetr, wmap_params 

 Hardcopy: WMAP - A Package for Producing Daily Weather Maps and Plotting Station Model Data

<h2>Copyright</h2>

Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
