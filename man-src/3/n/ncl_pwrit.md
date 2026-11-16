---
title: "ncl_pwrit(3)"
name: "ncl_pwrit"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_pwrit/"
---

PWRIT - draws a specified text string at a specified position in the user coordinate system. The call has arguments specifying the size, orientation, and centering of the string.

<h2>Status</h2>

PWRIT is an earlier version of the routine WTSTR in which the number of characters in the text string was specified in an argument. Both WTSTR and PWRIT are now considered obsolete. 

 PWRIT continues to be provided for compatibility of early NCAR Graphics codes. If you are writing new code, we suggest that you use the more general text writing routines of the Plotchar utility: PLCHLQ, PLCHMQ, and PLCHHQ.

<h2>Synopsis</h2>

CALL PWRIT (PX,PY,CH,NC,IS,IO,IC)

<h2>Description</h2>

<dl><dt>PX
</dt><dd>(an input expression of type REAL) defines the X user coordinate where the text string is to be drawn.
</dd><dt>PY
</dt><dd>(an input expression of type REAL) defines the Y user coordinate where the text string is to be drawn.
</dd><dt>CH
</dt><dd>(an input constant or variable of type CHARACTER) is the text string to be drawn.
</dd><dt>NC
</dt><dd>(an input expression of type INTEGER) specifies the number of characters in the 'CH' text string.
</dd><dt>IS
</dt><dd>(an input expression of type INTEGER) specifies the character width in plotter address units (PAUs).
</dd><dt>IO
</dt><dd>(an input expression of type INTEGER) specifies the rotation angle of the text string. IO is measured in degrees counter-clockwise from a horizontal orientation.
</dd><dt>IC
</dt><dd>(an input expression of type INTEGER) specifies the centering option, as follows:
</dd><dl><dd></dd><dl><dt>&lt;0
</dt><dd>(PX,PY) will be in the vertical center of the left edge of the leftmost character in the original horizontal string.
</dd><dt>=0
</dt><dd>(PX,PY) will be in the center of the text extent rectangle.
</dd><dt>&gt;0
</dt><dd>(PX,PY) will be in the vertical center of the right edge of the rightmost character in the original horizontal string.</dd></dl></dl>
</dl>
 

 A call to PWRIT causes the SPPS polyline buffer to be flushed and leaves the &quot;pen&quot; (for subsequent calls to FRSTPT, VECTOR, PLOTIF, and PLOTIT) at the location (PX,PY).

<h2>Access</h2>

To use PWRIT, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.

<h2>See Also</h2>

Online: gtx, gstxal, gstxp, gstxfp, gschh, gschsp, gschup, gschxp, gscr, gstxci, spps, plotchar, plchhq, plchmq, plchlq, wtstr, plotif, seti, getsi 

 Hardcopy: NCAR Graphics Fundamentals, UNIX Version; User's Guide for NCAR GKS-0A Graphics

<h2>Copyright</h2>

Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
