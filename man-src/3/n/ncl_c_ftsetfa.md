---
title: "ncl_c_ftsetfa(3)"
name: "ncl_c_ftsetfa"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_c_ftsetfa/"
---

Set float valued array parameters
<h2>Function Prototype</h2>int c_ftsetfa(char *pnam, int n, float *far);
<h2>Synopsis</h2>int c_ftsetfa (pnam, n, far);
<h2>Description</h2><dl COMPACT><dt>pnam
<dd>The name of the control parameter to be assigned a float array value.
<dt>n
<dd>The number of float values in the array.
<dt>far
<dd>A pointer to the n-element input array.</dl><h2>Usage</h2>c_ftsetra is used to set values for any of the control parameters that take floating arrays. The values set by c_ftsetfa remain in effect until changed by subsequent calls to c_ftsetfa .
<h2>Access</h2>To use c_ftsetfa, load the NCAR Graphics library ngmath.
<h2>See Also</h2>fitgrid_params, c_ftsetfa, c_ftgetfa_size, c_ftgetfa_data 

 Complete documentation for Fitgrid is available at URL 
 <a rel="nofollow" HREF="http://ngwww.ucar.edu/ngdoc/ng/ngmath/fitgrid/fithome.html">http://ngwww.ucar.edu/ngdoc/ng/ngmath/fitgrid/fithome.html</a>
<h2>Copyright</h2>Copyright (C) 2000 
 University Corporation for Atmospheric Research 
 

 The use of this Software is governed by a License Agreement.
