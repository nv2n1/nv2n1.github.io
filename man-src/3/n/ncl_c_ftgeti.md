---
title: "ncl_c_ftgeti(3)"
name: "ncl_c_ftgeti"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_c_ftgeti/"
---

c_ftgeti - retrieve an int valued parameter
<h2>Function Prototype</h2>void c_ftgeti(char *, int *);
<h2>Synopsis</h2>void c_ftgeti (pnam, ival);
<h2>Description</h2><dl COMPACT><dt>pnam
<dd>The name of the control parameter whose value is to be retrieved.
<dt>ival
<dd>*ival will be the value currently assigned to the control parameter whose nam.</dl><h2>Usage</h2>c_ftgeti is a called to obtain current values for any of the int valued control parameters.
<h2>Access</h2>To use c_ftgeti, load the NCAR Graphics library ngmath.
<h2>See Also</h2>fitgrid_params, c_ftseti 

 Complete documentation for Fitgrid is available at URL 
 <a rel="nofollow" HREF="http://ngwww.ucar.edu/ngdoc/ng/ngmath/fitgrid/fithome.html">http://ngwww.ucar.edu/ngdoc/ng/ngmath/fitgrid/fithome.html</a>
<h2>Copyright</h2>Copyright (C) 2000 
 University Corporation for Atmospheric Research 
 

 The use of this Software is governed by a License Agreement.
