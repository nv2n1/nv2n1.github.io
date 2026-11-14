---
title: "ncl_lbgetr(3)"
name: "ncl_lbgetr"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_lbgetr/"
---

LBGETR - Retrieves the real value of an internal parameter of Labelbar. 

<h2>Synopsis</h2>CALL LBGETR (PNAM, RVAL)
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/ncargC.h&gt; 

 void c_lbgetr (char *pnam, float *rval)
<h2>Description</h2><dl COMPACT><dt>PNAM
<dd>(an input constant or variable of type CHARACTER) is a string three or more characters in length, beginning with one of the six character strings 'CBL', 'CFL', 'CLB', 'WBL', 'WFL', or 'WLB'.
<dt>RVAL
<dd>(an output variable of type REAL) is the name of a variable into which the value of the parameter specified by PNAM is to be retrieved. If the internal parameter is of type INTEGER and has the value &quot;i&quot;, &quot;REAL(i)&quot; will be returned in RVAL.</dl><h2>C-Binding Description</h2>The C-binding argument descriptions are the same as the FORTRAN argument descriptions.
<h2>Usage</h2>This routine allows you to retrieve the current value of Labelbar parameters. For a complete list of parameters available in this utility, see the labelbar_params man page.
<h2>Access</h2>To use LBGETR or c_lbgetr, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.
<h2>Messages</h2>See the labelbar man page for a description of all Labelbar error messages and/or informational messages.
<h2>See Also</h2>Online: labelbar, labelbar_params, lbfill, lbgeti, lblbar, lbseti, lbsetr, ncarg_cbind 

 Hardcopy: NCAR Graphics Fundamentals, UNIX Version
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
