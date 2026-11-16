---
title: "ncl_srface(3)"
name: "ncl_srface"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_srface/"
---

SRFACE - Draws a perspective picture of a function of two variables with hidden lines removed. The function is approximated by a two-dimensional array of heights.

<h2>Synopsis</h2>

CALL SRFACE (X,Y,Z,M,MX,NX,NY,S,STEREO)

<h2>C-Binding Synopsis</h2>

#include &lt;ncarg/ncargC.h&gt; 

 void c_srface (float *x, float *y, float *z, int *m, 
 int mx, int nx, int ny, float s[6], float stereo)

<h2>Description</h2>

<dl><dt>X
</dt><dd>A linear array NX long containing the X coordinates of the points in the surface approximation. See &quot;USAGE&quot; below.
</dd><dt>Y
</dt><dd>The linear array NY long containing the Y coordinates of the points in the surface approximation. See &quot;USAGE&quot; below.
</dd><dt>Z
</dt><dd>An array MX by NY containing the surface to be drawn in NX by NY cells. Z(I,J) = F(X(I),Y(J)). See &quot;USAGE&quot; below.
</dd><dt>M
</dt><dd>Scratch array at least 2*NX*NY words long.
</dd><dt>MX
</dt><dd>First dimension of Z.
</dd><dt>NX
</dt><dd>Number of data values in the X direction (the first subscript direction) in Z to be plotted. When plotting an entire array, MX=NX.
</dd><dt>NY
</dt><dd>Number of data values in the Y direction (the second subscript direction) to be plotted.
</dd><dt>S
</dt><dd>S defines the line of sight. The viewer's eye is at (S(1), S(2), <a HREF="/docs/linux/man/3-s/">S</a>(3)) and the point looked at is at (S(4), S(5), S(6)). The eye should be outside the block with opposite corners (X(1), Y(1), ZMIN) and (X(NX), Y(NY), ZMAX) and the point looked at should be inside it. For a nice perspective effect, the distance between the eye and the point looked at should be 5 to 10 times the size of the block.
</dd><dt>STEREO
</dt><dd>Flag to indicate if stereo pairs are to be drawn. 0.0 means no stereo pair (one picture). Non-zero means put out two pictures. The value of STEREO is the relative angle between the eyes. A value of 1.0 produces standard separation. Negative STEREO reverses the left and right figures.</dd></dl>

<h2>C-Binding Description</h2>

The C-binding argument descriptions are the same as the FORTRAN argument descriptions, with the following exceptions: 

<dl><dt>z
</dt><dd>An array ny by mx.
</dd><dt>mx
</dt><dd>Second dimension of z.
</dd><dt>nx
</dt><dd>Number of data values in the y direction (the second subscript direction) in z to be plotted. When plotting an entire array, mx=nx.
</dd><dt>ny
</dt><dd>Number of data values in the x direction (the first subscript direction) to be plotted.</dd></dl>

<h2>Usage</h2>

<dl><dt>&bull;
</dt><dd>The range of Z compared with the range of X and Y determines the shape of the picture. They are assumed to be in the same units and not wildly different in magnitude. S is assumed to be in the same units as X, Y, and Z. 
</dd><dt>&bull;
</dt><dd>Picture size can be made relative to distance. 
</dd><dt>&bull;
</dt><dd>TRN32S can be used to translate from 3 space to 2 space. 
</dd><dt>&bull;
</dt><dd>Data with extreme discontinuities may cause visibility errors. If this problem occurs, use a distant eye position away from the +Z axis. 
</dd><dt>&bull;
</dt><dd>The default line color is set to color index 1. If the user wishes to change the line color, he can do so by defining color index 1 before calling SRFACE, or by putting the common block SRFINT in his calling program and defining and using color index ISRFMJ (defaulted to 1 in BLOCKDATA).</dd></dl>

<h2>Examples</h2>

Use the ncargex command to see the following relevant examples: srex01, tpwrzs, tsrfac, fsrpwrzs, fsrsrfac.

<h2>Access</h2>

To use SRFACE or c_srface, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.

<h2>See Also</h2>

Online: surface, surface_params, ezsrfc, pwrzs, setr, ncarg_cbind. 

 Hardcopy: NCAR Graphics Fundamentals, UNIX Version

<h2>Copyright</h2>

Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
