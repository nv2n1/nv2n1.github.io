---
title: "ncl_shgrid(3)"
name: "ncl_shgrid"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_shgrid/"
---

SHGRID - interpolate random data in 3-space using a modified Shepard's algorithm

<h2>Synopsis</h2>

CALL SHGRID (N, X, Y, Z, F, NXO, NYO, NZO, XO, YO, ZO, 
 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>FF, IWK, RWK, IER)

<h2>Description</h2>

<dl><dt>N
</dt><dd>(integer,input) The number of input data points (N &gt; 9).
</dd><dt>X
</dt><dd>(real, input) An array containing the X coordinates of the input data points. X is dimensioned for N.
</dd><dt>Y
</dt><dd>(real, input) An array containing the Y coordinates of the input data points. Y is dimensioned for N.
</dd><dt>Z
</dt><dd>(real, input) An array containing the Z coordinates of the input data points. Z is dimensioned for N.
</dd><dt>F
</dt><dd>(real, input) Array dimensioned for N containing data values. F(I) is a functional value at (X(I),Y(I),Z(I)) for I = 1 to N.
</dd><dt>NXO
</dt><dd>(integer, input) The number of X coordinate values in the output grid.
</dd><dt>NYO
</dt><dd>(integer, input) The number of Y coordinate values in the output grid.
</dd><dt>NZO
</dt><dd>(integer, input) The number of Z coordinate values in the output grid.
</dd><dt>XO
</dt><dd>(real, input) An array dimensioned for NXO containing the X coordinates of the output surface.
</dd><dt>YO
</dt><dd>(real, input) An array dimensioned for NYO containing the Y coordinates of the output surface.
</dd><dt>ZO
</dt><dd>(real, input) An array dimensioned for NZO containing the Y coordinates of the output surface.
</dd><dt>FF
</dt><dd>(real, output) An array dimensioned for NXO x NYO x NZO containing the calculated function values for the output function. FF(I,J,K) is the calculated functional value at (XO(I), YO(J), ZO(K)) for I=1,NXO and J=1,NYO and K=1,NZO.
</dd><dt>IRK
</dt><dd>(integer, input) An integer workspace of length at least 2*N.
</dd><dt>RWK
</dt><dd>(real, input) A work array dimensioned for 11*N+6.
</dd><dt>IER
</dt><dd>(integer, output) An error return value. If IER is returned as 0, then no errors were detected. If IER is non-zero, then refer to the man page for shgrid_errors for details.</dd></dl>

<h2>Usage</h2>

SHGRID is called to interpolate randomly spaced data in 3-space. SHGRID uses a modified Shepard's algorithm to construct an interpolatory surface.

<h2>Access</h2>

To use SHGRID, load the NCAR Graphics library ngmath.

<h2>See Also</h2>

shgrid_params, shseti, shgeti, shgetnp. 

 Complete documentation for Shgrid is available at URL 
 <a rel="nofollow" HREF="http://ngwww.ucar.edu/ngdoc/ng/ngmath/shgrid/shhome.html">http://ngwww.ucar.edu/ngdoc/ng/ngmath/shgrid/shhome.html</a>

<h2>Copyright</h2>

Copyright (C) 2000 
 University Corporation for Atmospheric Research 
 

 The use of this Software is governed by a License Agreement.
