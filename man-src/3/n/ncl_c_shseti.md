---
title: "ncl_c_shseti(3)"
name: "ncl_c_shseti"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_c_shseti/"
---

c_shseti - set int valued parameters
<h2>Function Prototype</h2>void c_shseti(char *, int);
<h2>Synopsis</h2>void c_shseti (pnam, ival);
<h2>Description</h2><dl COMPACT><dt>pnam
<dd>A string that specifies the name of the parameter to be set.
<dt>ival
<dd>An int value to be assigned to the internal parameter specified by pnam.</dl><h2>Usage</h2>This routine allows you to set the current value of Shgrid parameters. For a complete list of parameters available in this utility, see the shgrid_params man page.
<h2>Access</h2>To use c_shseti, load the NCAR Graphics library ngmath.
<h2>See Also</h2>c_shgrid, c_shgetnp, c_shgeti, shgrid_params. 

 Complete documentation for Shgrid is available at URL 
 <a rel="nofollow" HREF="http://ngwww.ucar.edu/ngdoc/ng/ngmath/shgrid/shhome.html">http://ngwww.ucar.edu/ngdoc/ng/ngmath/shgrid/shhome.html</a>
<h2>Copyright</h2>Copyright (C) 2000 
 University Corporation for Atmospheric Research 
 

 The use of this Software is governed by a License Agreement.
