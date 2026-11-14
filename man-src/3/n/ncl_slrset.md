---
title: "ncl_slrset(3)"
name: "ncl_slrset"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_slrset/"
---

SLRSET - Resets all parameters of Scrolled_title to the initial default values.

<h2>Synopsis</h2>

CALL SLRSET

<h2>C-Binding Synopsis</h2>

#include &lt;ncarg/ncargC.h&gt; 

 void c_slrset()

<h2>Description</h2>

SLRSET has no arguments.

<h2>Usage</h2>

Calling this routine restores all Scrolled_title parameters to their initial default values. For a complete list of parameters available in this utility, see the scrolled_title_params man page.

<h2>Examples</h2>

Use the ncargex command to see the following relevant example: slex02.

<h2>Access</h2>

To use SLRSET or c_slrset, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.

<h2>Messages</h2>

See the scrolled_title man page for a description of all Scrolled_title error messages and/or informational messages.

<h2>See Also</h2>

Online: ftitle, scrolled_title, scrolled_title_params, slgeti, slgetr, slogap, slseti, slsetr, stitle, ncarg_cbind. 

 Hardcopy: NCAR Graphics Fundamentals, UNIX Version; User's Guide for NCAR GKS-0A Graphics

<h2>Copyright</h2>

Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
