---
title: "ncl_nnpntendd(3)"
name: "ncl_nnpntendd"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_nnpntendd/"
---

NNPNTENDD - terminate interpolation in single point mode

<h2>Synopsis</h2>

CALL NNPNTENDD ()

<h2>Usage</h2>

This subroutine terminates single point mode. It should be called after entering single point mode using NNPNTINITD and interpolating at individual points with NNPNTD.

<h2>Access</h2>

To use NNPNTENDD, load the NCAR Graphics library ngmath.

<h2>See Also</h2>

natgrid_params, natgridd, nnpntinitd, nnpntd. 

 Complete documentation for Natgrid is available at URL 
 <a rel="nofollow" HREF="http://ngwww.ucar.edu/ngdoc/ng/ngmath/natgrid/nnhome.html">http://ngwww.ucar.edu/ngdoc/ng/ngmath/natgrid/nnhome.html</a>

<h2>Copyright</h2>

Copyright (C) 2000 
 University Corporation for Atmospheric Research 
 

 The use of this Software is governed by a License Agreement.
