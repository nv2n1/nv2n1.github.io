---
title: "ncl_cssetr(3)"
name: "ncl_cssetr"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_cssetr/"
---

CSSETR - Sets the value of an internal parameter of type REAL for the Cssgrid package. 

<h2>Synopsis</h2>CALL CSSETR (PNAM,RVAL)
<h2>Description</h2><dl COMPACT><dt>PNAM
<dd>A character string that specifies the name of the parameter to be set.
<dt>RVAL
<dd>A REAL value that is the value to be assigned to the internal parameter specified by PNAM.</dl><h2>Usage</h2>This routine allows you to set the current value of Cssgrid parameters. For a complete list of parameters available in this utility, see the cssgrid_params man page.
<h2>Access</h2>To use CSSETR, load the NCAR Graphics library ngmath.
<h2>See Also</h2>css_overview, cssgrid, cssgrid_params, csgetr. 

 Complete documentation for Cssgrid is available at URL 
 <a rel="nofollow" HREF="http://ngwww.ucar.edu/ngdoc/ng/ngmath/cssgrid/csshome.html">http://ngwww.ucar.edu/ngdoc/ng/ngmath/cssgrid/csshome.html</a>
<h2>Copyright</h2>Copyright (C) 2000 
 University Corporation for Atmospheric Research 
 

 The use of this Software is governed by a License Agreement.
