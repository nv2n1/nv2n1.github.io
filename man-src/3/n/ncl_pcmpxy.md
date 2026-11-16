---
title: "ncl_pcmpxy(3)"
name: "ncl_pcmpxy"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_pcmpxy/"
---

PCMPXY - This routine is normally not called directly by the user (though it can be). It is called by each of the routines PCHIQU, PCMEQU, and PCLOQU when the user has set the mapping flag 'MA' nonzero to request mapping of characters from one X/Y coordinate system to another.

<h2>Synopsis</h2>

CALL PCMPXY (IMAP,XINP,YINP,XOTP,YOTP)

<h2>C-Binding Synopsis</h2>

#include &lt;ncarg/ncargC.h&gt; 
 void c_pcmpxy (int imap, float xinp, float yinp, float *xotp, float *yotp)

<h2>Description</h2>

<dl><dt>IMAP
</dt><dd>(an input expression of type INTEGER) specifies which mapping is to be done. Whenever Plotchar routines call PCMPXY, IMAP = 'MA'. The default version of PCMPXY recognizes the following values of IMAP:
</dd><dl><dd></dd><dl><dt>IMAP = 0
</dt><dd></dd><dl><dd></dd><dl><dt>Type of mapping
</dt><dd>None. When IMAP is zero, the routine PCMPXY is being asked for information about its capabilities with respect to a particular mapping.
</dd><dt>XINP
</dt><dd>Input: the real equivalent of a possible value of IMAP about which information is desired.
</dd><dt>YINP
</dt><dd>Output (real): 0. says that the mapping specified by XINP is not available, 1. that it is available, 2. that its inverse is available, and 3. that both it and its inverse are available.</dd></dl></dl><dt>IMAP = 1
</dt><dd></dd><dl><dd></dd><dl><dt>Type of mapping
</dt><dd>Ezmap projection.
</dd><dt>XINP
</dt><dd>Longitude, in degrees.
</dd><dt>YINP
</dt><dd>Latitude, in degrees.</dd></dl></dl><dt>IMAP = 2
</dt><dd></dd><dl><dd></dd><dl><dt>Type of mapping
</dt><dd>Rho/theta mapping.
</dd><dt>XINP
</dt><dd>Rho, in user units.
</dd><dt>YINP
</dt><dd>Theta, in degrees.</dd></dl></dl><dt>IMAP = 3
</dt><dd></dd><dl><dd></dd><dl><dt>Type of mapping
</dt><dd>Projection from an arbitrary parallelogram in 3-space to an image plane. This is implemented using a package which is currently under development and is not yet generally available.
</dd><dt>XINP
</dt><dd>A multiplier for a unit vector along one edge of the parallelogram.
</dd><dt>YINP
</dt><dd>A multiplier for a unit vector along an intersecting edge of the parallelogram.</dd></dl></dl><dt>IMAP = 4
</dt><dd></dd><dl><dd></dd><dl><dt>Type of mapping
</dt><dd>A version of the EZMAP projection that is intended to be used to label specific points on the surface of the globe. When 'MA' = 4, use &quot;0.&quot; for each of the arguments XPOS, YPOS, and ANGD in calls to PCHIQU and PCMEQU. Initially, each label is assumed to be placed at the point on the globe with latitude zero and longitude zero and to be written along the equator. Three rotations are then performed to move the label to the point (PLAT,PLON) in such a way that it makes an angle PANG with the local eastward-pointing vector. Finally, the EZMAP routine MAPTRA is called to project the label as specified by the current state of EZMAP. The desired values of PANG, PLAT, and PLON (in degrees) are passed to PCMPXY in the labelled common block PCMP04, which contains just those three variables, in that order. Use the ncargex command to see the following relevant example: cpex10.
</dd><dt>XINP
</dt><dd>Longitude, in degrees.
</dd><dt>YINP
</dt><dd>Latitude, in degrees.</dd></dl></dl><dt>IMAP = 100
</dt><dd></dd><dl><dd></dd><dl><dt>Type of mapping
</dt><dd>The identity mapping, but returns 1.E12 outside a specified viewport. Used by the utility Scrolled_title to do clipping at the edges of the viewport.
</dd><dt>XINP
</dt><dd>X coordinate, in the fractional system.
</dd><dt>YINP
</dt><dd>Y coordinate, in the fractional system.</dd></dl></dl><dt>other &gt; 0
</dt><dd></dd><dl><dd></dd><dl><dt>Type of mapping
</dt><dd>The identity mapping.
</dd><dt>XINP
</dt><dd>Any real value.
</dd><dt>YINP
</dt><dd>Any real value.</dd></dl></dl><dt>other &lt; 0
</dt><dd></dd><dl><dd></dd><dl><dt>Type of mapping
</dt><dd>An inverse mapping.
</dd><dt>XINP
</dt><dd>A mapped X coordinate.
</dd><dt>YINP
</dt><dd>A mapped Y coordinate.</dd></dl></dl>
</dl></dl><dd>Note: Values of IMAP less than or equal to zero are not currently used by Plotchar in calling PCMPXY. The scheme described is the same as that used for the routine CPMPXY, in the NCAR Graphics package Conpack. It is possible that, in the future, values of IMAP less than or equal to zero will occur in calls to PCMPXY, so it is best to be prepared.
</dd><dt>XINP and YINP
</dt><dd>(input expressions of type REAL) specify the X and Y coordinates of a point to be mapped. 

 Note: When IMAP is less than or equal to zero (which cannot currently happen, but may someday be possible), XINP and YINP are used differently, as shown above.
</dd><dt>XOTP and YOTP
</dt><dd>(output variables of type REAL) in which PCMPXY returns the mapped X and Y coordinates of the point. If the point is not visible under the mapping selected (as, for example, when the orthographic projection of Ezmap is being used and the point to be mapped is on the other side of the globe), PCMPXY must return, as a signal that this is the case, whatever special nonzero value has been given to the internal parameter 'OR', so that the calling routine can take appropriate action (to properly clip the character being drawn, for example). 

 Note: When IMAP is less than or equal to zero (which cannot currently happen, but may someday be possible), XOTP and YOTP are used differently, as shown in the table above.</dd></dl>

<h2>C-Binding Description</h2>

The C-binding argument descriptions are the same as the FORTRAN argument descriptions.

<h2>Usage</h2>

This routine is normally not called directly by the user (though it can be). It is called by each of the routines PCHIQU, PCMEQU, and PCLOQU when the user has set the mapping flag 'MA' nonzero to request mapping of characters from one X/Y coordinate system to another. A call to PCMPXY has the following form: 

 CALL PCMPXY (IMAP,XINP,YINP,XOTP,YOTP) 

 The default version of PCMPXY does several useful mappings; a user version may be supplied to do others.

<h2>Access</h2>

To use PCMPXY or c_pcmpxy, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.

<h2>See Also</h2>

Online: plotchar, pcdlsc, pcgetc, pcgeti, pcgetr, pchiqu, pcloqu, pcmequ, pcpnwi, pcrset, pcsetc, pcseti, pcsetr, ncarg_cbind. 

 Hardcopy: NCAR Graphics Fundamentals, UNIX Version

<h2>Copyright</h2>

Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
