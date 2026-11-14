---
title: "ncl_nnpntd(3)"
name: "ncl_nnpntd"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_nnpntd/"
---

NNPNTD- Interpolate at a single point in double precision

<h2>Synopsis</h2>

CALL NNPNTD (X, Y, Z)

<h2>Description</h2>

<dl><dt>X
<dd>(Double precision, Input) - The X coordinate of the point where interpolation is desired.
<dt>Y
<dd>(Double precision, Input) - The Y coordinate of the point where interpolation is desired.
<dt>Z
<dd>(Double precision, Output) - The interpolated functional value at the point (X,Y).</dl>

<h2>Usage</h2>

This subroutine is called when you want to interpolate at an individal point. NNPNTINITD must be called prior to calling NNPNTD and NNPNTENDD must be called to terminate single point mode.

<h2>Access</h2>

To use NNPNTD, load the NCAR Graphics library ngmath.

<h2>See Also</h2>

natgrid, natgrid_params, natgridd, nnpntinitd, nnpntendd. 

 Complete documentation for Natgrid is available at URL 
 <a rel="nofollow" HREF="http://ngwww.ucar.edu/ngdoc/ng/ngmath/natgrid/nnhome.html">http://ngwww.ucar.edu/ngdoc/ng/ngmath/natgrid/nnhome.html</a>

<h2>Copyright</h2>

Copyright (C) 2000 
 University Corporation for Atmospheric Research 
 

 The use of this Software is governed by a License Agreement.
