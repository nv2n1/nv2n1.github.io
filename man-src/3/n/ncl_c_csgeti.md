---
title: "ncl_c_csgeti(3)"
name: "ncl_c_csgeti"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_c_csgeti/"
---

c_csgeti - Retrieves the value of an internal parameter of type int. 

<h2>Function Prototype</h2>void c_csgeti(char *, int *);
<h2>Synopsis</h2>c_csgeti (pnam,ival)
<h2>Description</h2><dl COMPACT><dt>pnam
<dd>A string that specifies the name of the parameter to get. The name must appear as the first three characters of the string.
<dt>ival
<dd>*ival will be the value currently assigned to the control parameter whose name is pointed to by pnam.</dl><h2>Usage</h2>This routine allows you to retrieve the current value of Cssgrid parameters. For a complete list of parameters available in this utility, see the csgrid_params man page.
<h2>Access</h2>To use c_csgeti, load the NCAR Graphics library ngmath.
<h2>See Also</h2>c_csgrid, csgrid_params, c_csseti. 

 Complete documentation for Cssgrid is available at URL 
 <a rel="nofollow" HREF="http://ngwww.ucar.edu/ngdoc/ng/ngmath/csgrid/cshome.html">http://ngwww.ucar.edu/ngdoc/ng/ngmath/csgrid/cshome.html</a>
<h2>Copyright</h2>Copyright (C) 2000 
 University Corporation for Atmospheric Research 
 

 The use of this Software is governed by a License Agreement.
