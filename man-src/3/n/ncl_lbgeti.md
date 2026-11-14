---
title: "ncl_lbgeti(3)"
name: "ncl_lbgeti"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_lbgeti/"
---

LBGETI - Retrieves the integer value of an internal parameter of Labelbar. 

<h2>Synopsis</h2>CALL LBGETI (PNAM, IVAL)
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/ncargC.h&gt; 

 void c_lbgeti (char *pnam, int *ival)
<h2>Description</h2><dl COMPACT><dt>PNAM
<dd>(an input constant or variable of type CHARACTER) is a string three or more characters in length, beginning with one of the six character strings 'CBL', 'CFL', 'CLB', 'WBL', 'WFL', or 'WLB'.
<dt>IVAL
<dd>(an output variable of type INTEGER) is the name of a variable into which the value of the parameter specified by PNAM is to be retrieved. If the internal parameter is of type REAL and has the value &quot;r&quot;, &quot;INT(r)&quot; will be returned in IVAL.</dl><h2>C-Binding Description</h2>The C-binding argument descriptions are the same as the FORTRAN argument descriptions.
<h2>Usage</h2>This routine allows you to retrieve the current value of Labelbar parameters. For a complete list of parameters available in this utility, see the labelbar_params man page.
<h2>Access</h2>To use LBGETI or c_lbgeti, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.
<h2>Messages</h2>See the labelbar man page for a description of all Labelbar error messages and/or informational messages.
<h2>See Also</h2>Online: labelbar, labelbar_params, lbfill, lbgetr, lblbar, lbseti, lbsetr, ncarg_cbind 

 Hardcopy: NCAR Graphics Fundamentals, UNIX Version
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
