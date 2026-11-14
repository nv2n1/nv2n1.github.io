---
title: "ncl_dsgrid_params(3)"
name: "ncl_dsgrid_params"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_dsgrid_params/"
---

dsgrid_params - This document briefly describes all the internal parameters of Dsgrid. 

<h2>Description</h2>Each entry below includes the name of a parameter, its Fortran type (use the obvious equivalents for C), its default value, and a short description of the parameter.
<dl COMPACT><dt>'DMV' - Real - any
<dd>A special value for data initialization and use with the dmx control parameter.
<dt>'DMX' - Real - &gt; 0.
<dd>Used in calculating weights - use only input data the distance dmx.
<dt>'ERF' - Character - stderr
<dd>Error file.
<dt>'EXP' - Real - &gt; 0.
<dd>Power to use for inverse distances in computing weights.
<dt>'SHD' - Integer - 0
<dd>Flag for controlling whether the shadowing feature is on (0 = no; 1 = yes).</dl><h2>See Also</h2>dsgrid, dsgrid_params, dsgrid_errors, dsgrid2s, dsgrid3s, dsseti, dsgeti, dssetr dsgetr, dssetc, dsgetc, dspnt2s, dspnt3s, dsgrid2d, dsgrid3d, dssetrd dsgetrd, dspnt2d, dspnt3d, c_dsgrid2s, c_dsgrid3s, c_dsseti, c_dsgeti c_dssetr, c_dsgetr, c_dssetc, c_dsgetc, c_dspnt2s, c_dspnt3s, c_dsgrid2d c_dsgrid3d, c_dssetrd, c_dsgetrd, c_dspnt2d, c_dspnt3d. 

 Complete documentation for Dsgrid is available at URL 
 <a rel="nofollow" HREF="http://ngwww.ucar.edu/ngdoc/ng/ngmath/dsgrid/dshome.html">http://ngwww.ucar.edu/ngdoc/ng/ngmath/dsgrid/dshome.html</a>
<h2>Copyright</h2>Copyright (C) 2000 
 University Corporation for Atmospheric Research 
 

 The use of this Software is governed by a License Agreement.
