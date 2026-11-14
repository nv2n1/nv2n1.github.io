---
title: "ncl_nngetc(3)"
name: "ncl_nngetc"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_nngetc/"
---

NNGETC - Retrieves the value of an internal parameter of type CHARACTER.

<h2>Synopsis</h2>

CALL NNGETC (PNAM,CVAL)

<h2>Description</h2>

<dl><dt>PNAM
<dd>A character string that specifies the name of the parameter to be retrieved. The name must appear as the first three characters of the string.
<dt>CVAL
<dd>A character string that is the name of the variable into which the value of the internal parameter specified by PNAM is to be retrieved.</dl>

<h2>Usage</h2>

This routine allows you to retrieve the current value of Natgrid parameters. For a complete list of parameters available in this utility, see the natgrid_params man page.

<h2>Access</h2>

To use NNGETC, load the NCAR Graphics library ngmath.

<h2>See Also</h2>

natgrid, natgrid_params, natgrids, nnsetc. 

 Complete documentation for Natgrid is available at URL 
 <a rel="nofollow" HREF="http://ngwww.ucar.edu/ngdoc/ng/ngmath/natgrid/nnhome.html">http://ngwww.ucar.edu/ngdoc/ng/ngmath/natgrid/nnhome.html</a>

<h2>Copyright</h2>

Copyright (C) 2000 
 University Corporation for Atmospheric Research 
 

 The use of this Software is governed by a License Agreement.
