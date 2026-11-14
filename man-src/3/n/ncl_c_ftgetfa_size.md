---
title: "ncl_c_ftgetfa_size(3)"
name: "ncl_c_ftgetfa_size"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_c_ftgetfa_size/"
---

c_ftgetfa_size - retrieve the size of an array
<h2>Function Prototype</h2>int c_ftgetfa_size(char *);
<h2>Synopsis</h2>int c_ftgetfa_size (pnam);
<h2>Description</h2><dl COMPACT><dt>pnam
<dd>The name of the control parameter whose value is to be retrieved.</dl><h2>Return Value</h2>c_ftgetfa_size returns the size of the array (or returns a zero if an error occurs).
<h2>Usage</h2>c_ftgetfa_size is a called to obtain current sizes for any of the float valued control parameters.
<h2>Access</h2>To use c_ftgetfa_size, load the NCAR Graphics library ngmath.
<h2>See Also</h2>fitgrid_params, c_ftsetfa, c_ftgetfa, c_ftgetfa_data 

 Complete documentation for Fitgrid is available at URL 
 <a rel="nofollow" HREF="http://ngwww.ucar.edu/ngdoc/ng/ngmath/fitgrid/fithome.html">http://ngwww.ucar.edu/ngdoc/ng/ngmath/fitgrid/fithome.html</a>
<h2>Copyright</h2>Copyright (C) 2000 
 University Corporation for Atmospheric Research 
 

 The use of this Software is governed by a License Agreement.
