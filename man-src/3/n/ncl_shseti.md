---
title: "ncl_shseti(3)"
name: "ncl_shseti"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_shseti/"
---

SHSETI - Sets the value of an internal parameter of type INTEGER.

<h2>Synopsis</h2>

CALL SHSETI (PNAM,IVAL)

<h2>Description</h2>

<dl><dt>PNAM
<dd>A character string that specifies the name of the parameter to be set.
<dt>IVAL
<dd>An INTEGER value that is the value to be assigned to the internal parameter specified by PNAM.</dl>

<h2>Usage</h2>

This routine allows you to set the current value of Shgrid parameters. For a complete list of parameters available in this utility, see the shgrid_params man page.

<h2>Access</h2>

To use SHSETI, load the NCAR Graphics library ngmath.

<h2>See Also</h2>

shgrid, shgrid_params, shgeti, shgetnp. 

 Complete documentation for Shgrid is available at URL 
 <a rel="nofollow" HREF="http://ngwww.ucar.edu/ngdoc/ng/ngmath/shgrid/shhome.html">http://ngwww.ucar.edu/ngdoc/ng/ngmath/shgrid/shhome.html</a>

<h2>Copyright</h2>

Copyright (C) 2000 
 University Corporation for Atmospheric Research 
 

 The use of this Software is governed by a License Agreement.
