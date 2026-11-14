---
title: "ncl_c_dssetrd(3)"
name: "ncl_c_dssetrd"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_c_dssetrd/"
---

c_dssetrd - Set double valued parameters
<h2>Function Prototype</h2>void c_dssetrd(char *, double);
<h2>Synopsis</h2>void c_dssetrd(pnam, dval);
<h2>Description</h2><dl COMPACT><dt>pnam
<dd>A string that specifies the name of the parameter to be set.
<dt>dval
<dd>A double value to be assigned to the internal parameter specified by pnam.</dl><h2>Usage</h2>This routine allows you to set the current value of Dsgrid parameters. For a complete list of parameters available in this utility, see the dsgrid_params man page.
<h2>Access</h2>To use c_dssetrd, load the NCAR Graphics library ngmath.
<h2>See Also</h2>c_dsgrid, c_dsgrid_params, c_dsgrid2s, c_dsgrid3s, c_dsgrid2d, c_dsgrid3d, c_dspnt2s, c_dspnt2d, c_dspnt3s, c_dspnt3d, c_dsgetrd 

 Complete documentation for Dsgrid is available at URL 
 <a rel="nofollow" HREF="http://ngwww.ucar.edu/ngdoc/ng/ngmath/dsgrid/dshome.html">http://ngwww.ucar.edu/ngdoc/ng/ngmath/dsgrid/dshome.html</a>
<h2>Copyright</h2>Copyright (C) 2000 
 University Corporation for Atmospheric Research 
 

 The use of this Software is governed by a License Agreement.
