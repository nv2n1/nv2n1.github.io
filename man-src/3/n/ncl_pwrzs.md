---
title: "ncl_pwrzs(3)"
name: "ncl_pwrzs"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_pwrzs/"
---

PWRZS - A character-plotting routine for plotting characters in three-space when using SRFACE.

<h2>Synopsis</h2>

CALL PWRZS (X,Y,Z,ID,N,ISIZE,LINE,ITOP,ICNT)

<h2>C-Binding Synopsis</h2>

#include &lt;ncarg/ncargC.h&gt; 

 void c_pwrzs (float x, float y, float z, char *id, 
 int n, int isize, int line, int itop, int icnt)

<h2>Description</h2>

<dl><dt>X,Y,Z
</dt><dd>Positioning coordinates for the characters to be drawn. These are floating point numbers in the same three-space as used in SRFACE.
</dd><dt>ID
</dt><dd>Character string to be drawn. ID is of type CHARACTER.
</dd><dt>N
</dt><dd>The number of characters in ID.
</dd><dt>ISIZE
</dt><dd>Size of the character:
</dd><dl><dd></dd><dl><dt>&bull;
</dt><dd>If between 0 and 3, ISIZE is 1., 1.5, 2., or 3. times a standard width equal to 1/128th of the screen width.
</dd><dt>&bull;
</dt><dd>If greater than 3, ISIZE is the character width in plotter address units.</dd></dl></dl><dt>LINE
</dt><dd>The direction in which the characters are to be written. 

 1 = +X -1 = -X 
 2 = +Y -2 = -Y 
 3 = +Z -3 = -Z
</dd><dt>ITOP
</dt><dd>The direction from the center of the first character to the top of the first character (the potential values for ITOP are the same as those for LINE as given above). Note that LINE cannot equal ITOP even in absolute value.
</dd><dt>ICNT
</dt><dd>Centering option.
</dd><dl><dd></dd><dl><dt>-1 (X,Y,Z)
</dt><dd>is the center of the left edge of the first character.
</dd><dt>0 (X,Y,Z)
</dt><dd>is the center of the entire string.
</dd><dt>1 (X,Y,Z)
</dt><dd>is the center of the right edge of the last character.</dd></dl></dl><dd>Note that the hidden character problem is solved correctly for characters near, but not inside, the three-space object.</dd></dl>

<h2>C-Binding Description</h2>

The C-binding argument descriptions are the same as the FORTRAN argument descriptions.

<h2>Usage</h2>

Call PWRZS after calling SRFACE and before calling FRAME.

<h2>Examples</h2>

Use the ncargex command to see the following relevant examples: fsrpwrzs, tpwrzs.

<h2>Access</h2>

To use PWRZS or c_pwrzs, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.

<h2>See Also</h2>

Online: surface, surface_params, ezsrfc, setr, srface. ncarg_cbind. 

 Hardcopy: NCAR Graphics Fundamentals, UNIX Version

<h2>Copyright</h2>

Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
