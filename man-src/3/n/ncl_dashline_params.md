---
title: "ncl_dashline_params(3)"
name: "ncl_dashline_params"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_dashline_params/"
---

Dashline_params - Brief descriptions of all internal parameters of Dashline. 

<h2>Description</h2>No parameter-access routines are available for the utility Dashline. Parameters are set through the common blocks SMFLAG, INTPR, and DASHD1. 

 There are four different versions of Dashline: normal, quick, smooth, and super. Which version is used depends on options used on the ncargf77 command line. The lines drawn by the different versions can vary considerably in appearance. 

 The following set of common blocks may be used to access any of the internal parameters of the Dashline utility:
<dl COMPACT><dd>&nbsp;<wbr>COMMON&nbsp;<wbr>/SMFLAG/&nbsp;<wbr>IOFFS 
&nbsp;<wbr>COMMON&nbsp;<wbr>/INTPR&nbsp;<wbr>/&nbsp;<wbr>IPAU,FPART,TENSN,NP,SMALL,L1,ADDLR,ADDTB,MLLINE, 
 + ICLOSE 
&nbsp;<wbr>COMMON&nbsp;<wbr>/DASHD1/&nbsp;<wbr>ISL,L,ISIZE,IP(100),NWDSM1,IPFLAG(100),MNCSTR,IGP</dd></dl>
 

 The following table indicates which of the internal parameters affect the behavior of the various versions of Dashline (&quot;Y&quot; indicates an effect, &quot;N&quot; indicates no effect):
<dl COMPACT><dd><table> <tr VALIGN=top><td>Parameter</td><td ALIGN=center>QUICK</td><td ALIGN=center>NORMAL</td><td ALIGN=center>SMOOTH</td><td ALIGN=center>SUPER
</td></tr><tr VALIGN=top><td>---------</td><td ALIGN=center>-----</td><td ALIGN=center>------</td><td ALIGN=center>------</td><td ALIGN=center>-----
</td></tr><tr VALIGN=top><td>ADDLR</td><td ALIGN=center>N</td><td ALIGN=center>N</td><td ALIGN=center>N</td><td ALIGN=center>Y
</td></tr><tr VALIGN=top><td>ADDTB</td><td ALIGN=center>N</td><td ALIGN=center>N</td><td ALIGN=center>N</td><td ALIGN=center>Y
</td></tr><tr VALIGN=top><td>FPART</td><td ALIGN=center>N</td><td ALIGN=center>Y</td><td ALIGN=center>Y</td><td ALIGN=center>Y
</td></tr><tr VALIGN=top><td>ICLOSE</td><td ALIGN=center>Y</td><td ALIGN=center>Y</td><td ALIGN=center>Y</td><td ALIGN=center>Y
</td></tr><tr VALIGN=top><td>IGP</td><td ALIGN=center>N</td><td ALIGN=center>Y</td><td ALIGN=center>Y</td><td ALIGN=center>Y
</td></tr><tr VALIGN=top><td>IOFFS</td><td ALIGN=center>N</td><td ALIGN=center>N</td><td ALIGN=center>Y</td><td ALIGN=center>Y
</td></tr><tr VALIGN=top><td>IPAU</td><td ALIGN=center>Y</td><td ALIGN=center>Y</td><td ALIGN=center>Y</td><td ALIGN=center>Y
</td></tr><tr VALIGN=top><td>L1</td><td ALIGN=center>N</td><td ALIGN=center>N</td><td ALIGN=center>Y</td><td ALIGN=center>Y
</td></tr><tr VALIGN=top><td>MLLINE</td><td ALIGN=center>N</td><td ALIGN=center>N</td><td ALIGN=center>N</td><td ALIGN=center>Y
</td></tr><tr VALIGN=top><td>NP</td><td ALIGN=center>N</td><td ALIGN=center>N</td><td ALIGN=center>Y</td><td ALIGN=center>Y
</td></tr><tr VALIGN=top><td>SMALL</td><td ALIGN=center>N</td><td ALIGN=center>N</td><td ALIGN=center>Y</td><td ALIGN=center>Y
</td></tr><tr VALIGN=top><td>TENSN</td><td ALIGN=center>N</td><td ALIGN=center>N</td><td ALIGN=center>Y</td><td ALIGN=center>Y
</td></tr> </table></dd></dl>
 

 PARAMETER DESCRIPTIONS
<dl COMPACT><dt>ADDLR
</dt><dd>The amount of free space to be left on the left and on the right of each character string, stated as the desired number of NDCs (Normalized Device Coordinates) times 1023. This only affects the &quot;super&quot; version of Dashline; it changes the size of the area marked around a label in the bit map that is used for culling crowded lines. [Default = 2. (2./1023. NDCs)]
</dd><dt>ADDTB
</dt><dd>The amount of free space to be left on the top and on the bottom of each character string, stated as the desired number of NDCs (Normalized Device Coordinates) times 1023. This only affects the &quot;super&quot; version of Dashline; it changes the size of the area marked around a label in the bit map that is used for culling crowded lines. [Default = 2. (2./1023. NDCs)]
</dd><dt>FPART
</dt><dd>A multiplication factor for the length of the first solid line segment on any curve. This can be used to offset labels. For example, if FPART = .5, the first solid line segment is only one-half as long as the other solid line segments. This will move all labels on the current curve towards the beginning of the curve and thereby reduce the probability of a label being written on top of a label on a nearby curve drawn with FPART = 1. [Default = 1.]
</dd><dt>ICLOSE
</dt><dd>An internal or external call to move the &quot;drawing pen&quot; (pen-up) to a specific position is executed only if the position is more than ICLOSE units away from the current pen position (the distance is measured as the absolute difference in X-coordinates plus the absolute difference in Y-coordinates). The unit of measurement is 32767 integer units in each of the X and Y dimensions. [Default = 6]
</dd><dt>IGP
</dt><dd>Flag to control whether gaps are left for labels along a curve. If no gaps are left, the labels don't look as good, but you can be sure of what the curve is doing in the regions occupied by the labels.
</dd><dl COMPACT><dd></dd><dl COMPACT><dt>9
</dt><dd>A gap is left.
</dd><dt>0
</dt><dd>No gap is left.</dd></dl></dl><dd>[Default = 9]
</dd><dt>IOFFS
</dt><dd>Flag used to turn smoothing off.
</dd><dl COMPACT><dd></dd><dl COMPACT><dt>0
</dt><dd>Smoothing.
</dd><dt>1
</dt><dd>No smoothing.</dd></dl></dl><dd>[Default = 0]
</dd><dt>IPAU
</dt><dd>The length of the gap or solid line associated with each element of a dash pattern defined by a call to DASHDB, given as the desired value in NDCs (Normalized Device Coordinates) times 1023. Such a dash pattern is repeated approximately every REAL(IPAU)/64. NDC units along the length of a curve. [Default = 3 (3./1023. NDCs)]
</dd><dt>L1
</dt><dd>The maximum number of points to be saved at one time. If there are more than L1 points on a given line, L1 points are processed, then the next L1, and so on, until the entire line is processed. Smoothness between segments is maintained automatically. If L1 is increased, the dimensions of XSAVE, YSAVE, XP, YP, TEMP, and SLEN in the routine FDVDLD must be increased to the new value of L1. [Default = 70]
</dd><dt>MLLINE
</dt><dd>The maximum length in either coordinate of a single line segment to be processed by the crowded line algorithm. Line segments longer than MLLINE units in either coordinate are broken into smaller segments, each of which is processed separately. This is done to prevent anomalies in the removal of long line segments, since only the starting point and end point of each line segment is checked in that process. The unit of measurement is 32767 integer units in each of the X and Y dimensions. [Default = 384]
</dd><dt>NP
</dt><dd>Determines how many points are used to draw each smoothed curve. The value of NP is twice the maximum number of interpolated points on a horizontal curve with length equal to that of the width of the grid. More points per unit length are interpolated for short lines than for long lines. [Default = 150]
</dd><dt>SMALL
</dt><dd>When the points on a line are being processed, only the first of two consecutive points is saved if the points are less than SMALL units apart. This procedure is to prevent cusps. The unit of measurement is 32767 integer units in each of the X and Y dimensions. [Default = 128.]
</dd><dt>TENSN
</dt><dd>Tension factor. Must be greater than 0. A large tension factor (30.) would essentially turn off smoothing. [Default = 2.5]</dd></dl><h2>See Also</h2>Online: dashline, curved, dashdb, dashdc, frstd, lastd, lined, reset, vectd, ncarg_cbind 

 Hardcopy: NCAR Graphics Contouring and Mapping Tutorial; NCAR Graphics Fundamentals, UNIX Version; User's Guide for NCAR GKS-0A Graphics
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
