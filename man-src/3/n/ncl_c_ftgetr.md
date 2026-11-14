---
title: "ncl_c_ftgetr(3)"
name: "ncl_c_ftgetr"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_c_ftgetr/"
---

c_ftgetr - retrieve a float valued parameter
<h2>Function Prototype</h2>void c_ftgetr(char *, float *);
<h2>Synopsis</h2>void c_ftgetr (pnam, fval);
<h2>Description</h2><dl COMPACT><dt>pnam
<dd>The name of the control parameter to be assigned a float value.
<dt>fval
<dd>*fval will be the value currently assigned to the control parameter whose name is pointed to by pnam.</dl><h2>Usage</h2>c_ftgetr is used to get values for any of the control parameters that take float values.
<h2>Access</h2>To use c_ftgetr, load the NCAR Graphics library ngmath.
<h2>See Also</h2>fitgrid_params, c_ftsetr 

 Complete documentation for Fitgrid is available at URL 
 <a rel="nofollow" HREF="http://ngwww.ucar.edu/ngdoc/ng/ngmath/fitgrid/fithome.html">http://ngwww.ucar.edu/ngdoc/ng/ngmath/fitgrid/fithome.html</a>
<h2>Copyright</h2>Copyright (C) 2000 
 University Corporation for Atmospheric Research 
 

 The use of this Software is governed by a License Agreement.
