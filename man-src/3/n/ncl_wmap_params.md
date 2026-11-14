---
title: "ncl_wmap_params(3)"
name: "ncl_wmap_params"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_wmap_params/"
---

Wmap_params - This document briefly describes all the internal parameters of Wmap.

<h2>Description</h2>

The following shows all of the internal parameters that affect the behavior of Wmap. Each entry includes the name of a parameter, its Fortran type, its default value, and a short description of the parameter.
<dl><dt>'ALO' - Integer - 0
<dd>A Flag to indicate whether a weather front is at the surface or aloft. ALO=0 is surface; ALO=1 is aloft.
<dt>'AOC' - Integer - -1
<dd>Color index for the outlines of arrows (outlines drawn only if AOC is non-negative).
<dt>'ARC' - Real - 0.
<dd>Length of current weather front line (retrieval only).
<dt>'ARD' - Real - 0.
<dd>Direction of arrows, expressed in degrees.
<dt>'ARL' - Real - 1.
<dd>Scale factor for the length of an arrow's tail, independent of the arrow's size.
<dt>'ARS' - Real - 0.035
<dd>Size of arrows, expressed as a fraction of the maximum screen height.
<dt>'ASC' - Integer - -1
<dd>Color index for the shadows of arrows (shadows are drawn only if ASC is non-negative).
<dt>'AWC' - Integer - 1
<dd>Color index for the interior of arrows.
<dt>'BEG' - Real - 0.015
<dd>Space, expressed in world coordinates, to leave along a front line before the first symbol is drawn.
<dt>'BET' - Real - 0.045
<dd>Space, expressed in world coordinates, to leave along a front line before the first symbol is drawn.
<dt>'CBC' - Integer - 1
<dd>The color index to be used for backgrounds of city and daily high/low labels.
<dt>'CC1' - Integer - 2
<dd>Color index for the interior of a cloud symbol.
<dt>'CC2' - Integer - 1
<dd>Color index for the outline of the cloud symbol.
<dt>'CC3' - Integer - 1
<dd>Color index for the shadow of the cloud symbol.
<dt>'CFC' - Integer - 1
<dd>Color index to use for cold front symbols.
<dt>'CHT' - Real - 0.0105
<dd>Height of characters, expressed as a fraction of the maximum screen width, of the city labels and daily high/low temperatures.
<dt>'CMG' - Real - 0.002
<dd>Size, expressed as a fraction of the maximum screen height, of the margins used for the city labels.
<dt>'COL' - Integer - 1
<dd>Color index to use for all objects that require only a single color setting.
<dt>'CS1' - Real - N/A
<dd>Slope of the left edge of a front line as calculated internally as measured in degrees from the X-axis (used when SLF=0,2, or 3). This parameter is for retrieval only.
<dt>'CS2' - Real - N/A
<dd>Slope of the right edge of a front line as calculated internally as measured in degrees from the X-axis (used when SLF=0,1, or 3). This parameter is for retrieval only.
<dt>'DBC' - Integer - 0
<dd>The color index to be used for the background shadow for the dots marking the city locations.
<dt>'DTC' - Integer - 1
<dd>The color index to use for the dots marking the city locations.
<dt>'DTS' - Real - 0.006
<dd>Size, expressed as a fraction of the maximum screen height, of the dots used to mark cities.
<dt>'DWD' - Real - 2.0
<dd>Line widths for front lines that do not have symbols along them (like tropical fronts and convergence lines).
<dt>'END' - Real - 0.015
<dd>Space, expressed in world coordinates, to leave along a front line after the last symbol has been drawn.
<dt>'FRO' - Character - 'WARM'
<dd>&nbsp;<wbr>Front type&nbsp;<wbr>(one of&nbsp;<wbr>`WARM',&nbsp;<wbr>`COLD',&nbsp;<wbr>`OCCLUDED',&nbsp;<wbr> `STATIONARY', `SQUALL', `TROPICAL', or `CONVERGENCE').
<dt>'HIB' - Integer - 0
<dd>Background color index for the &quot;H&quot; drawn for the high pressure symbols.
<dt>'HIC' - Integer - 1
<dd>Color index of the circumscribed circle for the &quot;H&quot; drawn for the high pressure symbols.
<dt>'HIF' - Integer - 1
<dd>Color index for the &quot;H&quot; drawn for the high pressure symbols.
<dt>'HIS' - Integer - 1
<dd>Color index for the shadow of the high pressure symbols
<dt>'LC1' - Integer - 2
<dd>Color index for the interior of the lightening bolt symbol
<dt>'LC2' - Integer - 1
<dd>Color index for the outline of the lightening bolt symbol.
<dt>'LC3' - Integer - 1
<dd>Color index for the shadow of the lightening bolt symbol
<dt>'LIN' - Real - 8.
<dd>Line widths, expressed as a fraction of the maximum screen width, for fronts having symbols along them.
<dt>'LOB' - Integer - 1
<dd>Color index for the background of the &quot;L&quot; drawn for the low pressure symbols.
<dt>'LOF' - Integer - 0
<dd>Color index for the &quot;L&quot; drawn for the low pressure symbols.
<dt>'LOS' - Integer - 0
<dd>Color index for the shadow of the low pressure symbols.
<dt>'LWD' - Real - 0.00275
<dd>Line width used when parameter WTY=1 (see below)
<dt>'MXS' - Integer - 300
<dd>Maximum number of symbols allowed along a weather front line.
<dt>'NBZ' - Integer - 51
<dd>The number of points to use in the Bezier curves for the symbols along the warm fronts.
<dt>'NMS' - Integer - internally calculated
<dd>Specifies precisely the number of symbols to appear along a weather front line (if this parameter has not been set by the user, then it is calculated internally).
<dt>'PAI' - Integer - 1
<dd>Current parameter array index used in specifying internal parameters that are arrays.
<dt>'RBS' - Integer - -1
<dd>The color index to use for the background of the regional temperature labels (plotted only if RBS is non-negative).
<dt>'RC1' - Integer - 1
<dd>Color index for the outline of the boxes drawn for the regional weather labels.
<dt>'RC2' - Integer - 0
<dd>Color index for the backgrounds of the boxes used for the regional weather labels.
<dt>'RC3' - Integer - 1
<dd>Color index for the shadow color of the boxes used for the regional weather labels.
<dt>'RC4' - Integer - 1
<dd>Color index for the text string used for regional weather labels.
<dt>'RC5' - Integer - 1
<dd>Color for the outlines of the characters in the text strings used for regional weather labels (plotted only if RC5 is non-negative).
<dt>'REV' - Integer - N/A
<dd>Reverses the current setting for the direction symbols will be drawn along front lines.
<dt>'RFC' - Integer - 1
<dd>The color index to be used for the foreground of regional temperature labels and cities.
<dt>'RHT' - Real - 0.008
<dd>Height, expressed as a fraction of the maximum screen width, of the characters used for the regional weather patterns (like rain, snow, etc.).
<dt>'RLS' - Integer - 1
<dd>The color index to use for shadows of regional temperature labels.
<dt>'RMG' - Real - 0.001
<dd>Size, expressed as a fraction of the maximum screen height, of the margins of the regional temperature labels.
<dt>'ROS' - Integer - -1
<dd>The color index to use for the outlines of the regional temperature labels (plotted only if ROS is non-negative).
<dt>'SC1' - Integer - 2
<dd>Color index to be used for the center of the sun symbol.
<dt>'SC2' - Integer - 3
<dd>Color index for the points of the sun symbol.
<dt>'SC3' - Integer - 1
<dd>Color index for the outline of the sun symbol.
<dt>'SC4' - Integer - 1
<dd>Color index for the shadow of the sun symbol.
<dt>'SHT' - Real - 0.02
<dd>Height of symbols, expressed as a fraction of the maximum screen width, for all the special symbols.
<dt>'SL1' - Real - 0.0
<dd>The slope of the beginning of a front line measured in degrees from the X-axis. This parameter is used in conjunction with the parameter SLF.
<dt>'SL2' - Real - 0.0
<dd>The slope of the end of a front line measured in degrees from the X-axis. This parameter is used in conjunction with the parameter SLF.
<dt>'SLF' - Integer - 3
<dd>Flag for indicating how the slopes at the end of a front line should be handled (0=use SL1 &amp; SL2; 1=use SL1 only; 2=use SL2 only; 3=use neither SL1 or SL2). When either SL1 or SL2 is not used, it is calculated internally.
<dt>'STY' - Integer Array - all 2s
<dd>An array for precisely specifying whether a warm front or cold front symbol is to be drawn at the specified position along a front line (1=cold; 2=warm). Use the internal parameter PAI for defining this array.
<dt>'SWI' - Real - 0.0325
<dd>Width of a symbol along a weather front, expressed as a fraction of the maximum screen width.
<dt>'T1C' - Integer - 1
<dd>One color to use for the alternating colors of the dashes in the tropical fronts.
<dt>'T2C' - Integer - 1
<dd>A second color to use for the alternating colors of the dashes in the tropical fronts.
<dt>'THT' - Real - 0.0165
<dd>Height of characters, expressed as a fraction of the maximum screen width, for the regional temperature labels.
<dt>'UNT' - Integer - 0
<dd>Flags whether imperial units (the default) or metric units are used.
<dt>'VVC' - Integer - 0
<dd>Flags whether the raw SYNOP codes are plotted for surface visibility (default is not to).
<dt>'WBA' - Real - 62.
<dd>Angle (in degrees) that the wind barb ticks make with the wind barb shafts.
<dt>'WBC' - Real - 0.3
<dd>Diameter of sky cover circle at base of wind barb, expressed as a fraction of the shaft length.
<dt>'WBD' - Real - 0.1
<dd>Spacing between tick marks along a wind barb expressed as a fraction of the wind barb shaft length.
<dt>'WBF' - Integer - 0
<dd>Flag indicating whether the base of a wind barb should be drawn to allow for the sky cover circle at its base (WBF=1 means yes; WBF=0 means no).
<dt>'WBL' - Real - 0.17
<dd>Size of the text labels in the station model display, expressed as a fraction of the shaft length.
<dt>'WBR' - Real - 0.25
<dd>Radius of the larger circle drawn for calm, as a fraction of the wind barb shaft length.
<dt>'WBS' - Real - 0.035
<dd>The size, expressed as a fraction of the maximum screen height, of a wind barb shaft.
<dt>'WBT' - Real - 0.33
<dd>Length of wind barb full tic as a fraction of its shaft length.
<dt>'WFC' - Integer - 1
<dd>Color index to use for warm front symbols.
<dt>'WHT' - Real - 0.014
<dd>Height of characters, expressed as a fraction of the maximum screen width, of the characters used for regional weather labels (plotted with WMLABW or c_wmlabw).
<dt>'WTY' - Integer - 0
<dd>Flag indicating whether linewidths are to be implemented via GKS (WTY=0), or simulated internally (WTY=1).</dl>

<h2>See Also</h2>

Online: wmap_params, wmbarb, wmdflt, wmdrft, wmdrrg, wmgetc, wmgeti, wmgetr, wmlabc, wmlabs, wmlabt, wmlabw, wmlgnd, wmsetc, wmseti, wmsetr, wmstnm, ncarg_cbind. 

 Hardcopy: WMAP - A Package for Producing Daily Weather Maps and Plotting Station Model Data

<h2>Copyright</h2>

Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
