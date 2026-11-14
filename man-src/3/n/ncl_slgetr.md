---
title: "ncl_slgetr(3)"
name: "ncl_slgetr"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_slgetr/"
---

SLGETR - Gets the current real value of an internal parameter of Scrolled_title of type INTEGER or REAL. See the scrolled_title_params man page for a complete list of all the Scrolled_title internal parameters.

<h2>Synopsis</h2>

CALL SLGETR (PNAM, RVAL)

<h2>C-Binding Synopsis</h2>

#include &lt;ncarg/ncargC.h&gt; 

 void c_slgetr (char *pnam, float *rval)

<h2>Description</h2>

<dl><dt>PNAM
<dd>(an input constant or variable of type CHARACTER) specifies the name of the parameter whose value is to be retrieved. Only the first three characters of the string are examined.
<dt>RVAL
<dd>(an output variable of type REAL) is the value of the internal parameter. If the internal parameter is of type INTEGER and has the value &quot;i&quot;, RVAL = REAL(i). If the internal parameter is of type REAL and has the value &quot;r&quot;, RVAL = r.</dl>

<h2>C-Binding Description</h2>

The C-binding argument descriptions are the same as the FORTRAN argument descriptions.

<h2>Usage</h2>

This routine allows you to retrieve the current value of Scrolled_title parameters. For a complete list of parameters available in this utility, see the scrolled_title_params man page.

<h2>Access</h2>

To use SLGETR or c_slgetr, load the NCAR Graphics libraries ncarg, ncarg_gks, ncarg_c, and ncarg_c, preferably in that order.

<h2>Messages</h2>

See the scrolled_title man page for a description of all Scrolled_title error messages and/or informational messages.

<h2>See Also</h2>

Online: ftitle, scrolled_title, scrolled_title_params, slgeti, slogap, slrset, slseti, slsetr, stitle, ncarg_cbind. 

 Hardcopy: NCAR Graphics Fundamentals, UNIX Version; User's Guide for NCAR GKS-0A Graphics

<h2>Copyright</h2>

Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
