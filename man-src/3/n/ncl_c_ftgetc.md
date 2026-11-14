---
title: "ncl_c_ftgetc(3)"
name: "ncl_c_ftgetc"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_c_ftgetc/"
---

c_ftgetc - retrieve a string valued parameter
<h2>Function Prototype</h2>void c_ftgetc(char *, char *);
<h2>Synopsis</h2>void c_ftgetc (pnam, cval);
<h2>Description</h2><dl COMPACT><dt>pnam
<dd>The name of the control parameter whose value is to be retrieved.
<dt>cval
<dd>cval will point to a string containing the returned value. The user is required to reserve enough space to store the string.</dl><h2>Usage</h2>c_ftgetc is a called to obtain current values for any of the string valued control parameters.
<h2>Access</h2>To use c_ftgetc, load the NCAR Graphics library ngmath.
<h2>See Also</h2>fitgrid_params, c_ftsetc 

 Complete documentation for Fitgrid is available at URL 
 <a rel="nofollow" HREF="http://ngwww.ucar.edu/ngdoc/ng/ngmath/fitgrid/fithome.html">http://ngwww.ucar.edu/ngdoc/ng/ngmath/fitgrid/fithome.html</a>
<h2>Copyright</h2>Copyright (C) 2000 
 University Corporation for Atmospheric Research 
 

 The use of this Software is governed by a License Agreement.
