---
title: "ncl_gasetr(3)"
name: "ncl_gasetr"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_gasetr/"
---

GASETR - Gives a real value to an internal parameter of Gridall. 

<h2>Synopsis</h2>CALL GASETR (PNAM,RVAL)
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/ncargC.h&gt; 

 void c_gasetr (char *pnam, float rval)
<h2>Description</h2><dl COMPACT><dt>PNAM
<dd>(an input constant or variable of type CHARACTER) is a string three or more characters in length, the first three characters of which constitute the name of the internal parameter whose value is to be set.
<dt>RVAL
<dd>(an input expression of type REAL) is the new value to be given to the internal parameter specified by PNAM. If the internal parameter is of type INTEGER, the value INT(RVAL) will be given to it.</dl><h2>C-Binding Description</h2>The C-binding argument descriptions are the same as the FORTRAN argument descriptions.
<h2>Usage</h2>This routine allows you to set the current value of Gridall parameters. For a complete list of parameters available in this utility, see the gridall_params man page.
<h2>Access</h2>To use GASETR or c_gasetr, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.
<h2>Messages</h2>See the gridall man page for a description of all Gridall error messages and/or informational messages.
<h2>See Also</h2>Online: gridall, gridall_params, gacolr, gagetc, gageti, gagetr, gasetc, gaseti, grid, gridal, gridl, halfax, labmod, perim, periml, tick4, ticks, ncarg_cbind. 

 Hardcopy: NCAR Graphics Fundamentals, UNIX Version
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
