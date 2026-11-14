---
title: "ncl_c_nngetaspects(3)"
name: "ncl_c_nngetaspects"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_c_nngetaspects/"
---

c_nngetaspects - retrieve the aspect at a specified coordinate. 

<h2>Function Prototype</h2>void c_nngetaspects(int, int, float *, int *);
<h2>Synopsis</h2>c_nngetaspects (row, column, aspect, ier);
<h2>Description</h2><dl COMPACT><dt>row
<dd>A subscript indexing the first dimensioned variable in the 2D grid array returned from the most recent call to c_natgrids.
<dt>column
<dd>A subscript indexing the second dimensioned variable in the 2D grid array returned from the most recent call to c_natgrids.
<dt>aspect
<dd>*aspect is the aspect at the grid point z[i,j], where z is the output grid in the most recent call to c_natgrids.
<dt>ier
<dd>An error value. If *ier is 0, then no errors were detected. If *ier is non-zero, then refer to the man page for natgrid_errors for details.</dl><h2>Usage</h2>This routine allows you to retrieve the current value of Natgrid parameters. For a complete list of parameters available in this utility, see the natgrid_params man page.
<h2>Access</h2>To use c_nngetaspects, load the NCAR Graphics library ngmath.
<h2>See Also</h2>natgrid, natgrid_params, c_nngetslopes. 

 Complete documentation for Natgrid is available at URL 
 <a rel="nofollow" HREF="http://ngwww.ucar.edu/ngdoc/ng/ngmath/natgrid/nnhome.html">http://ngwww.ucar.edu/ngdoc/ng/ngmath/natgrid/nnhome.html</a>
<h2>Copyright</h2>Copyright (C) 2000 
 University Corporation for Atmospheric Research 
 

 The use of this Software is governed by a License Agreement.
