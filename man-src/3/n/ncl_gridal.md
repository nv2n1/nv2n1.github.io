---
title: "ncl_gridal(3)"
name: "ncl_gridal"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_gridal/"
---

GRIDAL - Draws any of the supported types of backgrounds. Each of the other background-drawing routines is implemented by a call to GRIDAL. 

<h2>Utility</h2>This routine is part of the Gridall utility in NCAR Graphics. To see the overview man page for this utility, type &quot;man gridall&quot;.
<h2>Synopsis</h2>&nbsp;<wbr>CALL GRIDAL&nbsp;<wbr>(MJRX, MNRX, MJRY, MNRY, IXLB, IYLB, IGPH,&nbsp;<wbr> 
 + XINT, YINT)
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/ncargC.h&gt; 

 void c_gridal (int mjrx, int mnrx, int mjry, int mnry, 
 int ixlb, int iylb, int igph, float xint, float yint)
<h2>Description</h2><dl COMPACT><dt>MJRX, MNRX, MJRY, and MNRY
<dd>(input expressions of type INTEGER) specify the major and minor divisions of the horizontal (X) and vertical (Y) axes of the current viewport. The meanings of these parameters depend on the current setting of the internal parameter 'LS' of SPPS:
<dl COMPACT><dd><dl COMPACT><dt>&bull;
<dd>If the value of 'LS' implies that the axis is linear: MJRX(Y) specifies the number of major divisions of the X(Y) axis and MNRX(Y) specifies the number of minor divisions within each major division. In each case, the value specifies the number of spaces between grid lines or ticks rather than the number of lines or ticks. Including the ones at the ends of the axes, there is always one more major division line or mark than the number of major divisions specified by MJRX(Y). Similarly, there is always one less minor division line or tick per major division than the number of minor divisions per major division specified by MNRX(Y).
<dt>&bull;
<dd>If the value of 'LS' implies that the axis is logarithmic: Each major division point occurs at a value 10**MJRX(Y) times the previous point. For example, if the minimum X-axis value were 3., the maximum X-axis value 3000. and MJRX 1, then the major division points would be 3., 30., 300., and 3000. If MNRX(Y).LE.10, there are nine minor divisions within each major division. For example, between 3. and 30., there would be minor division points at 6., 9., 12., . . . 27. If MNRX(Y).GT.10., minor divisions are omitted.</dl></dl><dt>IXLB
<dd>(an input expression of type INTEGER) is defined as follows:
<dl COMPACT><dd><dl COMPACT><dt>&bull;
<dd>IXLB = -1 implies that no X axis is to be drawn.
<dt>&bull;
<dd>IXLB = 0 implies that the X axis is to be drawn unlabeled.
<dt>&bull;
<dd>IXLB = 1 implies that the X axis is to be drawn and labeled.</dl></dl><dt>IYLB
<dd>(an input expression of type INTEGER) is defined as follows:
<dl COMPACT><dd><dl COMPACT><dt>&bull;
<dd>IYLB = -1 implies that no Y axis is to be drawn.
<dt>&bull;
<dd>IYLB = 0 implies that the Y axis is to be drawn unlabeled.
<dt>&bull;
<dd>IYLB = 1 implies that the Y axis is to be drawn and labeled.</dl></dl><dt>IGPH
<dd>(an input expression of type INTEGER) specifies the background type, as follows: 

 <table> <tr VALIGN=top><td>IGPH</td><td>X axis</td><td>Y axis
</td></tr><tr VALIGN=top><td>----</td><td>------</td><td>------
</td></tr><tr VALIGN=top><td>0</td><td>grid</td><td>grid
</td></tr><tr VALIGN=top><td>1</td><td>grid</td><td>perim
</td></tr><tr VALIGN=top><td>2</td><td>grid</td><td>halfax
</td></tr><tr VALIGN=top><td>4</td><td>perim</td><td>grid
</td></tr><tr VALIGN=top><td>5</td><td>perim</td><td>perim
</td></tr><tr VALIGN=top><td>6</td><td>perim</td><td>halfax
</td></tr><tr VALIGN=top><td>8</td><td>halfax</td><td>grid
</td></tr><tr VALIGN=top><td>9</td><td>halfax</td><td>perim
</td></tr><tr VALIGN=top><td>10</td><td>halfax</td><td>halfax
</td></tr> </table><dt>XINT and YINT
<dd>(input expressions of type REAL), if IGPH has the value 10, are the user coordinates of the point of intersection of the two axes. For other values of IGPH for which one of the axes is of type HALFAX, XINT and/or YINT specify the position of that axis.</dl><h2>C-Binding Description</h2>The C-binding argument descriptions are the same as the FORTRAN argument descriptions.
<h2>Examples</h2>Use the ncargex command to see the following relevant examples: tgrida, ccpga, ccpmpxy.
<h2>Access</h2>To use GRIDAL or c_gridal, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.
<h2>Messages</h2>See the gridall man page for a description of all Gridall error messages and/or informational messages.
<h2>See Also</h2>Online: gridall, gridall_params, gacolr, gagetc, gageti, gagetr, gasetc, gaseti, gasetr, grid, gridl, halfax, labmod, perim, periml, tick4, ticks, ncarg_cbind. 

 Hardcopy: NCAR Graphics Contouring and Mapping Tutorial 

 Hardcopy: NCAR Graphics Fundamentals, UNIX Version
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
