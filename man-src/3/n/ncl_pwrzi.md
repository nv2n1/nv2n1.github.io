---
title: "ncl_pwrzi(3)"
name: "ncl_pwrzi"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_pwrzi/"
---

PWRZI - A character-plotting routine for plotting characters in three-space when using Isosurface. For a large class of possible positions, the hidden character problem is solved.

<h2>Synopsis</h2>

SUBROUTINE PWRZI (X,Y,Z,ID,N,ISIZE,LINE,ITOP,ICNT)

<h2>C-Binding Synopsis</h2>

#include &lt;ncarg/ncargC.h&gt; 

 void c_pwrzi (float x, float y, float z, char *id, int n, 
 int isize, int line, int itop, int icnt)

<h2>Description</h2>

<dl><dt>X,Y,Z
<dd>(input expressions of type REAL) are positioning coordinates for the characters to be drawn. These are floating point numbers in the same three-space coordinate system as that used in Isosurface.
<dt>ID
<dd>(an input expression of type CHARACTER) is the character string to be drawn.
<dt>N
<dd>(an input expression of type INTEGER) is the number of characters in ID.
<dt>ISIZE
<dd>(an input expression of type INTEGER) specifies the size of the characters to be used:
<dl><dd><dl><dt>&bull;
<dd>If between 0 and 3, ISIZE is 1., 1.5, 2., or 3. times a standard width equal to 1/128th of the screen width.
<dt>&bull;
<dd>If greater than 3, ISIZE is the character width in plotter address units (by default, 1/1024th of the screen width).</dl></dl><dt>LINE
<dd>(an input expression of type INTEGER) specifies the direction in which the characters are to be written. 

 <pre>+1 = +X
-1 = -X
+2 = +Y
-2 = -Y
+3 = +Z
-3 = -Z</pre><dt>ITOP
<dd>(an input expression of type INTEGER) specifies the direction from the center of the first character to the top of the first character (the potential values for ITOP are the same as those for LINE as given above). Note that LINE cannot equal ITOP even in absolute value.
<dt>ICNT
<dd>(an input expression of type INTEGER) is the centering option:
<dl><dd><dl><dt>-1
<dd>(X,Y,Z) is the center of the left edge of the first character.
<dt>+0
<dd>(X,Y,Z) is the center of the entire string.
<dt>+1
<dd>(X,Y,Z) is the center of the right edge of the last character.</dl></dl>
</dl>

<h2>C-Binding Description</h2>

The C-binding argument descriptions are the same as the FORTRAN argument descriptions.

<h2>Usage</h2>

Call PWRZI after calling ISOSRF and before calling FRAME.

<h2>Examples</h2>

Use the ncargex command to see the following relevant examples: tpwrzi, fsrpwrzs.

<h2>Access</h2>

To use PWRZI or c_pwrzi, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.

<h2>See Also</h2>

Online: isosurface, isosurface_params, ezisos, isgeti, isgetr, isosrf, isseti, issetr, ncarg_cbind 

 Hardcopy: NCAR Graphics Fundamentals, UNIX Version

<h2>Copyright</h2>

Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
