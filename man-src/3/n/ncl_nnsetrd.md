---
title: "ncl_nnsetrd(3)"
name: "ncl_nnsetrd"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_nnsetrd/"
---

NNSETRD - Sets the value of an internal parameter of type DOUBLE PRECISION.

<h2>Synopsis</h2>

CALL NNSETRD (PNAM,DVAL)

<h2>Description</h2>

<dl><dt>PNAM
<dd>A character string that specifies the name of the parameter to be set.
<dt>DVAL
<dd>A DOUBLE PRECISION value that is the value to be assigned to the internal parameter specified by PNAM.</dl>

<h2>Usage</h2>

This routine allows you to set the current value of Natgrid parameters. For a complete list of parameters available in this utility, see the natgrid_params man page.

<h2>Access</h2>

To use NNSETRD, load the NCAR Graphics library ngmath.

<h2>See Also</h2>

natgrid, natgrid_params, natgridd, nngetrd. 

 Complete documentation for Natgrid is available at URL 
 <a rel="nofollow" HREF="http://ngwww.ucar.edu/ngdoc/ng/ngmath/natgrid/nnhome.html">http://ngwww.ucar.edu/ngdoc/ng/ngmath/natgrid/nnhome.html</a>

<h2>Copyright</h2>

Copyright (C) 2000 
 University Corporation for Atmospheric Research 
 

 The use of this Software is governed by a License Agreement.
