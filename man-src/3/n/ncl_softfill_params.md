---
title: "ncl_softfill_params(3)"
name: "ncl_softfill_params"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_softfill_params/"
---

Softfill_params - This document briefly describes all Softfill internal parameters.

<h2>Description</h2>

Softfill has six internal parameters. For details, see the descriptions of the routines that are used to set and retrieve them. 

 Parameter descriptions, in alphabetical order, of all Softfill internal parameters follow. Each description begins with a line giving the parameter name and the intrinsic FORTRAN type of the parameter.
<dl><dt>'AN' - Integer or Real
<dd>Angle of fill lines, in degrees counterclockwise from horizontal. The default value is zero.
<dt>'CH' - Character or Integer
<dd>Character selector (-n =&gt; GKS polymarker n; 0 =&gt; dots; +n =&gt; <a HREF="/docs/linux/man/n-char/">CHAR</a>(n)). The default value is 0.
<dt>'DO' - Integer
<dd>Dot fill selector (0 =&gt; line fill; 1 =&gt; dot fill). The default value is 0, which implies line fill.
<dt>'SP' - Real
<dd>Spacing of fill lines, in the fractional coordinate system. The default value is 0.00125.
<dt>'TY' - Integer
<dd>Type of fill to be used by SFSGFA (-1 to -4 =&gt; patterns using lines in 1 to 4 different directions and varying in density as the argument ICI varies; 0 =&gt; color fill, by calling GFA, with ICI specifying the color index; 1 =&gt; simulated color fill, using lines in one direction, with ICI specifying the color index; 2 =&gt; simulated color fill, using lines in two directions, with ICI specifying the color index). The default value is 0.
<dt>'LDP' - Integer
<dd>An 8x8 array of type INTEGER, containing nothing but 0s and 1s, describing the dot pattern to be used when 'DO' is set non-zero to select dot fill, rather than line fill. This internal parameter, unlike the others, is accessed using the routines SFGETP and SFSETP.</dl>

<h2>See Also</h2>

Online: sfgetc, sfgeti, sfgetp, sfgetr, sfsetc, sfseti, sfsetp, sfsetr 

 Hardcopy: NCAR Graphics Fundamentals, UNIX Version

<h2>Copyright</h2>

Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
