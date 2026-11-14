---
title: "ncl_c_ftgetfa_data(3)"
name: "ncl_c_ftgetfa_data"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_c_ftgetfa_data/"
---

c_ftgetfa_data - retrieve array values
<h2>Function Prototype</h2>float *c_ftgetfa_data(char *);
<h2>Synopsis</h2>float *c_ftgetfa_data (pnam)
<h2>Description</h2><dl COMPACT><dt>pnam
<dd>The name of the control parameter whose value is to be retrieved.</dl><h2>Return Value</h2>c_ftgetfa_data returns a pointer to a array of data (or returns a null pointer if an error occurs). The size of the array can be obtained by using c_ftgetfa_size.
<h2>Usage</h2>c_ftgetfa_data is a called to obtain current values for any of the float valued array control parameters.
<h2>Access</h2>To use c_ftgetfa_data, load the NCAR Graphics library ngmath.
<h2>See Also</h2>fitgrid_params, c_ftsetfa, c_ftgetfa, c_ftgetfa_size 

 Complete documentation for Fitgrid is available at URL 
 <a rel="nofollow" HREF="http://ngwww.ucar.edu/ngdoc/ng/ngmath/fitgrid/fithome.html">http://ngwww.ucar.edu/ngdoc/ng/ngmath/fitgrid/fithome.html</a>
<h2>Copyright</h2>Copyright (C) 2000 
 University Corporation for Atmospheric Research 
 

 The use of this Software is governed by a License Agreement.
