---
title: "ncl_wtstr(3)"
name: "ncl_wtstr"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_wtstr/"
---

WTSTR - draws a specified text string at a specified position in the user coordinate system. The call has arguments specifying the size, orientation, and centering of the string.

<h2>Status</h2>

WTSTR specifies character sizes in Plotter Address Units (PAUs), which are no longer used in NCAR Graphics; thus, WTSTR is considered an obsolete routine. 

 The current recognized coordinate systems are GKS world coordinates, GKS normalized device coordinates, NCAR Graphics fractional coordinates, and NCAR Graphics user coordinates. See the NCAR Graphics document &quot;NCAR Graphics Fundamentals, UNIX Version&quot; for a description of these coordinate systems. 

 WTSTR continues to be provided for compatibility of early NCAR Graphics codes. If you are writing new code, we suggest that you use the more general text writing routines of the Plotchar utility: PLCHLQ, PLCHMQ, and PLCHHQ. 

 The following definition of the PAU Coordinate System is included for the purpose of interpreting and converting PAU codes: 

 The plotter coordinates of a point are integers IPX and IPY, where IPX is between 1 and 2**MX and IPY is between 1 and 2**MY. MX and MY are internal parameters of SPPS; each has the default value 10. Values of MX and MY can be set by the routine SETI and retrieved by the routine GETSI.

<h2>Synopsis</h2>

CALL WTSTR(PX,PY,CH,IS,IO,IC)

<h2>Description</h2>

<dl><dt>PX
<dd>(an input expression of type REAL) defines the X user coordinate where the text string is to be drawn.
<dt>PY
<dd>(an input expression of type REAL) defines the Y user coordinate where the text string is to be drawn.
<dt>CH
<dd>(an input constant or variable of type CHARACTER) is the text string to be drawn.
<dt>IS
<dd>(an input expression of type INTEGER) specifies the character width in plotter address units (PAUs).
<dt>IO
<dd>(an input expression of type INTEGER) specifies the rotation angle of the text string. IO is measured in degrees counter-clockwise from a horizontal orientation.
<dt>IC
<dd>(an input expression of type INTEGER) specifies the centering option, as follows:
<dl><dd><dl><dt>&lt;0
<dd>(PX,PY) will be in the vertical center of the left edge of the leftmost character in the original horizontal string.
<dt>=0
<dd>(PX,PY) will be in the center of the text extent rectangle.
<dt>&gt;0
<dd>(PX,PY) will be in the vertical center of the right edge of the rightmost character in the original horizontal string.</dl></dl>
</dl>
 

 A call to WTSTR causes the SPPS polyline buffer to be flushed and leaves the &quot;pen&quot; (for subsequent calls to FRSTPT, VECTOR, PLOTIF, and PLOTIT) at the location (PX,PY).

<h2>Access</h2>

To use WTSTR, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.

<h2>See Also</h2>

Online: gtx, gstxal, gstxp, gstxfp, gschh, gschsp, gschup, gschxp, gscr, gstxci, spps, plotchar, plchhq, plchmq, plchlq, pwrit, plotif, seti, getsi 

 Hardcopy: NCAR Graphics Fundamentals, UNIX Version; User's Guide for NCAR GKS-0A Graphics

<h2>Copyright</h2>

Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
