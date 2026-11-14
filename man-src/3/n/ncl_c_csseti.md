---
title: "ncl_c_csseti(3)"
name: "ncl_c_csseti"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_c_csseti/"
---

c_csseti - set int valued parameters
<h2>Function Prototype</h2>void c_csseti(char *, int);
<h2>Synopsis</h2>void c_csseti (pnam, ival);
<h2>Description</h2><dl COMPACT><dt>pnam
<dd>A string that specifies the name of the parameter to be set.
<dt>ival
<dd>An int value to be assigned to the internal parameter specified by pnam.</dl><h2>Usage</h2>This routine allows you to set the current value of Cssgrid parameters. For a complete list of parameters available in this utility, see the csgrid_params man page.
<h2>Access</h2>To use c_csseti, load the NCAR Graphics library ngmath.
<h2>See Also</h2>c_csgrid, c_csgeti, csgrid_params. 

 Complete documentation for Cssgrid is available at URL 
 <a rel="nofollow" HREF="http://ngwww.ucar.edu/ngdoc/ng/ngmath/csgrid/cshome.html">http://ngwww.ucar.edu/ngdoc/ng/ngmath/csgrid/cshome.html</a>
<h2>Copyright</h2>Copyright (C) 2000 
 University Corporation for Atmospheric Research 
 

 The use of this Software is governed by a License Agreement.
