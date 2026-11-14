---
title: "ncl_shgrid_errors(3)"
name: "ncl_shgrid_errors"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_shgrid_errors/"
---

shgrid_errors - This document briefly describes all the errors reported from Shgrid.

<h2>Description</h2>

Each entry below includes the error number and its meaning.
<dl><dt> 0
<dd>No error.
<dt> 1
<dd>number of input data must be &gt; 9
<dt> 2
<dd>NLS must be .GT. 9
<dt> 3
<dd>number of data points used in least squares fit must be &gt; 9
<dt> 4
<dd>NFL (number of points used to calculate weights) must be at least 1
<dt> 5
<dd>number of points used in least squares fit too large
<dt> 6
<dd>number of points used in calculating weights too large
<dt> 7
<dd>cell grid dimensions must be positive
<dt> 8
<dd>duplicate input points encountered
<dt> 9
<dd>collinear input, no unique solution
<dt> 10
<dd>at least two points must have different X coordinates
<dt> 11
<dd>at least two points must have different Y coordinates
<dt> 12
<dd>at least two points must have different Z coordinates
<dt> 13
<dd>no cells contain a point within the radius of influence of the input point
<dt> 14
<dd>negative search radius in calculating least squares fit</dl>

<h2>See Also</h2>

shgrid, shseti, shgeti, shsetnp, c_shgrid, c_shseti, c_shseti, c_shgetnp. 

 Complete documentation for Shgrid is available at URL 
 <a rel="nofollow" HREF="http://ngwww.ucar.edu/ngdoc/ng/ngmath/shgrid/shhome.html">http://ngwww.ucar.edu/ngdoc/ng/ngmath/shgrid/shhome.html</a>

<h2>Copyright</h2>

Copyright (C) 2000 
 University Corporation for Atmospheric Research 
 

 The use of this Software is governed by a License Agreement.
