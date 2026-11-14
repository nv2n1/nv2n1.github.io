---
title: "ncl_c_csgetd(3)"
name: "ncl_c_csgetd"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_c_csgetd/"
---

c_csgetd - Retrieves the value of an internal parameter of type double. 

<h2>Function Prototype</h2>void c_csgetd(char *, double *);
<h2>Synopsis</h2>c_csgetd (pnam,dval)
<h2>Description</h2><dl COMPACT><dt>pnam
<dd>A string that specifies the name of the parameter to get. The name must appear as the first three characters of the string.
<dt>dval
<dd>*dval will be the value currently assigned to the control parameter whose name is pointed to by pnam.</dl><h2>Usage</h2>This routine allows you to retrieve the current value of Cssgrid parameters. For a complete list of parameters available in this utility, see the csgrid_params man page.
<h2>Access</h2>To use c_csgetd, load the NCAR Graphics library ngmath.
<h2>See Also</h2>c_csgrid, csgrid_params, c_cssetd. c_cssetr. 

 Complete documentation for Cssgrid is available at URL 
 <a rel="nofollow" HREF="http://ngwww.ucar.edu/ngdoc/ng/ngmath/csgrid/cshome.html">http://ngwww.ucar.edu/ngdoc/ng/ngmath/csgrid/cshome.html</a>
<h2>Copyright</h2>Copyright (C) 2000 
 University Corporation for Atmospheric Research 
 

 The use of this Software is governed by a License Agreement.
