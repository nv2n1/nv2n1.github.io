---
title: "ncl_c_nnpnts(3)"
name: "ncl_c_nnpnts"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_c_nnpnts/"
---

c_nnpnts - interpolate at a single point 

<h2>Function Prototype</h2>void c_nnpnts(float, float, float *);
<h2>Synopsis</h2>void c_nnpntinits (x, y, z);
<h2>Description</h2><dl COMPACT><dt>x
<dd>The X coordinate of the point where interpolation is desired.
<dt>y
<dd>The Y coordinate of the point where interpolation is desired.
<dt>z
<dd>*z is the interpolated functional value at the point (X,Y).</dl><h2>Usage</h2>This function is invoked when you want to interpolate at an individal point. c_nnpntinits must be called prior to calling c_nnpnts. c_nnpntend must be called to terminate single point mode.
<h2>Access</h2>To use c_nnpnts, load the NCAR Graphics library ngmath.
<h2>See Also</h2>natgrid, natgrid_params, c_natgrids, c_nnpntinits, c_nnpntend. 

 Complete documentation for Natgrid is available at URL 
 <a rel="nofollow" HREF="http://ngwww.ucar.edu/ngdoc/ng/ngmath/natgrid/nnhome.html">http://ngwww.ucar.edu/ngdoc/ng/ngmath/natgrid/nnhome.html</a>
<h2>Copyright</h2>Copyright (C) 2000 
 University Corporation for Atmospheric Research 
 

 The use of this Software is governed by a License Agreement.
