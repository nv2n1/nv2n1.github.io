---
title: "ncl_natgrid_errors(3)"
name: "ncl_natgrid_errors"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_natgrid_errors/"
---

natgrid_errors - This document briefly describes all the errors reported from Natgrid. 

<h2>Description</h2><pre><code>Each entry below includes the error number and its meaning.

1
Insufficient data in gridded region to triangulate.
2
Duplicate input data coordinates are not allowed.
3
Unable to open file for writing algorithmic data.
4
WARNING:  The ratio of vertical to horizontal scales is too
large for meaningful gradient estimation.  Rescale the data if
gradients are required.
5
WARNING:  The ratio of vertical to horizontal scales is too small
for meaningful gradient estimation.  Rescale the data if gradients
are required.
6
WARNING:  The ratio of x-axis breadth to y-axis breadth of this
gridded region may be too extreme for good interpolation.
Changing the block proportions, or rescaling the x or y
coordinate may be indicated.  Gradient calculations have been disabled.
7
Unable to allocate storage for ivector.
8
Unable to allocate storage for dvector.
9
Unable to allocate storage for **imatrix.
10
Unable to allocate storage for imatrix[].
11
Unable to allocate storage for **fmatrix.
12
Unable to allocate storage for fmatrix[].
13
Unable to allocate storage for **dmatrix.
14
Unable to allocate storage for dmatrix[].
15
Unable to allocate storage for raw data.
16
Unable to allocate storage for a simplex.
17
Unable to allocate storage for temp.
18
Unable to allocate storage for neig.
19
slopes have not been computed, set sdip.
20
row argument out of range.
21
column argument out of range.
22
aspects have not been computed, set sdip.
23
Parameter name not known.
24
Cannot open error file.
25
Automatic scaling has been done - aspects will be distorted and
consequently are not returned.  Rescale your data manually, or
by setting magx, magy, and magz appropriately.
26
Automatic scaling has been done - slopes will be distorted and
consequently are not returned.  Rescale your data manually, or
by setting magx, magy, and magz appropriately.
27
Coordinate is outside of the gridded region for a single
point interpolation.
28
Cannot compute aspects and slopes in conjunction with single
point interpolation mode.
29
Fortran DOUBLE PRECISION entries are not supported on UNICOS.
30
Error number out of range.</code></pre>
<h2>See Also</h2>natgrid, c_natgridd, c_natgrids, c_nngetaspectd, c_nngetaspects, c_nngetsloped, c_nngetslopes, natgridd, natgrids, nngetaspectd, nngetaspects, nngetslopes, nngetslpped. <pre><code>Complete documentation for Natgrid is available at URL

http://ngwww.ucar.edu/ngdoc/ng/ngmath/natgrid/nnhome.html</code></pre>
<h2>Copyright</h2>Copyright (C) 2000 
 University Corporation for Atmospheric Research 
 

 The use of this Software is governed by a License Agreement.
