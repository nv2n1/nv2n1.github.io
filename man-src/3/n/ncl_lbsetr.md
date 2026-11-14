---
title: "ncl_lbsetr(3)"
name: "ncl_lbsetr"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_lbsetr/"
---

LBSETR - Gives a real value to an internal parameter of Labelbar. 

<h2>Synopsis</h2>CALL LBSETR (PNAM, RVAL)
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/ncargC.h&gt; 

 void c_lbsetr (char *pnam, float rval)
<h2>Description</h2><dl COMPACT><dt>PNAM
<dd>(an input constant or variable of type CHARACTER) is a string three or more characters in length, beginning with one of the six character strings 'CBL', 'CFL', 'CLB', 'WBL', 'WFL', or 'WLB'.
<dt>RVAL
<dd>(an input expression of type REAL) specifies the desired value of the parameter. If the internal parameter is of type INTEGER, the value INT(RVAL) will be given to it.</dl><h2>C-Binding Description</h2>The C-binding argument descriptions are the same as the FORTRAN argument descriptions.
<h2>Usage</h2>This routine allows you to set the current value of Labelbar parameters. For a complete list of parameters available in this utility, see the labelbar_params man page.
<h2>Examples</h2>Use the ncargex command to see the following relevant examples: cpex05, elblba, and tlblba.
<h2>Access</h2>To use LBSETR or c_lbsetr, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.
<h2>Messages</h2>See the labelbar man page for a description of all Labelbar error messages and/or informational messages.
<h2>See Also</h2>Online: labelbar, labelbar_params, lbfill, lbgeti, lbgetr, lblbar, lbseti, ncarg_cbind 

 Hardcopy: NCAR Graphics Fundamentals, UNIX Version
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
