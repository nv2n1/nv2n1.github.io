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
</dt><dd>A Flag to indicate whether a weather front is at the surface or aloft. ALO=0 is surface; ALO=1 is aloft.
</dd><dt>'AOC' - Integer - -1
</dt><dd>Color index for the outlines of arrows (outlines drawn only if AOC is non-negative).
</dd><dt>'ARC' - Real - 0.
</dt><dd>Length of current weather front line (retrieval only).
</dd><dt>'ARD' - Real - 0.
</dt><dd>Direction of arrows, expressed in degrees.
</dd><dt>'ARL' - Real - 1.
</dt><dd>Scale factor for the length of an arrow's tail, independent of the arrow's size.
</dd><dt>'ARS' - Real - 0.035
</dt><dd>Size of arrows, expressed as a fraction of the maximum screen height.
</dd><dt>'ASC' - Integer - -1
</dt><dd>Color index for the shadows of arrows (shadows are drawn only if ASC is non-negative).
</dd><dt>'AWC' - Integer - 1
</dt><dd>Color index for the interior of arrows.
</dd><dt>'BEG' - Real - 0.015
</dt><dd>Space, expressed in world coordinates, to leave along a front line before the first symbol is drawn.
</dd><dt>'BET' - Real - 0.045
</dt><dd>Space, expressed in world coordinates, to leave along a front line before the first symbol is drawn.
</dd><dt>'CBC' - Integer - 1
</dt><dd>The color index to be used for backgrounds of city and daily high/low labels.
</dd><dt>'CC1' - Integer - 2
</dt><dd>Color index for the interior of a cloud symbol.
</dd><dt>'CC2' - Integer - 1
</dt><dd>Color index for the outline of the cloud symbol.
</dd><dt>'CC3' - Integer - 1
</dt><dd>Color index for the shadow of the cloud symbol.
</dd><dt>'CFC' - Integer - 1
</dt><dd>Color index to use for cold front symbols.
</dd><dt>'CHT' - Real - 0.0105
</dt><dd>Height of characters, expressed as a fraction of the maximum screen width, of the city labels and daily high/low temperatures.
</dd><dt>'CMG' - Real - 0.002
</dt><dd>Size, expressed as a fraction of the maximum screen height, of the margins used for the city labels.
</dd><dt>'COL' - Integer - 1
</dt><dd>Color index to use for all objects that require only a single color setting.
</dd><dt>'CS1' - Real - N/A
</dt><dd>Slope of the left edge of a front line as calculated internally as measured in degrees from the X-axis (used when SLF=0,2, or 3). This parameter is for retrieval only.
</dd><dt>'CS2' - Real - N/A
</dt><dd>Slope of the right edge of a front line as calculated internally as measured in degrees from the X-axis (used when SLF=0,1, or 3). This parameter is for retrieval only.
</dd><dt>'DBC' - Integer - 0
</dt><dd>The color index to be used for the background shadow for the dots marking the city locations.
</dd><dt>'DTC' - Integer - 1
</dt><dd>The color index to use for the dots marking the city locations.
</dd><dt>'DTS' - Real - 0.006
</dt><dd>Size, expressed as a fraction of the maximum screen height, of the dots used to mark cities.
</dd><dt>'DWD' - Real - 2.0
</dt><dd>Line widths for front lines that do not have symbols along them (like tropical fronts and convergence lines).
</dd><dt>'END' - Real - 0.015
</dt><dd>Space, expressed in world coordinates, to leave along a front line after the last symbol has been drawn.
</dd><dt>'FRO' - Character - 'WARM'
</dt><dd>&nbsp;<wbr>Front type&nbsp;<wbr>(one of&nbsp;<wbr>`WARM',&nbsp;<wbr>`COLD',&nbsp;<wbr>`OCCLUDED',&nbsp;<wbr> `STATIONARY', `SQUALL', `TROPICAL', or `CONVERGENCE').
</dd><dt>'HIB' - Integer - 0
</dt><dd>Background color index for the &quot;H&quot; drawn for the high pressure symbols.
</dd><dt>'HIC' - Integer - 1
</dt><dd>Color index of the circumscribed circle for the &quot;H&quot; drawn for the high pressure symbols.
</dd><dt>'HIF' - Integer - 1
</dt><dd>Color index for the &quot;H&quot; drawn for the high pressure symbols.
</dd><dt>'HIS' - Integer - 1
</dt><dd>Color index for the shadow of the high pressure symbols
</dd><dt>'LC1' - Integer - 2
</dt><dd>Color index for the interior of the lightening bolt symbol
</dd><dt>'LC2' - Integer - 1
</dt><dd>Color index for the outline of the lightening bolt symbol.
</dd><dt>'LC3' - Integer - 1
</dt><dd>Color index for the shadow of the lightening bolt symbol
</dd><dt>'LIN' - Real - 8.
</dt><dd>Line widths, expressed as a fraction of the maximum screen width, for fronts having symbols along them.
</dd><dt>'LOB' - Integer - 1
</dt><dd>Color index for the background of the &quot;L&quot; drawn for the low pressure symbols.
</dd><dt>'LOF' - Integer - 0
</dt><dd>Color index for the &quot;L&quot; drawn for the low pressure symbols.
</dd><dt>'LOS' - Integer - 0
</dt><dd>Color index for the shadow of the low pressure symbols.
</dd><dt>'LWD' - Real - 0.00275
</dt><dd>Line width used when parameter WTY=1 (see below)
</dd><dt>'MXS' - Integer - 300
</dt><dd>Maximum number of symbols allowed along a weather front line.
</dd><dt>'NBZ' - Integer - 51
</dt><dd>The number of points to use in the Bezier curves for the symbols along the warm fronts.
</dd><dt>'NMS' - Integer - internally calculated
</dt><dd>Specifies precisely the number of symbols to appear along a weather front line (if this parameter has not been set by the user, then it is calculated internally).
</dd><dt>'PAI' - Integer - 1
</dt><dd>Current parameter array index used in specifying internal parameters that are arrays.
</dd><dt>'RBS' - Integer - -1
</dt><dd>The color index to use for the background of the regional temperature labels (plotted only if RBS is non-negative).
</dd><dt>'RC1' - Integer - 1
</dt><dd>Color index for the outline of the boxes drawn for the regional weather labels.
</dd><dt>'RC2' - Integer - 0
</dt><dd>Color index for the backgrounds of the boxes used for the regional weather labels.
</dd><dt>'RC3' - Integer - 1
</dt><dd>Color index for the shadow color of the boxes used for the regional weather labels.
</dd><dt>'RC4' - Integer - 1
</dt><dd>Color index for the text string used for regional weather labels.
</dd><dt>'RC5' - Integer - 1
</dt><dd>Color for the outlines of the characters in the text strings used for regional weather labels (plotted only if RC5 is non-negative).
</dd><dt>'REV' - Integer - N/A
</dt><dd>Reverses the current setting for the direction symbols will be drawn along front lines.
</dd><dt>'RFC' - Integer - 1
</dt><dd>The color index to be used for the foreground of regional temperature labels and cities.
</dd><dt>'RHT' - Real - 0.008
</dt><dd>Height, expressed as a fraction of the maximum screen width, of the characters used for the regional weather patterns (like rain, snow, etc.).
</dd><dt>'RLS' - Integer - 1
</dt><dd>The color index to use for shadows of regional temperature labels.
</dd><dt>'RMG' - Real - 0.001
</dt><dd>Size, expressed as a fraction of the maximum screen height, of the margins of the regional temperature labels.
</dd><dt>'ROS' - Integer - -1
</dt><dd>The color index to use for the outlines of the regional temperature labels (plotted only if ROS is non-negative).
</dd><dt>'SC1' - Integer - 2
</dt><dd>Color index to be used for the center of the sun symbol.
</dd><dt>'SC2' - Integer - 3
</dt><dd>Color index for the points of the sun symbol.
</dd><dt>'SC3' - Integer - 1
</dt><dd>Color index for the outline of the sun symbol.
</dd><dt>'SC4' - Integer - 1
</dt><dd>Color index for the shadow of the sun symbol.
</dd><dt>'SHT' - Real - 0.02
</dt><dd>Height of symbols, expressed as a fraction of the maximum screen width, for all the special symbols.
</dd><dt>'SL1' - Real - 0.0
</dt><dd>The slope of the beginning of a front line measured in degrees from the X-axis. This parameter is used in conjunction with the parameter SLF.
</dd><dt>'SL2' - Real - 0.0
</dt><dd>The slope of the end of a front line measured in degrees from the X-axis. This parameter is used in conjunction with the parameter SLF.
</dd><dt>'SLF' - Integer - 3
</dt><dd>Flag for indicating how the slopes at the end of a front line should be handled (0=use SL1 &amp; SL2; 1=use SL1 only; 2=use SL2 only; 3=use neither SL1 or SL2). When either SL1 or SL2 is not used, it is calculated internally.
</dd><dt>'STY' - Integer Array - all 2s
</dt><dd>An array for precisely specifying whether a warm front or cold front symbol is to be drawn at the specified position along a front line (1=cold; 2=warm). Use the internal parameter PAI for defining this array.
</dd><dt>'SWI' - Real - 0.0325
</dt><dd>Width of a symbol along a weather front, expressed as a fraction of the maximum screen width.
</dd><dt>'T1C' - Integer - 1
</dt><dd>One color to use for the alternating colors of the dashes in the tropical fronts.
</dd><dt>'T2C' - Integer - 1
</dt><dd>A second color to use for the alternating colors of the dashes in the tropical fronts.
</dd><dt>'THT' - Real - 0.0165
</dt><dd>Height of characters, expressed as a fraction of the maximum screen width, for the regional temperature labels.
</dd><dt>'UNT' - Integer - 0
</dt><dd>Flags whether imperial units (the default) or metric units are used.
</dd><dt>'VVC' - Integer - 0
</dt><dd>Flags whether the raw SYNOP codes are plotted for surface visibility (default is not to).
</dd><dt>'WBA' - Real - 62.
</dt><dd>Angle (in degrees) that the wind barb ticks make with the wind barb shafts.
</dd><dt>'WBC' - Real - 0.3
</dt><dd>Diameter of sky cover circle at base of wind barb, expressed as a fraction of the shaft length.
</dd><dt>'WBD' - Real - 0.1
</dt><dd>Spacing between tick marks along a wind barb expressed as a fraction of the wind barb shaft length.
</dd><dt>'WBF' - Integer - 0
</dt><dd>Flag indicating whether the base of a wind barb should be drawn to allow for the sky cover circle at its base (WBF=1 means yes; WBF=0 means no).
</dd><dt>'WBL' - Real - 0.17
</dt><dd>Size of the text labels in the station model display, expressed as a fraction of the shaft length.
</dd><dt>'WBR' - Real - 0.25
</dt><dd>Radius of the larger circle drawn for calm, as a fraction of the wind barb shaft length.
</dd><dt>'WBS' - Real - 0.035
</dt><dd>The size, expressed as a fraction of the maximum screen height, of a wind barb shaft.
</dd><dt>'WBT' - Real - 0.33
</dt><dd>Length of wind barb full tic as a fraction of its shaft length.
</dd><dt>'WFC' - Integer - 1
</dt><dd>Color index to use for warm front symbols.
</dd><dt>'WHT' - Real - 0.014
</dt><dd>Height of characters, expressed as a fraction of the maximum screen width, of the characters used for regional weather labels (plotted with WMLABW or c_wmlabw).
</dd><dt>'WTY' - Integer - 0
</dt><dd>Flag indicating whether linewidths are to be implemented via GKS (WTY=0), or simulated internally (WTY=1).</dd></dl>

<h2>See Also</h2>

Online: wmap_params, wmbarb, wmdflt, wmdrft, wmdrrg, wmgetc, wmgeti, wmgetr, wmlabc, wmlabs, wmlabt, wmlabw, wmlgnd, wmsetc, wmseti, wmsetr, wmstnm, ncarg_cbind. 

 Hardcopy: WMAP - A Package for Producing Daily Weather Maps and Plotting Station Model Data

<h2>Copyright</h2>

Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
