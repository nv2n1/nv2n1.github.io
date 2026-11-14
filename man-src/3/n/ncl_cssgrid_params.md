---
title: "ncl_cssgrid_params(3)"
name: "ncl_cssgrid_params"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_cssgrid_params/"
---

cssgrid_params - This document briefly describes all the internal parameters of Cssgrid. 

<h2>Description</h2>Each entry below includes the name of a parameter, its Fortran type (use the obvious equivalents for C), its default value, and a short description of the parameter.
<dl COMPACT><dt>'SIG' - Real - computed
<dd>value of the tension factor for the splines
<dt>'TOL' - Real - 0.01
<dd>Tolerance to use in calculating gradient differences to terminate the iteration sequence when computing global gradients
<dt>'TTF' - Real - 0.01
<dd>Tolerance to use in determining how accurately each tension factor should be calculated to approximate its optimum value
<dt>'NLS' - Integer - 10
<dd>Number of nodes to use in the least squares fit.
<dt>'NSG' - Integer - 10
<dd>Maximum number of iterations to use in the algorithm for computing automatic tension factors
<dt>'ISG' - Integer - 0
<dd>Flag to revert to calculating automatic tension factors rather than use a constant tension. Using a constant tension is effected by setting a value for the control parameter sig. If isg is 0, then a tension array is used, otherwise a constant tension is used.
<dt>'IGR' - Integer - 1
<dd>Flags whether global or local gradients are used (1 implies global, anything else implies local).
<dt>'MVL' - Real - -8.
<dd>Fill value to use in returns for NCL functions. Used only if mvl has been changed from its default.</dl><h2>See Also</h2>cssgrid, csstri, csvoro, css2c, csc2s, csseti, csgeti, cssetr, csgetr, cssetd, csgetd, cssgridd, csstrid, csvorod, css2cd, csc2sd, c_cssgrid, c_csstri, c_csvoro, c_css2c, c_csc2s, c_csseti, c_csgeti, c_cssetr, c_csgetr, c_cssetd, c_csgetd, c_cssgridd, c_csstrid, c_csvorod, c_css2cd, c_csc2sd. 

 Complete documentation for Cssgrid is available at URL 
 <a rel="nofollow" HREF="http://ngwww.ucar.edu/ngdoc/ng/ngmath/csgrid/cshome.html">http://ngwww.ucar.edu/ngdoc/ng/ngmath/csgrid/cshome.html</a>
<h2>Copyright</h2>Copyright (C) 2000 
 University Corporation for Atmospheric Research 
 

 The use of this Software is governed by a License Agreement.
