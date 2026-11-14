---
title: "ncl_psym3(3)"
name: "ncl_psym3"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_psym3/"
---

PWRZT - Draws the projections of character strings that are positioned in a plane parallel to one of the three coordinate planes. 

 NOTE: At one time, a Threed routine called PSYM3 was supported. It has long been considered obsolete. If you call PSYM3, you will get an error message telling you to use PWRZT instead and execution will be terminated. 

 As nearly as we can determine, the statement
<dl><dd>CALL PSYM3 (U,V,W,ICHAR,ISIZE,IDIR,ITOP,IUP)</dl>
 

 may be replaced by the statements
<dl><dd>IF (IUP.EQ.2) CALL VECT3 (U,V,W) 
 CALL PWRZT (U,V,W,ICHAR,1,ISIZE,IDIR,ITOP,0)</dl>
 

 (Old manuals seem to indicate that the fifth argument in the call to PSYM3 may have been a real called SIZE, rather than an integer called ISIZE; it is not clear whether this was a misprint or not.) 

 The function of PSYM3 was to plot a symbol at the projection of a particular point; this can now be done with PWRZT. If the eighth argument in the second and following of a series of calls to PSYM3 had the value 2, straight-line segments were drawn connecting the projections of the points; this is better done with a single call to CURVE3, or by calling FRST3 for the first point and VECT3 for each of the other points.

<h2>Synopsis</h2>

CALL PWRZT (U,V,W,CHRS,LCHRS,ISIZE,IDIR,ITOP,ICEN)

<h2>C-Binding Synopsis</h2>

#include &lt;ncarg/ncargC.h&gt; 

 void c_pwrzt (float u, float v, float w, char *chrs, int lchrs, 
 int isize, int idir, int itop, int icen)

<h2>Description</h2>

<dl><dt>U,V,W
<dd>(input expressions of type REAL) are the U, V, and W coordinates of a point, in the user's 3-space, relative to which the character string is to be positioned.
<dt>CHRS
<dd>(an input constant or variable of type CHARACTER) is the character string to be drawn. It may contain uppercase alphabetic characters, the digits 0 through 9, and a small set of &quot;special&quot; characters (plus, minus, asterisk, slash, left and right parentheses, equals sign, blank, comma, and period). Other characters are treated as blanks. (Note especially that lowercase alphabetic characters are not available.)
<dt>LCHRS
<dd>(an input expression of type INTEGER) is the number of characters in CHRS.
<dt>ISIZE
<dd>(an input expression of type INTEGER) specifies the character width to be used, defined in terms of the width of the plotter frame. Because projected characters vary in width depending on just where they are placed within the box being viewed and the position from which that box is viewed, ISIZE is interpreted as specifying the width of a character when that character is positioned and viewed in such a way as to make it as large as it could possibly be - when the character is on the near side of the box and in a plane perpendicular to the line of sight. Specifically,
<dl><dd><dl><dd>If between 0 and 3, ISIZE is 1., 1.5, 2., or 3. times a standard width equal to 1/128th of the screen width.
<dd>If greater than 3, ISIZE is the character width in units of 1/1024th of the plotter frame.</dl></dl><dd>One third of the &quot;width&quot; referred to here is white space. What ISIZE really specifies is the distance between the centers of adjacent characters in a string. Characters are digitized to be 7/6 * ISIZE units high and 4/6 * ISIZE units wide, excluding white space.
<dt>IDIR
<dd>(an input expression of type INTEGER) is the direction in which the character string is to be written, as follows:
<dl><dd><dl><dd>1 = +U -1 = -U
<dd>2 = +V -2 = -V
<dd>3 = +W -3 = -W</dl></dl><dt>ITOP
<dd>(an input expression of type INTEGER) is the direction from the center of the first character to the top of the first character; possible values of ITOP are the same as those of IDIR, above. ABS(ITOP) must not be equal to ABS(IDIR).
<dt>ICEN
<dd>(an input expression of type INTEGER) is the centering option, specifying where (U,V,W) is relative to the string written, as follows:
<dl><dd><dl><dt>-1
<dd>(U,V,W) is the center of the left edge of the first character.
<dt> 0
<dd>(U,V,W) is the center of the entire string.
<dt> 1
<dd>(U,V,W) is the center of the right edge of the last character.</dl></dl>
</dl>
 

 Because characters drawn by PWRZT are stroked using the GKS polyline primitive (so that they can be projected from 3-D to 2-D), they are drawn in the current polyline color, as determined by the last call to the GKS routine GSPLCI; by default, color index 1 is used. Line width is determined by the last call to the GKS routine GSLWSC; by default, the line width scale factor is 1.

<h2>C-Binding Description</h2>

The C-binding argument descriptions are the same as the FORTRAN argument descriptions.

<h2>Examples</h2>

Use the ncargex command to see the following relevant example: tpwrzt.

<h2>Access</h2>

To use PWRZT or c_pwrzt, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.

<h2>See Also</h2>

Online: threed, curve3, fence3, frst3, line3, perim3, point3, psym3, pwrz, set3, threed, tick3, tick43, vect3, ncarg_cbind.

<h2>Copyright</h2>

Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
