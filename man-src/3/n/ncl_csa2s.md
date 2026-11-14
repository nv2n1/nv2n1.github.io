---
title: "ncl_csa2s(3)"
name: "ncl_csa2s"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_csa2s/"
---

CSA2S - cubic spline approximation, simple entry for two-dimensional input, gridded output
<h2>Synopsis</h2>CALL CSA2S (NI, XI, UI, KNOTS, NXO, ,NYO, XO, YO, UO, NWRK, WORK, IER)
<h2>Description</h2><dl COMPACT><dt>NI
<dd>(integer,input) The number of input data points. It must be that NI .gt. 3 and, depending on the size of KNOTS below, NI may have to be larger.
<dt>XI
<dd>(real, input) An array containing the X - Y coordinates of the input data points. XI is dimensioned for 2 x NI. XI(1,L) is the X coordinate and XI(2,L) is the Y coordinate for the input domain for L=1,NI.
<dt>UI
<dd>(real, input) An array dimensioned for NI containing function values at the input XI values, that is UI(L) is the value of the input function at the coordinate (XI(1,L),XI(2,L)) for L=1,NI.
<dt>KNOTS
<dd>(integer, input) The number of knots to be used in constructing the approximation spline. KNOTS is dimensioned for 2 and provides the number of knots to be used in the X and the Y directions. Both <a HREF="/docs/linux/man/1-knots/">KNOTS</a>(1) and <a HREF="/docs/linux/man/2-knots/">KNOTS</a>(2) must be at least 4. The larger the values for KNOTS, the closer the approximated curve will come to passing through the input function values.
<dt>NXO
<dd>(integer, input) The number of X coordinate values in the output grid.
<dt>NYO
<dd>(integer, input) The number of Y coordinate values in the output grid.
<dt>XO
<dd>(real, input) An array dimensioned for NXO containing the X coordinates of the output surface.
<dt>YO
<dd>(real, input) An array dimensioned for NYO containing the Y coordinates of the output surface.
<dt>UO
<dd>(real, output) An array dimensioned for NXO x NYO containing the calculated function values for the output surface. UO(I,J) is the calculated functional value at (XO(I),YO(J)) for I=1,NXO and J=1,NYO.
<dt>NWRK
<dd>(integer, input) The size of the WORK array. NWRK must be at least <a HREF="/docs/linux/man/1-knots/">KNOTS</a>(1)*<a HREF="/docs/linux/man/2-knots/">KNOTS</a>(2)*(<a HREF="/docs/linux/man/1-knots/">KNOTS</a>(1)*<a HREF="/docs/linux/man/2-knots/">KNOTS</a>(2)+3).
<dt>WORK
<dd>(real, input) A work array dimensioned for NWRK.
<dt>IER
<dd>(integer, output) An error return value. If IER is returned as 0, then no errors were detected. If IER is non-zero, then refer to the man page for csagrid_errors for details.</dl><h2>Usage</h2>CSA2S is called to find an approximating cubic spline surface for two-dimensional input data. If you want to weight the input data values, calculate derivatives, or handle data sparse areas specially, then you will need to use CSA2XS.
<h2>Access</h2>To use CSA2S, load the NCAR Graphics library ngmath.
<h2>See Also</h2>csagrid, csa2xs, csa2ls, csa2lxs 

 Complete documentation for Csagrid is available at URL 
 <a rel="nofollow" HREF="http://ngwww.ucar.edu/ngdoc/ng/ngmath/csagrid/csahome.html">http://ngwww.ucar.edu/ngdoc/ng/ngmath/csagrid/csahome.html</a>
<h2>Copyright</h2>Copyright (C) 2000 
 University Corporation for Atmospheric Research 
 

 The use of this Software is governed by a License Agreement.
