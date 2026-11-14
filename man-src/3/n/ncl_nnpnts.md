---
title: "ncl_nnpnts(3)"
name: "ncl_nnpnts"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_nnpnts/"
---

NNPNTS- Interpolate at a single point

<h2>Synopsis</h2>

CALL NNPNTS (X, Y, Z)

<h2>Description</h2>

<dl><dt>X
<dd>(Real, Input) - The X coordinate of the point where interpolation is desired.
<dt>Y
<dd>(Real, Input) - The Y coordinate of the point where interpolation is desired.
<dt>Z
<dd>(Real, Output) - The interpolated functional value at the point (X,Y).</dl>

<h2>Usage</h2>

This subroutine is called when you want to interpolate at an individal point. NNPNTINITS must be called prior to calling NNPNTS. NNPNTEND must be called to terminate single point mode.

<h2>Access</h2>

To use NNPNTS, load the NCAR Graphics library ngmath.

<h2>See Also</h2>

natgrid, natgrid_params, natgrids, nnpntinits, nnpntend. 

 Complete documentation for Natgrid is available at URL 
 <a rel="nofollow" HREF="http://ngwww.ucar.edu/ngdoc/ng/ngmath/natgrid/nnhome.html">http://ngwww.ucar.edu/ngdoc/ng/ngmath/natgrid/nnhome.html</a>

<h2>Copyright</h2>

Copyright (C) 2000 
 University Corporation for Atmospheric Research 
 

 The use of this Software is governed by a License Agreement.
