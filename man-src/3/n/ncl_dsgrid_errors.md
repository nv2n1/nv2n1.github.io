---
title: "ncl_dsgrid_errors(3)"
name: "ncl_dsgrid_errors"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_dsgrid_errors/"
---

dsgrid_errors - This document briefly describes all the errors reported from Dsgrid. 

<h2>Description</h2>Each entry below includes the error number and its meaning.
<dl COMPACT><dt> 1
</dt><dd>Error number out of range.
</dd><dt> 2
</dt><dd>Insufficient data in gridded region to triangulate.
</dd><dt> 3
</dt><dd>Array dimension out of range.
</dd><dt> 4
</dt><dd>Parameter name not known.
</dd><dt> 5
</dt><dd>Cannot open error file.
</dd><dt> 6
</dt><dd>Error allocating memory for input points.
</dd><dt> 7
</dt><dd>Fortran DOUBLE PRECISION entries are not supported on UNICOS.
</dd><dt> 9
</dt><dd>Error allocating memory for array of distances between input points.
</dd><dt>10
</dt><dd>Error allocating memory for weights.
</dd><dt>11
</dt><dd>Error allocating memory for distance ordering vector.
</dd><dt>12
</dt><dd>Error allocating memory for output array.
</dd><dt>13
</dt><dd>Number of input points must be greater than 2.
</dd><dt>14
</dt><dd>No original data values within the specified distance - interpolated value set to missing value flag.</dd></dl><h2>See Also</h2>dsgrid, dsgrid_params, dsgrid2s, dsgrid3s, dsgrid2d, dsgrid3d, dspnt2s, dspnt2d, dspnt3s, dspnt3d 

 Complete documentation for Dsgrid is available at URL 
 <a rel="nofollow" HREF="http://ngwww.ucar.edu/ngdoc/ng/ngmath/dsgrid/dshome.html">http://ngwww.ucar.edu/ngdoc/ng/ngmath/dsgrid/dshome.html</a>
<h2>Copyright</h2>Copyright (C) 2000 
 University Corporation for Atmospheric Research 
 

 The use of this Software is governed by a License Agreement.
