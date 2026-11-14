---
title: "ncl_ngwsym(3)"
name: "ncl_ngwsym"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_ngwsym/"
---

NGWSYM - Draws a symbol from the standard WMO/NOAA meteorological fonts by reference to the font name and symbol number within that font.

<h2>Synopsis</h2>

CALL NGWSYM(FTYPE,NUM,X,Y,SIZE,ICOLOR,IALT)

<h2>C-Binding Synopsis</h2>

#include &lt;ncarg/ncargC.h&gt; 

 void c_ngwsym(char *ftype, int num, float x, float y, 
 float size, int icolor, int ialt)

<h2>Description</h2>

<dl><dt>FTYPE
<dd>(an input parameter of type CHARACTER) specifying the desired font. Legal values are:
<dl><dd><dl><dt>'WW'
<dd>- Present weather.
<dt>'C'
<dd>- Cloud types.
<dt>'CL'
<dd>- Low clouds.
<dt>'CM'
<dd>- Medium clouds.
<dt>'CH'
<dd>- High clouds.
<dt>'W'
<dd>- Past weather.
<dt>'N'
<dd>- Sky cover.
<dt>'a'
<dd>- Pressure tendency.</dl></dl><dt>NUM
<dd>(an input parameter of type INTEGER) specifying the number of the desired symbol within the specified font.
<dt>X
<dd>(an input parameter of type REAL) specifying the X coordinate position, in world coordinates, where the symbol is to be positioned. This X position marks the horizontal center of the symbol.
<dt>Y
<dd>(an input parameter of type REAL) specifying the Y coordinate position, in world coordinates, where the symbol is to be positioned. This Y position marks the vertical center of the symbol.
<dt>SIZE
<dd>(an input parameter of type REAL) the value of which is the height, in world coordinates, of the symbol.
<dt>ICOLOR
<dd>(an input parameter of type INTEGER) the value of which is the GKS color index specifying what color the symbol will be.
<dt>IALT
<dd>(an input parameter of type INTEGER) indicating whether an alternate representation for the specified symbol is to be used. If IALT=1, then the alternate symbol for the one specified is drawn. This applies only to a few symbols such as numbers 7, 93, 94, 95, 97 in the WW font and number 3 in the W font.</dl>

<h2>C-Binding Description</h2>

The C binding argument descriptions are the same as the FORTRAN argument descriptions.

<h2>Usage</h2>

This function simply looks up the appropriate symbol in either font 36 or 37 of Plotchar and uses Plotchar to draw the symbol. 

 To produce a table of all the weather symbols broken down by font and symbol number, execute &quot;ncargex fngwsym&quot;. 

 For the WW (present weather) font, the descriptions for the symbols are: 

<dl><dt> 0
<dd>Cloud development NOT observed or NOT observable during past hour
<dt> 1
<dd>Clouds generally dissolving or becoming less developed during past hour
<dt> 2
<dd>State of sky on the whole unchanged during past hour
<dt> 3
<dd>Clouds generally forming or developing during past hour
<dt> 4
<dd>Visibility reduced by smoke
<dt> 5
<dd>Haze
<dt> 6
<dd>Widespread dust in suspension in the air, NOT raised by wind, at time of observation
<dt> 7
<dd>Dust or sand raised by wind at time of observation
<dt> 8
<dd>Well-developed dust whirl(s) within past hour
<dt> 9
<dd>Dust storm or sandstorm within sight of or at station during past hour
<dt> 10
<dd>Light fog (mist)
<dt> 11
<dd>Patches of shallow fog at station, NOT deeper than 6 feet on land
<dt> 12
<dd>More or less continuous shallow fog at station, NOT deeper than 6 feet on land
<dt> 13
<dd>Lightning visible, no thunder heard
<dt> 14
<dd>Precipitation within sight, but NOT reaching the ground
<dt> 15
<dd>Precipitation within sight, reaching the ground but distant from station
<dt> 16
<dd>Precipitation within sight, reaching the ground, near to but NOT at station
<dt> 17
<dd>Thunderstorm, but no precipitation at the station
<dt> 18
<dd>Squall(s) within sight during past hour or at time of observation
<dt> 19
<dd>Funnel cloud(s) within sight of station at time of observation
<dt> 20
<dd>Drizzle (NOT freezing) or snow grains (NOT falling as showers) during past hour, but NOT at time of observation
<dt> 21
<dd>Rain (NOT freezing and not falling as showers) during past hour, but NOT at time of observation
<dt> 22
<dd>Snow (NOT falling as showers) during past hour, but NOT at time of observation
<dt> 23
<dd>Rain and snow or ice pellets (NOT falling as showers) during past hour, but NOT at time of observation
<dt> 24
<dd>Freezing drizzle or freezing rain (NOT falling as showers) during past hour, but NOT at time of observation
<dt> 25
<dd>Showers of rain during past hour, but NOT at time of observation
<dt> 26
<dd>Showers of snow or of rain and snow, during past hour, but NOT at time of observation
<dt> 27
<dd>Showers of hail or of hail and rain, during past hour, but NOT at time of observation
<dt> 28
<dd>Fog during past hour, but NOT at time of observation
<dt> 29
<dd>Thunderstorm (with or without precipitation) during past hour, but NOT at time of observation
<dt> 30
<dd>Slight or moderate dust storm or sandstorm, has decreased during past hour
<dt> 31
<dd>Slight or moderate dust storm or sandstorm, no appreciable change during past hour
<dt> 32
<dd>Slight or moderate dust storm or sandstorm has begun or increased during past hour
<dt> 33
<dd>Severe dust storm or sandstorm, has decreased during past hour
<dt> 34
<dd>Severe dust storm or sandstorm, no appreciable change during past hour
<dt> 35
<dd>Severe dust storm or sandstorm has begun or increased during past hour
<dt> 36
<dd>Slight or moderate drifting snow, generally low (less than 6 feet)
<dt> 37
<dd>Heavy drifting snow, generally low
<dt> 38
<dd>Slight or moderate blowing snow, generally high (more than 6 feet)
<dt> 39
<dd>Heavy blowing snow, generally high
<dt> 40
<dd>For or ice fog at distance at time of observation, but NOT at station during past hour
<dt> 41
<dd>Fog or ice fog in patches
<dt> 42
<dd>Fog or ice fog, sky discernible, has become thinner during past hour
<dt> 43
<dd>Fog or ice fog, sky NOT discernible, has become thinner during past hour
<dt> 44
<dd>Fog or ice fog, sky discernible, no appreciable change during past hour
<dt> 45
<dd>Fog or ice fog, sky NOT discernible, no appreciable change during past hour
<dt> 46
<dd>Fog or ice fog, sky discernible, has begun or become thicker during past hour
<dt> 47
<dd>Fog or ice fog, sky NOT discernible, has begun or become thicker during past hour
<dt> 48
<dd>Fog depositing rime, sky discernible
<dt> 49
<dd>Fog depositing rime, sky NOT discernible
<dt> 50
<dd>Intermittent drizzle (NOT freezing), slight at time of observation
<dt> 51
<dd>Continuous drizzle (NOT freezing), slight at time of observation
<dt> 52
<dd>Intermittent drizzle (NOT freezing), moderate at time of observation
<dt> 53
<dd>Continuous drizzle (NOT freezing), moderate at time of observation
<dt> 54
<dd>Intermittent drizzle (NOT freezing), heavy at time of observation
<dt> 55
<dd>Continuous drizzle (NOT freezing), heavy at time of observation
<dt> 56
<dd>Slight freezing drizzle
<dt> 57
<dd>Moderate or heavy freezing drizzle
<dt> 58
<dd>Drizzle and rain, slight
<dt> 59
<dd>Drizzle and rain, moderate or heavy
<dt> 60
<dd>Intermittent rain (NOT freezing), slight at time of observation
<dt> 61
<dd>Continuous rain (NOT freezing), slight at time of observation
<dt> 62
<dd>Intermittent rain (NOT freezing), moderate at time of observation
<dt> 63
<dd>Continuous rain (NOT freezing), moderate at time of observation
<dt> 64
<dd>Intermittent rain (NOT freezing), heavy at time of observation
<dt> 65
<dd>Continuous rain (NOT freezing), heavy at time of observation
<dt> 66
<dd>Slight freezing rain
<dt> 67
<dd>Moderate or heavy freezing rain
<dt> 68
<dd>Rain or drizzle and snow, slight
<dt> 69
<dd>Rain or drizzle and snow, moderate or heavy
<dt> 70
<dd>Intermittent fall of snowflakes, slight at time of observation
<dt> 71
<dd>Continuous fall of snowflakes, slight at time of observation
<dt> 72
<dd>Intermittent fall of snowflakes, moderate at time of observation
<dt> 73
<dd>Continuous fall of snowflakes, moderate at time of observation
<dt> 74
<dd>Intermittent fall of snowflakes, heavy at time of observation
<dt> 75
<dd>Continuous fall of snowflakes, heavy at time of observation
<dt> 76
<dd>Ice prisms (with or without fog)
<dt> 77
<dd>Snow grains (with or without fog)
<dt> 78
<dd>Isolated starlike snow crystals (with or without fog)
<dt> 79
<dd>Ice pellets or snow pellets
<dt> 80
<dd>Slight rain shower(s)
<dt> 81
<dd>Moderate or heavy rain shower(s)
<dt> 82
<dd>Violent rain shower(s)
<dt> 83
<dd>Slight shower(s) of rain and snow mixed
<dt> 84
<dd>Moderate or heavy shower(s) of rain and snow mixed
<dt> 85
<dd>Slight snow shower(s)
<dt> 86
<dd>Moderate or heavy snow shower(s)
<dt> 87
<dd>Slight shower(s) of snow pellets, or ice pellets with or without rain, or rain and snow mixed
<dt> 88
<dd>Moderate or heavy shower(s) of snow pellets, or ice pellets, or ice pellets with or without rain or rain and snow mixed
<dt> 89
<dd>Slight shower(s) of hail, with or without rain or rain and snow mixed, not associated with thunder
<dt> 90
<dd>Moderate or heavy shower(s) of hail, with or without rain, or rain and snow mixed, not associated with thunder
<dt> 91
<dd>Slight rain at time of observation; thunderstorm during past hour, but NOT at time of observation
<dt> 92
<dd>Moderate or heavy rain at time of observation; thunderstorm during past hour, but NOT at time of observation
<dt> 93
<dd>Slight snow, or rain and snow mixed, or hail at time of observation; thunderstorm during past hour, but NOT at time of observation
<dt> 94
<dd>Moderate or heavy snow, or rain and snow mixed, or hail at time of observation; thunderstorm during past hour, but NOT at time of observation
<dt> 95
<dd>Slight or moderate thunderstorm without hail, but with rain and/or snow at time of observation
<dt> 96
<dd>Slight or moderate thunderstorm, with hail at time of observation
<dt> 97
<dd>Heavy thunderstorm, without hail, but with rain and/or snow at time of observation
<dt> 98
<dd>Thunderstorm combined with dust storm or sandstorm at time of observation
<dt> 99
<dd>Heavy thunderstorm with hail at time of observation 

 

<dt>For the C (cloud types) font:
<dd><dt> 0
<dd>Ci - Cirrus
<dt> 1
<dd>Cc - Cirrocumulus
<dt> 2
<dd>Cs - Cirrostratus
<dt> 3
<dd>Ac - Altocumulus
<dt> 4
<dd>As - Altostratus
<dt> 5
<dd>Ns - Nimbostratus
<dt> 6
<dd>Sc - Stratocumulus
<dt> 7
<dd>St - Stratus
<dt> 8
<dd>Cu - Cumulus
<dt> 9
<dd>Cb - Cumulonimbus 

 

<dt>For the CL (low clouds) font:
<dd><dt> 0
<dd>not defined
<dt> 1
<dd>Cu of fair weather, little vertical development and seemingly flattened
<dt> 2
<dd>Cu of considerable development, generally towering, with or without other Cu or Sc bases all at same level
<dt> 3
<dd>Cb with tops lacking clear-cut outlines, but distinctly not cirriform or anvil-shaped; with or without Cu, Sc, St
<dt> 4
<dd>Sc formed by spreading out of Cu; Cu often present also
<dt> 5
<dd>Sc not formed by spreading out of Cu
<dt> 6
<dd>St or StFra (stratus fractus), but no StFra of bad weather
<dt> 7
<dd>StFra and/or CuFra of bad weather (scud)
<dt> 8
<dd>Cu and Sc (not formed by spreading out of Cu) with bases at different levels
<dt> 9
<dd>Cb having clearly fibrous (cirriform) top, often anvil-shaped, with or without Cu, Sc, St, or scud 

 

<dt>For the CM (medium clouds) font:
<dd><dt> 0
<dd>not defined
<dt> 1
<dd>Thin As (most of cloud layer semitransparent)
<dt> 2
<dd>Thick As, greater part sufficiently dense to hide sun (or moon), or Ns
<dt> 3
<dd>Thin Ac, mostly semitransparent: cloud elements not changing much and at a single level
<dt> 4
<dd>Thin Ac in patches; cloud elements continually changing and/or occurring at more than one level
<dt> 5
<dd>Thin Ac in bands or in a layer gradually spreading over sky and usually thickening as a whole
<dt> 6
<dd>Ac formed by the spreading out of Cu or Cb
<dt> 7
<dd>Double-layered Ac, or a thick layer of Ac, not increasing; or Ac with As and/or Ns
<dt> 8
<dd>Ac in the form of Cu-shaped tufts or Ac with turrets
<dt> 9
<dd>Ac of a chaotic sky, usually at different levels; patches of dense Ci are usually present also 

 

<dt>For the CH (high clouds) font:
<dd><dt> 0
<dd>not defined
<dt> 1
<dd>Filaments of Ci, or &quot;mares tails,&quot; scattered and not increasing
<dt> 2
<dd>Dense Ci in patches or twisted sheaves, usually not increasing, sometimes like remains of Cb; or towers or tufts
<dt> 3
<dd>Dense Ci, often anvil-shaped, derived from or associated with Cb
<dt> 4
<dd>Ci, often hook-shaped, gradually spreading over the sky and usually thickening as a whole
<dt> 5
<dd>Ci and Cs, often in converging bands, or Cs alone; generally overspreading and growing denser; the continuous layer not reaching 45 degree altitude
<dt> 6
<dd>Ci and Cs, often in converging bands, or Cs alone; generally overspreading and growing denser; the continuous layer exceeding 45 degree altitude
<dt> 7
<dd>Veil of Cs covering the entire sky
<dt> 8
<dd>Cs not increasing and not covering entire sky
<dt> 9
<dd>Cc alone or Cc with some Ci or Cs, but the Cc being the main cirriform cloud 

 

<dt>For the W (past weather) font:
<dd><dt> 0
<dd>Clear or few clouds [no associated symbol]
<dt> 1
<dd>Partly cloudy (scattered) or variable sky [no associated symbol]
<dt> 2
<dd>Cloudy (broken) or overcast [no associated symbol]
<dt> 3
<dd>Sandstorm or dust storm, or drifting or blowing snow
<dt> 4
<dd>Fog, ice fog, thick haze or thick smoke
<dt> 5
<dd>Drizzle
<dt> 6
<dd>Rain
<dt> 7
<dd>Snow, or rain and snow mixed, or ice pellets
<dt> 8
<dd>Shower(s)
<dt> 9
<dd>Thunderstorm, with or without precipitation 

 

<dt>For the N (sky cover) font:
<dd><dt> 0
<dd>No clouds
<dt> 1
<dd>One-tenth or less
<dt> 2
<dd>Two-tenths or three-tenths
<dt> 3
<dd>Four-tenths
<dt> 4
<dd>Five-tenths
<dt> 5
<dd>Six-tenths
<dt> 6
<dd>Seven-tenths or eight tenths
<dt> 7
<dd>Nine-tenths or overcast with openings
<dt> 8
<dd>Completely overcast (ten-tenths)
<dt> 9
<dd>Sky obscured 

 

<dt>For the a (pressure tendency) font:
<dd><dt> 0
<dd>Rising, then falling; same as or higher than 3 hours ago
<dt> 1
<dd>Rising, then steady; or rising, then rising more slowly
<dt> 2
<dd>Rising steadily, or unsteadily
<dt> 3
<dd>Falling or steady, then rising; or rising, then rising more rapidly
<dt> 4
<dd>Steady; same as 3 hours ago
<dt> 5
<dd>Falling, then rising; same as or lower than 3 hours ago
<dt> 6
<dd>Falling, then steady; or falling, then falling more slowly
<dt> 7
<dd>Falling steadily, or unsteadily
<dt> 8
<dd>Steady or rising, then falling; or falling, then falling more rapidly
<dt> 9
<dd>not defined</dl>

<h2>Examples</h2>

<dl><dt>CALL NGWSYM('N',5,.5,.5,.25,1,0)
<dd>Plots the symbol for six-tenths cloud cover at position (.5,.5) and height .25 in the foreground color.
<dt>CALL NGWSYM('a',6,.2,.8,.3,1,0)
<dd>Plots the symbol for barometric pressure that is falling then steady.
<dt>CALL NGWSYM('WW',95,.5,.5,.2,1,1)
<dd>Plots the alternate symbol for slight or moderate thunderstorm without hail. 

 Use the ncargex command to see the following relevant example: fngwsym.</dl>

<h2>Access</h2>

To use NGWSYM or c_ngwsym, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.

<h2>Messages</h2>

If an illegal font, or symbol number within a font, is requested, then a warning is issued.

<h2>See Also</h2>

Online: plotchar(3NCARG), ncarg_cbind(3NCARG) 

 Hardcopy: NCAR Graphics Fundamentals, UNIX Version

<h2>Copyright</h2>

Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
