---
title: "ncl_gridl(3)"
name: "ncl_gridl"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_gridl/"
---

GRIDL - Draws a labeled grid with each major division labeled with its numeric value. 

<h2>Synopsis</h2>CALL GRIDL (MJRX,MNRX,MJRY,MNRY)
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/ncargC.h&gt; 

 void c_gridl (int mjrx, int mnrx, int mjry, int mnry)
<h2>Description</h2><dl COMPACT><dt>MJRX, MNRX, MJRY, and MNRY
<dd>(input expressions of type INTEGER) specify the major and minor divisions of the horizontal (X) and vertical (Y) axes of the current viewport. The meanings of these parameters depend on the current setting of the internal parameter 'LS' of SPPS:
<dl COMPACT><dd><dl COMPACT><dt>&bull;
<dd>If the value of 'LS' implies that the axis is linear: MJRX(Y) specifies the number of major divisions of the X(Y) axis and MNRX(Y) specifies the number of minor divisions within each major division. In each case, the value specifies the number of spaces between grid lines or ticks rather than the number of lines or ticks. Including the ones at the ends of the axes, there is always one more major division line or mark than the number of major divisions specified by MJRX(Y). Similarly, there is always one less minor division line or tick per major division than the number of minor divisions per major division specified by MNRX(Y).
<dt>&bull;
<dd>If the value of 'LS' implies that the axis is logarithmic: Each major division point occurs at a value 10**MJRX(Y) times the previous point. For example, if the minimum X-axis value were 3., the maximum X-axis value 3000. and MJRX 1, then the major division points would be 3., 30., 300., and 3000. If MNRX(Y).LE.10, there are nine minor divisions within each major division. For example, between 3. and 30., there would be minor division points at 6., 9., 12., . . . 27. If MNRX(Y).GT.10., minor divisions are omitted.</dl></dl>
</dl><h2>C-Binding Description</h2>The C-binding argument descriptions are the same as the FORTRAN argument descriptions.
<h2>Usage</h2>The statement
<dl COMPACT><dd>CALL GRIDL (MJRX,MNRX,MJRY,MNRY) 

</dl>
 is equivalent to
<dl COMPACT><dd>CALL GRIDAL (MJRX,MNRX,MJRY,MNRY,1,1,0,0.,0.)</dl><h2>Examples</h2>Use the ncargex command to see the following relevant example: tgrida.
<h2>Access</h2>To use GRIDL or c_gridl, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.
<h2>See Also</h2>Online: gridall, gacolr, gagetc, gageti, gagetr, gasetc, gaseti, gasetr, grid, gridal, halfax, labmod, perim, periml, tick4, ticks, ncarg_cbind. 

 Hardcopy: NCAR Graphics Fundamentals, UNIX Version
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
