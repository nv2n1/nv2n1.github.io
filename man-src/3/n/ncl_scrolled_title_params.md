---
title: "ncl_scrolled_title_params(3)"
name: "ncl_scrolled_title_params"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_scrolled_title_params/"
---

Scrolled_title_params - This document briefly describes all Scrolled_title internal parameters.

<h2>Description</h2>

Parameter descriptions, in alphabetical order, of all Scrolled_title internal parameters follow. Each description begins with a line giving the parameter name and its default value.
<dl><dt>'ALN' - 0
<dd>Flag to control whether alignment frames with dots in the corners are produced in non-test mode. 'ALN' = 0 means &quot;suppress them&quot;, 'ALN' = 1 means &quot;produce them&quot;, and 'ALN' = 2 means &quot;produce them and label the frames as 'alignment frames'&quot;.
<dt>'BGC' - 0
<dd>An integer specifying the color index to be used for the background color. If 'BGC' = 0, GKS is depended upon to fill the background; otherwise, STITLE does a GFA call to fill it.
<dt>'BGF' - -2
<dd>An integer specifying the type of background fade-in/fade-out. 

 The value &quot;-1&quot; implies that background fades are suppressed. 

 The value &quot;-2&quot; implies a fade from/to black by mapping RGB values to HSV values and varying V. 

 A non-negative value of the form &quot;ni x 1000 + no&quot; implies a fade-in from the color with color index &quot;ni&quot; and a fade-out to the color with color index &quot;no&quot;; for example, the value &quot;11012&quot; implies fading in from color 11 and out to color 12. Use &quot;999&quot; to suppress one of the fades; for example, the value &quot;26999&quot; implies fading in from color 26, but no fade-out, while the value &quot;999026&quot; implies no fade-in, but a fade-out to color 26. These fades are done using linear interpolation in the RGB system.
<dt>'BGR', 'BGG', and 'BGB' - Device default.
<dd>Real values, in the range 0. to 1., to be used for the red, green, and blue components of the background color. When one of these values is set, it defines a component of the color associated with the current value of the color index 'BGC'.
<dt>'FGC' - 1
<dd>An integer specifying the color index to be used for the default foreground color. All informative information on &quot;test run&quot; frames and all title lines for which no other color index is specified will be in the color specified by this color index.
<dt>'FGF' - -2
<dd>An integer specifying the type of foreground fade-in/fade-out. 

 The value &quot;-1&quot; implies that foreground fades are suppressed. 

 The value &quot;-2&quot; implies a fade from/to black by mapping RGB values to HSV values and varying V. 

 A non-negative value of the form &quot;ni x 1000 + no&quot; implies a fade-in from the color with color index &quot;ni&quot; and a fade-out to the color with color index &quot;no&quot;; for example, the value &quot;11012&quot; implies fading in from color 11 and out to color 12. Use &quot;999&quot; to suppress one of the fades; for example, the value &quot;26999&quot; implies fading in from color 26, but no fade-out, while the value &quot;999026&quot; implies no fade-in, but a fade-out to color 26. These fades are done using linear interpolation in the RGB system. 

 Fades are done on all foreground colors known to STITLE because SLSETR has been called to define their RGB components or because their color indices have appeared on card images defined by the argument CRDS.
<dt>'FGR','FGG', and 'FGB' - Device default.
<dd>Real values, in the range 0. to 1., to be used for the red, green, and blue components of a specified foreground color. 

 The index of the color being defined may be specified in parentheses following the 'FGR', 'FGG', or 'FGB'; for example, the statement &quot;CALL SLSETR ('<a HREF="/docs/linux/man/2-fgr/">FGR</a>(2)',.5)&quot; defines the red component of the color associated with color index 2 to be .5. If no subscript appears, the color index defined by the current value of 'FGC' is the one whose definition is affected. 

 A color can also be defined by calling the GKS subroutine GSCR and specifying the color index on one of the card images in the CRDS array. Note, however, that any color which is to be used solely in a user-supplied version of the routine SLUBKG and which is desired to be subject to fade-in/fade-out should be defined by means of SLSETR calls. 

 Characters may be drawn in any of the foreground colors.
<dt>'FIN' - 0.
<dd>Number of seconds during which to fade in titles. The background color and foreground color are faded in independently. Each color is faded in in the manner specified by the value of either 'BGF' or 'FGF', whichever is appropriate.
<dt>'FOU' - 0.
<dd>Number of seconds during which to fade out titles. The background color and foreground color are faded out independently. Each color is faded out in the manner specified by the value of either 'BGF' or 'FGF', whichever is appropriate.
<dt>'GSZ' - 40.
<dd>Value for interline spacing, defined in terms of a 1024x1024 grid. Used only by FTITLE.
<dt>'ICO' - 1
<dd>Centering option. Set to 0 to get left edges lined up at X-coordinate 64, and to 2 to get right edges lined up at X-coordinate 960. Set to 1 for centered text. Used only by FTITLE.
<dt>'ICU' - 5
<dd>Unit number for reading input. Used only by FTITLE.
<dt>'INC' - 300
<dd>Vertical spacing between test frames.
<dt>'LOG' - 4
<dd>FORTRAN logical unit number for opening WISS (Workstation-Independent Segment Storage).
<dt>'LX1' - 0
<dd>Integer, in the range 0 to 32767, specifying the X coordinate of the lower left corner of the viewport. Use 'VPL', instead.
<dt>'LX2' - 32767
<dd>Integer, in the range 0 to 32767, specifying the X coordinate of the upper right corner of the viewport. Use 'VPR', instead.
<dt>'LY1' - 0
<dd>Integer, in the range 0 to 32767, specifying the Y coordinate of the lower left corner of the viewport. Use 'VPB', instead.
<dt>'LY2' - 32767
<dd>Integer, in the range 0 to 32767, specifying the Y coordinate of the upper right corner of the viewport. Use 'VPT', instead.
<dt>'MAP' - 100
<dd>internal parameter 'MA' is to be set; otherwise, the user will be assumed to have set it. The default values of 'MAP' and 'ORV' are such as to create scrolled titles in the normal way; other values may be used to create titles that scroll upwards on the surface of the globe or that scroll off into space (a la Star Wars); the appropriate transformations need to be embedded in a user-written version of the Plotchar routine PCMPXY. (This is still rather new; eventually, there will be an example showing how to do this.)
<dt>'NFS' - 24.
<dd>The number of frames per second. The default, 24, is appropriate for film. For video, use 'NFS' = 30.
<dt>'NXE' - 512
<dd>Analogous to the Scrolled_title argument IYND, to allow for limited scrolling in the X direction. 'NXE' must be within the current Scrolled_title window.
<dt>'NXS' - 512
<dd>Analogous to the Scrolled_title argument IYST, to allow for limited scrolling in the X direction. 'NXS' must be within the current Scrolled_title window.
<dt>'ORV' - 1.E12
<dd>If non-zero, the value to which Plotchar's internal parameter 'OR' is to be set; otherwise, the user will be assumed to have set it. See the discussion of the parameter 'MAP', above.
<dt>'PSZ' - 21.
<dd>Default character height on a 1024 by 1024 grid.
<dt>'SBK' - 0
<dd>Suppresses fade in/out of the background color when a fade in/out time has been specified. If 'SBK'=0, then the fade in/out will be honored; otherwise, the background color will appear at full intensity during a fade in/out. This parameter has been superseded by 'BGF', which should be used instead. 'SBK' = 0 is equivalent to 'BGF' = -2, while 'SBK' = 1 is equivalent to 'BGF' = -1.
<dt>'SFG' - 0
<dd>Suppresses fade in/out of the foreground color when a fade in/out time has been specified. If 'SFG'=0, then the fade in/out will be honored; otherwise, the foreground color will appear at full intensity during a fade in/out. This parameter has been superseded by 'FGF', which should be used instead. 'SFG' = 0 is equivalent to 'FGF' = -2, while 'SFG' = 1 is equivalent to 'FGF' = -1.
<dt>'TM1' - 1.
<dd>Number of seconds worth of blank frames (at 'NFS' frames/second) generated before any title frames produced by a call to FTITLE. Used only by FTITLE.
<dt>'TM2' - .5
<dd>Number of seconds worth of blank frames (at 'NFS' frames/second), between sets of title frames, and after the last set of title frames, produced by a call to FTITLE. Used only by FTITLE.
<dt>'TM3' - 0.
<dd>Number of additional seconds worth of blank frames (at 'NFS' frames/second) after the last title frame produced by a call to FTITLE. 'TM3' may be negative to suppress some of the frames specified by 'TM2'; the number of seconds of blank frames after the last title frame will be the sum of 'TM2' and 'TM3'. Used only by FTITLE.
<dt>'VPB' - 0.
<dd>A real, in the range from 0. to 1., specifying the Y coordinate of the bottom edge of the STITLE viewport. 

 The STITLE viewport is used in two ways: 1) characters are clipped at its edges; and 2) it defines the rectangle which is filled by STITLE when the value of 'BGC' is non-zero. 

 Changing the values of 'VPL', 'VPR', 'VPB', and 'VPT' changes the values of 'LX1', 'LX2', 'LY1', and 'LY2' (and vice-versa); use of the names 'VPL', 'VPR', 'VPB', and 'VPT' is now preferred.
<dt>'VPL' - 0.
<dd>A real, in the range from 0. to 1., specifying the X coordinate of the left edge of the STITLE viewport.
<dt>'VPR' - 0.
<dd>A real, in the range from 0. to 1., specifying the X coordinate of the right edge of the STITLE viewport.
<dt>'VPT' - 0.
<dd>A real, in the range from 0. to 1., specifying the Y coordinate of the top edge of the STITLE viewport.
<dt>'WID' - 9
<dd>Workstation identifier for WISS (Workstation-Independent Segment Storage); this is used internally in the calls to Gflash.</dl>

<h2>See Also</h2>

Online: gflash, plotchar, slgeti, slgetr, slseti, slsetr, ncarg_cbind. 

 Hardcopy: NCAR Graphics Fundamentals, UNIX Version; User's Guide for NCAR GKS-0A Graphics

<h2>Copyright</h2>

Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
