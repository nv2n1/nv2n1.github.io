---
title: "ncl_sfsetc(3)"
name: "ncl_sfsetc"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_sfsetc/"
---

SFSETC - Used to set the character value of a specified internal parameter.

<h2>Synopsis</h2>

CALL SFSETC (CNP, CVP)

<h2>C-Binding Synopsis</h2>

#include &lt;ncarg/ncargC.h&gt; 

 void c_sfsetc (char *cnp, char *cvp)

<h2>Description</h2>

<dl><dt>CNP
<dd>(an input expression of type CHARACTER) is the name of an internal parameter of SOFTFILL. Currently, the only legal value is 'CH' (or any longer string beginning with 'CH'), which stands for &quot;CHaracter&quot;.
<dt>CVP
<dd>(an input expression of type CHARACTER) is the desired new value of the parameter specified by CNP. This value will be used until the next call resetting it.</dl>

<h2>C-Binding Description</h2>

The C-binding argument descriptions are the same as the FORTRAN argument descriptions.

<h2>Usage</h2>

This routine allows you to set the current value of Softfill parameters. For a complete list of parameters available in this utility, see the softfill_params man page.

<h2>Examples</h2>

Use the ncargex command to see the following relevant examples: sfex01, tsoftf.

<h2>Access</h2>

To use SFSETC or c_sfsetc, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.

<h2>Messages</h2>

See the softfill man page for a description of all Softfill error messages and/or informational messages.

<h2>See Also</h2>

Online: softfill, softfill_params, sfgetc, sfgeti, sfgetp, sfgetr, sfseti, sfsetp, sfsetr, sfsgfa, sfwrld, ncarg_cbind 

 Hardcopy: NCAR Graphics Fundamentals, UNIX Version

<h2>Copyright</h2>

Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 

 The use of this Software is governed by a License Agreement.
