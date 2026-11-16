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
</dt><dd>No error.
</dd><dt> 1
</dt><dd>number of input data must be &gt; 9
</dd><dt> 2
</dt><dd>NLS must be .GT. 9
</dd><dt> 3
</dt><dd>number of data points used in least squares fit must be &gt; 9
</dd><dt> 4
</dt><dd>NFL (number of points used to calculate weights) must be at least 1
</dd><dt> 5
</dt><dd>number of points used in least squares fit too large
</dd><dt> 6
</dt><dd>number of points used in calculating weights too large
</dd><dt> 7
</dt><dd>cell grid dimensions must be positive
</dd><dt> 8
</dt><dd>duplicate input points encountered
</dd><dt> 9
</dt><dd>collinear input, no unique solution
</dd><dt> 10
</dt><dd>at least two points must have different X coordinates
</dd><dt> 11
</dt><dd>at least two points must have different Y coordinates
</dd><dt> 12
</dt><dd>at least two points must have different Z coordinates
</dd><dt> 13
</dt><dd>no cells contain a point within the radius of influence of the input point
</dd><dt> 14
</dt><dd>negative search radius in calculating least squares fit</dd></dl>

<h2>See Also</h2>

shgrid, shseti, shgeti, shsetnp, c_shgrid, c_shseti, c_shseti, c_shgetnp. 

 Complete documentation for Shgrid is available at URL 
 <a rel="nofollow" HREF="http://ngwww.ucar.edu/ngdoc/ng/ngmath/shgrid/shhome.html">http://ngwww.ucar.edu/ngdoc/ng/ngmath/shgrid/shhome.html</a>

<h2>Copyright</h2>

Copyright (C) 2000 
 University Corporation for Atmospheric Research 
 

 The use of this Software is governed by a License Agreement.
