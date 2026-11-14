---
title: "ncl_slsetr(3)"
name: "ncl_slsetr"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_slsetr/"
---

SLSETR - Provides a new real value for an internal parameter of Scrolled_title of type INTEGER or REAL. See the scrolled_title_params man page for a complete list of all the Scrolled_title internal parameters.

<h2>Synopsis</h2>

CALL SLSETR (PNAM, RVAL)

<h2>C-Binding Synopsis</h2>

#include &lt;ncarg/ncargC.h&gt; 

 void c_slsetr (char *pnam, float rval)

<h2>Description</h2>

<dl><dt>PNAM
<dd>(an input constant or variable of type CHARACTER) specifies the name of the parameter to be set. Only the first three characters of the string are examined.
<dt>RVAL
<dd>(an input expression of type REAL) is the desired value of the internal parameter. If the internal parameter is of type INTEGER, it will be given the value INT(RVAL). If the internal parameter is of type REAL, it will be given the value RVAL.</dl>

<h2>C-Binding Description</h2>

The C-binding argument descriptions are the same as the FORTRAN argument descriptions.

<h2>Usage</h2>

This routine allows you to set the current value of Scrolled_title parameters. For a complete list of parameters available in this utility, see the scrolled_title_params man page.

<h2>Examples</h2>

Use the ncargex command to see the following relevant example: slex01.

<h2>Access</h2>

To use SLSETR or c_slsetr, load the NCAR Graphics libraries ncarg, ncarg_gks, ncarg_c, and ncarg_c, preferably in that order.

<h2>Messages</h2>

See the scrolled_title man page for a description of all Scrolled_title error messages and/or informational messages.

<h2>See Also</h2>

Online: ftitle, scrolled_title, scrolled_title_params, slgeti, slgetr, slogap, slrset, slseti, stitle, ncarg_cbind. 

 Hardcopy: NCAR Graphics Fundamentals, UNIX Version; User's Guide for NCAR GKS-0A Graphics

<h2>Copyright</h2>

Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
