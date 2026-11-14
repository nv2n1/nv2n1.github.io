---
title: "ncl_c_ftsetc(3)"
name: "ncl_c_ftsetc"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_c_ftsetc/"
---

c_ftsetc - set char valued parameters
<h2>Function Prototype</h2>void c_ftsetc(char *, char *);
<h2>Synopsis</h2>void c_ftsetc (pnam, cval);
<h2>Description</h2><dl COMPACT><dt>pnam
<dd>The name of the control parameter to be assigned an string value.
<dt>ival
<dd>The value to be assigned to the control parameter whose name is pointed to by pnam.</dl><h2>Usage</h2>c_ftsetc is used to set values for any of the control parameters that take string values. The values set by c_ftsetc remain in effect until changed by subsequent calls to c_ftsetc.
<h2>Access</h2>To use c_ftsetc, load the NCAR Graphics library ngmath.
<h2>See Also</h2>fitgrid_params, c_ftgetc 

 Complete documentation for Fitgrid is available at URL 
 <a rel="nofollow" HREF="http://ngwww.ucar.edu/ngdoc/ng/ngmath/fitgrid/fithome.html">http://ngwww.ucar.edu/ngdoc/ng/ngmath/fitgrid/fithome.html</a>
<h2>Copyright</h2>Copyright (C) 2000 
 University Corporation for Atmospheric Research 
 

 The use of this Software is governed by a License Agreement.
