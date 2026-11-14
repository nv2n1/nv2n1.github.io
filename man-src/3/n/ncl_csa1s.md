---
title: "ncl_csa1s(3)"
name: "ncl_csa1s"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_csa1s/"
---

CSA1S - cubic spline approximation, simple entry for one-dimensional input
<h2>Synopsis</h2>CALL CSA1S (NI, XI, YI, KNOTS, NO, XO, YO, NWRK, WORK, IER)
<h2>Description</h2><dl COMPACT><dt>NI
<dd>(integer,input) The number of input data points. It must be that NI .gt. 3 and, depending on the size of KNOTS below, NI may have to be larger.
<dt>XI
<dd>(real, input) An array dimensioned for NI containing the X coordinates of the input data points.
<dt>YI
<dd>(real, input) An array dimensioned for NI containing function values at the input XI values, that is, YI(L) is the value of the input function at XI(L) for L=1,NI.
<dt>KNOTS
<dd>(integer, input) The number of knots to be used in constructing the approximation spline. KNOTS must be at least 4. The larger the value for KNOTS, the closer the approximated curve will come to passing through the input function values.
<dt>NO
<dd>(integer, input) The number of values to be calculated for the output curve.
<dt>XO
<dd>(real, input) An array dimensioned for NO containing the X coordinates of the output curve.
<dt>YO
<dd>(real, output) An array dimensioned for NO containing the calculated function values for the output curve.
<dt>NWRK
<dd>(integer, input) The size of the WORK array. NWRK must be at least KNOTS*(KNOTS+3).
<dt>WORK
<dd>(real, input) A work array dimensioned for NWRK.
<dt>IER
<dd>(integer, output) An error return value. If IER is returned as 0, then no errors were detected. If IER is non-zero, then refer to the man page for csagrid_errors for details.</dl><h2>Usage</h2>CSA1S is called to find an approximating cubic spline for one-dimensional input data. If you want to weight the input data values, calculate derivatives, or handle data sparse areas specially, then you will need to use CSA1XS.
<h2>Access</h2>To use CSA1S, load the NCAR Graphics library ngmath.
<h2>See Also</h2>csagrid, csa1xs, csa1ls, csa1lxs 

 Complete documentation for Csagrid is available at URL 
 <a rel="nofollow" HREF="http://ngwww.ucar.edu/ngdoc/ng/ngmath/csagrid/csahome.html">http://ngwww.ucar.edu/ngdoc/ng/ngmath/csagrid/csahome.html</a>
<h2>Copyright</h2>Copyright (C) 2000 
 University Corporation for Atmospheric Research 
 

 The use of this Software is governed by a License Agreement.
