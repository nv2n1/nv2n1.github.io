---
title: "ncl_tdplch(3)"
name: "ncl_tdplch"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_tdplch/"
---

TDPLCH - Draw a character string at a specified position in the plane of the reference parallelogram.

<h2>Synopsis</h2>

CALL TDPLCH (XPOS, YPOS, CHRS, SIZE, ANGD, CNTR)

<h2>C-Binding Synopsis</h2>

#include &lt;ncarg/ncargC.h&gt; 

 void c_tdplch(float xpos, float ypos, char *chrs, float size, float angd, float cntr)

<h2>Description</h2>

The arguments of TDPLCH are as follows:
<dl><dt>XPOS and YPOS
<dd>(input expressions of type REAL) - the parallelogram coordinates of a point relative to which the character string is to be positioned.
<dt>CHRS
<dd>(input, of type CHARACTER) - a string suitable for input to the PLOTCHAR routine PLCHHQ.
<dt>SIZE
<dd>(an input expression of type REAL) - specifies the width of the characters to be used as a multiple of the &quot;X&quot; dimension of the reference parallelogram. If the reference parallelogram is not a square, distortion of the characters is to be expected: for example, if the reference parallelogram is twice as wide as it is high, then the same will be true of characters drawn by TDPLCH.
<dt>ANGD
<dd>(an input expression of type REAL) - specifies the angle, in degrees, at which the character string is to be drawn relative to the reference parallelogram (0 =&gt; in the direction of positive X, 90 =&gt; in the direction of positive Y, 180 =&gt; in the direction of negative X, and so on).
<dt>CNTR
<dd>(an input expression of type REAL) - specifies how the character string is to be centered relative to the point (XPOS,YPOS) within the reference parallelogram. If CNTR = -1, the leading edge of the character string will be placed at (XPOS,YPOS); if CNTR = 0, the center of the character string will be placed at (XPOS,YPOS); and if CNTR = +1, the trailing edge of the character string will be placed at (XPOS,YPOS). Other values may be used, with the logical results; for example, if CNTR = -.5, the point halfway between the leading edge and the center of the character string will be placed at (XPOS,YPOS).</dl>

<h2>C-Binding Description</h2>

The C-binding argument descriptions are the same as the FORTRAN argument descriptions.

<h2>Access</h2>

To use TDPLCH or c_tdplch, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.

<h2>See Also</h2>

Online: tdclrs, tdctri, tddtri, tdgeti, tdgetr, tdgrds, tdgrid, tdgtrs, tdinit, tditri, tdlbla, tdlbls, tdline, tdlnpa, tdmtri, tdotri, tdpack, tdpack_params, tdpara, tdprpa, tdprpi, tdprpt, tdseti, tdsetr, tdsort, tdstri, tdstrs

<h2>Copyright</h2>

Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
