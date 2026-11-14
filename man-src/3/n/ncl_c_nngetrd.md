---
title: "ncl_c_nngetrd(3)"
name: "ncl_c_nngetrd"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_c_nngetrd/"
---

c_nngetrd - retrieves the value of an internal parameter of type double. 

<h2>Function Prototype</h2>void c_nngetrd(char *, double *);
<h2>Synopsis</h2>c_nngetrd (pnam, dval)
<h2>Description</h2><dl COMPACT><dt>pnam
<dd>A string that specifies the name of the parameter to get. The name must appear as the first three characters of the string.
<dt>dval
<dd>*dval is the value currently assigned to the control parameter whose name is pointed to by pnam.</dl><h2>Usage</h2>This routine allows you to retrieve the current value of Natgrid parameters. For a complete list of parameters available in this utility, see the natgrid_params man page.
<h2>Access</h2>To use c_nngetrd, load the NCAR Graphics library ngmath.
<h2>See Also</h2>natgrid, natgrid_params, c_natgrids, c_nnsetrd. 

 Complete documentation for Natgrid is available at URL 
 <a rel="nofollow" HREF="http://ngwww.ucar.edu/ngdoc/ng/ngmath/natgrid/nnhome.html">http://ngwww.ucar.edu/ngdoc/ng/ngmath/natgrid/nnhome.html</a>
<h2>Copyright</h2>Copyright (C) 2000 
 University Corporation for Atmospheric Research 
 

 The use of this Software is governed by a License Agreement.
