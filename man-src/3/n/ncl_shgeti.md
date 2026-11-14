---
title: "ncl_shgeti(3)"
name: "ncl_shgeti"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_shgeti/"
---

SHGETI - Retrieves the value of an internal parameter of type INTEGER.

<h2>Synopsis</h2>

CALL SHGETI (PNAM,IVAL)

<h2>Description</h2>

<dl><dt>PNAM
<dd>A character string that specifies the name of the parameter to get. The name must appear as the first three characters of the string.
<dt>IVAL
<dd>An INTEGER variable that is the name of the variable into which the value of the internal parameter specified by PNAM is to be retrieved.</dl>

<h2>Usage</h2>

This routine allows you to retrieve the current value of Shgrid parameters. For a complete list of parameters available in this utility, see the shgrid_params man page.

<h2>Access</h2>

To use SHGETI, load the NCAR Graphics library ngmath.

<h2>See Also</h2>

shgrid, shgrid_params, shseti, shgetnp. 

 Complete documentation for Shgrid is available at URL 
 <a rel="nofollow" HREF="http://ngwww.ucar.edu/ngdoc/ng/ngmath/shgrid/shhome.html">http://ngwww.ucar.edu/ngdoc/ng/ngmath/shgrid/shhome.html</a>

<h2>Copyright</h2>

Copyright (C) 2000 
 University Corporation for Atmospheric Research 
 

 The use of this Software is governed by a License Agreement.
