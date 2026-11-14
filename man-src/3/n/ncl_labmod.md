---
title: "ncl_labmod(3)"
name: "ncl_labmod"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_labmod/"
---

LABMOD - Presets parameters controlling the appearance of labels drawn by GRIDAL, GRIDL,... et al. LABMOD itself does no plotting and, in order to have any effect, must be called prior to the background-drawing routines for which it is presetting parameters. 

<h2>Synopsis</h2>&nbsp;<wbr>CALL LABMOD&nbsp;<wbr>(FMTX, FMTY, NUMX, NUMY, ISZX, ISZY, IXDC,&nbsp;<wbr> 
 + IYDC, IXOR)
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/ncargC.h&gt; 

 void c_labmod (char *fmtx, char *fmty, int numx, int numy, 
 int iszx, int iszy, int ixdc, int iydc, int ixor)
<h2>Description</h2><dl COMPACT><dt>FMTX and FMTY
<dd>(input expressions of type CHARACTER) contain format specifications for the X-axis and Y-axis numerical labels produced by GRIDAL, GRIDL, HALFAX, or PERIML. The specification must begin with a left parenthesis and end with a right parenthesis and must not be more than ten characters long. Conversions of types E, F, G, and I are allowed; for example, one might use FMTX='(F8.2)' and FMTY='(E10.0)'. The default for both formats is '(E10.3)'. 

 NOTE: I formats are allowed by this version of Gridall; they were not allowed by previous versions.
<dt>NUMX
<dd>(an input expression of type INTEGER), if non-zero, is the number of characters in each X-axis numeric label; if LBLX is a string produced by the format FMTX, then the label will be the substring LBLX(1:NUMX). If NUMX is 0, then the label will be the substring LBLX(m:n), where LBLX(m:m) is the first non-blank character in LBLX, and LBLX(n:n) is the last non-blank character following LBLX(m:m). Using a non-zero NUMX causes the labels to be centered differently than if a zero value is used. The default value for NUMX is 0.
<dt>NUMY
<dd>(an input expression of type INTEGER) is defined just like NUMX, but applies to Y-axis numeric labels.
<dt>ISZX and ISZY
<dd>(input expressions of type INTEGER) are character sizes for the labels, specified in plotter address units, just as for the SPPS routines PWRIT and WTSTR. The default value for both is 10.
<dt>IXDC
<dd>(an input expression of type INTEGER) is the decrement, in plotter address units (PAUs - by default, the plotter frame is 1023 PAUs in width and height), from the left edge of the current viewport to the nearest X address of the label specified by FMTY, NUMY, and ISZY. For example, if the horizontal extent of the current viewport is defined by the normalized device coordinates .1 and .9, and if IXDC is 60, and if there has been no call to the SPPS routine SETI (which can change the size of a PAU), then labels on the Y axis will end at plotter coordinate 43 (.1*1023+1-60). Negative values may be used to put labels on the other side of the viewport; in the example given, changing IXDC to -878 (-.8*1023 -60) would put the labels on the right side of the viewport, with their left edges 60 plotter-coordinate units away from the edge of the viewport. There are two special values of IXDC:
<dl COMPACT><dd><dl COMPACT><dt>&bull;
<dd>If IXDC=0, the Y-axis labels will end 20 plotter address units to the left of the viewport (equivalent to using IXDC=20).
<dt>&bull;
<dd>If IXDC=1, Y-axis labels will begin 20 plotter address units to the right of the viewport (equivalent to using IXDC=-20-w, where w is the width of the viewport, in plotter address units).</dl></dl><dd>The default value of IXDC is 20. 

 When HALFAX is called or when GRIDAL is called with IGPH = 2, 6, or 10, IXDC is the distance from the Y axis, rather than from the minimum viewport coordinate, and the special values 0 and 1 are equivalent to 20 and -20.
<dt>IYDC
<dd>(an input expression of type INTEGER) is the decrement, in plotter address units (PAUs - by default, the plotter frame is 1023 PAUs in width and height), from the bottom edge of the current viewport to the nearest Y address of the label specified by FMTX, NUMX, and ISZX. Note that negative values may be used to put labels above the viewport. There are two special values of IYDC:
<dl COMPACT><dd><dl COMPACT><dt>&bull;
<dd>If IYDC=0, the top of the X-axis labels will be 20 plotter address units below the bottom edge of the viewport (equivalent to using IYDC=20).
<dt>&bull;
<dd>If IYDC=1, the bottom of the X-axis labels will be 20 plotter address units above the top edge of the viewport (equivalent to using IYDC=-20-h, where h is the height of the viewport, in plotter address units).</dl></dl><dd>The default value of IYDC is 20. 

 When HALFAX is called or when GRIDAL is called with IGPH = 8, 9, or 10, IYDC is the distance from the X axis, rather than from the minimum viewport coordinate, and the special values 0 and 1 are equivalent to 20 and -20.
<dt>IXOR
<dd>(an input expression of type INTEGER) specifies the orientation of the X-axis labels:
<dl COMPACT><dd><dl COMPACT><dt>&bull;
<dd>IXOR = 0 implies the use of horizontal labels.
<dt>&bull;
<dd>IXOR = 1 implies the use of vertical labels.</dl></dl><dd>The default orientation is horizontal.</dl><h2>C-Binding Description</h2>The C-binding argument descriptions are the same as the FORTRAN argument descriptions.
<h2>Usage</h2>This routine allows you to set the current value of Gridall parameters. For a complete list of parameters available in this utility, see the gridall_params man page.
<h2>Examples</h2>Use the ncargex command to see the following relevant examples: bnchmk, tgrida, ccpga, ccpmpxy.
<h2>Access</h2>To use LABMOD or c_labmod, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.
<h2>See Also</h2>Online: gridall, gridall_params, gacolr, gagetc, gageti, gagetr, gasetc, gaseti, gasetr, grid, gridal, gridl, halfax, perim, periml, tick4, ticks, ncarg_cbind. 

 Hardcopy: NCAR Graphics Contouring and Mapping Tutorial 

 Hardcopy: NCAR Graphics Fundamentals, UNIX Version
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
