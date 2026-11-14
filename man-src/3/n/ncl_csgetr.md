---
title: "ncl_csgetr(3)"
name: "ncl_csgetr"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_csgetr/"
---

CSGETR - Retrieves the value of an internal parameter of type REAL. 

<h2>Synopsis</h2>CALL CSGETR (PNAM,RVAL)
<h2>Description</h2><dl COMPACT><dt>PNAM
<dd>A character string that specifies the name of the parameter to get. The name must appear as the first three characters of the string.
<dt>RVAL
<dd>A REAL variable that is the name of the variable into which the value of the internal parameter specified by PNAM is to be retrieved.</dl><h2>Usage</h2>This routine allows you to retrieve the current value of Cssgrid parameters. For a complete list of parameters available in this utility, see the cssgrid_params man page.
<h2>Access</h2>To use CSGETR, load the NCAR Graphics library ngmath.
<h2>See Also</h2>css_overview, cssgrid, cssgrid_params, cssetr. 

 Complete documentation for Cssgrid is available at URL 
 <a rel="nofollow" HREF="http://ngwww.ucar.edu/ngdoc/ng/ngmath/cssgrid/csshome.html">http://ngwww.ucar.edu/ngdoc/ng/ngmath/cssgrid/csshome.html</a>
<h2>Copyright</h2>Copyright (C) 2000 
 University Corporation for Atmospheric Research 
 

 The use of this Software is governed by a License Agreement.
