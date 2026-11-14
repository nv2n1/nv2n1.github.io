---
title: "ncl_ezmap_params(3)"
name: "ncl_ezmap_params"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_ezmap_params/"
---

Ezmap_params - This document briefly describes all internal parameters of EZMAP. 

<h2>Description</h2>EZMAP has a large group of internal parameters, each of which affects the behavior of one or more of the EZMAP routines. The current values of the internal parameters may be retrieved using the routines MAPGTC, MAPGTI, MAPGTL, and MAPGTR. The values of most of the internal parameters may be reset using the routines MAPSTC, MAPSTI, MAPSTL, and MAPSTR; some of the parameters are intended for retrieval only and may not be given new values in this way. 

 Parameter descriptions, in alphabetical order, of all EZMAP internal parameters follow. Each description begins with a line giving the parameter name and the intrinsic FORTRAN type of the parameter.
<dl COMPACT><dt>'AR' - Character
<dd>For retrieval only. The value of the map limits specifier JLTS from the last call to MAPSET. The default value is 'MA'.
<dt>'Cn' - Integer
<dd>The character &quot;n&quot; is a digit between 1 and 8. Each 'Cn', if zero or greater, specifies the color index of some part of the map. The user must do the calls to GKS routines to define the color indices. All default values are -1s, indicating no change in color index from one part of the map to another.
<dt>'C1' - Integer
<dd>Color index for perimeter. See 'Cn', above.
<dt>'C2' - Integer
<dd>Color index for grid. See 'Cn', above.
<dt>'C3' - Integer
<dd>Color index for labels. See 'Cn', above.
<dt>'C4' - Integer
<dd>Color index for limb lines. See 'Cn', above.
<dt>'C5' - Integer
<dd>Color index for continent outlines. See 'Cn', above.
<dt>'C6' - Integer
<dd>Color index for U.S. state outlines. See 'Cn', above.
<dt>'C7' - Integer
<dd>Color index for outlines of countries of the world.
<dt>'C8' - Integer
<dd>Color index for outlines of counties of the world. See 'Cn', above.
<dt>'DA' - Integer
<dd>Dashed-line pattern for the grids. A 16-bit quantity. The default is 21845 (octal 52525 or binary 0101010101010101).
<dt>'DD' - Integer or Real
<dd>Distance between dots along a dotted line drawn by MAPIT. The default value is 12 (out of 4096; see 'RE', below).
<dt>'DL' - Integer or Logical
<dd>If true (non-zero), user calls to MAPIT draw dotted lines. The default is false (zero); lines drawn by MAPIT are solid or dashed, depending on the current state of the Dashline package. 'DL' may be reset by a user version of MAPUSR or MPCHLN to change the way in which the perimeter, the grid, the limb lines, and the outlines are drawn.
<dt>'DO' - Integer or Logical
<dd>If true (non-zero), outlines are dotted. The default is false (zero); outlines are solid.
<dt>'EL' - Integer or Logical
<dd>If true (non-zero), only that part of the map which falls inside an ellipse inscribed within the normal rectangular perimeter is drawn. This is particularly appropriate for use with azimuthal projections and angular limits specifying a square, in which case the ellipse becomes a circle, but it will work for any map. The default value is false (zero).
<dt>'GD' - Real
<dd>The distance between points used to draw the grid, in degrees. The default value is 1.; user values must fall between 0.001 and 10.0.
<dt>'GP' - Integer or Real
<dd>Specifies the way in which the grid, if drawn, is to be modified near the poles on projections which map the poles into single points; 'GP' is given a value of the form &quot;1000*GLAT+GLON&quot;, where GLAT is an integer between 0 and 90 and GLON is a positive real between 0 and 360. 

 If GLAT is zero, all the latitude lines of the grid are drawn; if GLAT is non-zero, latitude lines at latitudes from GLAT to 90, inclusive (South or North) are omitted. 

 If GLON is zero, no longitude lines are drawn near the poles; if GLON is non-zero, only longitude lines of the grid at multiples of GLON are drawn near the poles. 

 Examples: &quot;'GP'=0&quot; says &quot;draw all the latitude lines of the grid; omit longitude lines of the grid near the poles.&quot; &quot;'GP'=1&quot; says &quot;draw entire grid.&quot; &quot;'GP'=75045&quot; says &quot;suppress latitude lines of the grid above 75N and below 75S; near the poles, draw the longitude lines of the grid only at multiples of 45 degrees.&quot; The default is &quot;'GP'=90&quot;, which says &quot;draw all latitude lines of the grid; near the poles, omit longitude lines of the grid except those at multiples of 90 degrees&quot;.
<dt>'GR' - Integer or Real
<dd>The desired grid spacing, in degrees. (Note that, when 'GT' and/or 'GN' have values greater than zero, they are used in place of 'GR'.) Giving 'GR' a value less than or equal to zero suppresses the grid. The default value of 'GR' is 10 degrees.
<dt>'GT' and 'GN' - Integer or Real
<dd>The desired spacings of latitude and longitude grid lines, respectively (in degrees); if either is less than or equal to zero, the value of 'GR' is used instead.
<dt>'G1' - Integer
<dd>The group identifier to be used by MAPBLA or MPLNAM when putting into the area map the group of edges that define the division of the plotter frame into the projected images of geographic entities.
<dt>'G2' - Integer
<dd>The group identifier to be used by MAPBLA or MPLNAM when putting into the area map the group of edges that define the division of the plotter frame into vertical strips.
<dt>'IN' - Integer or Logical
<dd>For retrieval only. Initialization flag. If true (non-zero), it says that EZMAP is in need of initialization (by a CALL MAPINT). The default value is true (non-zero).
<dt>'LA' - Integer or Logical
<dd>If true (non-zero), label the meridians and the poles. The default is true (non-zero).
<dt>'LS' - Integer
<dd>Controls label size. A character width, to be used in a call to PWRIT. The default value is 1, which gives a character width of 12 plotter units.
<dt>'MV' - Integer or Real
<dd>Minimum vector length for MAPIT. A point closer to the previous point than this is omitted. The default value is 4 (out of 4096; see 'RE', below).
<dt>'OU' - Character
<dd>Says which set of outline data are be used by MAPLOT, MAPBLA, and MAPBLM. The possible values are 'NO' (no outlines), 'CO' (continental outlines), 'US' (U.S. state outlines), 'PS' (continental outlines plus international outlines plus U.S. outlines), and 'PO' (continental outlines plus international outlines). Default is 'CO'.
<dt>'PE' - Integer or Logical
<dd>If true (non-zero), draw the perimeter. The default is true (non-zero).
<dt>'PN' - Integer or Real
<dd>For retrieval only. The value of PLON from the last call to MAPROJ. The default value is zero.
<dt>'PR' - Character
<dd>For retrieval only. The value of the projection specifier JPRJ from the last call to MAPROJ. The default value is 'CE'.
<dt>'PT' - Integer or Real
<dd>For retrieval only. The value of PLAT from the last call to MAPROJ. The default value is zero.
<dt>'Pn' - Integer or Real
<dd>For retrieval only. The character &quot;n&quot; is a digit from 1 to 8, inclusive. Retrieves values from the call to MAPSET. P1 through P4 specify <a HREF="/docs/linux/man/1-plm1/">PLM1</a>(1), <a HREF="/docs/linux/man/1-plm2/">PLM2</a>(1), <a HREF="/docs/linux/man/1-plm3/">PLM3</a>(1), and <a HREF="/docs/linux/man/1-plm4/">PLM4</a>(1), while P5 through P8 specify <a HREF="/docs/linux/man/2-plm1/">PLM1</a>(2), <a HREF="/docs/linux/man/2-plm2/">PLM2</a>(2), <a HREF="/docs/linux/man/2-plm3/">PLM3</a>(2), and <a HREF="/docs/linux/man/2-plm4/">PLM4</a>(2). Default values are all zero.
<dt>'RE' - Integer or Real
<dd>The width of the target plotter, in plotter units. The default value is 4096.
<dt>'RO' - Integer or Real
<dd>For retrieval only. The value of ROTA from the last call to MAPROJ. The default value is zero.
<dt>'SA' - Integer or Real
<dd>If 'SA' is greater than 1., a satellite-view projection replaces the orthographic. The value is the distance of the satellite from the center of the earth, in multiples of the earth's radius. The default value is zero. See also 'S1' and 'S2', below.
<dt>'S1' and 'S2' - Integer or Real
<dd>Used only when 'SA' is greater than 1. Both are angles, in degrees. 'S1' measures the angle between the line to the center of the earth and the line of sight (to which the projection plane is perpendicular). If 'S1' is zero, the projection shows the earth as seen by a satellite looking straight down; call this the &quot;basic view&quot;. If 'S1' is non-zero, 'S2' measures the angle from the positive u axis of the basic view to the line OP, where O is the origin of the basic view and P is the projection of the desired line of sight on the basic view. 'S2' is positive if measured counter-clockwise.
<dt>'SR' - Real
<dd>A search radius, in degrees, used by MAPINT in finding the latitude/longitude range of a map. The default value is 1.; user values must lie between 0.001 and 10.0. Should not be changed except by advice of a consultant.
<dt>'VS' - Integer
<dd>The vertical-stripping parameter, which determines whether MAPBLA and MPLNAM put into the area map edge group 'G2', defining a set of vertical strips. A negative or zero value of 'VS' prevents MAPBLA and MPLNAM from doing this. A value greater than zero requests that it be done and specifies the number of vertical strips to be created. The default value of 'VS' is 1.
<dt>'XL', 'XR', 'YB', and 'YT' - Real
<dd>For retrieval only. The parameters XLOW, XROW, YBOW, and YTOW from the last call to MAPPOS. Defaults are 0.05, 0.95, 0.05, and 0.95, respectively.</dl><h2>See Also</h2>Online: mapgtc, mapgti, mapgtl, mapgtr, mappos, maproj, maprst, mapsav, mapset, mapstc, mapsti, mapstl, mapstr, mpchln, mpfnme, mpgetc, mpgeti, mpgetl, mpgetr, mpglty, mpiaty, mpifnb, mpilnb, mpiola, mpiosa, mpipai, mpipan, mpipar, mpisci, mplnam, mplndm, mplndr, mplnri, mpname, mprset, mpsetc, mpseti, mpsetl, mpsetr, 

 Hardcopy: NCAR Graphics Contouring and Mapping Tutorial
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
