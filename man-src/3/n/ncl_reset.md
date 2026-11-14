---
title: "ncl_reset(3)"
name: "ncl_reset"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_reset/"
---

RESET - The &quot;super&quot; version of RESET zeroes the internal integer array used to detect crowded lines; other versions do nothing.

<h2>Synopsis</h2>

CALL RESET

<h2>C-Binding Synopsis</h2>

#include &lt;ncarg/ncargC.h&gt; 

 void c_reset()

<h2>Usage</h2>

The &quot;super&quot; version of the Dashline utility attempts to cull crowded lines from the output picture. It does this using an internal integer array, ISCREN, in which each bit used represents a single pixel in a square array of 1024x1024 pixels of the picture. Initially, all the bits must be set to zero by calling the routine RESET. When a line segment is about to be drawn, an appropriate set of bits in ISCREN (representing the pixels through which the line segment passes) is examined; if any bit in that set is a 1, the line segment is not drawn. Then, the bits representing the pixels in the immediate vicinity of the line segment are set to 1, so as to prevent any subsequent line segment from being drawn through the area. 

 As each label is drawn, the bits in ISCREN representing the area occupied by the label are set to 1, as well, which prevents subsequent line segments from being drawn through the label. 

 This culling process has the following implications for the user of the &quot;super&quot; version of Dashline:
<dl><dt>&bull;
<dd>The routine RESET should be called at the beginning of each new picture. If this is not done, each of a consecutive series of pictures will have progressively more gaps where line segments have been culled.
<dt>&bull;
<dd>More important lines should be drawn first, followed by less important lines. For example, the &quot;super&quot; version of the routine CONREC draws labeled contour lines first, followed by the contour lines halfway in between the labeled lines, followed by the rest of the lines.
<dt>&bull;
<dd>Because each line segment is either drawn in its entirety or not at all, long straight line segments are broken into shorter pieces. The internal parameter MLLINE determines how small the resulting pieces will be; you may wish to reduce its value so that smaller pieces will be used.</dl>

<h2>Examples</h2>

Use the ncargex command to see the following relevant examples: tdashp, fdlsmth.

<h2>Access</h2>

To use RESET or c_reset, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.

<h2>See Also</h2>

Online: dashline, dashline_params, curved, dashdb, dashdc, frstd, lastd, lined, vectd, ncarg_cbind 

 Hardcopy: NCAR Graphics Contouring and Mapping Tutorial; NCAR Graphics Fundamentals, UNIX Version; User's Guide for NCAR GKS-0A Graphics

<h2>Copyright</h2>

Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
