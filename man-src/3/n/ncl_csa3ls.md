---
title: "ncl_csa3ls(3)"
name: "ncl_csa3ls"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_csa3ls/"
---

CSA3LS - cubic spline approximation, simple entry for three-dimensional input, list output
<h2>Synopsis</h2>CALL CSA3LS (NI, XI, UI, KNOTS, NO, XO, YO, ZO, UO, 
 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>NWRK, WORK, IER)
<h2>Description</h2><dl COMPACT><dt>NI
<dd>(integer,input) The number of input data points. It must be that NI .gt. 3 and, depending on the size of KNOTS below, NI may have to be larger.
<dt>XI
<dd>(real, input) An array containing the X - Y - Z coordinates of the input data points. XI is dimensioned for 3 x NI. XI(1,L) is the X coordinate, XI(2,L) is the Y coordinate, and XI(3,L) is the Z coordinate for the input domain for L=1,NI.
<dt>UI
<dd>(real, input) An array dimensioned for NI containing function values at the input XI values, that is, UI(L) is the value of the input function at XI(L) for L=1,NI.
<dt>KNOTS
<dd>(integer, input) An array dimensioned for 3 containing the number of knots to be used in each coordinate direction for constructing the approximation spline. KNOTS(I) must be at least 4 for I=1,3. The larger the value for KNOTS, the closer the approximated curve will come to passing through the input function values.
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
<dd>(integer, output) An error return value. If IER is returned as 0, then no errors were detected. If IER is non-zero, then refer to the man page for csagrid_errors for details.</dl><h2>Usage</h2>CSA3LS is called to find an approximating cubic spline for three-dimensional input data. If you want to weight the input data values, calculate derivatives, or handle data sparse areas specially, then you will need to use CSA3LXS.
<h2>Access</h2>To use CSA3LS, load the NCAR Graphics library ngmath.
<h2>See Also</h2>csagrid, csa3s, csa3xs, csa3lxs 

 Complete documentation for Csagrid is available at URL 
 <a rel="nofollow" HREF="http://ngwww.ucar.edu/ngdoc/ng/ngmath/csagrid/csahome.html">http://ngwww.ucar.edu/ngdoc/ng/ngmath/csagrid/csahome.html</a>
<h2>Copyright</h2>Copyright (C) 2000 
 University Corporation for Atmospheric Research 
 

 The use of this Software is governed by a License Agreement.
