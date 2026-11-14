---
title: "ncl_dssetc(3)"
name: "ncl_dssetc"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_dssetc/"
---

DSSETC - Sets the value of an internal parameter of type CHARACTER. 

<h2>Synopsis</h2>CALL DSSETC (PNAM, CVAL);
<h2>Description</h2><dl COMPACT><dt>PNAM
<dd>A character string that specifies the name of the parameter to be set. The name must appear as the first three characters of the string.
<dt>CVAL
<dd>A character string that is the value to be assigned to the internal parameter specified by pnam.</dl><h2>Usage</h2>This function allows you to set the current value of Dsgrid parameters. For a complete list of parameters available in this utility, see the dsgrid_params man page.
<h2>Access</h2>To use DSSETC, load the NCAR Graphics library ngmath.
<h2>See Also</h2>dsgrid, dsgrid_params, dsgrid2s, dsgrid3s, dsgrid2d, dsgrid3d, dspnt2s, dspnt2d, dspnt3s, dspnt3d dsgetc. 

 Complete documentation for Dsgrid is available at URL 
 <a rel="nofollow" HREF="http://ngwww.ucar.edu/ngdoc/ng/ngmath/dsgrid/dshome.html">http://ngwww.ucar.edu/ngdoc/ng/ngmath/dsgrid/dshome.html</a>
<h2>Copyright</h2>Copyright (C) 2000 
 University Corporation for Atmospheric Research 
 

 The use of this Software is governed by a License Agreement.
