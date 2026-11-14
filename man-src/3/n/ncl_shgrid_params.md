---
title: "ncl_shgrid_params(3)"
name: "ncl_shgrid_params"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_shgrid_params/"
---

shgrid_params - This document briefly describes all the internal parameters of Shgrid.

<h2>Description</h2>

Each entry below includes the name of a parameter, its Fortran type (use the obvious equivalents for C), its default value, and a short description of the parameter.
<dl><dt>'NCL' - Integer - (N/3)**(1/3)
<dd>Granularity of 3-D cell grid
<dt>'NFL' - Integer - 32
<dd>Number of input data values within the sphere of influence.
<dt>'NLS' - Integer - 17
<dd>Nouber of data values used in the least squares fit.</dl>

<h2>See Also</h2>

shgrid, shseti, shgeti, shsetnp, c_shgrid, c_shseti, c_shseti, c_shgetnp. 

 Complete documentation for Shgrid is available at URL 
 <a rel="nofollow" HREF="http://ngwww.ucar.edu/ngdoc/ng/ngmath/shgrid/shhome.html">http://ngwww.ucar.edu/ngdoc/ng/ngmath/shgrid/shhome.html</a>

<h2>Copyright</h2>

Copyright (C) 2000 
 University Corporation for Atmospheric Research 
 

 The use of this Software is governed by a License Agreement.
