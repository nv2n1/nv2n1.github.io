---
title: "ncl_c_shgeti(3)"
name: "ncl_c_shgeti"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_c_shgeti/"
---

c_shgeti - Retrieves the value of an internal parameter of type int. 

<h2>Function Prototype</h2>void c_shgeti(char *, int *);
<h2>Synopsis</h2>c_shgeti (pnam,ival)
<h2>Description</h2><dl COMPACT><dt>pnam
<dd>A string that specifies the name of the parameter to get. The name must appear as the first three characters of the string.
<dt>ival
<dd>*ival will be the value currently assigned to the control parameter whose name is pointed to by pnam.</dl><h2>Usage</h2>This routine allows you to retrieve the current value of Shgrid parameters. For a complete list of parameters available in this utility, see the shgrid_params man page.
<h2>Access</h2>To use c_shgeti, load the NCAR Graphics library ngmath.
<h2>See Also</h2>c_shgrid, c_shgetnp, shgrid_params, c_shgrid, c_shseti. 

 Complete documentation for Shgrid is available at URL 
 <a rel="nofollow" HREF="http://ngwww.ucar.edu/ngdoc/ng/ngmath/shgrid/shhome.html">http://ngwww.ucar.edu/ngdoc/ng/ngmath/shgrid/shhome.html</a>
<h2>Copyright</h2>Copyright (C) 2000 
 University Corporation for Atmospheric Research 
 

 The use of this Software is governed by a License Agreement.
