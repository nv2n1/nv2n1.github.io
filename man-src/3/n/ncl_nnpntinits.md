---
title: "ncl_nnpntinits(3)"
name: "ncl_nnpntinits"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_nnpntinits/"
---

NNPNTINITS- Enter single point mode

<h2>Synopsis</h2>

CALL NNPNTINITS (NPNTS, X, Y, Z)

<h2>Description</h2>

<dl><dt>NPNTS
<dd>(Integer, Input) - The number of input data points. (NPNTS &gt; 3).
<dt>X
<dd>(Real, Input) - An array of dimension NPNTS containing the X coordinates of the input data points.
<dt>Y
<dd>(Real, Input) - An array of dimension NPNTS containing the Y coordinates of the input data points.
<dt>Z
<dd>(Real, Input) - An array of dimension NPNTS containing the functional values of the input data points. That is, Z(L) is the value of the input function at coordinate (X(L),Y(L)), for L=1,NPNTS.</dl>

<h2>Usage</h2>

This subroutine is called when you want to interpolate at individal points. It is an initialization routine that sets up some internal variables and does this initial triangulation. To actually do the interplation, use subroutine NNPNTS. To terminate single point mode, use the subroutine NNPNTEND.

<h2>Access</h2>

To use NNPNTINITS, load the NCAR Graphics library ngmath.

<h2>See Also</h2>

natgrid, natgrid_params, natgrids, nnpnts, nnpntend. 

 Complete documentation for Natgrid is available at URL 
 <a rel="nofollow" HREF="http://ngwww.ucar.edu/ngdoc/ng/ngmath/natgrid/nnhome.html">http://ngwww.ucar.edu/ngdoc/ng/ngmath/natgrid/nnhome.html</a>

<h2>Copyright</h2>

Copyright (C) 2000 
 University Corporation for Atmospheric Research 
 

 The use of this Software is governed by a License Agreement.
