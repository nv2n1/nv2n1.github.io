---
title: "ncl_dsgetr(3)"
name: "ncl_dsgetr"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_dsgetr/"
---

DSGETR - Retrieves the value of an internal parameter of type REAL. 

<h2>Synopsis</h2>CALL DSGETR (PNAM,RVAL)
<h2>Description</h2><dl COMPACT><dt>PNAM
<dd>A character string that specifies the name of the parameter to get. The name must appear as the first three characters of the string.
<dt>RVAL
<dd>A REAL variable that is the name of the variable into which the value of the internal parameter specified by PNAM is to be retrieved.</dl><h2>Usage</h2>This routine allows you to retrieve the current value of Dsgrid parameters. For a complete list of parameters available in this utility, see the dsgrid_params man page.
<h2>Access</h2>To use DSGETR, load the NCAR Graphics library ngmath.
<h2>See Also</h2>dsgrid, dsgrid_params, dsgrid2s, dsgrid3s, dsgrid2d, dsgrid3d, dspnt2s, dspnt2d, dspnt3s, dspnt3d dssetr. 

 Complete documentation for Dsgrid is available at URL 
 <a rel="nofollow" HREF="http://ngwww.ucar.edu/ngdoc/ng/ngmath/dsgrid/dshome.html">http://ngwww.ucar.edu/ngdoc/ng/ngmath/dsgrid/dshome.html</a>
<h2>Copyright</h2>Copyright (C) 2000 
 University Corporation for Atmospheric Research 
 

 The use of this Software is governed by a License Agreement.
