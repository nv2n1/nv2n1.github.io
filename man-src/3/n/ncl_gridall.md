---
title: "ncl_gridall(3)"
name: "ncl_gridall"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_gridall/"
---

Gridall - Allows one to draw backgrounds for X/Y plots. Included are routines for drawing grids, perimeters, and pairs of axes. Internal parameters of Gridall control such things as the color indices and line width scale factors used to draw various parts of the background, the formats to be used for labels, the sizes of the characters to be used for labels, the amount by which labels are to be offset from the axes, and the routine to be called to draw the labels (the SPPS routine WTSTR or the Plotchar routine PLCHHQ). 

<h2>Synopsis</h2>Each of the routines GRID, GRIDL, HALFAX, PERIM, PERIML, and GRIDAL draws a background of some sort within the part of the plotter frame occupied by the current GKS viewport, as follows:
<dl COMPACT><dt>&bull;
<dd>GRID draws an unlabeled grid.
<dt>&bull;
<dd>GRIDL draws a labeled grid.
<dt>&bull;
<dd>HALFAX draws a pair of intersecting axes.
<dt>&bull;
<dd>PERIM draws an unlabeled perimeter.
<dt>&bull;
<dd>PERIML draws a labeled perimeter.
<dt>&bull;
<dd>GRIDAL draws any of the above.</dl><h2></h2>The positioning of ticks and grid lines is determined partly by the arguments of these routines and partly by the nature of the current mapping from the &quot;user&quot; coordinate system to the &quot;fractional&quot; coordinate system, as determined by the current definitions of the GKS viewport and window and by the values of two internal parameters of the package SPPS: 'LS' and 'MI'. Numeric labels reflect values in the &quot;user&quot; coordinate system. 

 Note: Calling the SPPS routine SET defines the GKS viewport and window and the values of the parameters 'LS' and 'MI'. The parameter 'LS' determines whether the mappings of user coordinates to fractional coordinates are linear or logarithmic and the parameter 'MI' determines whether the mappings are mirror-imaged or not. 

 Each of the internal parameters of Gridall has a three-character mnemonic name of the form 'xxx'. Each of the routines GAGETC, GAGETI, GAGETR, GASETC, GASETI, and GASETR is intended either to retrieve the value of a specific internal parameter of Gridall or to give a new value to it, as follows:
<dl COMPACT><dt>&bull;
<dd>GAGETC is called with the name of an internal parameter of type CHARACTER and a character variable in which the value of the parameter is to be returned.
<dt>&bull;
<dd>GAGETI is called with the name of an internal parameter of type INTEGER or REAL and an integer variable in which the integer equivalent of the value of the parameter is to be returned.
<dt>&bull;
<dd>GAGETR is called with the name of an internal parameter of type INTEGER or REAL and a real variable in which the real equivalent of the value of the parameter is to be returned.
<dt>&bull;
<dd>GASETC is called with the name of an internal parameter of type CHARACTER and a character expression that is to become the new value of the parameter.
<dt>&bull;
<dd>GASETI is called with the name of an internal parameter of type INTEGER or REAL and an integer expression that is to become the new value of the parameter.
<dt>&bull;
<dd>GASETR is called with the name of an internal parameter of type INTEGER or REAL and a real expression that is to become the new value of the parameter.</dl><h2></h2>These six routines allow one to access all of the internal parameters of Gridall in a manner consistent with other NCAR Graphics utilities and are intended to replace some older routines, each of which allows access to a limited subset of the internal parameters. However, the older routines are still available and will remain so for the foreseeable future:
<dl COMPACT><dt>&bull;
<dd>GACOLR sets the value of internal parameters that control the color of various parts of the background.
<dt>&bull;
<dd>LABMOD sets the value of internal parameters that affect the appearance of labels.
<dt>&bull;
<dd>TICKS and TICK4 set the value of internal parameters that determine the length and direction of ticks.</dl><h2>C-Binding Synopsis</h2>c_grid 
 c_gridl 
 c_halfax 
 c_perim 
 c_periml 
 c_gridal 
 c_gagetc 
 c_gageti 
 c_gagetr 
 c_gasetc 
 c_gaseti 
 c_gasetr 
 c_gacolr 
 c_labmod 
 c_ticks 
 c_tick4
<h2>User-Modifiable Internal Routines</h2>None.
<h2>Access</h2>To use Gridall C or Fortran routines, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.
<h2>Messages</h2>Various error conditions can occur in Gridall. Each of these results in a call to the error-handling routine SETER, with a final argument indicating that the error is recoverable; by default, an error message is printed and execution is terminated, but, if you turn on error recovery (as described in the &quot;man&quot; page for &quot;error_handling&quot;), you can get control back. 

 The error messages are as follows; all should be more or less self-explanatory. 

 GACOLR - UNCLEARED PRIOR ERROR 
 GAGETC - UNCLEARED PRIOR ERROR 
 GAGETC - UNRECOGNIZED PARAMETER NAME 
 GAGETI - UNCLEARED PRIOR ERROR 
 GAGETR - UNCLEARED PRIOR ERROR 
 GAGETR - UNRECOGNIZED PARAMETER NAME 
 GASETC - UNCLEARED PRIOR ERROR 
 GASETC - UNRECOGNIZED PARAMETER NAME 
 GASETI - UNCLEARED PRIOR ERROR 
 GASETR - UNCLEARED PRIOR ERROR 
 GASETR - UNRECOGNIZED PARAMETER NAME 
 GRID - UNCLEARED PRIOR ERROR 
 GRIDAL - ERROR EXIT FROM GQCLIP 
 GRIDAL - ERROR EXIT FROM GQLWSC 
 GRIDAL - ERROR EXIT FROM GQPLCI 
 GRIDAL - ERROR EXIT FROM GQTXCI 
 GRIDAL - UNCLEARED PRIOR ERROR 
 GRIDL - UNCLEARED PRIOR ERROR 
 HALFAX - UNCLEARED PRIOR ERROR 
 LABMOD - UNCLEARED PRIOR ERROR 
 PERIM - UNCLEARED PRIOR ERROR 
 PERIML - UNCLEARED PRIOR ERROR 
 TICK4 - UNCLEARED PRIOR ERROR 
 TICKS - UNCLEARED PRIOR ERROR
<h2>See Also</h2>Online: gridall_params, gacolr, gagetc, gageti, gagetr, gasetc, gaseti, gasetr, grid, gridal, gridl, halfax, labmod, perim, periml, tick4, ticks, ncarg_cbind. 

 Hardcopy: NCAR Graphics Fundamentals, UNIX Version
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
