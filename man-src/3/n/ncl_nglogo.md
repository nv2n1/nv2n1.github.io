---
title: "ncl_nglogo(3)"
name: "ncl_nglogo"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_nglogo/"
---

NGLOGO - Draws various NCAR and UCAR logos on a specified workstation. 

<h2>Synopsis</h2>CALL NGLOGO(IWK,X,Y,SIZE,ITYPE,ICOL1,ICOL2)
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/ncargC.h&gt; 

 void c_nglogo(int iwk, float x, float y, float size, 
 int itype, int icol1, int icol2) 

<h2>Description</h2><pre><code>IWK
(an input parameter of type INTEGER) The workstation identifier for
the workstation you want the logo plotted to.
X,Y
(input parameters of type REAL) specifying the X-Y coordinate
position, in normalized device coordinates (between 0. and 1.),
where the symbol is to be positioned.
This position marks the horizontal and vertical center of the symbol.
SIZE
(an input parameter of type REAL) The desired height of the logo,
expressed in normalized device coordinates.
ITYPE
(an input parameter of type INTEGER) the logo type.  The choices are:


'1'
-  An NCAR logo.  This logo will be drawn in a single color if IWK
is not a PostScript workstation.  A full color logo will be put to a
PostScript workstation.
'2'
-  A UCAR logo (just the UCAR star symbol).
'3'
-  The text &quot;NCAR&quot; in Bell Gothic Black font.
'4'
-  The text &quot;UCAR&quot; in Bell Gothic Black font.
'5'
-  UCAR star logo, plus &quot;UCAR&quot; in Bell Gothic font at
half the height of the star.  In this case, the
coordinate (X,Y) specifies the center of the star part
of the logo.



ICOL1
(an input parameter of type INTEGER) The color index to be used for the
logo color.  For the NCAR logo on PostScript output, this argument
is ignored.
ICOL2
(an input parameter of type INTEGER) A secondary color index used
only for logo type 5.  For that type, the UCAR star logo is drawn
using color index ICOL1 and the text string &quot;UCAR&quot; is drawn using
color index ICOL2.</code></pre>
<h2>C-Binding Description</h2>The C binding argument descriptions are the same as the FORTRAN argument descriptions.
<h2>Usage</h2>Call this subroutine to produce the desired logo. 

 Use the ncargex command to see the following relevant example: miex01.
<h2>Examples</h2><dl COMPACT><dt>CALL NGLOGO(1, 0.5, 0.5, 0.1, 1, 1, 1)
<dd>Plots an NCAR logo on workstation with ID 1 in the center of the plot with height one-tenth the maximum plot size. If going to a PostScript workstation, the logo will be a full-color logo, otherwise the logo will be plotted using color index 1.
<dt>CALL NGLOGO(1, 0.5, 0.5, 0.1, 2, 2, 1)
<dd>Plots a UCAR star logo on workstation with ID 1 in the center of the plot with height one-tenth the maximum plot size. The logo will be plotted using color index 2.</dl><h2>Access</h2>To use NGLOGO or c_nglogo, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.
<h2>See Also</h2>Online: plotchar (font 35) (3NCARG), 

 Hardcopy: NCAR Graphics Fundamentals, UNIX Version
<h2>Copyright</h2>Copyright (C) 1987-2002 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
