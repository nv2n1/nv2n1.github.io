---
title: "ncl_csa1xs(3)"
name: "ncl_csa1xs"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_csa1xs/"
---

CSA1XS - cubic spline approximation, expanded entry for one-dimensional input
<h2>Synopsis</h2>CALL CSA1XS (NI, XI, YI, WTS, KNOTS, SMTH, DERIV, NO, XO, YO, NWRK, WORK, IER)
<h2>Description</h2><dl COMPACT><dt>NI
<dd>(integer,input) The number of input data points. It must be that NI &gt; 3 and, depending on the size of KNOTS below, NI may have to be larger.
<dt>XI
<dd>(real, input) An array dimensioned for NI containing the X coordinates of the input data points.
<dt>YI
<dd>(real, input) An array dimensioned for NI containing function values at the input XI values, that is, YI(L) is the value of the input function at XI(L) for L=1,NI.
<dt>WTS
<dd>(real, input) An array dimensioned for NI containing weights for the YI values at the input XI values, that is, WTS(L) is a weight for the value of YI(L) for L=1,NI. If you do not desire to weight the input YI values, then set <a HREF="/docs/linux/man/1-wts/">WTS</a>(1) to -1. The weights in the WTS array are relative and may be set to any non-negative value. When CSA1XS is called, the weights are summed and the individual weights are normalized so that the weight sum is unity.
<dt>KNOTS
<dd>(integer, input) The number of knots to be used in constructing the approximation spline. KNOTS must be at least 4. The larger the value for KNOTS, the closer the approximated curve will come to passing through the input function values.
<dt>SMTH
<dd>(real, input) A parameter that controls extrapolation into data sparse regions. If SMTH is zero, then nothing special is done in data sparse regions. A good first choice for SMTH is 1.
<dt>NDERIV
<dd>(integer, input) Specifies whether you want functional values (NDERIV=0), first derivative values (NDERIV=1), or second derivative values (NDERIV=2).
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
<dd>(integer, output) An error return value. If IER is returned as 0, then no errors were detected. If IER is non-zero, then refer to the man page for csagrid_errors for details.</dl><h2>Usage</h2>CSA1XS is called to find an approximating cubic spline for one-dimensional input data. CSA1XS is called if you want to weight the input data values, calculate derivatives, or handle data sparse areas specially. If you do not want to do any of these three things, then use CSA1S.
<h2>Access</h2>To use CSA1XS, load the NCAR Graphics library ngmath.
<h2>See Also</h2>csagrid, csa1s, csa1ls, csa1lxs 

 Complete documentation for Csagrid is available at URL 
 <a rel="nofollow" HREF="http://ngwww.ucar.edu/ngdoc/ng/ngmath/csagrid/csahome.html">http://ngwww.ucar.edu/ngdoc/ng/ngmath/csagrid/csahome.html</a>
<h2>Copyright</h2>Copyright (C) 2000 
 University Corporation for Atmospheric Research 
 

 The use of this Software is governed by a License Agreement.
