---
title: "ncl_csa2ls(3)"
name: "ncl_csa2ls"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_csa2ls/"
---

CSA2LS - cubic spline approximation, simple entry for two-dimensional input, list output
<h2>Synopsis</h2>CALL CSA2LS (NI, XI, UI, KNOTS, NO, XO, YO, UO, NWRK, 
 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>WORK, IER)
<h2>Description</h2><dl COMPACT><dt>NI
</dt><dd>(integer,input) The number of input data points. It must be that NI .gt. 3 and, depending on the size of KNOTS below, NI may have to be larger.
</dd><dt>XI
</dt><dd>(real, input) An array containing the X - Y coordinates of the input data points. XI is dimensioned for 2 x NI. XI(1,L) is the X coordinate and XI(2,L) is the Y coordinate for the input domain for L=1,NI.
</dd><dt>UI
</dt><dd>(real, input) An array dimensioned for NI containing function values at the input XI values, that is UI(L) is the value of the input function at the coordinate (XI(1,L),XI(2,L)) for L=1,NI.
</dd><dt>KNOTS
</dt><dd>(integer, input) The number of knots to be used in constructing the approximation spline. KNOTS is dimensioned for 2 and provides the number of knots to be used in the X and the Y directions. Both KNOTS(1) and KNOTS(2) must be at least 4. The larger the values for KNOTS, the closer the approximated curve will come to passing through the input function values.
</dd><dt>NO
</dt><dd>(integer, input) The number of coordinate values in the output list. NO can be any positive number.
</dd><dt>XO
</dt><dd>(real, input) An array dimensioned for NO containing the X coordinates of the output list.
</dd><dt>YO
</dt><dd>(real, input) An array dimensioned for NO containing the Y coordinates of the output list.
</dd><dt>UO
</dt><dd>(real, output) An array dimensioned for NO containing the calculated function values for the output spline. UO(I) is the calculated functional value at (XO(I),YO(I)) for I=1,NO.
</dd><dt>NWRK
</dt><dd>(integer, input) The size of the WORK array. NWRK must be at least KNOTS(1)*KNOTS(2)*(KNOTS(1)*KNOTS(2)+3).
</dd><dt>WORK
</dt><dd>(real, input) A work array dimensioned for NWRK.
</dd><dt>IER
</dt><dd>(integer, output) An error return value. If IER is returned as 0, then no errors were detected. If IER is non-zero, then refer to the man page for csagrid_errors for details.</dd></dl><h2>Usage</h2>CSA2LS is called to find an approximating cubic spline surface for two-dimensional input data with output values calculated at a list of user-specified points. If you want to weight the input data values, calculate derivatives, or handle data sparse areas specially, then you will need to use CSA2LXS.
<h2>Access</h2>To use CSA2LS, load the NCAR Graphics library ngmath.
<h2>See Also</h2>csagrid, csa2s, csa2xs, csa2ls, 

 Complete documentation for Csagrid is available at URL 
 <a rel="nofollow" HREF="http://ngwww.ucar.edu/ngdoc/ng/ngmath/csagrid/csahome.html">http://ngwww.ucar.edu/ngdoc/ng/ngmath/csagrid/csahome.html</a>
<h2>Copyright</h2>Copyright (C) 2000 
 University Corporation for Atmospheric Research 
 

 The use of this Software is governed by a License Agreement.
