---
title: "ncl_csa3lxs(3)"
name: "ncl_csa3lxs"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_csa3lxs/"
---

CSA3LXS - cubic spline approximation, expanded entry for three-dimensional input, list output
<h2>Synopsis</h2>CALL CSA3LXS (NI, XI, UI, WTS, KNOTS, SMTH, NDERIV, 
 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>NO, XO, YO, ZO, UO, NWRK, WORK, IER)
<h2>Description</h2><dl COMPACT><dt>NI
<dd>(integer,input) The number of input data points. It must be that NI .gt. 3 and, depending on the size of KNOTS below, NI may have to be larger.
<dt>XI
<dd>(real, input) An array containing the X - Y - Z coordinates of the input data points. XI is dimensioned for 3 x NI. XI(1,L) is the X coordinate, XI(2,L) is the Y coordinate, and XI(2,L) is the Z coordinate for the input domain for L=1,NI.
<dt>UI
<dd>(real, input) An array dimensioned for NI containing function values at the input XI values, that is, UI(L) is the value of the input function at XI(L) for L=1,NI.
<dt>WTS
<dd>(real, input) An array dimensioned for NI containing weights for the UI values at the input XI values, that is, WTS(L) is a weight for the value of UI(L) for L=1,NI. If you do not desire to weight the input UI values, then set <a HREF="/docs/linux/man/1-wts/">WTS</a>(1) to -1. The weights in the WTS array are relative and may be set to any non-negative value. When CSA3LXS is called, the weights are summed and the individual weights are normalized so that the weight sum is unity.
<dt>KNOTS
<dd>(integer, input) The number of knots to be used in constructing the approximation spline. KNOTS is dimensioned for 3 and provides the number of knots to be used in the X, Y, and Z directions. KNOTS(I) must be at least 4 for I=1,3. The larger the values for KNOTS, the closer the approximated curve will come to passing through the input function values.
<dt>SMTH
<dd>(real, input) A parameter that controls extrapolation into data sparse regions. If SMTH is zero, then nothing special is done in data sparse regions. A good first choice for SMTH is 1.
<dt>NDERIV
<dd>(integer, input) An array dimensioned for 3 that specifies, for each coordinate, whether you want functional values (=0), first derivative values (=1), or second derivative values (=2).
<dt>NO
<dd>(integer, input) The number of coordinate values in the output list. NO can be any positive number.
<dt>XO
<dd>(real, input) An array dimensioned for NO containing the X coordinates of the output list.
<dt>YO
<dd>(real, input) An array dimensioned for NO containing the Y coordinates of the output list.
<dt>ZO
<dd>(real, input) An array dimensioned for NO containing the Z coordinates of the output list.
<dt>UO
<dd>(real, output) An array dimensioned for NO containing the calculated function values for the output spline. UO(I) is the calculated functional value at (XO(I),YO(I),ZO(I)) for I=1,NO.
<dt>NWRK
<dd>(integer, input) The size of the WORK array. NWRK must be at least NK * (NK+3) where NK = <a HREF="/docs/linux/man/1-knots/">KNOTS</a>(1) * <a HREF="/docs/linux/man/2-knots/">KNOTS</a>(2) * <a HREF="/docs/linux/man/3-knots/">KNOTS</a>(3).
<dt>WORK
<dd>(real, input) A work array dimensioned for NWRK.
<dt>IER
<dd>(integer, output) An error return value. If IER is returned as 0, then no errors were detected. If IER is non-zero, then refer to the man page for csagrid_errors for details.</dl><h2>Usage</h2>CSA3LXS is called if you want to weight the input data values, calculate derivatives, or handle data sparse areas specially. If you do not want to do any of these three things, then use CSA3LS.
<h2>Access</h2>To use CSA3LXS, load the NCAR Graphics library ngmath.
<h2>See Also</h2>csagrid, csa3s, csa3xs, csa3ls 

 Complete documentation for Csagrid is available at URL 
 <a rel="nofollow" HREF="http://ngwww.ucar.edu/ngdoc/ng/ngmath/csagrid/csahome.html">http://ngwww.ucar.edu/ngdoc/ng/ngmath/csagrid/csahome.html</a>
<h2>Copyright</h2>Copyright (C) 2000 
 University Corporation for Atmospheric Research 
 

 The use of this Software is governed by a License Agreement.
