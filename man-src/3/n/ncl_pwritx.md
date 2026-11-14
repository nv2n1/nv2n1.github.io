---
title: "ncl_pwritx(3)"
name: "ncl_pwritx"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_pwritx/"
---

PWRITX - draws text and other characters using polylines.

<h2>Utility</h2>

This routine is part of the Pwrite_family utility in NCAR Graphics. To see the overview man page for this utility, type &quot;man pwrite_family&quot;.

<h2>Status</h2>

PWRITX is obsolete. It has been replaced by the PLCHHQ, PLCHMQ, and PLCHLQ entries of the Plotchar utility. 

 PWRITX continues to be provided for compatibility of early NCAR Graphics codes. If you are writing new code, we suggest that you use Plotchar.

<h2>Synopsis</h2>

CALL PWRITX (X,Y,IDPC,NCHAR,JSIZE,JOR,JCTR)

<h2>Description</h2>

<dl><dt>X
<dd>(an input parameter of type REAL) defining the X world coordinate of the text string to be drawn using polylines.
<dt>Y
<dd>(an input parameter of type REAL) defining the Y world coordinate of the text string to be drawn using polylines.
<dt>IDPC
<dd>(an input string of type CHARACTER) which are the characters to be drawn. There may also be embedded function codes describing how certain characters are to be drawn.
<dt>NCHAR
<dd>(an input parameter of type INTEGER) giving the number of characters in the IDPC string. NCHAR includes a count of all characters in the string including the function codes.
<dt>JSIZE
<dd>(an input parameter of type INTEGER) giving the width of the characters to be drawn. <pre> 0 - 1.0 * the size of the digitized
 characters in the database
 1 - 1.5 * digitized size
 2 - 2.0 * digitized size
 3 - 3.0 * digitized size
 If greater than 3:
 Principal characters = JSIZE
 Indexical characters = (13/21)*JSIZE
 Cartographic characters = ( 9/21)*JSIZE</pre>One can relate these sizes to a viewport in normalized device coordinates (each axis runs 0. to 1.) by dividing by 1023. That is a character of width .05 would take up 5% of the possible picture width meaning that less than 20 characters could fit on a line. 

 Note that there is an important difference in how text sizes are handled in GKS versus PWRITX. In GKS, text size is given in terms of character heights. In PWRITX, text size (JSIZE) is given in character width.
<dt>JOR
<dd>(an input parameter of type INTEGER) giving the orientation at which the IDPC string is to be drawn. JOR is measured counter-clockwise from the positive X axis.
<dt>JCTR
<dd>(an input parameter of type INTEGER) giving the centering option for the IDPC character string. <pre> 0, (X,Y) is the center of the entire IDPC string.
 -1, (X,Y) is the center of the left edge of the
 first character.
 1 (X,Y) is the center of the right edge of the
 last character.</pre></dl>

<h2>Access</h2>

To use PWRITX, load the NCAR Graphics libraries ncarg, ncarg_gks, ncarg_c, and ncarg_c, preferably in that order.

<h2>See Also</h2>

Online: pwrite_family, pwrity, plotchar, plchhq, plchmq, plchlq 

 Hardcopy: NCAR Graphics Fundamentals, UNIX Version; User's Guide for NCAR GKS-0A Graphics

<h2>Copyright</h2>

Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
