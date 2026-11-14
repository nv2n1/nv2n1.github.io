---
title: "ncl_c_nnsetc(3)"
name: "ncl_c_nnsetc"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_c_nnsetc/"
---

c_nnsetc - Set char valued parameters
<h2>Function Prototype</h2>void c_nnsetc(char *, char *);
<h2>Synopsis</h2>void c_nnsetc (pnam, cval);
<h2>Description</h2><dl COMPACT><dt>pnam
<dd>A string that specifies the name of the parameter to be set.
<dt>cval
<dd>A string that specifies the value to be assigned to the internal parameter specified by pnam.</dl><h2>Usage</h2>This routine allows you to set the current value of Natgrid parameters. For a complete list of parameters available in this utility, see the natgrid_params man page.
<h2>Access</h2>To use c_nnsetc, load the NCAR Graphics library ngmath.
<h2>See Also</h2>natgrid, natgrid_params, c_natgrids, c_nngetc. 

 Complete documentation for Natgrid is available at URL 
 <a rel="nofollow" HREF="http://ngwww.ucar.edu/ngdoc/ng/ngmath/natgrid/nnhome.html">http://ngwww.ucar.edu/ngdoc/ng/ngmath/natgrid/nnhome.html</a>
<h2>Copyright</h2>Copyright (C) 2000 
 University Corporation for Atmospheric Research 
 

 The use of this Software is governed by a License Agreement.
