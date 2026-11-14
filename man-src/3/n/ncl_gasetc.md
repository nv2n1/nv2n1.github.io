---
title: "ncl_gasetc(3)"
name: "ncl_gasetc"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_gasetc/"
---

GASETC - Gives a new value to a specified internal parameter of type CHARACTER. 

<h2>Synopsis</h2>CALL GASETC (PNAM,CVAL)
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/ncargC.h&gt; 

 void c_gasetc (char *pnam, char *cval)
<h2>Description</h2><dl COMPACT><dt>PNAM
<dd>(an input constant or variable of type CHARACTER) is a string three or more characters in length, the first three characters of which constitute the name of the internal parameter whose value is to be set.
<dt>CVAL
<dd>(an input expression of type CHARACTER) is the new value to be given to the internal parameter specified by PNAM.</dl><h2>C-Binding Description</h2>The C-binding argument descriptions are the same as the FORTRAN argument descriptions.
<h2>Usage</h2>This routine allows you to set the current value of Gridall parameters. For a complete list of parameters available in this utility, see the gridall_params man page.
<h2>Access</h2>To use GASETC or c_gasetc, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.
<h2>Messages</h2>See the gridall man page for a description of all Gridall error messages and/or informational messages.
<h2>See Also</h2>Online: gridall, gridall_params, gacolr, gagetc, gageti, gagetr, gaseti, gasetr, grid, gridal, gridl, halfax, labmod, perim, periml, tick4, ticks ncarg_cbind. 

 Hardcopy: NCAR Graphics Fundamentals, UNIX Version
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
