---
title: "ncl_sfgetc(3)"
name: "ncl_sfgetc"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_sfgetc/"
---

SFGETC - Used to retrieve the current value of a specified internal parameter.

<h2>Synopsis</h2>

CALL SFGETC (CNP,CVP)

<h2>C-Binding Synopsis</h2>

#include &lt;ncarg/ncargC.h&gt; 

 void c_sfgetc (char *cnp, char *cvp, int len)

<h2>Description</h2>

<dl><dt>CNP
<dd>(an input expression of type CHARACTER) is the name of an internal parameter of SOFTFILL. Currently, the only legal value is 'CH' (or any longer string beginning with 'CH'), which stands for &quot;CHaracter&quot;.
<dt>CVP
<dd>(an output variable of type CHARACTER) is the name of a variable into which the value of the parameter specified by CNP is to be retrieved.</dl>

<h2>C-Binding Description</h2>

The C-binding argument descriptions are the same as the FORTRAN argument descriptions with the following exception:
<dl><dt>len
<dd>Size of cvp as dimensioned in the calling program.</dl>

<h2>Usage</h2>

This routine allows you to retrieve the current value of Softfill parameters. For a complete list of parameters available in this utility, see the softfill_params man page.

<h2>Access</h2>

To use SFGETC or c_sfgetc, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.

<h2>Messages</h2>

See the softfill man page for a description of all Softfill error messages and/or informational messages.

<h2>See Also</h2>

Online: softfill, softfill_params, sfgeti, sfgetp, sfgetr, sfseti, sfsetp, sfsetr, sfsgfa, sfwrld, ncarg_cbind 

 Hardcopy: NCAR Graphics Fundamentals, UNIX Version

<h2>Copyright</h2>

Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 

 The use of this Software is governed by a License Agreement.
